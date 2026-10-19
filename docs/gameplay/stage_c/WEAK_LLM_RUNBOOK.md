# Etap C: instrukcja wykonawcza dla kolejnego, słabszego modelu

**2026-10-19. Zakres bieżący: dokumentacja i analiza. Nie implementuj gry na podstawie samego istnienia tego pliku.**

## 1. Kolejność czytania

1. [STAGE_C_README.md](../STAGE_C_README.md): status, zakres i pięć rekomendacji.
2. [SOURCES_AND_METHOD.md](SOURCES_AND_METHOD.md): oryginalne gry, źródła, daty i klasy dowodu.
3. [BENCHMARK_15_GAMES.md](BENCHMARK_15_GAMES.md): co zadeklarowali autorzy i co proponujemy my.
4. [TRANSFER_MATRIX.md](TRANSFER_MATRIX.md): wzorce przypisane do istniejących minigier.
5. [Bank M01–M40](../../world/atlas/MECHANICS_MATRIX.md), [Muchawka](../../world/atlas/MUCHAWKA_FEATURE.md) i [program klas 2–4](../../education/CURRICULUM_2_4.md).
6. [MATHCITY_EXPERIENCE.md](MATHCITY_EXPERIENCE.md), [MVP_AND_ACCEPTANCE.md](MVP_AND_ACCEPTANCE.md) i [ECONOMY_SAFETY_AND_SOCIAL.md](ECONOMY_SAFETY_AND_SOCIAL.md).
7. [PLAYTEST_PROTOCOL.md](PLAYTEST_PROTOCOL.md) przed wpisaniem jakiegokolwiek wyniku testu.

Nie czytaj wyłącznie starego pliku ROBLOX_MARKET_RESEARCH_2026 i nie traktuj sześciu dawnych dzielnic jako aktualnego zamkniętego planu. Etap A rozszerzył koncepcję do **7 stref, 41 miejsc i 40 minigier**, ale nie zatwierdził ich automatycznie do produkcji.

## 2. Słownik identyfikatorów: nie mylić

| Oznaczenie | Znaczenie |
| --- | --- |
| G01…G15 w Etapie C | Analizowane gry Roblox, np. G01 Brookhaven, G06 Fisch |
| G2/G3/G4 w kartach edukacji | Robocze poziomy szkolne; to nie kody gier G02/G03/G04 |
| C01/C02/C03 w atlasie | Miejskie landmarki, np. C01 Jacek; nie eksperymenty Etapu C |
| N01 | Zalew Muchawka |
| S02 | Park Wodny, inna atrakcja niż N01 |
| M01…M40 | Istniejące kandydatury minigier z Etapu A |
| C-P01…C-P05 | Pięć proponowanych eksperymentów Etapu C; nie nowe minigry M41+ |
| S01…S13 w SOURCES_AND_METHOD | Źródła badania; nie identyfikatory obiektów sportowych atlasu |

Zawsze podawaj przestrzeń nazw, jeśli samo ID mogłoby wprowadzić błąd, np. „źródło S02” albo „landmark S02”. Przebieg prawdziwych tras i lokalizacja Górki Grześ wymagają dowodu z Etapu A. Nie wymyślaj współrzędnych.

## 3. Czego nie wolno dopowiadać

**Nie zamieniaj F w O.** Opis producenta jest źródłem funkcji, nie naszą obserwacją jej jakości. Wszystkie 15 gier mają w tym pakiecie **0 własnych sesji**. Nie dopisuj czasu pierwszej nagrody, FPS, cen, liczników graczy, pozycji rankingu i zachowania dziecka bez dowodu.

**Nie zamieniaj I/MC w decyzję właściciela.** Proponowany zegar, katalog, klomb, ekonomia i ścieżka 20-minutowa są pomysłami do sprawdzenia. Nie mają statusu zaimplementowane, przetestowane ani zatwierdzone.

**Nie myl dat.** Odczyt 19 października nie dowodzi, że karta gry opisuje patch z 19 października. Nie używaj historycznego raportu Roblox 2025 jako bieżącego rankingu. Wydarzenie wrześniowe S02 już się zakończyło. Przy aktualizacji zasad platformy porównuj nowsze oficjalne źródła z poprzednimi, zamiast automatycznie sklejać sprzeczne limity.

**Nie traktuj braku danych jako zera.** NOT_MEASURED to nie 0 sekund, zero zakupów ani brak graczy. Komunikat strony bez JavaScript nie jest licznikiem CCU.

