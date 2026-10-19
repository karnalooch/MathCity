# M01: Zegar Jacka

SPEC_READY / TEACHER_REVIEW_PENDING / CODE_NOT_STARTED. C01, zegar ćwiczeniowy obok ratusza, nie zmiana prawdziwego zegara ani sezonowego rozkładu miasta. CLOCK: O:II.6.4; N:2.9, [źródła](../CURRICULUM_SOURCES.md).

## Zadanie

„Jest 09:20. Za 15 minut zaczyna się spotkanie. Ustaw godzinę rozpoczęcia.” Stała karta z godziną początkową i odstępem; duża tarcza odpowiedzi. Na tarczy etykiety godzin, minutowe znaczniki i rozróżnione długości wskazówek, nie tylko kolor. Dodatkowy cyfrowy podgląd tego, co ustawiło dziecko, nie podpowiada wyniku.

Sterowanie: dotyk wybiera wskazówkę; szerokie przyciski ±5 minut i ±1 godzina oraz możliwość przeciągania ze skokiem co5min. Obie wskazówki renderują JEDEN czas, nie dwa niezależne stany mogące być sprzeczne. Ustawienie 09:35 oznacza godzinową między9 a10, nie nieruchomo na9. Bez stopera czytania i rozwiązywania.

## Reprezentacja i walidator

Parametry t0 w minutach od północy, delta w minutach; rezultat t0+delta. Bieżący wyświetlany zegar nie nadpisuje t0. Dla 09:20: t0=560, delta15, expected575=09:35. Kąty kontrolne: minutowa210°, godzinowa287,5° zgodnie z ruchem wskazówek od12. Po stronie protokołu liczba całkowita minut, skończona0…1439. Tekstowy adapter akceptuje09:35 lub9:35, ale nie9:75, NaN albo godzinę poza zakresem. Nie normalizuje błędnego09:75 jako10:15 za plecami dziecka.

## Zakres kontrolowany

Ręczny pierwszy przykład:09:20+15. Domena pilota: godzina początkowa9…16; minuty początkowe{0,15,20,30,35,45}; delta{5,10,15,25,30}. 240 kombinacji, wszystkie kończą się tego samego dnia. Łatwy band to pełne/połowy godzin i mały krok; średni bez przejścia pełnej godziny; wyższy obejmuje przejście, np.09:35+25=10:00. Przejście przez północ NIE jest wariantem pilota, a nie wolno usuwać informacji o zmianie dnia przez modulo1440. Klasy i kolejność bandów oczekują review.

## Pomoc i błąd

UI_HELP pokazuje, jak przesunąć wskazówkę na neutralnej mini-tarczy. HINT1: „Do czasu początkowego dodaj 15 minut.” HINT2: zaznacz trzy odcinki po5min od20. GUIDED: dziecko przesuwa20→25→30→35 i zatwierdza; potem animacja pokazuje zgodny ruch godzinowej. To ASSISTED, pełna podstawowa nagroda. Przy09:25: „To jeszcze nie 15 minut później. Sprawdź liczbę kroków.” Nie przestawiaj tarczy na poprawny wynik bez jawnej pomocy. Kliknięcie palcem poza tarczą nie liczy się jako zła odpowiedź.

## Współpraca, efekt i zapis

1–4 osoby przygotowują niezależne godziny swoich stanowisk wydarzenia. Różne zadania nie oznaczają innej podstawowej wartości roli. Wspólna plansza pokazuje „stanowisko gotowe”, nie błędne odpowiedzi kolegi. Efekt: fikcyjne spotkanie jest gotowe w osobistej przygodzie. Grupa nie zmienia zegara całego serwera w zależności od prywatnych liczb. Parametry i najwyższa pomoc zapisane; grant stałego celu C01_CLOCK_INTRO raz, nie raz na minutę lub seed.

## Odbiór

09:35 poprawne;09:25 i10:35 nie;09:75 odrzucone jako niepoprawny format;09:35+25=10:00; oba kąty poprawne; brak samoczynnego odliczania; wynik guided nie tworzy independent evidence; zamknięcie/przywrócenie UI zachowuje zadanie. Widoczność tarczy i przycisków na iPadzie i obu telefonach.
