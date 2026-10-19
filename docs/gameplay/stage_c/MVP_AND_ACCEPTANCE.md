# Pięć eksperymentów MathCity: zakres i kryteria odbioru

**PROPOZYCJA, nie polecenie wdrożenia. Nie uruchomiono Roblox Studio ani nie zmieniono gry.**

## 1. Granica zakresu

Potrzebujemy przetestować pięć wzorców, nie wyprodukować pięciu osobnych gier. W pierwszej iteracji do zatwierdzenia wystarczy moduł paszportu, jedno lokalne zadanie i wariant współpracy. Pozostałe stanowiska mogą korzystać z tych samych komponentów. UE, Blender i Material Forge należą do późniejszego dowodu assetowego; nie są zależnością logicznego testu z klocków Roblox.

Wszystkie oznaczenia **C-P01…C-P05** dotyczą eksperymentów badawczych, nie nowych minigier M41+. Oryginalne karty: [MECHANICS_MATRIX.md](../../world/atlas/MECHANICS_MATRIX.md).

## C-P01. Paszport i trzy miejsca

**Inspiracja:** G01/G15. **Miejsca:** C01 Jacek, C03 park, N01 Muchawka jako odrębne oznaczone stanowiska; nie wymagają finalnych modeli. **Cel:** sprawdzić, czy zbieranie wiedzy o mieście daje powód do eksploracji.

**Zakres:** trzy autorskie sylwetki, trzy nazwy, trzy osobiste pieczątki, podpowiedź kierunku i zapis. Brak fotografii dzieci, otwartego tekstu i handlu. Pierwsze miejsce widoczne bez zagadki. Minigra edukacyjna jest opcją, nie blokadą pieczątki odwiedzin.

**Odbiór:** A i B mogą zdobyć tę samą pieczątkę niezależnie; ponowne dotknięcie nie duplikuje nagrody; po rozłączeniu zatwierdzony zapis wraca; gracz rozpoznaje, która sylwetka odpowiada miejscu. Odkrycie N01 nie zalicza S02. Przy wczytywaniu błędu nie ogłaszamy zapisu jako udanego.

**Odrzucamy rozszerzenia:** pełną minimapę GPS, 41 gotowych modeli, globalny ranking odkrywców i wymianę pieczątek.

## C-P02. Pomost Muchawki

**Inspiracja:** G12. **Powiązanie:** M24/M34, N01. **Cel:** podział na grupy i poprawianie konstrukcji.

**Fikcyjny przypadek testowy:** 12 desek, 3 oznaczone sekcje, każda po 4. Błąd 5/4/3 nie niszczy budowy: wyróżnione zostają nierówne sekcje. Gracz sam przenosi jedną deskę. Wariant liczbowy podlega zatwierdzeniu przez nauczyciela.

**Zakres:** snap-grid, wybór sekcji, przyciski dodaj/odejmij lub przeciąganie z alternatywą dotykową, cofanie ruchu, animowany test pomostu. Bez swobodnej symulacji pływalności i fizycznych luźnych desek.

**Odbiór:** system przyjmuje 4/4/4, nie przyjmuje 5/4/3; cofanie działa; trzy błędy nie odbierają życia, waluty ani postępu; dwie równoczesne operacje nie wykorzystują tej samej deski dwa razy; tryb solo obejmuje całość. Stan pomostu jest prywatny dla uczestników instancji zadania, nie niszczy globalnego przejścia innym graczom.

## C-P03. Plażowe zamówienie

**Inspiracja:** G14. **Powiązanie:** M33 Plażowy Sklep; M20/M21 jako późniejsze warianty. **Cel:** odczytanie listy, kompletowanie i współpraca.

**Fikcyjny przykład:** w sklepie gry woda kosztuje 4 żetony, jabłko 3, płatność wynosi 15. Reszta: 8. Nie opisujemy tym prawdziwego cennika nad Muchawką.

**Zakres:** jedna osoba kompletuje produkty, druga sprawdza kwotę; przy braku kolegi można przejść przez obie czynności samodzielnie. Zlecenie jest pokazane ikonami, ze stałym podglądem. Nie wymaga przesyłania kodów i liczb na czacie.

