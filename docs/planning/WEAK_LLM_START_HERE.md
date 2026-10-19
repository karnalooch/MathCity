# MathCity: START HERE dla wykonawcy o ograniczonym kontekście

Wersja 1, 2026-10-19. Repozytorium: `karnalooch/MathCity`. Baza opracowania: `030c8637010525ec0533daffe44c2e3f963bc1da`. **Dostarczono plan i dokumentację; implementacja nowych systemów NIE jest wykonana.**

## 0. Twoje zadanie i kolejność ważności

Właściciel wybrał 33 reguły produktu. Nie wybieraj ponownie A/B/C, nie odtwarzaj projektu z własnej pamięci i nie kopiuj wzorców GTA/Mario dosłownie. Najpierw przeczytaj [OWNER_DECISIONS_20261019.md](OWNER_DECISIONS_20261019.md). Następnie wykonuj JEDEN pakiet z [EXECUTION_PACKETS.md](EXECUTION_PACKETS.md), z wymaganymi wejściami i dowodami.

Kolejność: decyzje Q01–Q33 > kontrakty tego pakietu > zaakceptowane wyniki testów > starszy research > pomysły wykonawcy. Nowe ustalenia nie kasują realnych punktów atlasu M01–M40, Cxx/Nxx/Sxx/Txx. `N01` = Zalew Muchawka, `S02` = Park Wodny; Sekuła = biegówki, lokalizacja Grześ nadal niepotwierdzona. Roboczy masterplan 7 stref nie jest certyfikowaną mapą Siedlec.

## 1. Granica upoważnienia

Obecne zlecenie: plan i dokumentacja. Wolno zmieniać `docs/**`; nie ruszać `MathCity.rbxl`, `src/**`, `tests/**`, `tools/**`, `assets/**`, konfiguracji, publikacji Roblox ani lokalnego YACS. W kodowych pakietach Pxx wejściem jest osobne zlecenie właściciela uruchamiające ten pakiet. Po takim zleceniu pracuj w osobnej gałęzi i testowej kopii miejsca, nigdy przez nadpisanie sprawdzonej mapy. Dopuszczenie kodu nie oznacza zgody na publikację dla dzieci.

Stan PR #1 przy odczycie: Draft, niepołączony, zgoda stylistyczna oczekiwana. Nie merge ani rebase tego PR w ramach tej pracy. Dokumentacja artystyczna na jego gałęzi może nie istnieć na main; używaj adresu PR, nie zmyślonego lokalnego linku.

## 2. Pięć niezależnych stanów

1. **Postęp przygody:** odkrycia i osobiste etapy historii; pozwala odblokowywać następne kroki.
2. **Poziom przygody:** EXP, rangi i kosmetyka; NIE jest przepustką do misji.
3. **Umiejętności matematyczne:** prywatne, per skill; NIE rosną od EXP ani sportu.
4. **Wyniki sportowe:** czas/medale na określonych zasadach; NIE ocena matematyki.
5. **Świat współdzielony:** atrakcje i krótkie wydarzenia; NIE ukończenie osobistej historii za wszystkich.

Pomylenie dowolnych dwóch stanów jest błędem blokującym odbiór.

## 3. Minimalny kontekst na jedno podejście

Przeczytaj ten plik, właściwe wiersze Qxx, jeden kontrakt i kartę minigry. Nie ładuj całego repo do prompta i nie przepisuj wszystkich docs przy jednej poprawce. Rekomendowany rozmiar PR: jeden problem, do 3 plików logiki i odpowiednie testy; gdy trzeba więcej, wyjaśnij zależność przed poszerzeniem zakresu. To ograniczenie robocze, nie pretekst do pomijania testu integracji.

## 4. Mapa dokumentacji wykonawczej

