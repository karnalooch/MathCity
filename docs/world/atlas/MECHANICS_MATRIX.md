# MathCity — Etap A: bank minigier przypisanych do miejsc

**Data:** 2026-10-18. **Status: koncepcje i hipotetyczne przypisanie klas.** NIE jest to gotowy program dydaktyczny ani kod. G2/G3/G4 to propozycja docelowej grupy; zgodność z odpowiednią podstawą i stopień trudności zatwierdza nauczyciel. Realne wymiary wyraźnie rozróżnia się od wymyślonych liczb gry.

## Wspólny kontrakt zachowania

1. Dziecko może zwiedzać miasto bez kończenia zadań. Minigry są zaproszeniem.
2. Wejście: znak i jednozdaniowy cel, bez ściany tekstu.
3. Mechanika: manipulowanie obiektami 3D, wybór drogi lub krótki dotykowy interfejs.
4. Odpowiedź oceniana deterministycznie; punktów nie wolno naliczać wielokrotnie przez odświeżanie/lag.
5. Błąd = wskazówka, brak utraty ekwipunku/życia. Trzy próby → rozwiązanie krok po kroku.
6. Po sukcesie pokazujemy matematyczną zasadę oraz **małą pewną** nagrodę bez hazardu.
7. W kooperacji każdy ma swój udział; żaden uczestnik nie powinien bezpowrotnie blokować drugiego.
8. Wirtualny ruch sportowy NIE jest instrukcją bezpiecznego pływania, narciarstwa czy trików w prawdziwym świecie.
9. Brak zapisu danych identyfikujących dziecko w zadaniach; logika ocen na serwerze po przyszłej implementacji.

## Indeks minigier

| ID | Nazwa | Landmark | Dzielnica | Kandydat do klasy | Odpowiedź próbki |
| --- | --- | --- | --- | --- | --- |
| M01 | Zegar Jacka | C01 | Jackowo | G2/G3 | 09:35 |
| M02 | Pałac Lustrzanych Okien | C02 | Ogrody | G2/G3 | 4 |
| M03 | Parkowe Wzory | C03 | Ogrody | G2/G3 | Y |
| M04 | Mostki Aleksandrii | C04 | Ogrody | G2/G3 | 5 |
| M05 | Osiem Stacji Sekuły | N06 | Sekuła | G2/G3 | 5 stacji pozostało |
| M06 | Biegówki Sekuła: długość pętli | N05 | Sekuła | G2/G3 | 100 m |
| M07 | Biegówki Sekuła: stoper | N05 | Sekuła | G3/G4 | 2:15, różnica 25 sekund |
| M08 | Górka Grześ: wybór szlaku | N07 | Sekuła (do potwierdzenia) | G2/G3 | B jest krótsza o 25m |
| M09 | Park Wodny: długości basenu | S02 | Sport | G3/G4 | 100 m |
| M10 | Dwie Zjeżdżalnie | S02 | Sport | G2/G3 | 30 m |
| M11 | Basen Osiem Torów | S02 | Sport | G2/G3 | 4 tory w każdej |
| M12 | Basen: suma zjeżdżalni | S02 | Sport | G3/G4 | 126 m |
| M13 | Stadion: układ krzesełek | S01 | Sport | G2/G3 | 24 foteliki |
| M14 | Stadion: pole boiska | S01 | Sport | G4-ROZSZERZENIE | 7140 m² |
| M15 | Sztafeta na Prusa | S03 | Sport | G2/G3 | 10 |
| M16 | Kręgle Dziesiątki | S10 | Sport | G2 | 6 stojących |
| M17 | Rolkowe Ósemki | S06 | Sport | G2/G3 | 12 ślizgów |
| M18 | Skateplaza: próby | S04 | Sport | G3 | 20 punktów |
| M19 | Parkour Park: trzy bramy | S05 | Sport | G3/G4 | 18 |
| M20 | Miejski targ | C13 | Jackowo | G2/G3 | Reszta 3 |
| M21 | Poczta i kurier | C14 | Jackowo | G2/G3 | 12 < 21 < 35 |
| M22 | Dworzec: rozkład | T01 | Kolejowo | G3/G4 | 12:45 |
| M23 | Ogród: geometryczne klomby | C03 | Ogrody | G3/G4 | 15 kwiatów |
| M24 | Muchawka: podziel tratwę | N01 | Muchawka | G3 | 4 belki w grupie |
| M25 | Muchawka: części całego | N01 | Muchawka | G3/G4 | 6 pól |
| M26 | Zielone Siedlce: dostawy rowerowe | N12 | Trasy miejskie | G3/G4 | 1000m = 1km |
| M27 | Obserwatorium Doliny | N03 | Muchawka | G2/G3 | 10 |
| M28 | Muzealna symetria | C11 | Kultura | G2/G3 | 3 po prawej, 6 razem |
| M29 | CKiS rytm sceniczny | C10 | Kultura | G2/G3 | 10 |
| M30 | Plac Sikorskiego: wzór fontann | C15 | Jackowo | G2/G3 | Niebieski |
| M31 | Amfiteatr: grupa na widowni | C16 | Kultura | G2/G3 | 15 osób |
| M32 | Stawy: diagram obserwacji | N08 | Zielone Obrzeża | G3/G4 | 12 |

