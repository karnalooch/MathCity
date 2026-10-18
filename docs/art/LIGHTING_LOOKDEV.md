# B4 — dzień / golden hour / noc: lookdev i testy

**Status:** DOCUMENTED / NOT_TESTED_IN_ROBLOX. Ujęcie referencyjne LOCK-C01-A z [B1](STYLE_VARIANTS.md); powtórz dla Muchawki LOCK-N01-A, z wariantami zima/lato dla Sekuły.

| ID | Światło i klimat | Cel | Fail |
|---|---|---|---|
| L1 DAY | neutralny dzień, czyste światło, naturalna zieleń | znaki, wieża i drogi czytelne bez efektów | biała elewacja zlewa się z niebem |
| L2 GOLDEN | brzoskwiniowy zachód, różowo-złota poświata, łagodny kontrast | przyjemny klimat zachowując kształt i fakturę | przepalone dachy i tafla wody |
| L3 NIGHT | błękitno-fioletowe niebo, stonowane neony tylko przy drogach / zadaniach | miejski wieczór, widoczny cel i przyjazny nastrój | bloom zasłania cyfry, droga ginie |

### Roblox (parametry do przyszłego testu, nie implementacja)
- `Lighting.LightingStyle`: `Soft` (stylizowany) / `Realistic`; **nie** definiować presetów przez przestarzałe `Lighting.Technology=Future` [R01].
- `PrioritizeLightingQuality`: zmiana priorytetu światła względem dystansu; testować porównawczo na docelowej skali, bez uznawania wartości true/false za obowiązkową [R01].
- `GlobalShadows`, `ClockTime`, `Ambient`, `OutdoorAmbient`, `ExposureCompensation`: opisać dopiero jako warianty; nie narzucać przypadkowych „magicznych” liczb [R01].
- `Atmosphere`: Density, Haze, Glare, Offset, Color, Decay; nadmiar gęstości zasłania odległe landmarki [R02].
- `ColorCorrectionEffect`: delikatny grading; nie wgrywać wypalonych na stałe tekstur albedo [R04].
- `BloomEffect`: Intensity/Size/Threshold; neonowe krawędzie nie mogą uniemożliwiać czytania poleceń [R03].
- Cienie, światła lokalne i mobile: spadki jakości na słabym telefonie są realną możliwością; wymagane przyszłe porównanie [R10,R12].

### Specjalne testy wizualne
- **Muchawka:** DAY pokazuje piasek, groblę, taflę i drogę; GOLDEN nie przepala wody; NIGHT nie robi z prawdziwej Doliny Muchawki wesołego miasteczka [L06,L07,L08].
- **Sekuła LATO:** naturalne zielone drzewa i łatwo odróżnialne leśne ścieżki. **ZIMA:** śnieg, trasy NART BIEGOWYCH, czytelne oznaczenia; brak wyciągu narciarskiego [L12].
- **Miejsca pamięci:** spokojny detal i brak efektów nagrody [L14].
- **C01:** figura Atlasa pozostaje czytelna w każdym świetle; na nocnym ujęciu brak efektu „wybuchającego neonu”.

### Karta światła, do skopiowania i wypełnienia
~~~text
LIGHT_SHOT_ID: L1|L2|L3
CAMERA_LOCK: LOCK-C01-A
SCENE_ASSET_ID: UNCHANGED
LIGHTING_DAYPART:
KEY_LIGHT_DIRECTION:
AMBIENT:
ATMOSPHERE:
TONEMAPPING:
BLOOM:
TOOL: TEXT_ONLY | AI_IMAGE | UNREAL | ROBLOX_STUDIO
OUTPUT_FILE_OR_LINK: NOT_CREATED
MOBILE_CAPTURE: NOT_TESTED
LEGIBILITY_TEST: NOT_TESTED
LANDMARK_VISIBLE: NOT_TESTED
STATUS: DOCUMENTED | RENDERED_CONCEPT | BLOCKED
~~~

**Nigdy** nie wpisuj ROBLOX_STUDIO, jeżeli nie uruchomiono Roblox Studio. Nie podawaj FPS ani zgodności mobile na podstawie renderu UE/AI.
