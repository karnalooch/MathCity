# Dane testowe ośmiu pilotów i kontrola rachunkowa

2026-10-19. **Dane i oczekiwane wyniki, nie raport testów Roblox.** Uruchomiono niezależną kontrolę rachunkową domen w Pythonie: 810 konfiguracji dodatnich opisanych niżej. Nie uruchomiono implementacji Luau, generatora gry, testów UI, multiplayer ani urządzeń. Scenariusze negatywne są przygotowanymi wymaganiami do wykonania. Wynik liczenia zbioru nie potwierdza przyszłego kodu.

## 1. Wielkości skończonych domen

| Karta | Domena | Liczba konfiguracji / kontrola |
|---|---|---|
| M34 | g∈{2,3,4}, q∈{2,3,4,5,6}, n=gq |15; wszystkie podzielne i n≤24 |
| M01 | h9…16, m∈{0,15,20,30,35,45}, d∈{5,10,15,25,30} |240; wszystkie wyniki tego samego dnia |
| M02 |2,3 lub4 różne pozycje z9 po lewej |246; odbicie mieści się po prawej |
| M05 | każdy podzbiór8 stacji jako już odkryte |256; liczba pozostałych=8−liczebność zbioru |
| M13 | n∈{6,8,10,12,15,16,18,20,24}; boki2…6 |9 wielkości; każda ma co najmniej1 dopuszczoną parę |
| M21 |6 ustalonych trójek ×6 permutacji |36; sortowanie numeryczne daje ustaloną kolejność |
| M33 |4 jawne budżety i pary cen |4; całkowita nieujemna reszta |
| M35 |4 listy długości |4; suma zgodna z kartą |
| **Razem** | różne konfiguracje wejścia, nie wszystkie ruchy użytkownika | **810** |

M13 dla n12 ma4 rozmiary prostokąta i34 legalne położenia tych prostokątów na siatce6×6. Te34 położenia są dodatkowym wynikiem kombinatorycznym, nie dodajemy ich drugi raz do powyższej liczby konfiguracji n. Permutacje identycznych krzeseł nie zmieniają rozwiązania.

## 2. Scenariusze walidatorów

| ID | Dane / działanie | Oczekiwany rezultat |
|---|---|---|
| TV-34-01 |12 desek,3 grupy, wszystkie unikalneID, liczności4/4/4 | poprawne, q4 |
| TV-34-02 | te same12, liczności5/4/3 | błędne: nierówne grupy; suma12 nie wystarcza |
| TV-34-03 | liczności4/4/3 | niekompletne; bez utraty stanu |
| TV-34-04 |4/4/4, ale jedenID występuje dwa razy zamiast innego | odrzucenie danych, nie zaliczenie |
| TV-34-05 | n15,g3 | q5, prawidłowe trzy grupy |
| TV-34-06 | n12,g0 lub n13,g3 | generator nie publikuje takich danych |
| TV-01-01 |09:20+15 min |09:35;575 minut; minutowa210°, godzinowa287,5° |
| TV-01-02 | odpowiedź09:25 albo10:35 | niepoprawne, dane niezmienione |
| TV-01-03 | tekst9:35 /09:35 | oba adaptery dają575 |
| TV-01-04 |09:75 | błąd formatu, nie automatyczne10:15 |
| TV-01-05 |09:35+25 |10:00 |
| TV-01-06 |23:50+20 w domenie pilota | dane poza domeną, nie ukryty rollover |
| TV-02-01 | L={(-1,1),(-2,1),(-3,2),(-1,3)};R={(1,1),(2,1),(3,2),(1,3)} | poprawne odbicie |
| TV-02-02 | cztery prawe okna, ale jedno na(2,3) zamiast(1,3) | niepoprawne mimo liczby4 |
| TV-02-03 | te same poprawne pozycje w innej kolejności listy | poprawne |
| TV-02-04 | dwa okna w jednym slocie albo dodatkowe piąte | niepoprawne |
| TV-05-01 | wszystkie1…8;V={1,3,6} |U={2,4,5,7,8}, wynik5 |
| TV-05-02 | V puste /V wszystkie | wyniki8 /0 |
| TV-05-03 | dwa wejścia do tej samej stacji | jedno odkrycie |
| TV-05-04 | odkrycie nowej stacji świata w trakcie planszy | nie zmienia snapshotu zadania |
| TV-13-01 | n12, prostokąt2×6/3×4/4×3/6×2 | wszystkie poprawne, równoważna nagroda |
| TV-13-02 | n12,1×12 albo12×1 | nie mieści się w jawnej domenie2…6 |
| TV-13-03 | n12, rzędy5/4/3 albo dziura | błędne |
| TV-13-04 | przesunięcie poprawnego prostokąta wewnątrz planszy | poprawne, brak ukrytej preferencji narożnika |
| TV-13-05 | n7 i boki2…6 | brak rozwiązania; generator odrzuca konfigurację |
| TV-21-01 | paczki35,12,21 | kolejność12,21,35 |
| TV-21-02 |102,120,201 | porządek numeryczny, nie stringowy |
| TV-21-03 |21,12,35 | błąd porządku |
| TV-21-04 | poprawne liczby lecz powtórzonyID paczki | odrzucenie nielegalnej permutacji |
| TV-33-01 |2000−700−500 groszy |800 groszy, nie1200 |
| TV-33-02 | reszta5zł+2zł+1zł /4×2zł | oba układy poprawne |
| TV-33-03 | poprawna reszta, ale brak jednej zakupionej pozycji | zadanie niekompletne |
| TV-33-04 | zmiana modelowego budżetu zadania | saldo portfela przygody niezmienione |
| TV-33-05 |30−12−7 |11zł |
| TV-35-01 |200+150+250 |600m |
| TV-35-02 | wariant sumy A, odpowiedź550 | błędne; nie pomyl z wariantem wyboru tras |
| TV-35-03 | trasy A600,B550,C700; cel≤600 | A iB poprawne, C błędne |
| TV-35-04 | te same trasy; cel „najkrótsza” | tylkoB; wymaga zgodnej instrukcji i predykatu |
| TV-35-05 | teleport między checkpointami | nie dodaje dystansu legalnego przejazdu |