## Karty operacyjne: konkretny przebieg i wynik

### M01. Zegar Jacka → C01

- **Miejsce:** Jackowo, karta C01.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Ustaw analogowy zegar.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Na ekranie 09:20 i dodaj 15 minut.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **09:35**.
- **Wskazówka dla błędu:** Widzisz przestawione wskazówki; pomyłka pokazuje 20+15 i drugą próbę.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M02. Pałac Lustrzanych Okien → C02

- **Miejsce:** Ogrody, karta C02.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Ułóż drugą część pałacu.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Po lewej 4 okna, po prawej mają być symetrycznie 4.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **4**.
- **Wskazówka dla błędu:** Po stronie lewej wskazujemy elementy do odbicia; nie ma kar.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M03. Parkowe Wzory → C03

- **Miejsce:** Ogrody, karta C03.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Sadź wirtualne kwiaty.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Sekwencja R,Y,R,Y,R,?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **Y**.
- **Wskazówka dla błędu:** Podpowiedź: identyczny kolor wraca co drugi kwiat.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M04. Mostki Aleksandrii → C04

- **Miejsce:** Ogrody, karta C04.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Podziel segmenty mostku.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „8 kafelków, 3 już ułożone; ile brak?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **5**.
- **Wskazówka dla błędu:** Podpowiedź: przesuń trzy kafle do ramki i licz pozostałe.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M05. Osiem Stacji Sekuły → N06

- **Miejsce:** Sekuła, karta N06.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Odwiedź stanowiska leśne.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Na trasie 8 stacji, odkryto 3.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **5 stacji pozostało**.
- **Wskazówka dla błędu:** Podpowiedź: odsuń 3 z 8 ikonek; nie musimy odtwarzać oryginalnych tablic.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M06. Biegówki Sekuła: długość pętli → N05

- **Miejsce:** Sekuła, karta N05.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Biegowy wyścig po bezpiecznej fikcyjnej pętli.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „4 oznaczone odcinki gry po 25m.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **100 m**.
- **Wskazówka dla błędu:** Podpowiedź: dodaj 25 cztery razy. 25m to wymyślony fragment toru, nie pomiar oryginału.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M07. Biegówki Sekuła: stoper → N05

- **Miejsce:** Sekuła, karta N05.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Porównaj czasy dwóch zawodników.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „2:15 vs 2:40, który krótszy i o ile?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **2:15, różnica 25 sekund**.
- **Wskazówka dla błędu:** Podpowiedź: obie minuty są takie same, porównaj sekundy.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M08. Górka Grześ: wybór szlaku → N07

- **Miejsce:** Sekuła (do potwierdzenia), karta N07.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Dwie fikcyjne ścieżki na wzgórze.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Trasa A 70m, trasa B 45m.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **B jest krótsza o 25m**.
- **Wskazówka dla błędu:** BLOKER REALNEJ LOKALIZACJI: minigra tylko w fantazyjnym otoczeniu, bez publikacji prawdziwych współrzędnych.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M09. Park Wodny: długości basenu → S02

- **Miejsce:** Sport, karta S02.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Policz długości, nie okrążenia.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Jeden basen ma 25m, przebyto cztery DŁUGOŚCI.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **100 m**.
- **Wskazówka dla błędu:** Podpowiedź: 25+25+25+25. Nie myl długości basenu z okrążeniem tam i z powrotem.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M10. Dwie Zjeżdżalnie → S02

- **Miejsce:** Sport, karta S02.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Wybierz dłuższą trasę.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „48m i 78m, o ile druga dłuższa?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **30 m**.
- **Wskazówka dla błędu:** Przesuń oba paski na wspólny punkt i zobacz różnicę.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M11. Basen Osiem Torów → S02

- **Miejsce:** Sport, karta S02.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Podziel tory na zespoły.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „8 torów w dwóch równych grupach.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **4 tory w każdej**.
- **Wskazówka dla błędu:** Dla młodszych polecenie graficzne z płytkami, nie samo równanie.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M12. Basen: suma zjeżdżalni → S02

