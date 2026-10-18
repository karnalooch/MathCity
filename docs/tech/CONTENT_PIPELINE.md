# Pipeline: YACS UE / Blender / Material Forge → Roblox

**Status:** propozycja architektury. Nie instalowano ani nie uruchomiono lokalnych narzędzi na potrzeby MathCity. **Roblox to jedyny runtime gry.**

## Podział ról

| Narzędzie | Rola | Nie przenosi do Roblox |
| --- | --- | --- |
| Unreal Engine z warsztatu YACS | wizualizacja światła, layout 3D, blockout, prezentacje dla zespołu | Lumen, Nanite, Blueprinty, pełna logika UE |
| Blender używany w YACS | modelowanie, retopo, UV, triangulacja, LOD i przygotowanie siatek | skrypty Blender, sceny jako runtime |
| Material Forge z YACS | tworzenie palety, stylizowanych PBR, atlasów i tekstur | grafy materiałowe UE jako gotowe shadery Roblox |
| Roblox Studio | import, montaż świata, fizyka, Lighting, instancje, gra, test F5 | render UE i jego systemy |
| Rojo/Git | późniejsza synchronizacja i wersjonowanie Luau | Terrain i części danych MeshPart nie zawsze są synchronizowane wprost |

## Schemat

1. Brief + fotografie i prawa do obrazów.
2. Blockout i ustalona skala sceny w UE/Blenderze.
3. W Blenderze: oczyszczenie geometrii, uproszczenia, UV, pivot, kontrola osi, podział na moduły.
4. Materiały: tekstury PBR / stylizowany kolor / atlasy; test ich czytelności na telefonie.
5. Eksport modelu (preferencyjnie FBX lub glTF; format dopasować do ograniczeń importera).
6. Import do Roblox Studio i przypisanie SurfaceAppearance / materiałów Roblox.
7. Kolizje, zakotwiczenie, streaming i LOD konfigurowane po stronie Roblox.
8. Test F5, klient mobilny, screenshot porównawczy, profiling.
9. Dopiero po PASS asset dostaje etykietę „gotowy do reużycia”.

## Udokumentowane ograniczenia

- Roblox Importer obsługuje modele/siatki FBX, glTF, OBJ i tekstury PBR; obsługa szczegółów zależy od obiektu i importerowej walidacji: [Importer](https://create.roblox.com/docs/studio/importer).
- Pojedynczy mesh nie może przekroczyć 20 000 trójkątów: [General specifications](https://create.roblox.com/docs/art/modeling/specifications). Limit nie oznacza 20 tys. trójkątów na całe miasto.
- UE glTF exporter **nie eksportuje kolizji** i wybiera pojedynczy LOD siatki zamiast przenosić cały komplet: [Epic — glTF exporter](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-the-gltf-exporter-handles-unreal-engine-content).
- Roblox zaleca importowanie elementów mapy oddzielnie i ponowne używanie unikalnych siatek zamiast jednego masowego importu: [Improve performance](https://create.roblox.com/docs/performance-optimization/improve).
- Rojo służy do kodu i modelów, ale Terrain / binaria i niektóre właściwości MeshPart wymagają osobnego procesu: [Rojo — Sync details](https://github.com/rojo-rbx/rojo.space/blob/master/docs/sync-details.md).

## Jednostki i konwencje

Roblox podaje **1 stud = 0,28 m** w standardzie fizycznym. Importer może zachowywać jednostki pliku w zależności od ustawień; nie zakładamy automatycznej zgodności skali UE i Roblox bez testu.

Przed produkcją ustalić:
- kanoniczną jednostkę w Blenderze i Roblox oraz skalę 1:1 na testowym metrze;
- orientację przodu i góry, pivoty, konwencję nazewnictwa;
- maksymalną liczbę materiałów na mały i duży budynek;
- liczbę instancji unikalnych modeli;
- proces aktualizacji assetu i zamiany na istniejącej mapie bez duplikatów;
- idempotentny import i rejestr licencji.

## Proof-of-pipeline: „Jacek, próbka elewacji”

**Jeszcze nie wykonano.** Najpierw sprawdzić faktyczne wersje i ścieżki UE, Blendera i Material Forge w folderach YACS. Nie zakładamy wersji, działania GPU ani licencji na podstawie wspomnień.

Pojedynczy mały fragment rozpoznawalnej fasady Ratusza Jacek + dwie-trzy próbki materiałów:
1. Zbudować jeden model i atlas.
2. Wyeksportować do FBX/glTF.
3. Otworzyć w Roblox Studio, sprawdzić proporcje, materiały, UV, kolizje.
4. Zmierzyć czas importu, liczbę meshów, pamięć, FPS w realnym kliencie.
5. Udokumentować problemy i przeliczyć koszt wykonania 100 modeli tą samą metodą.
6. PASS dopiero po odtwarzalnym imporcie, udokumentowanym materiale i wydajności.

**Nie przenosić materiałów YACS do MathCity bez przeglądu licencji**. Zob. [prawa](../legal/RIGHTS_AND_COMPLIANCE.md) i [testy](PLAYTESTING.md).
