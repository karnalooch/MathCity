# P00 + H00: pierwszy wykonywalny test Houdini → Roblox

**Zakres uruchomiony przez właściciela 2026-10-20: P00 + H00.** To syntetyczny test produkcji terenu. H01, H02, przebudowa gry i publikacja pozostają kolejnymi zadaniami. [Decyzja D-014](../planning/DECISION_LOG.md) nadal obowiązuje: Houdini tworzy proceduralny świat, UE/Blender/Material Forge pomagają, Roblox jest runtime.

**Stan tego dostarczenia:** kod i testy kontraktu plików przygotowane. Windows, cook Houdiniego, ponowne otwarcie HIP i import Studio nie zostały uruchomione w sesji autora pakietu. Zobacz [raport](../reports/P00_H00_DELIVERY_20261020.md). Nie odczytuj poniższych oczekiwanych wyników jako istniejących dowodów.

## 1. Co uruchomić

W istniejącym checkout MathCity pobierz gałąź `codex/mathcity-p00-h00-terrain` i pracuj na czystej gałęzi funkcjonalnej. Jeśli są cudze zmiany, zachowaj je i użyj osobnego checkout/worktree na D:. Nie resetuj ani nie stashuj ich automatycznie. Skrypt sprawdza origin `karnalooch/MathCity`, gałąź, HEAD i blob mapy.

Z katalogu głównego tego checkout, w PowerShell na Windows:

```powershell
.\tools\worldgen\Invoke-MathCityH00.ps1 -Cook
```

Ta jedna komenda wykonuje P00, cook H00, kontrolę w świeżym procesie hython i kontrolę wszystkich wyeksportowanych próbek. Domyślny katalog wyników: nowy, unikalny `D:\MathCity\work\H00_<czas>_<id>`. Nie jest częścią YACS ani repozytorium. Niczego nie instaluje; nie uruchamia UE, Blendera, Material Forge ani Roblox.

