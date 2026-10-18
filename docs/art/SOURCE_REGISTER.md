# Etap B — źródła i fakty do lookdev (aktualizacja 2026-10-19)

**Status:** zweryfikowano strony; zdjęcia na stronach = LINK_ONLY / RIGHTS_UNKNOWN. Nie wolno ich kopiować do repo bez zgody lub licencji. Etap A: [źródła](../world/atlas/SOURCE_EVIDENCE.md), [41 ID](../world/atlas/LANDMARK_CATALOG.md).

## Reguła prawdy dla lekkiego LLM
- REAL: twierdzenie wprost ze źródła + identyfikator poniżej.
- STYLIZATION: zmiana kolorów, brył wtórnych, odległości; to nie fakt o Siedlcach.
- FANTASY: wymyślony pomost, portal, wyspa matematyczna itp.; oznacz jawnie.
- UNKNOWN: brak potwierdzenia; nie zgaduj. RIGHTS_UNKNOWN = nie pobieraj fotografii.
- Fotografia ze strony internetowej nie jest licencją do publikacji. Nie wpisuj `PHOTO_READY` z samym linkiem.
- Starsze ustalenia nie nadpisują 41 kart Etapu A. Konflikt odnotuj jako `NEEDS_REVIEW`.

## Oficjalne / instytucjonalne źródła miejsc

| ID | POI | URL | Fakty istotne dla kadru | Prawa zdjęć |
|---|---|---|---|---|
| L01 | C01 Jacek | https://turystyka.siedlce.pl/118-siedlce-ratusz-miejski | historyczny ratusz, wieża z niższą partią rokokową i górą klasycystyczną, figura Atlasa „Jacka”, boczne pawilony | UNKNOWN |
| L02 | C02 Pałac | https://turystyka.siedlce.pl/139-siedlce-palac-oginskich | klasycystyczny front z portykiem kolumnowym, skrzydła, kontekst pałacowo-parkowy | UNKNOWN |
| L03 | C03 Aleksandria | https://turystyka.siedlce.pl/park-aleksandria | park po rewitalizacji, alejki, pawilon, plac zabaw i ścieżki edukacyjne | UNKNOWN |
| L04 | C04 staw | https://turystyka.siedlce.pl/352-siedlce-staw-w-parku-aleksandria | wyspa, zabytkowa brama-mostek, dwie fontanny | UNKNOWN |
| L05 | C04 mostek | https://turystyka.siedlce.pl/353-siedlce-zabytkowy-mostek | charakterystyczny mostek-brama przy stawie | UNKNOWN |
| L06 | N01 Muchawka | https://turystyka.siedlce.pl/267-siedlce-kapielisko-nad-zalewem-muchawka | kąpielisko, ścieżki rowerowe, dwa place zabaw, rekreacja | UNKNOWN |
| L07 | N02 grobla | https://turystyka.siedlce.pl/264-siedlce-zalew-muchawka-grobla | grobla i kanał, tablica edukacyjna Doliny Muchawki | UNKNOWN |
| L08 | N03 Dolina | https://turystyka.siedlce.pl/274-siedlce-uzytek-ekologiczny-dolina-muchawki | obszar przyrodniczy, oddzielny od kąpieliska | UNKNOWN |
| L09 | S01 Stadion ARMS | https://arm.siedlce.pl/pl/stadion-glowny | stadion piłkarski, boisko 105×68 m, zadaszona trybuna 2901 miejsc, Jana Pawła II 6 | UNKNOWN |
| L10 | S02 Park Wodny | https://arm.siedlce.pl/pl/hala-basenowa | basen sportowy 25×21 m, 8 torów, dwie zjeżdżalnie 48 i 78 m | UNKNOWN |
| L11 | S03 lekkoatletyka | https://arm.siedlce.pl/pl/stadion-lekkoatletyczny | oddzielny stadion, nie S01 | UNKNOWN |
| L12 | N05 biegówki | https://siedlce.pl/aktualnosci/2025/aktualnosci-01-2025/trasy-narciarstwa-biegowego-w-siedlcach/show | na Sekule są trasy narciarstwa BIEGOWEGO, nie stok zjazdowy | UNKNOWN |
| L13 | N06 las edukacyjny | https://siedlce.warszawa.lasy.gov.pl/oferta-edukacyjna/-/asset_publisher/kCS6/content/obiekty-edukacyjne | źródło do dalszej weryfikacji ścieżki edukacyjnej; nie dopowiadać trasy | UNKNOWN |
| L14 | Sekuła, miejsca pamięci | https://pttksiedlce.pl/siedlecki-klub-turystyki-pieszej-i-nordic-walking-wloczy-kije-17-05-2026r-sekula/ | obszary pamięci i pochówków wymagają wyłączenia zabawy | UNKNOWN |

