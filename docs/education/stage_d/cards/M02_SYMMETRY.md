# M02: Pałac Lustrzanych Okien

SPEC_READY / TEACHER_REVIEW_PENDING / CODE_NOT_STARTED. C02. Własna plansza inspirowana fasadą pałacu, nie pomiar zabytku. SYMMETRY O:II.5.4; N:4.12. [Źródła](../CURRICULUM_SOURCES.md).

## Poprawka względem atlasu

Sama odpowiedź „4 okna” nie dowodzi symetrii. Oceniamy **odbite położenie i cechę obiektu**, a liczba elementów jest tylko jednym warunkiem. Nie zmieniać identyfikatora M02.

## Plansza i dane

Widoczna pionowa oś x=0, siatka trzech kolumn po każdej stronie i trzech rzędów. x∈{-3,-2,-1,1,2,3}, y∈{1,2,3}. W pierwszej próbie okna lewe są w (-1,1),(-2,1),(-3,2),(-1,3). Cztery ruchome okna na tacy, pusta prawa strona. Polecenie: „Ułóż po prawej odbicie okien. Każde ma być tak samo daleko od linii.” Współrzędne są wewnętrzne; dziecko widzi sloty, nie musi znać liczb ujemnych.

Tap na okno, tap na slot; przeciąganie opcjonalne. Nieprawidłowe pole poza planszą wraca na tacę. Wszystkie dozwolone sloty mogą się podświetlić jako pomoc obsługowa; tylko właściwy slot nie może świecić automatycznie w trybie samodzielnym.

## Walidator

Dla każdego obiektu typu/kategorii k w (x,y) po lewej musi istnieć odpowiadający mu obiekt k w (-x,y) po prawej. Bez dodatkowych okien, bez duplikatów obiektów i nakładania slotów. W próbce expected={(1,1),(2,1),(3,2),(1,3)}. Cztery okna w innym układzie nie przechodzą. Porządek ruchów i tożsamość zamiennych wizualnie okien nie ograniczają poprawnych rozwiązań. Nie używać prostej równości tablic przesłanych w różnej kolejności.

## Warianty

Ręcznie przygotuj pierwszą próbę z2 oknami w(-1,1),(-2,2), potem próbkę4okien. Domena generatora: wybierz2,3 albo4 różne miejsca spośród9 lewych slotów, odbij je. To246 kombinacji zestawów. Nie generuj okna na osi ani pary nakładającej się. Dodatkowe kolory nie są konieczne; późniejszy wariant może rozróżniać kształty razem z kolorem, po osobnym review. Łatwość wynika z liczby/układu, nie z prędkości drag.

## Podpowiedzi

UI_HELP demonstruje wybór i umieszczenie neutralnego kafla poza właściwą planszą. HINT1: „Sprawdź odległość od linii i wysokość okna.” HINT2: rysuje prowadnicę od jednego okna przez oś. GUIDED: dziecko wybiera lewe okno, liczy sloty do osi, wybiera slot po prawej i powtarza. Prowadnica ujawniająca parę = matematyczna pomoc. Po złym układzie nie zerować wszystkich poprawnych okien; wyróżnić warunek bez wstydu. Podstawowa nagroda zostaje.

## Integracja

Każdy członek drużyny ma własny fragment planszy oraz własną odpowiedź. Wspólny rezultat to dekoracyjne rozświetlenie fikcyjnych okien w wydarzeniu, nie zmiana trwałej kolizji pałacu. Solo kończy jeden pełny fragment. Wznowienie odtwarza lewy wzór i rozstawione prawe okna. Nagroda C02_MIRROR_STORY niezależna od seed i permutacji okien; późniejsze ćwiczenie nie daje kolejnych kopii wyjątkowej nagrody.

## Testy

Właściwy zbiór przechodzi w każdej kolejności. Tyle samo okien w innych miejscach nie. Brak1, dodatkowe1, dwa w jednym slocie i obceID są obsługiwane. Domena246 wzorów ma odbicia w siatce. UI_HELP nie zmienia pomocy matematycznej; prowadnica tak. Prawe/lewe rozumiane względem stałej planszy, nie ruchomej kamery gracza.