- **Miejsce:** Sport, karta S02.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Policz łączny dystans.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „48m i 78m (prawdziwe wartości ze strony operatora).”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **126 m**.
- **Wskazówka dla błędu:** Do zatwierdzenia przez nauczyciela; wariant prostszy 78-48=30.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M13. Stadion: układ krzesełek → S01

- **Miejsce:** Sport, karta S01.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Ustaw widoczne rzędy.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „6 rzędów po 4 foteliki w symulacji.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **24 foteliki**.
- **Wskazówka dla błędu:** Nie odwoływać się do rzeczywistej liczby 2901 foteli bez potrzeby.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M14. Stadion: pole boiska → S01

- **Miejsce:** Sport, karta S01.
- **Grupa robocza:** G4-ROZSZERZENIE; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Zobacz model prostokąta.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „105m na 68m (boisko rzeczywiste).”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **7140 m²**.
- **Wskazówka dla błędu:** Do weryfikacji edukacyjnej; ułamek klasy 4 może wymagać uproszczenia. To zaawansowany wariant opcjonalny.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M15. Sztafeta na Prusa → S03

- **Miejsce:** Sport, karta S03.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Wybierz kolejne znaczniki sztafety.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „2,4,6,8,?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **10**.
- **Wskazówka dla błędu:** Podpowiedź: dodawaj po 2.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M16. Kręgle Dziesiątki → S10

- **Miejsce:** Sport, karta S10.
- **Grupa robocza:** G2; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Wirtualnie strąć kręgle.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „10 kręgli, 4 przewrócone.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **6 stojących**.
- **Wskazówka dla błędu:** Zaznacz pozostałe kręgle; żadnych płatnych losowych nagród.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M17. Rolkowe Ósemki → S06

- **Miejsce:** Sport, karta S06.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Oblicz wirtualne pętle.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „3 serie po 4 ślizgi.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **12 ślizgów**.
- **Wskazówka dla błędu:** Podpowiedź: 4+4+4; bez wymagania realnego trenowania trików.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M18. Skateplaza: próby → S04

- **Miejsce:** Sport, karta S04.
- **Grupa robocza:** G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Przejdź 4 bezpieczne etapy obby.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „4 etapy po 5 punktów.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **20 punktów**.
- **Wskazówka dla błędu:** Nie wykonywać niebezpiecznych akrobacji; to wyłącznie ruch postaci Roblox.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M19. Parkour Park: trzy bramy → S05

- **Miejsce:** Sport, karta S05.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Wybierz bramę z wynikiem.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „6×3”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **18**.
- **Wskazówka dla błędu:** Błędna brama prowadzi do podpowiedzi, NIE do upadku z wysokości.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M20. Miejski targ → C13

- **Miejsce:** Jackowo, karta C13.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Kup 2 produkty.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „10 monet, jabłko 4, bułka 3.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **Reszta 3**.
- **Wskazówka dla błędu:** Podpowiedź: 4+3=7; 10-7=3. Monety gry, nie rzeczywiste ceny.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M21. Poczta i kurier → C14

- **Miejsce:** Jackowo, karta C14.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Sortowanie numerów paczek.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Sortuj domy 12, 21, 35 rosnąco.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **12 < 21 < 35**.
- **Wskazówka dla błędu:** Rozróżnianie dziesiątek i jedności; budynki fikcyjne.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M22. Dworzec: rozkład → T01

- **Miejsce:** Kolejowo, karta T01.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Wybierz właściwą godzinę.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Odjazd 12:15; podróż 30 minut.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **12:45**.
- **Wskazówka dla błędu:** Wyświetl animację upływającego czasu; rozkład jest fikcyjny i nie jest rozkładem PKP.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M23. Ogród: geometryczne klomby → C03

- **Miejsce:** Ogrody, karta C03.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Ułóż równe rzędy roślin.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „3 rzędy po 5 kwiatów.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **15 kwiatów**.
- **Wskazówka dla błędu:** Wyświetl siatkę 3×5 i zróżnicowane tryby liczenia.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M24. Muchawka: podziel tratwę → N01

- **Miejsce:** Muchawka, karta N01.
- **Grupa robocza:** G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Równe części przedmiotu.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „12 wirtualnych belek podziel na 3 równoliczne zestawy.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **4 belki w grupie**.
- **Wskazówka dla błędu:** Nie zachęcać do budowania realnych tratw i pływania po zalewie.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M25. Muchawka: części całego → N01

