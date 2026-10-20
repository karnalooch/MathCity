# MathCity — HOUDINI FIRST: pipeline świata i assetów do Roblox

**Decyzja właściciela 2026-10-20: APPROVED_ARCHITECTURE.**
**Houdini jest głównym wykonawcą proceduralnego świata i produkcji środowiska. Unreal Engine, Blender i Material Forge z warsztatu YACS są narzędziami pomocniczymi. Roblox Studio jest jedynym runtime i miejscem ostatecznej walidacji.**

Ta hierarchia jest obowiązująca dla kolejnych pakietów świata. Nie tworzymy czterech konkurencyjnych wersji tej samej mapy.

## 1. Hierarchia narzędzi

| Priorytet | Narzędzie | Odpowiedzialność |
|---|---|---|
| **P1** | **Houdini** | master terrain, HeightFields, erozja, maski, drogi/korytarze, building pads, proceduralne meshe, scatter, placement data, bake i eksport |
| P2 | Material Forge | źródło/opracowanie materiałów i tekstur PBR zgodnych z kierunkiem artystycznym |
| P2 | Blender | ręczne poprawki, retopo/UV, cleanup, pivoty, wyjątkowe hero assety i zgodność eksportu, gdy Houdini nie jest wygodniejszy |
| P2 | Unreal Engine | lookdev, światło, kompozycja, preview jakości, porównanie wariantów i review; **nie master świata** |
| Runtime | Roblox Studio | Terrain, MeshPart, SurfaceAppearance/MaterialVariant, Luau, streaming, fizyka, testy i urządzenia |

Jeżeli tę samą czynność można wykonać w Houdinim i innym narzędziu bez utraty jakości, wybieramy Houdiniego, bo zależy nam na regenerowalnym proceduralnym świecie.

## 2. Source of truth

### Houdini jest źródłem prawdy dla
- makro-ukształtowania terenu;
- wysokości i masek terenu;
- korytarzy dróg i chodników;
- building pads / stref zabudowy;
- nasypów, wykopów, skarp i brzegów;
- proceduralnych obiektów środowiska;
- danych scatter/placement;
- powtarzalnych generatorów wariantów;
- bake'ów wynikających z proceduralnej geometrii.

### Roblox jest źródłem prawdy dla
- logiki gry i Luau;
- runtime physics;
- obiektów interaktywnych;
- finalnych asset IDs;
- streamingu;
- testów klienta/serwera i faktycznej wydajności.

### UE nie jest źródłem prawdy dla geometrii MathCity
UE może importować wynik Houdiniego i pomagać ocenić światło, kadr, gęstość detalu i wygląd. Zmiana wykonana wyłącznie w UE nie jest zmianą master świata. Jeżeli ma zostać zachowana, wraca do Houdiniego/Blendera/Material Forge albo jest jawnie opisana jako Roblox-only.

## 3. Terrain: Houdini HeightField → Roblox Terrain

Roblox Terrain przyjmuje heightmapę i opcjonalną colormapę. Roblox dokumentuje voxel terrain 4×4×4 stud oraz import heightmap, gdzie 1 piksel reprezentuje 4 study, do maks. 4096×4096 px.

| Świat Roblox | Heightmap | Pokrycie |
|---|---:|---:|
| 8192 × 8192 studów | **2048 × 2048 px** | 4 study / px |
| 16384 × 16384 studów | **4096 × 4096 px** | 4 study / px |

To nie wybór finalnej mapy. To dwa profile testowe zgodne z rozdzielczością importera.

### Minimalny graf HeightField
1. HF_BASE — wejściowy raster/DEM, jeżeli legalny i potrzebny, albo proceduralny base terrain.
2. HF_MACRO_SHAPING — doliny, pagórki, strefy Muchawki, Sekuły i osi miasta.
3. HF_EROSION — umiarkowana erozja hydro/thermal dla naturalnych powierzchni.
4. HF_ROAD_AND_BUILDING_CONSTRAINTS — flatten/terrace building pads, grade corridors, cut/fill.
5. HF_WATER_AND_BANKS — brzegi Muchawki, pomosty, plaża, promenada.
6. HF_MATERIAL_MASKS — grass, ground, rock, sand, mud, pavement-like areas.
7. HF_EXPORT — heightmap PNG, colormap PNG, dodatkowe maski diagnostyczne, manifest parametrów.

