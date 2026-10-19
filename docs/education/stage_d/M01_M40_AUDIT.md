# Audyt M01–M40: zakres, korekty i kolejność

2026-10-19. Źródło projektu: [MECHANICS_MATRIX](../../world/atlas/MECHANICS_MATRIX.md) na bazie `030c863`. Punkty O/N: [CURRICULUM_SOURCES](CURRICULUM_SOURCES.md). Audyt jest analizą dokumentacji, nie testem gry. Wszystkie przypisania klasy mają **TEACHER_REVIEW_PENDING**.

Disposition: `PILOT` = rekomendowana pierwsza ósemka; `LATER` = zachować po pilotach; `SIMPLIFY` = potrzebna konkretna korekta; `HOLD_GRADE` = formalny zakres oczekuje recenzji; `HOLD_GEO` = brak miejsca. Żaden status nie jest zgodą na implementację teraz. ID pozostają M01–M40.

| ID / miejsce | Próbka i wynik | Umiejętność / punkty | Disposition / wymagane działanie |
|---|---|---|---|
| M01 C01 | 09:20 + 15 min = 09:35 | CLOCK O:II.6.4; N:2.9 | PILOT. Ruch obu wskazówek; bez limitu czasu. |
| M02 C02 | Cztery okna mają cztery odbicia | SYMMETRY O:II.5.4; N:4.12 | PILOT. **Korekta:** liczba4 sama nie dowodzi symetrii; walidować pozycje. |
| M03 C03 | R,Y,R,Y,R → Y | PATTERN O:II.6.1 | LATER. Dodać figury/ikony i polskie podpisy; nie tylko barwy. |
| M04 C04 | 8−3 = 5 kafli | ADD_SUB O:II.3.2; N:1.9 | LATER. Liczenie brakujących elementów, nie formalne dzielenie. |
| M05 N06 | 8 stacji − 3 odkryte = 5 | COUNT/ADD_SUB O:II.2.1, II.3.2; N:1.9 | PILOT. Zbiór unikalnych ID odkryć, nie liczba wejść w trigger. |
| M06 N05 | 4×25 = 100 m | MULTIPLY_GROUPS/LENGTH O:II.3.3, II.5.2; N:1.10, N:2.2 | SIMPLIFY. Start4×5; suma czterech25 w wyższym wariancie. Biegówki, nie stok. |
| M07 N05 | 2:40−2:15 = 25 s | CLOCK O:II.6.4; N:2.9 | LATER. Analiza gotowych wyników bez presji; stoper sportu oddzielny. |
| M08 N07 | 70−45 = 25 m, B krótsza | LENGTH/ADD_SUB O:II.5.2, II.3.4; N:2.2, N:1.9 | HOLD_GEO. Fikcyjna plansza dopuszczalna, bez zgadywania współrzędnych Grześ. |
| M09 S02 | 4 długości × 25 m = 100 m | MULTIPLY_GROUPS/LENGTH O:II.3.3, II.5.2; N:1.10 | SIMPLIFY. Długość basenu ≠ okrążenie; bez instrukcji realnego pływania. |
| M10 S02 | 78−48 = 30 m | ADD_SUB O:II.3.4; N:1.9 | LATER. Paski mają wspólny początek; jawny cel porównania. |
| M11 S02 | 8÷2 = 4 tory | EQUAL_SHARING O:II.3.1, II.3.3; N:1.11 | LATER. Dwie grupy torów, nie dwie obowiązkowe osoby. |
| M12 S02 | 48+78 = 126 m | ADD_SUB O:II.3.4; N:1.9 | SIMPLIFY. Wyższy wariant rachunku. Zmienionych liczb nie nazywać realnymi parametrami obiektu. |
| M13 S01 | 6×4 = 24; otwarty wariant12 krzeseł | MULTIPLY_GROUPS/OPEN_CONSTRAINT O:II.3.3, II.4.1; N:1.10, N:6.3 | PILOT. Kilka poprawnych prostokątów z jawnymi granicami. |
| M14 S01 | 105×68 = 7140 m² | AREA N:4.14 | HOLD_GRADE. Poprawny, ale trudny rachunek; mały model6×4 jako późniejsza alternatywa. |
| M15 S03 | Co2: 2,4,6,8 → 10 | COUNT O:II.2.1 | LATER. Wskazać zasadę, bo sam skończony ciąg nie określa jednej kontynuacji. |
| M16 S10 | 10−4 = 6 kręgli | ADD_SUB O:II.3.2; N:1.9 | LATER. Utrwalić stan po rzucie przed pytaniem; matematyka nie wymaga zręczności. |
| M17 S06 | 3×4 = 12 ślizgów | MULTIPLY_GROUPS O:II.3.3; N:1.10 | LATER. Fikcyjne serie, bez instrukcji realnych trików. |
| M18 S04 | 4×5 = 20 pkt | MULTIPLY_GROUPS O:II.3.3; N:1.10 | LATER. Punkty ćwiczenia ≠ EXP; dostępna alternatywa dla trudnego obby. |
| M19 S05 | 6×3 = 18 | MULTIPLY_GROUPS O:II.3.3; N:1.10 | SIMPLIFY. Bez drzwi śmierci; spokojne rozumowanie przed skokiem. |
| M20 C13 | 10−4−3 = 3 | MONEY O:II.6.3; N:2.13 | LATER. Reużyj M33; budżet zadania odrębny od portfela. |
| M21 C14 | 35,12,21 → 12,21,35 | ORDER O:II.2.4; N:1.1 | PILOT. Nie dawaj zawsze już posortowanego wejścia. Adresy fikcyjne. |
| M22 T01 | 12:15 + 30 min = 12:45 | CLOCK O:II.6.4; N:2.9 | LATER. Reużyj M01; fikcyjny, nie rzeczywisty rozkład PKP. |
| M23 C03 | 3×5 = 15 kwiatów | MULTIPLY_GROUPS O:II.3.3; N:1.10 | LATER. Reużyj układ M13, bez dublowania generatora. |
| M24 N01 | 12÷3 = 4 belki | EQUAL_SHARING O:II.3.3; N:1.11 | LATER. Reużyj M34; grupowanie elementów ≠ ułamek powierzchni tratwy. |
| M25 N01 | 3/4 z8 = 6 pól | FRACTION_AMOUNT N:1.31 | HOLD_GRADE. Osobny prostszy wariant połowy, nie automatyczna etykietaG3. |
| M26 N12 | 250+250+500 = 1000 m = 1 km | LENGTH/ADD_SUB O:II.5.2, II.3.4; N:2.2, N:1.9 | LATER. Obliczenia i przejazd osobno; teleport nie zalicza odcinków. |
| M27 N03 | 2+3+5 = 10 ikon | COUNT/ADD_SUB O:II.2.1, II.3.2; N:1.9 | LATER. Dane potwierdzone ponownym odczytem karty; plansza poza terenem chronionym, nie pogoń za ptakami. |
| M28 C11 | 3 odbicia, 6 razem | SYMMETRY O:II.5.4; N:4.12 | SIMPLIFY. Odbicie pozycji jak M02, nie tylko liczba kwadratów. Własna mozaika. |
| M29 C10 | Co2: 2,4,6,8 → 10 | COUNT/PATTERN O:II.2.1, II.6.1 | LATER. Sekwencja czytelna bez dźwięku i timingu odpowiedzi. |
| M30 C15 | Niebieski/róż naprzemiennie → niebieski | PATTERN O:II.6.1 | LATER. Symbol przy każdym kolorze; ograniczyć migotanie. |
| M31 C16 | 5×3 = 15 miejsc | MULTIPLY_GROUPS O:II.3.3; N:1.10 | LATER. Fikcyjny model, nie pomiar widowni; reużyj M13. |
| M32 N08 | 2+4+6 = 12 ikon | DATA_READ/ADD_SUB O:II.3.2; N:5.1 | LATER. Legenda/skala jawna; bez wejścia do rezerwatu. |
| M33 N01 | 20−7−5 = 8 | MONEY O:II.6.3; N:2.13 | PILOT. Model pieniędzy, nigdy wydawanie majątku dziecka za rozwiązanie. |
| M34 N01 | 12÷3 = 4 na sekcję | EQUAL_SHARING O:II.3.1, II.3.3; N:1.11 | PILOT. Generator n=g×q; kontrola kompletu i unikalnychID desek. |
| M35 N12 | 200+150+250 = 600 m | LENGTH/ADD_SUB O:II.5.2, II.3.4; N:2.2, N:1.9 | PILOT. Matematyka przed przejazdem, dane planu zamiast przypadkowego GPS. |
| M36 N01 | 09:35 + 25 min = 10:00 | CLOCK O:II.6.4; N:2.9 | LATER. Przejście pełnej godziny, reużycie M01. |
| M37 N01 | 100+400+200 = 700 m | ADD_SUB/LENGTH O:II.3.4, II.5.2; N:1.9, N:2.2 | LATER. Sport w grze nie jest instrukcją bezpieczeństwa realnego triathlonu. |
| M38 N01 | 3/4 z12 = 9 | FRACTION_AMOUNT N:1.31 | HOLD_GRADE. WeryfikacjaG4; młodszym oddzielny wizualny podział. |
| M39 N01 | Prostokąt6×4: obwód20 m, pole24 m² | PERIMETER O:II.5.3/N:4.15; AREA N:4.14 | SIMPLIFY + HOLD_GRADE dla pola. Dwa odrębne cele, nie mieszać jednostek. |
| M40 N03 | 4+6+3 = 13 ikon | COUNT/ADD_SUB O:II.3.2; N:5.1 przy wykresie | LATER. Fikcyjne obserwacje, nie liczebność prawdziwych gatunków. |

