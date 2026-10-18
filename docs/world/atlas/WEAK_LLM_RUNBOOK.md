# MathCity — ETAP A: instrukcja wykonawcza dla słabszego LLM

**Wersja 1.0 / 2026-10-18.** Czytaj W CAŁOŚCI. Ten plik jest kontraktem dla agenta badawczego i ilustratora. **NIE IMPLEMENTUJ** gry, nie uruchamiaj importów ani nie zmieniaj pliku `MathCity.rbxl`. Na tym etapie pracujemy nad referencjami i planem, nie produkcją świata.

## 0. Jednoznaczna misja

Projekt MathCity w repo `karnalooch/MathCity` ma być ogromnym, otwartym miastem Roblox inspirowanym Siedlcami, nie odtworzonym 1:1. Odbiorcy to uczniowie klas 2–4. Miasto ma promować rzeczywiste miejsca i dawać radosne minigry matematyczne. **User specifically demands:** Las Sekuła, **trasy NARCIARSTWA BIEGOWEGO**, lokalna „Górka Grześ”, stadion i basen z pełnym potencjałem mechanicznym. To wymagania, nie dodatki do usunięcia w optymalizacji.

## 1. Co jest prawdą, a co propozycją?

- **FAKT** tylko wtedy, gdy wiąże się z konkretną stroną źródłową i dotyczy dokładnie tego obiektu.
- **LOKALNA NAZWA OD WŁAŚCICIELA** (np. „Górka Grześ”) to autentyczny wymóg kreatywny, lecz bez pewnej geolokalizacji. Zachowaj nazwę, wpisz BLOKER pin.
- **HIPOTEZA**: fikcyjne dzielnice, basenowe gry, fantasy wzgórze, rozmieszczenie ulic, nagrody, kolory.
- **NIEPOTWIERDZONE**: dokładna lokalizacja Grześ, trasa GPS nart, adres wejścia do Parku Wodnego, prawo do cudzych fotografii.
- **BRAK DOWODU** nie oznacza NIE ISTNIEJE. **NIE WOLNO** dopełnić braków zgadywaniem.

## 2. Gdzie co zapisać

| Cel | Dokładna ścieżka | Co ma zawierać |
| --- | --- | --- |
| Indeks researchu A | `docs/world/STAGE_A_README.md` | status, linki i gate |
| Tabela wszystkich punktów | `docs/world/atlas/LANDMARK_CATALOG.md` | stabilne ID, kategoria, źródła, uwagi |
| Karty architektury | `docs/world/atlas/CITY_CARDS.md` | sylwetka, foto, mechanika, ograniczenia |
| Karty natury | `docs/world/atlas/NATURE_CARDS.md` | las, narciarstwo, Grześ, woda, ochrona |
| Karty sportowe | `docs/world/atlas/SPORT_CARDS.md` | 2 stadiony, basen, parkour, skate, lód |
| Linki zdjęć | `docs/world/atlas/PHOTO_REFERENCES.md` | źródła, wymagane kadry, licencja/autor |
| Matematyka w lokacjach | `docs/world/atlas/MECHANICS_MATRIX.md` | 32 kandydatów, wyniki, feedback |
| Granice prawne/etyczne | `docs/world/atlas/CONSERVATION_AND_RESPECT.md` | zakazy, miejsca pamięci |
| Słownik źródeł | `docs/world/atlas/SOURCE_EVIDENCE.md` | źródła pierwotne i konflikty |
| Finał prac | `docs/planning/RESEARCH_ROADMAP.md` | zaznaczenie etapów i pozostałe blokery |

**Nie dokładaj chaotycznych plików JSON ani dziesiątek kopii GDD.** Dodawaj i rozwijaj istniejące karty przez te same ID.

## 3. Procedura pracy nad JEDNYM miejscem (nie przeskakuj)

**Krok 1: ID**. Znajdź identyfikator w `LANDMARK_CATALOG.md`. Jeśli nie ma, zaproponuj nowe ID z nieużywanym numerem, dopisz do rejestru i podaj uzasadnienie.

**Krok 2: Źródło**. Otwórz co najmniej jedno źródło pierwotne (miasto, ARMS, Nadleśnictwo, instytucja). Jeśli niedostępne, wpisz `SOURCE_UNAVAILABLE` i nie twierdź, że tekst został przeczytany. Dodatkowe portale turystyczne i społeczność traktuj pomocniczo. Dla konkurencyjnych opisów wskaż różnice.

**Krok 3: Fact sheet**. Zapisz dosłownie w polu osobnym: nazwa, region, adres tylko potwierdzony, przeznaczenie obiektu, **faktyczne** wymiary jeśli źródło je podaje, sygnaturę bryły. Każda liczba musi być opisana realna/fikcyjna.

**Krok 4: Referencje**. Dodaj wyłącznie URL do legalnie oglądalnej strony zdjęciowej i shot list: panorama, front, detal, otoczenie, pora/sezon. Osobno zapisz `copyright_owner`, `licence`, `permission` jako `UNKNOWN`, jeśli nie sprawdzono. **Nie pobieraj** automatycznie zdjęć z portali.

