# M33: Plażowy Sklep

SPEC_READY / TEACHER_REVIEW_PENDING / CODE_NOT_STARTED. N01, fikcyjne stoisko na Muchawce. MONEY O:II.6.3; N:2.13. [Źródła](../CURRICULUM_SOURCES.md). Ceny służą ćwiczeniu, nie są cenami prawdziwych lokali.

## Dwa portfele: obowiązkowe rozdzielenie

Budżet zadania to rekwizyt. Nie pobieraj monet przygody z konta dziecka, nie wymagaj zarobienia20 przed ćwiczeniem i nie traktuj błędu jako utraty zakupionych rzeczy. Propozycja dydaktycznej rewizji: w tej karcie używamy modelowych złotych/groszy zamiast samych muszelek, aby ćwiczyć pojęcie pieniędzy. Waluta ekonomii MathCity pozostaje oddzielna.

## Pierwsze zadanie

„Masz 20 zł na dwa zakupy. Jedna rzecz kosztuje 7 zł, druga 5 zł. Przygotuj zakupy i resztę.” Widoczne dwie wymagane pozycje zamówienia oraz ich ceny; koszyk na przedmioty i tacka na modelową resztę. Na ekranie „Pieniądze do zadania”, a nie saldo gry. Dziecko wybiera obie rzeczy, następnie nominały reszty lub wpisuje/ustawia wartość w dużym kontrolerze. Podsumowanie nie podaje automatycznie odpowiedzi8 przed sprawdzeniem.

## Dane i walidator

Przechowuj grosze jako liczby całkowite: budget2000, prices700 i500, expectedChange800. Oba itemID obecne dokładnie raz; suma wybranych nominałów albo wpisana wartość po normalizacji =800. Nie akceptować samego8, jeżeli protokół oczekuje groszy; adapter UI jasno tłumaczy zł→grosze. 5+2+1zł i cztery monety po2zł są równoważne. Reszta12 jest błędem (pomylenie sumy zakupu z resztą), poprawny koszyk ale reszta0 też nie przechodzi. W wariancie bez reszty expected0 jest legalne.

## Domena kontrolowana

Na pilot cztery zestawy (budżet, cena1,cena2) w zł: (10,4,3)→3; (20,7,5)→8; (20,6,8)→6; (30,12,7)→11. Do każdego ceny/modelowe monety są możliwe do przedstawienia. Generator wybiera z listy, nie dodaje trzeciego produktu ani zadłużenia. Wariant z groszami poniżej1zł dopiero jako osobna recenzowana domena; nie generuj liczb zmiennoprzecinkowych. Pierwszy przykład ręcznie (20,7,5).

## UI i pomoc

Tap rzecz→koszyk, tap nominał→tacka; ponowny tap odejmuje jedną sztukę. Widoczne „Cofnij”, „Sprawdź”, „Pomoc”. UI_HELP pokazuje technikę przeniesienia bez cen zadania. HINT1: „Najpierw policz, ile kosztują oba zakupy.” HINT2: rozbij7+5 na7+3+2. GUIDED: dziecko składa12 kosztu, odkłada tę wartość z modelowych20, liczy pozostałe8. Zmiana reprezentacji na liczmany jest pomocą matematyczną, ale nie obniża wypłaty podstawowej. Dodatkowe ilustracje nie powinny wymagać czytania długich nazw produktów.

## Solo/co-op i wynik

Wspólne wydarzenie ma kilka małych zamówień; każde dziecko własny budżet i tackę. Bez współdzielonej kasy pozwalającej opróżnić portfel drugiego gracza. Solo jedno kompletne zamówienie daje pełny sens etapu; w grupie każdy realizuje swoją część. Wspólny efekt: fikcyjne stoisko przygotowane. Cel N01_SHOP_STORY rozliczany raz; ponowne liczenie tego koszyka nie tworzy unikalnej nagrody od nowa.

## Testy

Wynik800 groszy, suma1200 nie jest resztą; obie reprezentacje8zł przechodzą; brak produktu, dodatkowy produkt, ujemny nominał, NaN i fałszyweID odrzucane. Model20 nie wpływa na saldo konta. Pause/resume zachowuje budżet i koszyk. Assisted=pełna podstawa, brak independent mastery. Nowy seed nie odnawia firstGrant.