## Osiem rekomendowanych pilotów

M01, M02, M05, M13, M21, M33, M34, M35. Obejmują czas, symetrię, liczenie, rzędy, porządkowanie, zakupy, podział i długość. Kolejność produkcji nie jest kolejnością szkolnego sylabusa. M34 to pierwszy proponowany test techniczny; prostsze odkrywanie ikon może inspirować onboarding, bez przenoszenia N06 do centrum miasta.

## Wspólne korekty przed wdrożeniem

Nie przenosić dawnego „3 próby, potem automat pokazuje wszystko” jako bezwzględnej reguły. UI proponuje pomoc, a uczeń może kontynuować; guided nie wykonuje całego zadania za niego. Przypadkowy drop, utrata internetu i anulowanie nie są błędami matematycznymi. Nie nadawać etykietyG4 na podstawie samej poprawności rachunku. Liczby zadania i prawdziwa informacja o miejscu są oddzielnymi danymi.

M27 doprecyzowano po odczycie oryginalnej karty: grupy2,3,5. Wszystkie40 wierszy mają teraz jawny model przykładu. Dla M02 i M28 poprawność symetrii wymaga położeń; szczegółowe pozycyjne dane pilota są w karcie M02. Próbki w tabeli nie dowodzą skuteczności dydaktycznej. M08 nadal geograficznie zablokowany, a tematy HOLD_GRADE nie są gotowym kursem dla klasy4.