**Odbiór:** zły produkt wskazany bez straty, wynik 8 akceptowany, 7 odrzucony z pomocą; rozłączenie na jednym stanowisku nie blokuje drugiego; jedna runda daje nagrodę raz każdemu uprawnionemu uczestnikowi; spam żądania odbioru nie mnoży żetonów.

## C-P04. Klomb Aleksandrii

**Inspiracja:** G03/G10. **Powiązanie:** M03/M23, C03. **Cel:** rytm albo rzędy z widocznym efektem w świecie.

**Przykład A:** naprzemienny układ dwóch oznaczonych gatunków, ostatni element do wstawienia. **Przykład B:** 3 rzędy po 5 kwiatów, razem 15. Każdy gatunek ma znak graficzny oprócz barwy, aby wynik nie zależał wyłącznie od rozróżniania kolorów.

**Zakres:** mała siatka i wybrany zestaw kwiatów. Rezultat jest natychmiastowy. Nie ma płatnych nasion, losowej oferty i odliczania do podlewania. Zapisuje się dekoracja, nie obowiązek opieki.

**Odbiór:** zły element można wymienić, alternatywne poprawne rozmieszczenia w dopuszczonym wariancie są uznawane, pomoc działa na dotyku, powrót następnego dnia nie pokazuje kary za nieobecność. Bez kopiowania cudzych assetów lub muzyki.

## C-P05. Krótka runda sportowa

**Inspiracja:** G09/G11/G13. **Powiązanie:** M06/M07 na Sekule lub M09 w Parku Wodnym. Najpierw wybrać **jedną** scenerię, nie budować obu.

**Fikcyjny przykład M06:** cztery odcinki gry po 25 m, suma 100 m. Jednostki należy przeliczać zgodnie z późniejszą konwencją świata, ale w teście używa się oznaczonych danych zadania, nie pomiarów prawdziwej trasy narciarskiej.

**Zakres:** stanowisko startowe, czytelny cel, lokalny checkpoint, wyłączenie presji czasu, wynik sportowy oddzielony od obliczenia. Brak konieczności czekania na innych. Element wodny nie jest poradnikiem realnego pływania.

**Odbiór:** błędny wynik obliczenia nie resetuje przejazdu; opuszczenie rundy nie kasuje paszportu; przy rozłączeniu partnera zadanie pozostaje wykonalne; na telefonie wszystkie elementy są osiągalne; restart dotyczy tylko bieżącej próby.

## 2. Wspólny kontrakt przyszłej minigry

Stany projektowe: **DOSTĘPNA → INSTRUKCJA → DZIAŁANIE → SPRAWDZENIE → PODPOWIEDŹ albo SUKCES → POWRÓT**. WYJŚCIE dostępne z każdego stanu aktywnego. Zdarzenia mają unikalny identyfikator próby. Serwer weryfikuje warunek, uczestnictwo i to, czy wynik już nagrodzono. Klient nie wysyła autorytatywnego „zaliczone=true”.

Nie narzucamy dziś nazw przyszłych modułów ani implementacji API. Kontrakt musi obsłużyć reset próby, rozłączenie, powtórzony komunikat, błędne dane, opóźnienia i dwie równoczesne interakcje. Opisy stanów nie są dowodem istnienia takiej maszyny w obecnym kodzie.

## 3. Kolejność eksperymentów i warunki przerwania

Najpierw C-P01+C-P02: kierunek eksploracji oraz jedna działająca czynność matematyczna. Potem C-P03: wariant dwóch uczestników. C-P04 i C-P05 sprawdzają, czy wspólny schemat nie zamienia każdej minigry w identyczne przekładanie klocków.

Przerwać i poprawić UX, jeśli tester nie rozumie celu mimo krótkiej demonstracji, zadanie wymaga rozmowy tekstowej, błąd ruchowy jest oceniany jako błąd matematyczny lub nowa mechanika wymusza nadmiar systemów. Nie podnosić złożoności, aby ukryć brak zabawy.

## 4. Bramka wyjścia

Każdy eksperyment potrzebuje nagranego albo udokumentowanego przebiegu, wyniku PC/telefon, próby solo i wymaganej próby 2 klientów. Następnie nauczyciel ocenia treść, a właściciel wybiera zakres produkcji. **Obecny status wszystkich C-P01…C-P05: NOT_IMPLEMENTED / NOT_TESTED.**