- **Miejsce:** Muchawka, karta N01.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Wypełnij pasek z ośmiu pól.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „3/4 z 8 pól.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **6 pól**.
- **Wskazówka dla błędu:** Pokaż połówki i ćwiartki; dydaktyka do sprawdzenia.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M26. Zielone Siedlce: dostawy rowerowe → N12

- **Miejsce:** Trasy miejskie, karta N12.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Trzy miejskie przystanki.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Wymyślone fragmenty 250m + 250m + 500m.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **1000m = 1km**.
- **Wskazówka dla błędu:** Nie sugerować, że to faktyczna długość fragmentów oficjalnej trasy 13,1 km.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M27. Obserwatorium Doliny → N03

- **Miejsce:** Muchawka, karta N03.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Policz ikony ptaków z tablicy.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „2+3+5 modeli = ?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **10**.
- **Wskazówka dla błędu:** Zwierzęta są ekranowymi rysunkami, nie nagradzać za gonienie ptaków.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M28. Muzealna symetria → C11

- **Miejsce:** Kultura, karta C11.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Ułóż artystyczny geometryczny wzór.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Po lewej 3 kwadraty, po prawej dodaj 3.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **3 po prawej, 6 razem**.
- **Wskazówka dla błędu:** Tylko autorskie abstrakcyjne dzieło, nie reprodukcja El Greca.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M29. CKiS rytm sceniczny → C10

- **Miejsce:** Kultura, karta C10.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Uzupełnij sekwencję uderzeń.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „2, 4, 6, 8, ?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **10**.
- **Wskazówka dla błędu:** Muzyka wyłącznie oryginalna lub legalna; tryb wyciszenia.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M30. Plac Sikorskiego: wzór fontann → C15

- **Miejsce:** Jackowo, karta C15.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Powtórz układ świecących figur.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Niebieski, róż, niebieski, róż, ?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **Niebieski**.
- **Wskazówka dla błędu:** Zawsze pokazać symbole obok kolorów; nie tylko zmysł barw.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M31. Amfiteatr: grupa na widowni → C16

- **Miejsce:** Kultura, karta C16.
- **Grupa robocza:** G2/G3; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Rozsadź grupę w modelu widowni.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „5 ławek po 3 fikcyjne miejsca.”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **15 osób**.
- **Wskazówka dla błędu:** Nie sugerować, że to realna liczba miejsc lub przekrój widowni.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

### M32. Stawy: diagram obserwacji → N08

- **Miejsce:** Zielone Obrzeża, karta N08.
- **Grupa robocza:** G3/G4; konsultacja z nauczycielem PRZED implementacją.
- **Cel w jednym zdaniu:** Przeanalizuj wykres planszowy.
- **Scenariusz krok po kroku:** (1) gracz dobrowolnie wchodzi w strefę minigry; (2) NPC/znak pokazuje: „Ilości na wykresie 2,4,6, czyli razem?”; (3) gracz manipuluje wizualnymi obiektami; (4) gra weryfikuje wynik; (5) przy poprawnej odpowiedzi wyświetla krótkie wyjaśnienie; (6) wraca do miasta bez resetu postępu.
- **Poprawna odpowiedź do testu:** **12**.
- **Wskazówka dla błędu:** Wyłącznie tablica edukacyjna, bez wejścia do rezerwatu ani zbliżania się do ptaków.
- **Niepoprawne zachowanie do wykrycia:** automatyczne uznanie złego wyniku, cofnięcie checkpointu, zaliczenie nagrody dwa razy, niezrozumiała instrukcja bez wizualizacji.
- **Do implementacji dopiero później:** osobny prefab/UI, wariant dotykowy, 3 poziomy trudności, lokalizacja PL, test solo/2 klientów, walidacja serwerowa.

## Przykładowe wymagania akceptacyjne prototypu każdej gry (nie teraz)

- Przy 10 próbach z przewidywalnymi danymi poprawne wyniki są zawsze akceptowane; wszystkie błędne odrzucane bez kar.
- Próbę można zakończyć bez utraty przedmiotów i pozostałych postępów.
- Dziecko może poprosić o minimum jedną naprawdę pomocną podpowiedź.
- Interfejs mieści się na ekranie telefonu; symbol i liczba mają podpis tekstowy.
- NPC nie używa prawdziwych godzin PKP, cen, poziomów wody czy informacji publicznej bez wyraźnego oznaczenia autorskiego zadania.
- Przy miejscach pamięci/obszarach chronionych mechanika jest odsunięta albo zastąpiona spokojną tablicą.

Zobacz [karty lokalizacji](LANDMARK_CATALOG.md), [skutki dydaktyczne](../../education/CURRICULUM_2_4.md), [ochrona](CONSERVATION_AND_RESPECT.md).
