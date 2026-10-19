# M34: Pomost Równych Desek

Status: SPEC_READY, TEACHER_REVIEW_PENDING, CODE_NOT_STARTED. Miejsce N01, fikcyjny pomost Muchawki. skill EQUAL_SHARING; O:II.3.1/3.3 i N:1.11 z [rejestru](../CURRICULUM_SOURCES.md). To model matematyczny, nie instrukcja realnej budowy ani wejścia na zalew.

## Cel i stan początkowy

Instrukcja: **„Rozłóż wszystkie 12 desek na 3 sekcje. W każdej ma być tyle samo.”** Na scenie trzy szerokie oznaczone sekcje A/B/C i 12 numerowanych wewnętrznie obiektów. UI nie pokazuje liczby 4 jako celu. Każda deska ma niezmienne ID; do manipulacji nie potrzebuje fizyki swobodnego spadania. Na niskiej grafice wszystkie deski, sekcje i podświetlenia pozostają widoczne.

Dziecko dotyka deski, potem sekcji; przeciągnięcie jest alternatywą. Zły drop wraca na tacę bez błędu matematycznego. „Cofnij” cofa ostatnie własne przełożenie. „Sprawdź” wykonuje jedną walidację. Wskaźnik umieszczonych sztuk może pokazywać postęp techniczny; nie wyrównuje automatycznie grup.

## Walidator

Poprawne wyłącznie, gdy zbiór ID na sekcjach jest dokładnie zbiorem wszystkich n desek, każda występuje raz, nie ma obcych ID, sekcji jest g, a każda ma n/g elementów. Dla n=12,g=3 jedyny wektor liczebności to [4,4,4], lecz kolejność samych desek jest dowolna. [5,4,3] jest niepoprawne mimo sumy12; [4,4,3] niekompletne; powtórzone ID jest błędem danych, nie błędem liczenia dziecka.

Wynik formalny q nie jest jedynym wejściem: w tym wariancie sprawdzamy rzeczywisty rozdział obiektów. Oddzielny wariant pytania liczbowego wymaga oddzielnego renderera, nie udawania, że wpisane4 dowodzi konstrukcji.

## Generator i poziomy robocze

B0: g=2,q∈{2,3,4}. B1: g∈{2,3},q∈{2,3,4,5}. B2: g∈{2,3,4},q∈{2,3,4,5,6}; zawsze n=g×q≤24. Ręczny pierwszy przykład12/3. Cała unikalna domena B2:15 par. Bandy są projektem do review, nie sztywnymi klasami szkolnymi. Przykłady:8/2→4;15/3→5;24/4→6. Przy g=0, n niezgodnym z g×q lub liczbie>24 nie pokaż zadania; użyj zatwierdzonego zapasowego12/3 i zapisz błąd generatora.

## Podpowiedzi

UI_HELP: animowana dłoń przenosi neutralny klocek na dowolne stanowisko demonstracyjne, nie rozwiązuje bieżącego problemu. MATH_HINT1: „Porównaj sekcje. Czy w każdej jest tyle samo?”. HINT2: pokaż parowanie pierwszej deski każdej grupy bez ujawnienia całego wyniku. GUIDED: dziecko układa po jednej do A/B/C; powtarza serie aż taca pusta; porównuje grupy; dopiero wtedy pokazujemy zapis12÷3=4. Nie wykonuj całego rozdziału przyciskiem „Gotowe”. Podstawowa nagroda nie maleje.

Po [5,4,3] komunikat „W sekcjach jest różna liczba desek. Możesz je przełożyć.” Bez dźwięku porażki, resetu sceny, utraty punktów. Po ujawnieniu strategii zapis ASSISTED. Kolejne niezależne zadanie na innych liczbach może sprawdzić samodzielność.

## Solo i 2–4 osoby

Każdy ma osobistą małą sekcję roboczą/porcję pomostu i własny wariant. Do świata trafia efekt ukończenia jego porcji, nie prywatne odpowiedzi. Nie rozdawaj tej samej deski czterem osobom. Solo potrzebuje jednej kompletnej porcji, nie czterech cudzych ról. W większej grupie porcje powstają równolegle. Odejście partnera nie zeruje poprawnych porcji; nowe osoby wchodzą dopiero na granicy etapu.

## Zapis i nagroda

Stały cel `N01_PIER_FIRST_BUILD`, powiązany z M34, nie seed. Ukończenie roli, wynik i grant idempotentne. Dekoracja pomostu/pamiątka to propozycja nagrody; finalny asset później. Błędy i pomoc nie odejmują podstawy. Nowy seed nie odnawia pierwszej pamiątki. Wznowienie przywraca te same deski i rozkład. Wyjście nie oznacza nieopanowania dzielenia.

## Dowód odbioru

Poprawne [4,4,4]; dwa złe układy; brak/duplikatID; cofnięcie; UI_HELP vs MATH_HINT; guided; reconnect; drugi grant; 1/2/3/4 osoby; iPad tap zamiast drag. Kontrola generatora15 par i warianty [TEST_VECTORS](../TEST_VECTORS.md). Pomiar urządzenia jest osobnym wynikiem, nie wynika z poprawności n/g.