**Zakaz:** po imporcie do Roblox nie rzeźbimy ręcznie całej mapy tak, że Houdini przestaje móc ją odtworzyć. Lokalny wyjątek ma być opisany albo wrócić do generatora.

## 4. Co jest Terrain, a co MeshPart

### Roblox Terrain
- pagórki, doliny, łagodne skarpy;
- naturalne brzegi;
- szerokie nasypy i wykopy;
- ziemia, trawa, piasek i duże powierzchnie skalne.

### Mesh z Houdiniego/Blendera
- mury oporowe, ostre krawędzie, schody i krawężniki;
- mosty, pomosty, nabrzeża, tunele i przewieszenia;
- hero cliffs wymagające podcięcia;
- budynki i mała architektura;
- drogi, jeżeli Terrain nie daje odpowiedniej geometrii i prowadzenia pojazdów.

Reguła: terrain robi makroformę, meshe robią kontrolowany detal i formy niemożliwe albo brzydkie w voxel terrain.

## 5. Drogi i place

Houdini ma generować drogę jako dane i/lub mesh, nie tylko linię namalowaną na płaskiej mapie. Dla każdego korytarza przechowujemy centerline, szerokość, shoulder/chodnik, flatten/cut/fill mask, maskę nawierzchni, opcjonalne krawężniki i punkty scatter.

Nie kopiujemy pipeline'u fizyki YACS 1:1, ale wykorzystujemy jego doświadczenie: droga musi mieć poprawny kontakt z terenem i nie może falować od voxelowego szumu.

## 6. Proceduralne budynki i landmarki

Zwykła zabudowa powstaje z modularnego kitu w Houdinim: fasady, narożniki, dachy, okna, drzwi, balkony i warianty. Generator wypluwa reużywalne modele, nie jeden gigantyczny mesh dzielnicy.

Landmarki: Houdini robi proporcje, blockout i powtarzalne elementy. Blender wchodzi tylko tam, gdzie potrzebny jest ręczny hero-detail, retopo lub UV. Material Forge dostarcza PBR. Roblox jest finalnym importem i testem.

Priorytet Houdini oznacza proceduralny master i regenerowalność, nie zakaz używania Blendera do rzeczy, które ręcznie robi lepiej.

## 7. Materiały

Unikatowy mesh: Roblox SurfaceAppearance — Color/Albedo, Normal, Roughness, Metalness, opcjonalnie Emissive. Normal maps przygotować jako OpenGL tangent-space.

Powtarzalne powierzchnie: Roblox MaterialVariant — asfalt, chodnik, tynk, cegła, drewno, piasek, trawa/ziemia i miejski kit.

Material Forge ma dostarczać spójną stylizację i PBR. Houdini przypisuje/maskuje materiały i może bake'ować dane. UE materials nie są eksportem do Roblox; UE jest tylko lookdevem/referencją.

## 8. Bake

Dla hi→low preferować aktualne narzędzia SideFX dostępne w zainstalowanej wersji. W Houdini 22 dokumentowany jest Labs Maps Baker, ale SideFX wskazuje też nowsze Bake Geometry Textures COP / Karma Texture Baker LOP. Przed standardem sprawdzić faktycznie dostępne nodes w YACS.

Minimalne wyniki: albedo/color, tangent normal, roughness, metallic. AO/curvature mogą być danymi pomocniczymi. Preset bake musi być zapisany i deterministyczny.

## 9. Scatter i roślinność

Houdini generuje punkty drzew, krzewów, kamieni, ławek, latarni i dekoracji wraz z density masks i exclusion zones. Nie eksportujemy miliona unikalnych meshów. Generator ma produkować placement data wskazujące prefab key i transform albo sektorowe instancje gotowe do przetworzenia.