Istniejący checkout właściciela znajduje się w `D:\gem\Matma roblox`. Można uruchomić go z dowolnego katalogu PowerShella, przekazując jawne ścieżki:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'D:\gem\Matma roblox\tools\worldgen\Invoke-MathCityH00.ps1' -RepoRoot 'D:\gem\Matma roblox' -WorkRoot 'D:\MathCity\work' -Cook
```

Zgłoszony 2026-10-20 błąd `Split-Path` z pustym `$PSScriptRoot` dotyczył wyliczania domyślnego `RepoRoot` w bloku `param`, jeszcze przed P00. Zachowanie opisuje [PowerShell #4688](https://github.com/PowerShell/PowerShell/issues/4688). Poprawka przenosi wyliczanie ścieżek do ciała skryptu po związaniu parametrów; jawny `-RepoRoot` pozostaje obsługiwany. Samo usunięcie tej przyczyny błędu startowego nie stanowi dowodu cook ani importu.

Samo rozpoznanie warsztatu:

```powershell
.\tools\worldgen\Invoke-MathCityH00.ps1 -PreflightOnly
```

Jeżeli wykrywanie nie znalazło istniejącej instalacji, podaj rzeczywiście sprawdzoną ścieżkę:

```powershell
.\tools\worldgen\Invoke-MathCityH00.ps1 -Cook -HythonPath 'D:\yacs\tools\houdini-22.0.466\bin\hython.exe'
```

Powyższa ścieżka jest kandydatem z warsztatu YACS, a nie twierdzeniem, że znajduje się na każdym komputerze. Skrypt sprawdza jej istnienie i uruchamia inwentaryzację. Dostępne są również jawne `-WorkRoot`, `-BlenderPath`, `-UnrealEditorPath`, `-MaterialForgePath`. Dla H00 wymagany jest działający Houdini; brak narzędzia pomocniczego nie oznacza potrzeby jego instalowania.

## 2. P00: sprawdzane wejście

- Wersja i kategoria licencji z działającego hython; brak kluczy licencyjnych w raporcie.
- Rzeczywiste typy SOP, nazwy i etykiety parametrów oraz zadeklarowane menu.
- Obecność SideFX Labs. **Ten konkretny H00 używa natywnych SOP**, więc Labs może mieć `NOT_DETECTED_IN_THIS_PROCESS`. Brak wymaganego operatora blokuje cook.
- Ścieżki i wersje plików UE/Blendera/Material Forge, jeśli wykryte. `PATH_DETECTED_ONLY` nie oznacza uruchomienia ani sprawności.
- Istnienie `Roblox\mcp.bat`, jeżeli obecne w profilu użytkownika. To nie jest `MCP_CONNECTED`.
- SHA-256 `MathCity.rbxl`, blob z HEAD i stan checkout przed/po przebiegu.

Każdy podproces ma limit czasu, oddzielny stdout/stderr i kod wyjścia. Przekroczenie limitu przerywa tylko proces uruchomiony przez ten skrypt. Raport nie ukrywa nieudanego etapu. Nie udostępniaj surowych raportów z lokalnymi ścieżkami publicznie bez przeglądu.

## 3. Recepta H00

Źródło parametrów: [`worldgen/h00/recipe.json`](../../worldgen/h00/recipe.json). Wszystkie wartości poniżej są `TEST_DEFAULT`, nie zatwierdzonym rozmiarem miasta.

| Parametr | Wartość testowa |
|---|---|
| Heightmapa | 256 × 256 px |
| Pokrycie Roblox | 1024 × 1024 studów |
| Konwencja skali | 0,28 m/stud |
| Rozmiar Houdini | 286,72 × 286,72 m |
| Odstęp próbek | 1,12 m; próbki w środkach komórek |
| Stały zakres kodowania Y | −64…256 studów, czyli −17,92…71,68 m |
| Import Position | **X=0, Y=96, Z=0** |
| Import Size | **X=1024, Y=320, Z=1024** |
| Erozja | natywny HeightField Erode 3.0, jawny seed, freeze frame 12 |
| Warstwy | grass, ground, sand, rock, asphalt |

Graf ma natywny HeightField, makroformy, natywną erozję, dopasowanie drogi i placu po erozji oraz pięć rozłącznych masek. Makroformy obejmują asymetryczne wzgórze, dolinę, nieckę i brzeg. Droga ma kontrolowany spadek; building pad ma płaski rdzeń i przejście do otoczenia. To nie są pomiary Siedlec. Niecka jest na razie sucha: geometria brzegu i materiał nie są dowodem poprawnej wody.

Reguły kodowania:

- PNG wysokości: grayscale **16 bit**, ustalony zakres bez Auto Remap.
- PNG materiałów: **RGB8**, dokładny klucz importera: Grass `(106,127,63)`, Ground `(102,92,59)`, Sand `(143,126,95)`, Rock `(102,108,111)`, Asphalt `(115,123,107)`.
- Kolumny obrazu: −X → +X. Wiersze: −Z → +Z. Położenia pobierane przez `indexToPos`, nie przez założenie o kolejności osi wolumenu.
- Zgodność orientacji i rzeczywistej precyzji importu 16 bit w Studio pozostaje testem do wykonania. Nie zmieniaj po cichu PNG na 8 bit ani nie obracaj obrazu bez aktualizacji kontraktu/prob.

**Sposób eksportu w tej implementacji:** adapter PNG serializuje wyłącznie natywnie ugotowane wolumeny Houdiniego i zachowuje surowe próbki float32. Nie generuje zastępczego terenu w zwykłym Pythonie. Zapisany graf ma też podłączony preset `HeightField Output` z udokumentowanymi parametrami, oznaczony `NOT_RUN` i `NOT_CALIBRATED`; kod nie naciska jego Execute. Nie raportuj tego presetu jako przetestowanego natywnego eksportu. Porównanie natywnego zapisu z kontraktem jest późniejszą, jawną zmianą po dostępie do Houdiniego.

## 4. Wyniki udanego lokalnego przebiegu

| Plik w katalogu przebiegu | Znaczenie |
|---|---|
| `run_report.json`, `*.stdout.log`, `*.stderr.log` | rzeczywiste wykonane etapy i kody wyjścia |
| `houdini_environment.json` | instalacja, licencja, operatory i Labs |
| `MathCity_H00_Terrain.hip` lub `.hiplc` | prawdziwy projekt zgodny z wykrytą licencją; recepta i kod SOP osadzone w HIP |
| `h00.bgeo.sc` | natywny wynik wolumenów |
| `terrain/heightmap.png`, `terrain/colormap.png` | wejścia do Terrain Editor |
| `terrain/masks/*.png`, `terrain/height_samples.f32` | pięć masek i wszystkie źródłowe wysokości |
| `manifest.json` | parametry, źródła, SHA-256, wersja Houdini i ustawienia importu |
| `reopen_verification.json` | odczyt/recook w świeżym procesie, porównanie każdej wysokości i materiału |
| `file_verification.json` | kontrola każdego piksela, masek, kodowania i metadanych |
| `verify_import.command.luau` | **tylko odczyt** terenu po imporcie; gotowy kod z próbkami tego przebiegu |

Manifest opisuje stan w chwili eksportu i nie jest przepisywany po reopen. Status ponownego otwarcia pochodzi z osobnego `reopen_verification.json`, związanego z SHA-256 właściwego HIP. Powtórzenia używają nowego katalogu, nigdy nadpisania istniejącego raportu.

## 5. MCP00 i import w Roblox

1. Wykonaj [read-only smoke test MCP](ROBLOX_STUDIO_MCP.md). Odkryj rzeczywistą listę narzędzi, wylistuj instancje, zapisz jawny `studio_id`. Sam plik `mcp.bat` nie dowodzi połączenia.
2. Utwórz **nowe, lokalne, nieopublikowane miejsce H00**, bez skryptów gry i dostępu do DataStore. Zapisz je poza repo jako osobny `.rbxl`. Oryginalny `MathCity.rbxl` pozostaje bazą chronioną przez P00.
3. W Terrain Editor wybierz Import, `terrain/heightmap.png` i `terrain/colormap.png` z tego samego przebiegu. Wprowadź Position i Size z manifestu. Dla domyślnej recepty: `(0,96,0)` i `(1024,320,1024)`.
4. Uruchom Generate. Potwierdź wizualnie wzgórze, dolinę, brzeg, płaski plac i drogę. Zachowaj widok z góry i dwa ujęcia z poziomu postaci wraz z ustawieniami importu.
5. W **Edit**, przez odkryte `execute_luau` i właściwy `studio_id` albo Command Bar, uruchom treść `verify_import.command.luau`. Kod nie tworzy instancji, nie rzeźbi terenu i niczego nie publikuje. Zapisz JSON z Output jako dowód lokalny.
6. Probe sprawdza wysokości z tolerancją **4 studów** i materiały w próbkach z jednorodnym sąsiedztwem. To próba wykrycia błędnej skali, przesunięcia, odbicia i palety; nie pomiar zachowanej precyzji 16 bit. Brak pokrycia materiału daje `INCOMPLETE`.
7. Zapisz i ponownie otwórz testowe miejsce. Powtórz odczyt. Dopiero w tej pozbawionej skryptów gry scenie wykonaj krótki spacer po placu, drodze i skarpie; zachowaj log i screenshot. Osobno oceń kolizję oraz wygląd.

Oficjalne MCP pozwala wykonywać Luau i odczytywać Studio, lecz nie dokumentuje narzędzia natywnego importu heightmap. `HeightmapImporterService` nie jest dostępnym API experience scripts. **Nie wpisuj wymyślonego `ImportHeightmap` i nie zastępuj tego testu generatorem `WriteVoxels`.** Wbudowany Terrain Editor jest etapem importu tego pakietu.

## 6. Ponowny cook i następny krok

Po udanym pierwszym przebiegu zmień jeden parametr recepty, np. `features.hill.height_m` z 34 na 38, w osobnym lokalnym commicie tej gałęzi. P00 wymaga czystego checkout, więc nie omijaj kontroli brudnego drzewa. Uruchom `-Cook` ponownie. Porównaj zakres, współrzędne stałych obiektów i oczekiwaną zmianę wzgórza; ten sam zakres kodowania Y ma pozostać stały.

W kopii miejsca testowego wróć do pustego stanu H00 przed importem i zaimportuj nowy komplet. Nie nakładaj kolejnych eksperymentów na istniejący teren, nie naprawiaj kształtu ręcznie w Roblox. HIP zawiera powiązania parametrów bazowego HeightField i erozji z receptą; produkcyjne dowody eksportu nadal twórz przez jawny przebieg CLI i nowy manifest.

Po H00 podejmujemy H01/H02, następnie sektor Muchawki wraz z masterplanem całego świata. Ten mały spike nie zmienia celu dużego miasta. iPad 6 oraz 16 klientów pozostają wymaganiami późniejszego odbioru; H00 nie nadaje im PASS.

## 7. Co oznacza BLOCKED

Brak hython/licencji/operatora, zmieniony schemat parametrów, niepoprawny raster, pusta klasa materiału, brak działania erozji, inna geometria po reopen lub błędny import kończą właściwy etap jako `BLOCKED`/`FAIL`. Zachowaj log i napraw wskazany etap. Nie instaluj drugiego Houdiniego, nie ruszaj projektu YACS i nie zastępuj krajobrazu baseplate'em.

## Źródła

- [Roblox: terrain, import i paleta RGB](https://github.com/Roblox/creator-docs/blob/main/content/en-us/parts/terrain.md)
- [Roblox: jednostki](https://create.roblox.com/docs/physics/units)
- [Roblox: Studio MCP](https://create.roblox.com/docs/studio/mcp)
- [Roblox: ograniczenia HeightmapImporterService](https://github.com/Roblox/creator-docs/blob/main/content/en-us/reference/engine/classes/HeightmapImporterService.yaml)
- [Roblox: Raycast](https://create.roblox.com/docs/reference/engine/classes/WorldRoot#Raycast)
- [SideFX: HeightField](https://www.sidefx.com/docs/houdini/nodes/sop/heightfield.html), [Erode](https://www.sidefx.com/docs/houdini/nodes/sop/heightfield_erode.html), [Output](https://www.sidefx.com/docs/houdini/nodes/sop/heightfield_output.html)
- [SideFX: hou.Volume](https://www.sidefx.com/docs/houdini/hom/hou/Volume.html), [hou.Geometry](https://www.sidefx.com/docs/houdini/hom/hou/Geometry.html)
- [Oficjalny SideFXLabs, przypięty commit użyty do odczytu parametrów](https://github.com/sideeffects/SideFXLabs/tree/d7cfd09854a0939a912dbd05fcec7a51d8a9975d): `otls/mesh_tiler.hda/labs_8_8Sop_1mesh__tiler/Contents.dir/Contents.mime` oraz `otls/terrain_layer_export.hda/labs_8_8Sop_1terrain__layer__export/Contents.dir/Contents.mime`. Te pliki są referencją schematu natywnych SOP; nie instalujemy ich jako zależności H00.