**Krok 5: Rozpoznawalność**. Opisz 3–5 elementów, które mieszkaniec musi poznać. Np. Jacek = wieża z Atlasem, nie „losowy biały pałac”; park Aleksandria = historyczny park, a nie tropikalna dżungla.

**Krok 6: Adaptacja fantasy**. W osobnej części wypisz co wolno swobodnie zmienić (dystans, łączniki, kolory, kształt ruchu), a czego nie wolno przedstawiać jako rzeczywisty stan miasta.

**Krok 7: Mechanika**. Zaproponuj co najmniej jedną aktywność: wejście → cel → działanie gracza → odpowiedź matematyczna → wskazówka przy błędzie → drobna bezpieczna nagroda → powrót do świata. Wpisz ID minigry z `MECHANICS_MATRIX.md`.

**Krok 8: Poziom edukacyjny**. Oznacz G2/G3/G4 wyłącznie jako `PROPOSED`. **Nie wpisuj `MEN_APPROVED`** bez cytatu z odpowiedniej podstawy i kontroli nauczyciela.

**Krok 9: Ryzyka**. Sprawdź czy obiekt jest rezerwatem, miejscem pamięci, świątynią, terenem wojskowym, prywatną własnością albo w okolicy ruchu pojazdów. Przypisz `SPORT_ALLOWED_FANTASY`, `EDUCATION_ONLY` lub `RESTRICTED`.

**Krok 10: Akceptacja**. Karta przechodzi `FACT_RESEARCHED` tylko po źródle; przechodzi `PHOTO_READY` po zdjęciach i prawach; przechodzi `DESIGN_READY` dopiero po zatwierdzeniu. Odróżniaj te poziomy w każdym raporcie.

## 4. Sześć obowiązkowych, niepomijalnych kart

1. **N01 ZALEW MUCHAWKA**: Otwórz [pełną kartę N01](MUCHAWKA_FEATURE.md). Zalew to główna rekreacyjna strefa MathCity (plaża, pomost, rowery, grobla, fantasy wyspy, triathlon fantasy) oraz **12 powiązanych minigier M24–M27, M33–M40**. Nie myl z krytym Parkiem Wodnym `S02`; nie zamieniaj 54 m brzegu **kąpieliska** na obwód całego akwenu; nie zmieniaj chronionej Doliny Muchawki `N03` w tor wyścigowy. **Każda liczba gry jest FIKCYJNA** poza faktami jawnie opisanymi źródłem.
2. **N05 trasy narciarskie Sekuła**: sport to **biegówki**, miasto podaje Domanicka 71. **Nie** automatycznie wyciąg narciarski i skoki. **Nie** przypisywać narciarskim torom 2,1 km ścieżki N06. Przyda się realny ślad trasy lub odpowiednie zdjęcia zimowe.
3. **N07 Górka Grześ**: nazwa i pomysł użytkownika. Punkt Grześ w trasach pod Rakowcem nie jest wystarczającą identyfikacją. **Bez potwierdzenia pinu przez mieszkańca nie geokodować**, nie wymyślać wysokości ani nachylenia. Gry saneczkowe / geometrii dopiero jako fantasy propozycja.
4. **S01 Stadion ARMS**: boisko **105×68 m**, **2901 miejsc**. Stadion futbolowy na Jana Pawła II 6. Nie myl z S03.
5. **S02 Park Wodny**: **8 torów, 25×21 m, zjeżdżalnie 48/78 m**, część rekreacyjna i kręgielnia. Oddzielny numer adresowy wejścia do ustalenia. Gry cyfrowe nie stanowią instrukcji rzeczywistego pływania.
6. **S03 stadion lekkoatletyczny**: oddzielny kompleks przy **Prusa 6**, z bieżnią. Są tam również S04 skateplaza, S05 Parkour Park i S06 lód/rolki.

## 5. Krótkie gotowe przykłady do kodowania karty

**DOBRZE:**
- „Miejski portal 25.02.2025 potwierdza trasy nart biegowych w Sekule na Domanickiej 71 [URL]. W grze zaproponowano trzy wirtualne odcinki po 25 m; ich suma to 75 m. Liczba odcinków i długość są fikcyjne”.
- „Górka Grześ została zgłoszona przez właściciela; brak potwierdzonego pinu; N07.status=LOKALIZACJA_DO_WERYFIKACJI”.
- „Krzyż na Błoniach zostaje symbolem miejsca pamięci; sportowe obby odsunięte do nowej fikcyjnej strefy”.

**ŹLE:**
- „Trasa Sekuła ma zawsze 2,1 km, bo tak mówi Las Państwowy” (miesza ścieżkę i narciarstwo).
- „Górka Grześ na pewno jest przy strzelnicy wojskowej” (nie potwierdzono).
- „Basen przy Jana Pawła II 6 ma wejście nr 6” (może to adres operatora).
- „Stadion ma 2901 miejsc i 400-metrową bieżnię” (miesza S01 i S03).
- „Jest pozwolenie na zdjęcia z miejskiego portalu” (samo opublikowanie zdjęcia nie daje praw).

