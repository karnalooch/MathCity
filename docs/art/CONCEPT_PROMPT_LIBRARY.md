# B5 — biblioteka gotowych promptów obrazowych (dla słabego LLM)

**Status:** sześć promptów do porównania + warianty światła, UI i blokery. Prompty NIE są obrazami. Bez generatora zapis `PROMPT_READY_IMAGE_NOT_GENERATED`. Nie dodawaj pustych plików PNG. Właściwości realnych miejsc pochodzą z [SOURCE_REGISTER](SOURCE_REGISTER.md).

## REGUŁA KOMPARATYWNOŚCI

W każdym z dwóch zestawów zmieniasz **wyłącznie** styl S1/S2/S3. Nie zmieniaj perspektywy, kompozycji, geometrii bazowego landmarku, liczby osób, słońca czy layoutu. LLM obrazowy bez zablokowanego seed/reference geometry **może mimo instrukcji zmienić kadr**: oznacz wówczas `COMPARABILITY_LIMITED`, poproś o korektę zamiast uznać wynik za pomiar jakości.

### Stała scena JACEK (prepend identycznie do trzech promptów)

„MathCity, autorska gra Roblox w fikcyjnie przekomponowanych Siedlcach, Polska. Ujęcie frontalne z historycznego rynku, perspektywa z oczu spacerującego awatara (około 35 mm fotograficznego ekwiwalentu, 16:9), neutralne południe, pogodny dzień, stały kierunek słońca. Główny obiekt: ratusz Jacek w Siedlcach, środkowy korpus z bocznymi pawilonami i arkadami, wysoka historyczna wieża z niższą częścią rokokową i górą klasycystyczną, rzeźba Atlasa Jacka na zwieńczeniu, prawdziwy zarys ważniejszy niż fantastyczne dekoracje [L01]. Na placu wyłącznie trzy małe oryginalne, blokowe postaci dla skali; obok niski punkt zagadki z dużym symbolem zegara, nie przyklejony do zabytku. Matowe materiały, czytelne proporcje, brak hiperrealistycznego miasta. Budynek i kamera dokładnie takie same w trzech stylach, **zmieniać tylko drugorzędną architekturę, paletę, materiały i nastrój stylizacji**.”

### Stała scena MUCHAWKA (prepend identycznie)

„MathCity, autorska gra Roblox w Siedlcach, Polska. Perspektywa dziecka stojącego na plaży z promenadą rowerową na pierwszym planie, pomostem w środkowym planie, taflą jednego dużego zbiornika wodnego i naturalną zielenią na horyzoncie, kadr poziomy 16:9, umowny 35 mm ekwiwalentu, neutralny pogodny dzień, identyczny kształt linii brzegowej we wszystkich trzech stylach. Odwołanie do rzeczywistego Zalewu Muchawka jako miejsca spacerów, rowerów i rekreacji [L06]; nie przedstawiać fikcyjnych wysp jako prawdziwe. Trzy nieduże autorskie postaci, przy brzegu dyskretny znak minigry liczenia, bez niebezpiecznych wodnych atrakcji. **W 3 porównaniach zmieniaj tylko styl materiałów, kolorystykę i wtórne prop-y, a nie geografię.**”

## Sześć promptów testowych do bezpośredniego wysłania do generatora

### B1-C01-S1 — Jacek, Słoneczne Neonowe Siedlce
**Input:** Stała scena JACEK + „S1: wesoła pastelowa retro-miejska atmosfera, elewacje kremowe i brzoskwiniowe, turkus dachów i znaków, różowe akcenty tylko punktowo, subtelne ciepłe światło dnia, naturalne drzewa liściaste, matowy bruk, spokojne okna. Ratusz architektonicznie rozpoznawalny. Bez fikcyjnych palm tropikalnych, bez kopii Vice City.”

**Output:** `V02_S1_day_v01.png` (status tylko po prawdziwym generowaniu).

### B1-C01-S2 — Jacek, Bajkowa Przygoda
**Input:** Stała scena JACEK + „S2: czytelna kolorowa grafika przygodowej platformówki 3D, łagodnie zaokrąglone ławki, skrzynie i znak zadania, wyraziste figury, miękkie uproszczone materiały, duża czytelność przy podglądzie 360 px. Historia i sylwetka Jacka bez deformacji. Bez elementów Mario/Nintendo.”

**Output:** `V02_S2_day_v01.png`.

### B1-C01-S3 — Jacek, Signature
**Input:** Stała scena JACEK + „S3: dokładna charakterystyczna sylwetka historycznego ratusza, pastelowy tynk i dachy, wyraźnie stylizowane funkcjonalne elementy gry. Materiały matowe, delikatne światło, neutralne niebo, wysoka czytelność 3D Roblox, 8–11 lat, jednoznacznie siedleckie centrum.”

**Output:** `V02_S3_day_v01.png`.

### B1-N01-S1 — Muchawka, Słoneczne Neonowe Siedlce
**Input:** Stała scena MUCHAWKA + „S1: letni retro-miejski pastel, ciepły piasek i drewniane deski, turkusowy akwen, akcenty różu tylko na drogowskazie i rowerze, autorskie nabrzeże, matowe tekstury, bez tropikalnych resortów.”