| Potrzeba | Czytaj |
|---|---|
| Co zostało wybrane? | [33 decyzje](OWNER_DECISIONS_20261019.md) |
| Co zrobić po kolei? | [Pakiety D/P](EXECUTION_PACKETS.md) |
| Co i jak sprawdzić? | [Testy](ACCEPTANCE_MATRIX.md) |
| Etap D i status programu | [STAGE_D_README](../education/STAGE_D_README.md) |
| Źródła i konkretne punkty programu | [CURRICULUM_SOURCES](../education/stage_d/CURRICULUM_SOURCES.md) |
| Audyt wszystkich 40 propozycji | [M01_M40_AUDIT](../education/stage_d/M01_M40_AUDIT.md) |
| Szablony, walidatory, adaptacja | [TASK_MODEL_AND_ADAPTATION](../education/stage_d/TASK_MODEL_AND_ADAPTATION.md) |
| Osiem kart pilotowych | [Indeks kart](../education/stage_d/PILOT_INDEX.md) |
| EXP, pomoc i antygrind | [PROGRESSION_AND_REWARDS](../gameplay/specs/PROGRESSION_AND_REWARDS.md) |
| Drużyny, późne wejście, historia | [COOP_AND_WORLD_STATE](../gameplay/specs/COOP_AND_WORLD_STATE.md) |
| Pokój, paszport, onboarding, transport | [EXPLORATION_HOME_ONBOARDING](../gameplay/specs/EXPLORATION_HOME_ONBOARDING.md) |
| Wyścigi, profile, boty i przedmioty | [RACING](../gameplay/specs/RACING.md) |
| Silne podpowiedzi UI | [LEARNING_UI_CONTRACT](../ux/LEARNING_UI_CONTRACT.md) |
| Sieć, zapis, bezpieczeństwo | [DATA_AND_SERVER_CONTRACT](../tech/DATA_AND_SERVER_CONTRACT.md) |
| iPad, Android, PC i 16 graczy | [DEVICE_ACCEPTANCE](../tech/DEVICE_ACCEPTANCE.md) |

## 5. Preflight przed każdym pakietem

Ustal HEAD i gałąź; przeczytaj diff od poprzedniego zadania. Sprawdź, czy ktoś zmienił wymagane pliki. Jeśli stan lokalny brudny, nie resetuj ani nie stashuj cudzych zmian bez decyzji. Zapisz blob SHA mapy i drzew kodu przed pracą. Potwierdź zakres upoważnienia oraz istnienie narzędzi; ścieżki instalacji na D: trzeba wykryć, nie skopiować z YACS na ślepo. Nie instaluj na C: na podstawie domyślnych ustawień.

Przed uploadem porównaj bazowy HEAD z bieżącym; przy zmianie przeczytaj różnice i przebuduj commit z nowej bazy. Nie stosuj force push, nie nadpisuj równoległej pracy. Na main może trafić wyłącznie uzgodniona dokumentacja. Kod idzie do gałęzi i review.

## 6. Stop rules

STOP lokalnego zadania: brakuje wymaganego źródła; identyfikator nie istnieje; przykład matematyczny ma sprzeczne warunki; próba dotknięcia produkcyjnego DataStore; nieznana licencja; test nie ma właściwego urządzenia; nie da się bezpiecznie pogodzić równoległych zmian. Oznacz właściwe pole `BLOCKED_*`, opisz co już ustalono i dokończ niezależne zadania dokumentacyjne. Nie wymyślaj wyniku, narzędzia, lokalizacji, zgody nauczyciela lub renderu.

Nie blokuj całego planu tylko dlatego, że progi EXP nie są finalne: stosuj jawny parametr testowy, nie zmieniaj reguły właściciela. Dokumentacja prawa i polityk wymaga ponownego sprawdzenia przed premierą.

## 7. Raport końcowy każdego pakietu

Podaj: packet_id; baza i końcowy SHA; zmienione ścieżki; Qxx; wykonane komendy; liczbę uruchomionych i nieuruchomionych przypadków; dowody i urządzenia; ograniczenia; następny dozwolony pakiet. Rozdziel `DOC_CHECKED`, `UNIT_PASS`, `STUDIO_PASS`, `DEVICE_PASS`, `TEACHER_APPROVED`, `OWNER_APPROVED`. Nie istnieje ogólny PASS wynikający tylko z commita.

Najbliższa praca: D00, potem D01–D06. Pierwszy późniejszy eksperyment kodowy: P00/P01 i M34, NIE jednocześnie całe miasto, mieszkania i Mario Kart.