## 6. Prompty pomocnicze do późniejszego delegowania

**PROMPT-MUCHAWKA:** „Zanim odpowiesz o zalewie otwórz `docs/world/atlas/MUCHAWKA_FEATURE.md` i `docs/education/CURRICULUM_2_4.md`. Wykorzystaj ID N01/N02/N03/N12 oraz M24–M27/M33–M40. Rozdziel realne fakty od wymyślonych wysp, podaj konkretne zadania z wynikiem, oznacz brak legalnych fotografii. Nie ruszaj gry.”

**PROMPT-FACTS:** „Pracuj wyłącznie na dokumentacji `docs/world/atlas/`. Dla ID [POI] sprawdź oficjalny URL, podaj wszystkie fakty z dowodem, oddziel hipotezy, wypisz brakujące zdjęcia. Nie generuj kodu, modeli ani plików poza docs.”

**PROMPT-ART:** „Dla ID [POI] przygotuj opis 3 kadrów, cytując 3 cechy prawdziwej sylwetki. Zachowaj nasz art bible, ale dodaj tylko autorskie elementy. Nie kopiuj fotografii ani znaków i nie przypisuj grafice statusu zdjęcia miejsca.”

**PROMPT-EDU:** „Dla minigry [M-ID] przeanalizuj przykład, matematyczny wynik, poziom poznawczy, 3 stopnie podpowiedzi i 5 testów akceptacji. Nie deklaruj oficjalnej zgodności MEN bez źródła.”

**PROMPT-QA:** „Sprawdź, czy uaktualnienie dokumentacji nie modyfikuje `MathCity.rbxl`, `src/`, `assets/`. Zweryfikuj identyfikatory, linki, brak fikcyjnych współrzędnych, rozbieżności N05/N06/N07 i S01/S03/S02. Brak dowodu oznacz jako OPEN.”

## 7. Wzorcowy raport z prac nad jedną kartą

```text
POI_ID: N05
NAME: Trasy narciarstwa biegowego Sekuła
SOURCE_STATUS: PRIMARY_VERIFIED
SOURCE_URL: https://siedlce.pl/aktualnosci/2025/aktualnosci-01-2025/trasy-narciarstwa-biegowego-w-siedlcach/show
ADDRESS: Domanicka 71, Siedlce
REAL_FACTS: narciarstwo biegowe; styl klasyczny i dowolny
PHOTO_STATUS: REFERENCE_LINK_ONLY
PHOTO_LICENSE: UNKNOWN
GEOMETRY_GPS_STATUS: UNKNOWN
FANTASY_IDEA: matematyczne biegi + letnia gra ruchowa po fikcyjnej pętli
EDUCATION_STATUS: PROPOSED_G2_G3
ETHICS_GUARD: KEEP_OUT_OF_MEMORIAL_ZONES
NEXT_ACTION: uzyskać legalne zdjęcia trasy i zweryfikować GPX
STAGE_A_STATUS: OPEN_PHOTOS
```

## 8. Gate i raport dla właściciela

| Gate | Akceptacja | Teraz |
| --- | --- | --- |
| A0 Lista lokacji | Minimum 20 ID, źródło z linkiem, sport/las/basen/Grześ obecne | **WYKONANE: 41 kandydatów** |
| A1 Fakty | Konkretne źródła dla priorytetu A, żaden fałszywy adres | **CZĘŚCIOWO, konflikty odnotowane** |
| A2 Fotografie | Min. trzy kadry własne lub legalne na każdy A; jawne autorstwo | **OPEN** |
| A3 Masterplan | Logika połączeń Siedlec, transport i oddzielne strefy ochrony | **SZKIC, NIEZATWIERDZONY** |
| A4 Mechanika | Każdy A ma przynajmniej 1 minigrę koncepcyjną | **SZKIC 40 minigier** |
| A5 Weryfikacja mieszkańca | Użytkownik potwierdza przede wszystkim Górkę Grześ i widoki ikon | **OPEN** |
| A6 Akceptacja prawna | Audyt zdjęć i symboli miasta przed użyciem assetów | **OPEN** |

Etap A **nie jest PASS**, mimo obszernego researchu. Uczciwe raportowanie braków ma większą wartość niż sztuczne „DONE”.

## 9. Granica odpowiedzialności słabszego LLM

Nie pobiera assetów z YACS, nie pisze Luau, nie edytuje levelu, nie wysyła w ciemno do Roblox Open Cloud, nie publikuje doświadczenia i nie przerabia planu projektu bez zatwierdzenia. **Jeśli nie wiesz, wpisz DO WERYFIKACJI i wskaż jak sprawdzić.**

[Indeks Etapu A](../STAGE_A_README.md) | [Baza 41](LANDMARK_CATALOG.md) | [Źródła](SOURCE_EVIDENCE.md).
