# M05: Osiem Stacji Sekuły

SPEC_READY / TEACHER_REVIEW_PENDING / CODE_NOT_STARTED. N06, robocza strefa Sekuły. COUNT/ADD_SUB O:II.2.1,II.3.2; N:1.9. [Źródła](../CURRICULUM_SOURCES.md). Osiem ikon w ćwiczeniu to model gry; tekst geograficzny korzysta z osobnej karty atlasu.

## Rozdzielenie odkrywania i matematyki

Odkrywanie punktu jest dostępne bez matematyki. Osobne ćwiczenie pyta o liczbę odkrytych i pozostałych stacji. Nie zamykaj całej trasy po błędzie i nie podmieniaj danych, gdy dziecko odpowiada.

## Pierwsza próba

Osiem ikon z podpisami1…8; trzy oznaczone jako odkryte. Polecenie: „Na planie jest 8 stacji. Odkryto 3. Zaznacz te, które jeszcze zostały.” Potem krótki wybór liczby pozostałych; można policzyć symbole. Zadanie zachowuje visitedSnapshot z momentu rozpoczęcia. Dalsze odkrycia w świecie nie zmieniają planszy trwającej próby. Podpis: „Plan z początku zadania”. Nie wyświetlaj równocześnie gotowej liczby „pozostało5”, aby samo jej przepisanie nie udawało samodzielnego odejmowania.

## Stan i walidacja

StationIDs{1…8}, V unikalny podzbiór, U=all minus V. Odpowiedź zaznaczenia dokładnieU, liczba8−|V|. Dla V={1,3,6}, U={2,4,5,7,8}, wynik5. Powtórne wejście w ten sam trigger nie zwiększa liczby odkryć. Plansza matematyczna nie daje prawa do dopisania nieodwiedzonego punktu podróży; właściwe odkrycia wymagają serwerowej kontroli miejsca. NieistniejąceID9 odrzucone.

## Warianty

n8 stałe, k0…8. Wszystkie podzbiory V dają256 możliwych stanów. Dla k0 wynik8, dla k8 wynik0 i neutralny komunikat o komplecie. Pierwsze ręczne przykłady: k3→5,k5→3,k7→1. Ćwiczenie nie wymaga ponownego obchodzenia prawdziwych ośmiu punktów dla każdego wariantu. Klasa i kolejność trudności wymagają review, a wynik nie wpływa na fizyczną dostępność trasy.

## UI i pomoc

Duże pola wyboru, zaznaczenie symbolem/tekstem i kolorem, tap–tap bez wymagania drag. UI_HELP pokazuje zaznaczanie neutralnej ikony. HINT1: „Pomiń stacje już odkryte.” HINT2: wizualnie grupuje odkryte i pozostałe. GUIDED: dziecko odkłada trzy oznaczone ikonki z ośmiu i liczy resztę; na końcu zapis8−3=5. To pomoc matematyczna i ASSISTED, bez utraty podstawowej nagrody. Wyjście i wznowienie zachowują ten sam V i pomoc. Błędy nie kasują odkryć ani EXP.

## Drużyna i nagrody

Każdy ma własne odkrycia i przypisane zadanie. Przy wspólnym dotarciu do punktu obecni gracze mogą otrzymać własne odkrycie; nieobecni nie dostają go przez samą przynależność do grupy. Matematyka wymaga własnej pracy, nie tylko pójścia za kolegą. Cel N06_STATIONS_STORY ma stabilny identyfikator; odkrycie i rozwiązanie nie mogą przypadkowo wypłacić tej samej nagrody dwa razy.

Efekt osobisty: paszport. Wspólna prezentacja: gotowość fikcyjnej wyprawy. Nie wyświetla błędów poszczególnych dzieci i nie odbiera historii późniejszym graczom. Solo realizuje pełną porcję, w grupie są odrębne porcje per osoba. Nowy gracz dołącza w granicy etapu, nie zmienia otwartej planszy partnera.

## Testy

Próbka5, dziewięć liczebności i256 podzbiorów; duplicate trigger; ID9; zaznaczenie odkrytej stacji; brak jednej pozostałej; zmiana realnych odkryć przy otwartym zadaniu; pause/resume; wynik0; prywatność. Mechanika może inspirować prostą aktywność w centrum, ale nie wolno przenosić ani przemianowywać N06 jako placu przy ratuszu.