Każdy przypadek ma być odtworzony z właściwym przypisaniem ID i wersji. Współrzędne symetrii są reprezentacją wewnętrzną, a nie materiałem wymagającym liczb ujemnych od młodszych dzieci.

## 3. Sprawdzone przykłady ekonomii, wyłącznie TEST_DEFAULTS

B100 i r1: solo100; co-op bez catch-up120; co-op z maksymalnym c0,30 daje150. Powtórka r0,25 z t0,20 daje30. Kwalifikowana pomoc r0,50 i t0,20 daje60. To niezależne obliczenie propozycji wzoru, nie test legalności uprawnienia do grantu. Uprawnienie sprawdza przyszły kod według [PROGRESSION](../../gameplay/specs/PROGRESSION_AND_REWARDS.md).

Tabela przedmiotów [50,20,30], [25,40,35], [10,50,40] sumuje się do100 w każdym wierszu. To kontrola normalizacji, nie pomiar rzeczywistych szans ani dowód balansu.

## 4. Jak powtórzyć kontrolę arytmetyczną

Poniższy samodzielny kod nie wymaga Roblox ani zależności zewnętrznych. To wzorzec rachunkowy dokumentacji. W przyszłym P01 trzeba osobno porównać z nim wyniki rzeczywistego generatora Luau i dodać testy negatywne.

```python
from itertools import combinations, permutations, product
from fractions import Fraction
from math import floor
counts = {}
groups = list(product((2, 3, 4), range(2, 7)))
assert all(g*q <= 24 and (g*q)//g == q for g, q in groups)
counts['M34'] = len(groups)
clocks = list(product(range(9, 17), (0, 15, 20, 30, 35, 45), (5, 10, 15, 25, 30)))
assert all(0 <= h*60+m+d < 1440 for h, m, d in clocks)
assert 560+15 == 575 and ((575 % 60)*6, (575 % 720)*.5) == (210, 287.5)
counts['M01'] = len(clocks)
left = list(product((-3, -2, -1), (1, 2, 3)))
patterns = [p for n in (2, 3, 4) for p in combinations(left, n)]
assert all(len({(-x, y) for x, y in p}) == len(p) for p in patterns)
counts['M02'] = len(patterns)
subsets = [set(p) for n in range(9) for p in combinations(range(1, 9), n)]
assert all(len(set(range(1, 9))-p) == 8-len(p) for p in subsets)
counts['M05'] = len(subsets)
row_pairs = {n: [(r, c) for r, c in product(range(2, 7), repeat=2) if r*c == n]
             for n in (6, 8, 10, 12, 15, 16, 18, 20, 24)}
assert all(row_pairs.values())
assert row_pairs[12] == [(2, 6), (3, 4), (4, 3), (6, 2)]
assert sum((7-r)*(7-c) for r, c in row_pairs[12]) == 34
counts['M13'] = len(row_pairs)
triples = ((2, 5, 7), (3, 8, 10), (12, 21, 35), (5, 12, 20), (102, 120, 201), (7, 17, 70))
posts = [p for t in triples for p in permutations(t)]
assert all(tuple(sorted(p)) in triples for p in posts)
counts['M21'] = len(posts)
shops = [(10, 4, 3, 3), (20, 7, 5, 8), (20, 6, 8, 6), (30, 12, 7, 11)]
assert all((b-p-q)*100 == change*100 for b, p, q, change in shops)
counts['M33'] = len(shops)
routes = [((20, 10, 30), 60), ((100, 50, 150), 300),
          ((200, 150, 250), 600), ((250, 250, 500), 1000)]
assert all(sum(parts) == result for parts, result in routes)
counts['M35'] = len(routes)
assert sum(counts.values()) == 810
xp = [floor(100*r*(1+t+c)) for r, t, c in (
    (1, 0, 0), (1, Fraction(1, 5), 0),
    (1, Fraction(1, 5), Fraction(3, 10)),
    (Fraction(1, 4), Fraction(1, 5), 0),
    (Fraction(1, 2), Fraction(1, 5), 0))]
assert xp == [100, 120, 150, 30, 60]
assert all(sum(row) == 100 for row in ((50, 20, 30), (25, 40, 35), (10, 50, 40)))
print(counts, sum(counts.values()), xp)
```

Oczekiwany stdout: liczniki M34=15,M01=240,M02=246,M05=256,M13=9,M21=36,M33=4,M35=4; suma810; XP=[100,120,150,30,60]. Traktowanie powyższego jako810 zaliczonych testów gry jest błędem raportowania.
