# MathCity — pętla rozgrywki, progresja i minigry

**Status:** propozycja do prototypowania i testów z dziećmi, 2026-10-18.

## Core loop

**Swobodne zwiedzanie → napotkanie aktywności → wykonanie zadania fizycznego lub matematycznego → nagroda + nowa wiedza → odblokowanie drobnej personalizacji / trasy → dalsze zwiedzanie.**

Gra musi też mieć **free-play**: dziecko może jeździć, zwiedzać, spotykać innych i odkrywać ciekawostki bez ciągłego quizu. Dla uczniów mniej pewnych siebie zadania nie mogą blokować całego świata.

## Osiem kandydatów minigier

| Minigra | Punkt | Przykładowa interakcja | Dział matematyki | Tryb |
| --- | --- | --- | --- | --- |
| Zegar Jacka | Ratusz | Nastaw ruchome wskazówki / oblicz upływ czasu | zegar, czas, arytmetyka | solo, duet |
| Bilet do Kolejowa | Dworzec | Wybierz bilet i ustal czas przyjazdu | pieniądze, dodawanie, czas | solo |
| Ogrody Symetrii | Park Aleksandria | Ułóż drugą połowę wzoru w ogrodzie | geometria, symetria | solo, duet |
| Mosty Muchawki | Zalew | Podziel belki/odcinki na równe części | ułamki, dzielenie, długość | solo, kooperacja |
| Budowniczy Stadionu | Stadion | Rozstaw sektory i odmierz boisko | długość, obwód, pole | solo, kooperacja |
| Siedlecki Kurier | Całe miasto | Zaplanuj trasę 3 przystanków | szacowanie, dystans, czas | solo, duet |
| Neonowy Sklep | Rynek | Przygotuj koszyk i wydaj resztę | pieniądze, działania | solo |
| Muzyczne Kody | Teatr / Aleja Kultury | Odtwórz i rozbuduj sekwencję rytmów | wzory, rytm, sekwencja | solo, zespół |

Zadania muszą mieć warianty trudności według **umiejętności**, a nie wyłącznie deklarowanej klasy. Katalog prawdziwych wymagań: [edukacja](../education/CURRICULUM_2_4.md).

### Przykład: „6 × 4” nie jako quiz

Gracz ma rozstawić 6 rzędów po 4 siedzenia na stadionie. Widzi liczbę rzędów i siedzeń; może przesuwać obiekty, liczyć pojedynczo lub mnożyć. Po sukcesie otrzymuje informację o wybranej strategii. Pomyłka pokazuje różnicę i daje wskazówkę zamiast kary.

## Progresja (PROPOZYCJA)

- **Paszport odkrywcy:** lista odwiedzonych miejsc, ciekawostki i bezpieczne osiągnięcia.
- **Paszport umiejętności:** tematy, które uczeń ćwiczył; bez publicznego rankingu „najgorszych uczniów”.
- **Waluta zdobywana grą:** wyłącznie do personalizacji, środków transportu i elementów dekoracyjnych; ceny dopiero po badaniu ekonomii.
- **Kolekcja niehazardowa:** widoczna zawartość i znane zasady zdobywania, bez losowych płatnych skrzynek.
- **Kooperacja:** gracze pomagają sobie, ale rozwiązania nie powinny być zdradzane przez innych z automatu.

## Projekt rundy minigry

1. Czytelna zachęta i krótkie pokazanie celu (bez ściany tekstu).
2. Część manipulacyjna 3D / zadanie.
3. Pierwszy błąd: spokojny feedback, wyróżnij co jest nie tak.
4. Drugi błąd: opcjonalna konkretna podpowiedź i możliwość uproszczenia.
5. Sukces: wyjaśnienie, krótka nagroda i powrót do miasta.
6. Zapis umiejętności po stronie serwera. Bez kar i bez przymusu pozostania.

## Bezpieczeństwo i dostępność

- Czytelne kolory + ikony (nie tylko kolor jako informacja).
- Napisy zamiast niezbędnego dźwięku, sterowanie dotykowe, wariant spokojniejszego tempa.
- Krótkie komunikaty po polsku, bez publicznego zawstydzania po błędzie.
- Zero agresywnych streaków, lootboxów i sprzedaży przewagi w nauce.
- Dziecko może samodzielnie opuścić grę i później wrócić.
- Minimalizujemy gromadzenie danych dotyczących postępów dzieci.

## Z prototypu, co zachowujemy jako materiał referencyjny?

Obecne 3 etapy / 9 drzwi, statystyki i kryształy tworzą gotowy prototyp testowy. **Nie zmieniamy go automatycznie.** Wzorzec „złe drzwi = śmierć” należy uznać za antywzorzec edukacyjny w docelowej formule.

## Otwarta decyzja

Czy Wieża Matematyczna stanie się jedną z atrakcji centrum, czy zostanie zastąpiona minigrami całkowicie miejskimi? Do ustalenia po testach.