## 4. Jak wykonać kolejne zadanie dokumentacyjne

Odczytaj bieżący `main` oraz plik, który chcesz zmienić. Wybierz jedno konkretne pytanie, np. „czy tę czynność da się ukończyć bez partnera?”. Znajdź źródło pierwotne albo rzeczywisty wynik sesji. Zapisz osobno fakt, interpretację i propozycję. Zaktualizuj tylko dokumenty, które z tego wynikają.

Przy pozycji gry sprawdzaj autora i Place ID. Kopie o identycznej nazwie są innymi doświadczeniami. Nie podstawiaj Place ID do endpointu wymagającego Universe ID. Nie dodawaj zależności od niepotwierdzonego API, planowanej funkcji lub przypadkowego poradnika.

Zadanie zakończ raportem: zmienione pliki, użyte źródła, wciąż otwarte kwestie, wynik walidacji linków i hash commita. Nie zamykaj całego Etapu C, jeśli wykonałeś jedynie edycję tekstu.

## 5. Jak wpisywać wyniki rozgrywek

Tylko po rzeczywistej sesji z urządzeniem i operatorem uzupełnij protokół 1/5/10/20. Istotne opóźnienie, brak konta początkującego albo niemożność wejścia są wynikiem BLOCKED/PARTIAL, nie pretekstem do wygenerowania brakujących obserwacji. Nagranie materiału promocyjnego nie jest własną sesją; jego analizę oznacz osobno jako źródło zewnętrzne i datę materiału.

Nie porównuj retencji po tygodniu na podstawie jednej wizyty. Nie wyciągaj opinii całej grupy wiekowej z odpowiedzi jednego dziecka. Ocena matematyki wymaga nauczyciela i testu własnego zadania; wynik konkurencyjnej gry nie zastępuje tego dowodu.

## 6. Gdy właściciel później zatwierdzi eksperyment

Wykonuj wskazany C-P, nie wszystkie systemy naraz. Zanim rozpoczniesz, odczytaj aktualny stan projektu i uzgodnione reguły synchronizacji `.rbxl` z `src`. Zrób bezpieczny punkt odniesienia i test na osobnym stanowisku. Respektuj kryteria błędnej odpowiedzi, podpowiedzi, wyjścia, dwóch uczestników i jednokrotnego naliczenia nagrody.

Nie dodawaj hydrodynamiki do testu dzielenia desek, edytora całego domu do albumu ani pełnego multiplayerowego tycoona do jednego zamówienia. Podstawowe klocki Roblox wystarczają do pierwszej oceny logiki; wysokiej jakości assety powstają później w zaplanowanym pipeline.

W obecnym zleceniu nie ma zgody na ten krok. `MathCity.rbxl`, `src/`, `tests/`, `tools/` i `assets/` pozostają bez zmian.

## 7. Zasady jakości i bezpieczeństwa

- Linki w dokumentacji mają być repozytoryjne względne albo prowadzić do właściwego źródła, nie do lokalnego dysku twórcy.
- Nie publikuj sekretów, danych kont, szkół, rozmów i nagrań dzieci.
- Współpraca działa przy wyłączonym czacie. Nie twórz ukrytego komunikatora ani kodowania wiadomości ikonami.
- Gotowe Quick Words są opcjonalną funkcją platformy; ich konfiguracji dla MathCity jeszcze nie wykonano.
- Matematyka, odkrywanie i sprawność ruchowa mają oddzielne wyniki. Podpowiedź nie jest płatną przewagą.
- Propozycje 10 żetonów, 30 za dekorację, 12 desek czy odcinki po 25 m są liczbami testu gry, a nie danymi rzeczywistych atrakcji.
- Zmiany GitHub wykonuj względem sprawdzonego HEAD, bez wymuszonego nadpisywania cudzych commitów. Przy zmianie gałęzi w trakcie pracy ponownie odczytaj zmodyfikowane pliki.

## 8. Status końcowy, którego nie wolno zawyżać

**Research źródłowy: dostarczony. Manualny benchmark: oczekuje. Eksperymenty MathCity: niezbudowane i nietestowane. Etap C: PARTIAL.** Pełny PASS wymaga spełnienia bramki z protokołu i zaakceptowania wniosków przez właściciela. Sam zielony diff dokumentacji nie jest zielonym wynikiem rozgrywki.