**N07 Górka Grześ: GEO_LOCATION_OPEN**. Bez potwierdzonej lokalizacji nie można robić „wiernej panoramy” ani rzekomo realnego stoku. **S01 ≠ S03**, **N01 ≠ S02**, **N05 ≠ N06**.

## Roblox Creator Hub, stan na dzień researchu

| ID | URL | Potwierdzona zasada |
|---|---|---|
| R01 | https://create.roblox.com/docs/environment/lighting | `LightingStyle` Soft/Realistic, `PrioritizeLightingQuality`, ClockTime, GlobalShadows; `Lighting.Technology` to starszy/deprecated kierunek |
| R02 | https://create.roblox.com/docs/environment/atmosphere | Atmosphere: Density/Offset/Haze/Glare/Color/Decay; dalekie landmarki mogą zniknąć |
| R03 | https://create.roblox.com/docs/reference/engine/classes/BloomEffect | Intensity, Size, Threshold; glow nie może zjadać cyfr |
| R04 | https://create.roblox.com/docs/reference/engine/classes/ColorCorrectionEffect | Saturation, Contrast, TintColor i artystyczny grading |
| R05 | https://create.roblox.com/docs/art/modeling/specifications | 20 000 trójkątów na **pojedynczy** mesh, nie na całe miasto |
| R06 | https://create.roblox.com/docs/art/modeling/texture-specifications | jeden materiał / mesh, UV 0–1, OpenGL tangent normal, mapy PBR; budżety tekstur wymagają testu |
| R07 | https://create.roblox.com/docs/art/modeling/surface-appearance | pięć map PBR: Color, Normal, Roughness, Metalness, Emissive Mask |
| R08 | https://create.roblox.com/docs/studio/importer | FBX, glTF i OBJ do importu 3D; szczegóły zależą od formatu |
| R09 | https://create.roblox.com/docs/art/blender | Blender Z-up / Roblox Y-up; jawna walidacja osi i skali |
| R10 | https://create.roblox.com/docs/performance-optimization/improve | streaming instancji, SLIM, RenderFidelity, reuse zasobów i tekstur |
| R11 | https://create.roblox.com/docs/performance-optimization/design | wiele Places bywa alternatywą; teleporty kosztują ładowanie |
| R12 | https://create.roblox.com/docs/performance-optimization/identify | fps/RAM/load mierz w kliencie; Studio może fałszować pomiar |
| R13 | https://create.roblox.com/docs/ui/position-and-size | mobile thumb zones i obszary zarezerwowane pod skok/joystick |
| R14 | https://create.roblox.com/docs/reference/engine/classes/ScreenGui | ScreenInsets, CoreUISafeInsets i obszary bezpieczne |
| R15 | https://create.roblox.com/docs/production/publishing/accessibility | kontrast, ikonografia poza kolorem, sygnały także wizualne, reduced motion |
| R16 | https://create.roblox.com/docs/studio/device-simulator | Device Simulator w beta, nie zastępuje telefonu |
| R17 | https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/implement-designs-in-studio | testy UI na wielu proporcjach i rozdzielczościach |

## Pipeline, prawa

| ID | URL | Wniosek |
|---|---|---|
| P01 | https://dev.epicgames.com/documentation/en-us/unreal-engine/how-the-gltf-exporter-handles-unreal-engine-content | UE glTF pomija kolizje, eksportuje pojedynczy LOD zamiast wszystkich |
| P02 | https://www.fab.com/eula | Fab Standard pozwala na kompatybilne silniki, ale zakazuje dystrybucji surowego assetu osobno; starsze licencje audytować |
| P03 | https://github.com/rojo-rbx/rojo | Synchronizacja kodu, nie automatyczny pełny świat Roblox |

## Ostrożnie z liczbami

- Roblox dokumentuje obsługę tekstur 4K ogólnie, ale w części UV także rekomendacje/limit przestrzeni map do 1024. **Nie ustawiaj 4K jako domyślnego budżetu**, mierz w klientach i dobieraj minimalny rozmiar.
- Dla projektu Art Bible brak sprawdzenia PC/telefonu i renderowania oznacza `NOT_TESTED`, a nie PASS.
- Link potwierdza możliwość OBEJRZENIA zdjęcia, nie prawo jego pobrania, publikacji i przerobienia.
- Podawaj [Lxx] przy fakcie lokalnym, [Rxx] przy technologii, [Pxx] przy pipeline. Znaczenie ID stabilne w tym pliku.