Format placement data zostanie zatwierdzony w spike'u; JSON/CSV nie jest narzucony. Minimalny rekord: prefab key, sektor, position, rotation, opcjonalna scale, source recipe/version.

## 10. Sektory

Nie eksportować jednego 4–20 km² mesha. Terrain może być spójnym Roblox Terrain, natomiast meshe/props/scatter są sektorowymi paczkami, landmarki osobnymi pakietami, a drogi dzielone bez widocznych szczelin. Rozmiar sektora jest TEST_DEFAULT dobieranym po benchmarku na iPadzie 6.

## 11. Produkty eksportowe Houdiniego

Planowany katalog roboczy poza repo:
- terrain/ — heightmaps, colormaps, masks;
- meshes/roads, retaining, buildings, landmarks, props;
- textures/pbr i materials;
- placements/;
- manifests/;
- evidence/.

Dużych binariów nie commitować bez osobnej decyzji o Git LFS albo magazynie assetów.

## 12. Obowiązkowe spike'i

### H00 — Terrain
Mała scena: dolina, pagórek, brzeg i płaski building pad. Eksport heightmap + colormap. Import do testowego Roblox Place. Dowód: screenshot, wymiary, zakres wysokości, materiały i artefakty.

### H01 — Procedural mesh
Pomost, murek albo moduł ulicy. UV, pivot, skala, FBX lub glTF, import, kolizja i ponowny cook po zmianie parametru.

### H02 — Material
Asfalt, chodnik i tynk/kamień. PBR → SurfaceAppearance/MaterialVariant. Porównanie dzień/noc w Roblox Studio.

Dopiero po H00+H01+H02 wybieramy produkcyjny preset.

## 13. Kryterium sukcesu

PASS pipeline'u wymaga: ta sama recepta odtwarza wynik; zmiana parametru w Houdini daje przewidywalną zmianę w Roblox; nie ma ręcznej rekonstrukcji po każdym cooku; skala/orientacja są poprawne; materiały wyglądają dobrze w Roblox; update nie robi duplikatów; benchmark mobilny nie zostaje pominięty.

## 14. Role pomocnicze

### Unreal Engine
Lookdev, lighting studies, cinematic preview, ocena kompozycji. Nie master HeightField, nie finalna logika, nie autorytatywny placement i nie benchmark Roblox.

### Blender
Hero model, retopo, UV, cleanup, triangulacja i kontrola FBX/glTF. Nie przebudowuje ręcznie proceduralnego świata.

### Material Forge
Biblioteka materiałów, stylizowane PBR, warianty i paleta. Nie tworzy rozwiązania zależnego wyłącznie od UE.

## 15. Stop rules dla słabszego LLM

STOP i BLOCKED, gdy nie znaleziono istniejącej instalacji Houdiniego YACS; SideFX Labs/node nie istnieje; licencja assetu jest nieznana; skala eksportu niepotwierdzona; importer Roblox odrzuca plik; normal map jest odwrócona; terrain import ma zły zakres; albo rozwiązanie wymaga ręcznego poprawiania setek elementów po każdym cooku.

LLM nie omija Houdiniego i nie przechodzi na ręczne budowanie świata w Roblox tylko dlatego, że pipeline wymaga naprawy.

## 16. Źródła pierwszej strony

- Roblox Importer: https://create.roblox.com/docs/studio/importer
- Roblox Terrain: https://create.roblox.com/docs/parts/terrain
- Roblox Terrain Editor: https://create.roblox.com/docs/studio/terrain-editor
- Roblox PBR: https://create.roblox.com/docs/art/modeling/surface-appearance
- Roblox Materials: https://create.roblox.com/docs/parts/materials
- SideFX HeightField Output: https://www.sidefx.com/docs/houdini/nodes/sop/heightfield_output.html
- SideFX erosion: https://www.sidefx.com/docs/houdini/heightfields/erosion.html
- SideFX Labs Maps Baker: https://www.sidefx.com/docs/houdini/nodes/sop/labs--maps_baker-5.0.html
- SideFX ROP FBX Output: https://www.sidefx.com/docs/houdini/nodes/top/ropfbx.html
