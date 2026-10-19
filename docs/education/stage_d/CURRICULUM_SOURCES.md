# Źródła programu, wersje i identyfikatory umiejętności

Sprawdzenie: 2026-10-19. To rejestr źródłowy i projekt mapowania, nie opinia prawna ani zatwierdzenie dydaktyczne wszystkich klas. Punkty skrótowe poniżej zachowują numerację źródeł. Opis lekcji dla klasy 2/3/4 wymaga osobnego osądu pedagogicznego.

## Źródła pierwotne

- **ED26:** [Dz.U. 2026 poz. 378, ELI](https://eli.gov.pl/eli/DU/2026/378/ogl/pol), [PDF ogłoszony](https://dziennikustaw.gov.pl/D2026000037801.pdf). Załącznik 2, Matematyka, Klasy IV–VI, PDF s. 236–243. Wskazane numery stron liczą PDF od 1, nie wewnętrzną paginację załącznika. Odczytano tekst i sprawdzono obrazy stron z arytmetyką, miarami i figurami.
- **ED26-A1:** [Dz.U. 2026 poz. 958](https://eli.gov.pl/eli/DU/2026/958/ogl/pol), [PDF zmiany](https://eli.gov.pl/api/acts/DU/2026/958/text/I/D20260958.pdf). §1 pkt 1 lit. a utrzymuje wdrażanie od I i IV. Nie opierać oceny aktualności wyłącznie na komunikacie marcowym; akt ma zmianę.
- **ED17-ZPE:** [ZPE: edukacja wczesnoszkolna, wersja strony oznaczona 2025/2026](https://zpe.gov.pl/podstawa-programowa/edukacja-wczesnoszkolna). Sekcja II: Edukacja matematyczna. Użyta jako oficjalnie prezentowany tekst wcześniejszego etapu I–III, nie jako nowy rocznik 2026. Do końcowej recenzji zachować numer wersji i porównać właściwe akty zmieniające.
- **ED17:** [Dz.U. 2017 poz. 356](https://eli.gov.pl/eli/DU/2017/356/ogl/pol) z właściwymi zmianami; jego stosowanie przejściowe wskazuje §4 ust.2 ED26. Nie czytać statusu uchylenia bez przepisów przejściowych.

## Rocznik a zakres

Dla 2026/2027: klasa 2 i 3 korzysta z dotychczasowego etapu I–III, klasa 4 z nowej podstawy. Dla 2027/2028 nowa dotyczy już 2 i 4; klasa 3 pozostaje na dotychczasowej. Od 2028/2029 wszystkie nasze klasy 2–4 należą do nowej. Wynika to z §4 ED26 ze zmianą ED26-A1; aktualność sprawdzić ponownie przed publikacją.

Przykładowe identyfikatory techniczne: `PL_2026_27_G2_OLD`, `PL_2026_27_G3_OLD`, `PL_2026_27_G4_NEW`. Nie są nazwami prawnymi. Nie wyliczać roku szkolnego z daty urządzenia dziecka; wersję kontentu publikuje serwer. Zmiana klasy nie kasuje umiejętności ani przygód. Wymagania nowych klas I–III będą osobnym pakietem aktualizacji, nie automatyczną kopią starego.

## Skróty do kart (krótkie mapowanie, nie pełny sylabus)

`O:II.a.b` = ED17-ZPE sekcja II, dział a, punkt b. `N:a.b` = ED26 Matematyka IV–VI, dział a, punkt b.

| skill_id | Zakres projektu | Stary etap I–III | Nowy etap IV–VI |
|---|---|---|---|
| COUNT | Liczenie | O:II.2.1 | arytmetyka, zależnie od zadania N:1.9 |
| ORDER | Porządkowanie liczb | O:II.2.4 | N:1.1 |
| ADD_SUB | Suma/różnica | O:II.3.2, II.3.4 | N:1.9 |
| MULTIPLY_GROUPS | Rzędy/grupy | O:II.3.1, II.3.3 | N:1.10 |
| EQUAL_SHARING | Równy podział | O:II.3.1, II.3.3 | N:1.11 |
| PATTERN | Powtarzalność | O:II.6.1 | ogólne rozumowanie N:6.3, nie osobny zapis o rytmach |
| CLOCK | Zegar/czas | O:II.6.4 | N:2.9 |
| MONEY | Zakup/reszta | O:II.6.3 | N:2.13, N:1.35 |
| LENGTH | Długość/jednostki | O:II.5.2 | N:2.2 |
| SYMMETRY | Odbicie | O:II.5.4 | N:4.12 |
| PERIMETER | Obwód | O:II.5.3 | N:4.15 |
| AREA | Pole prostokąta | brak analogicznego wymogu pola w użytym fragmencie | N:4.14 |
| FRACTION_PART | Połowa/ćwierć | O:II.6.2 | N:1.17 |
| FRACTION_AMOUNT | Ułamek wielkości | NIE utożsamiać z O:II.6.2 | N:1.31 |
| DATA_READ | Odczyt danych | dla prostych ikon oceniaj COUNT/ADD_SUB, nie pełne statystyki | N:5.1 |
| OPEN_CONSTRAINT | Kilka rozwiązań | O:II.4.1–2 | N:6.1, N:6.3 |

Te powiązania są autorską interpretacją zastosowania wymagań do minigier. Wpis punktu oznacza `SOURCE_ANCHOR_IDENTIFIED`, nie `GRADE_APPROVED`. Szczególnie N:4.14 i N:1.31 opisują etap IV–VI: to nie dowód, że formalne pole albo trzy czwarte wielkości należy dać każdemu czwartoklasiście od początku.

## Pola obligatoryjne w recenzji karty

`source_id`, `source_point`, `source_stage`, `school_year_profile`, `grade_recommendation`, `grade_review_status`, `reviewed_task_revision`, `review_date`, `review_reference`, `limitations`. Bez zatwierdzonego zakresu nie oznaczać jako gotowe dla dzieci; syntetyczny test techniczny z dorosłym nie jest takim wdrożeniem.

Gra ma uczyć zastosowania pojęć, a nie wymuszać jedną metodę. Źródło nie wyznacza procentu EXP, liczby sukcesów do mastery ani doboru barw UI. Te liczby są projektem MathCity i wymagają testów, a nie cytowania MEN jako ich autora.