**Output:** `V05_S1_day_v01.png`.

### B1-N01-S2 — Muchawka, Bajkowa Przygoda
**Input:** Stała scena MUCHAWKA + „S2: zabawkowe, miękkie formy 3D, wysokie kontrasty ścieżki i brzegu, bezpieczna platformówkowa stacja liczb na SUCHYM brzegu, uproszczona woda i liściaste drzewa; bez zmiany brzegu, bez fikcyjnych wysp udających realne.”

**Output:** `V05_S2_day_v01.png`.

### B1-N01-S3 — Muchawka, Signature
**Input:** Stała scena MUCHAWKA + „S3: naturalna czytelna forma Zalewu Muchawka i mądrze stylizowane pomosty/ścieżki, oszczędne pastele, miękki niebiesko-turkusowy akwen, widoczny piasek i zieleń, nieliczne figury matematyczne tylko przy fikcyjnym punkcie zadania.”

**Output:** `V05_S3_day_v01.png`.

## GLOBALNY NEGATIVE (doklej do KAŻDEGO promptu)

„NO copyrighted game characters or logos, no GTA/Mario assets, no Siedlce official logo without license, no giant palm groves, no Miami skyscraper skyline, no generic castle instead of Ratusz Jacek, no false real geography, no weapons or violence, no unreadable math text, no flashing effects, no huge overexposed neon bloom, no watermarks, no real-life identifiable children, no intrusive advertisements.”

## Światło — trzy osobne prompty porównawcze

**B4-L1:** „Weź `V02_S3_day` i zachowaj absolutnie tę samą kamerę, budynki i postaci. Neutralny czytelny dzień, brak bloom i neonów, naturalny pastel i matowy tynk. Światło jako jedyna zmiana.” → `V02_S3_L1_day_v01.png`.

**B4-L2:** „Ten sam nieruchomy kadr V02 S3; słońce nisko, ciepły brzoskwiniowy golden hour, chłodne cienie, delikatne odbicia; cyfry i Atlas Jacka nadal czytelne, bez przepaleń. Zmień wyłącznie światło.” → `V02_S3_L2_golden_v01.png`.

**B4-L3:** „Dokładnie ten sam kadr V02 S3; spokojna noc z granatowym niebem, stonowane punktowe światła na placu, 1–2 delikatne neony na drodze, bez przesadnego bloom. Czytelne cyfry i sylwetka wieży. Zmień tylko światło.” → `V02_S3_L3_night_v01.png`.

**Dodatkowo:** dla Muchawki analogiczny L2/L3 z `LOCK-N01-A`; dla Sekuły V11/V12 dwie odrębne pory roku, **nie** traktować ich jako identycznej geometrii lub trasy.

## UI V-09: dwa jawnie FIKCYJNE mockupy

**PC:** „Original MathCity Roblox-style UI mockup ONLY, no real screenshot. Wide landscape 1920×1080 design board, simple objective ‘Ustaw godzinę 10:30’, mini map 7 fictional districts, discoverer passport icon, button ‘Podpowiedź’, exit button, bright readable high contrast dark ink on warm cream background, minimal overlay; typography clean Polish diacritics.”

**PHONE:** „The SAME action and text as PC concept, landscape smartphone layout ~19.5:9, keep top safe area clear, bottom-left reserved for thumbstick and bottom-right for Roblox jump, interaction button not overlapping; legible text and clear exit, reduced motion.”

**Ochrona:** nie publikuj mockupów z udawanym oficjalnym logiem Roblox.

## V-13 — BLOKER

Górka Grześ ma niepotwierdzoną lokalizację. **Nie wolno** generować „wiernego widoku prawdziwej Górki”. Wolno przygotować opis i abstrakcyjny moodboard podpisany `FANTASY_SLED_HILL_NOT_GEOREFERENCED`, ale status V13 pozostaje `BLOCKED_GEOLOCATION`.

## Minimalny manifest każdej generacji

~~~text
SHOT_ID: V-02
STYLE_ID: S1
CAMERA_LOCK: LOCK-C01-A
SOURCE_FACTS: L01
TOOL: AI_IMAGE / UNREAL / BLENDER / ROBLOX_SCREENSHOT
USED_SOURCE_PHOTOS: NO / LICENSED_WITH_EVIDENCE
OUTPUT_FILE: docs/art/concepts/V02_S1_day_v01.png
IMAGE_STATUS: GENERATED_CONCEPT / PROMPT_ONLY
GEOMETRY_COMPARABILITY: SAME / LIMITED
LANDMARK_RECOGNITION: PASS / FAIL / NOT_TESTED
COPYRIGHT_CHECK: PASS / FAIL / NOT_TESTED
OWNER_APPROVAL: PENDING
~~~

Jeśli plik nie istnieje, wpisz `OUTPUT_FILE: NOT_CREATED`. Nie używaj manifestu jako dowodu powstania pliku.
