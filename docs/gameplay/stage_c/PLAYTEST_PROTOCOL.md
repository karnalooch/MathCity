# Etap C: protokół rzeczywistych rozgrywek i rejestr dowodów

**Stan: 2026-10-19. Wykonane sesje: 0. Wszystkie pozycje poniżej mają status NOT_RUN.** Dokument określa sposób dokończenia etapu; nie jest raportem z testów już przeprowadzonych.

## 1. Cel i granica badania

Sprawdzić, jak zadeklarowane przez twórców mechaniki naprawdę wyglądają dla nowego gracza. Mierzymy początek zabawy, czytelność celu, powtórki, sterowanie, współpracę i presję zakupów. Nie wyciągamy z jednej sesji wniosków o przychodach gry, jej D1/D7, bezpieczeństwie wszystkich serwerów lub zachowaniu wszystkich dzieci.

Do porównania używać dokładnych adresów i Place ID z [SOURCES_AND_METHOD.md](SOURCES_AND_METHOD.md). Nie uruchamiać kopii o identycznym tytule. Źródłowe gry są przedmiotem badania przez dorosłych, a nie listą gier polecanych dzieciom. Zwłaszcza horror, strzelanie i kradzież nie wymagają sesji dziecka, aby zespół zbadał ich strukturę.

## 2. Metryka sesji

Przed startem zapisać: identyfikator G01–G15, datę i czas ze strefą, Place ID, wersję gry jeśli jest faktycznie widoczna, urządzenie, ekran, metodę sterowania, ustawienia grafiki, stabilność połączenia oraz czy konto ma wcześniejszy postęp. Nie podszywać się pod dziecko i nie zmieniać deklaracji wieku na potrzeby testu. Różne ustawienia komunikacji i uprawnień kont należy zanotować bez zapisywania danych osobowych.

Konto z historią gry nie jest równoważne nowemu użytkownikowi. Gdy nie da się legalnie uzyskać początku rozgrywki, oznaczyć ONBOARDING_NOT_OBSERVED i zapisać przyczynę. Nie kasować zapisów produkcyjnych użytkownika ani nie kupować przepustek w celu „uzyskania kompletnych danych”.

Uruchomić dwa pomiary czasu: **T-launch** od wybrania uruchomienia do możliwości sterowania oraz **T-play** od faktycznego przejęcia kontroli. Punkty 1/5/10/20 minut odnoszą się do T-play. Czekania i rozłączenia mają osobne znaczniki, zamiast znikać z rachunku.

## 3. Cztery punkty obserwacji

| Punkt | Co zapisać |
| --- | --- |
| 1 minuta | Pierwszy widoczny cel, pierwsza czynność ze skutkiem, liczba obowiązkowych ekranów, obecność sklepu przed zabawą, samodzielne zrozumienie sterowania |
| 5 minut | Pierwsza nagroda, znaczenie walut i przedmiotów, rzeczywiste czekanie, możliwość odmowy zadania, pierwsze zdarzenie współpracy |
| 10 minut | Czy zmienił się rodzaj czynności, czy gracz tylko powtarza cykl, dostęp do kolejnego miejsca, źródła frustracji, jakość podpowiedzi |
| 20 minut | Czy istnieje sensowny kolejny cel, czy można skończyć bez straty, jakie są powody powrotu, dominujący koszt czasu i liczba decyzji o zakupie |

W każdym punkcie oddzielić **obserwację** („trzy ekrany przed kontrolą postaci”) od **interpretacji** („może to utrudniać szybki start”). Nie dopisywać wypowiedzi testera, których nie wypowiedział. Nie wystawiać ocen „dzieci uwielbiają”, jeśli badanie dotyczy jednego dorosłego obserwatora.

## 4. Metryki robocze

| Pole | Jednostka i definicja |
| --- | --- |
| time_to_control | Sekundy od uruchomienia do sterowania postacią |
| time_to_first_meaningful_action | Sekundy T-play do działania, które zmienia stan gry i którego cel tester potrafi wyjaśnić |
| time_to_first_reward | Sekundy T-play do pierwszej rozpoznanej nagrody; nie sam ekran reklamy nagrody |
| mandatory_ui_count | Liczba obowiązkowych ekranów przed pierwszą czynnością |
| passive_wait_seconds | Łączny czas przymusowego czekania w obserwowanym odcinku |
| purchase_prompts | Liczba ofert zakupowych i kontekst ich wyświetlenia; nie liczba zakupów |
| repeated_identical_cycles | Kolejne powtórzenia bez nowej decyzji lub zmiany reprezentacji |
| input_actions_per_cycle | Kliknięcia/dotknięcia wymagane do jednej podstawowej czynności; szczególnie G06/G07 |
| recovery_seconds | Czas odzyskania kontroli po błędzie i powrotu do porównywalnej próby |
| blocked_without_partner | Czy brak drugiej osoby uniemożliwia zadanie; opisać warunek |
| playable_without_chat | Czy cel i kolejny krok są czytelne przy wyłączonym czacie |
| next_goal_explanation | Jedno zdanie testera o tym, co zrobiłby dalej; brak odpowiedzi też jest wynikiem |

Brak pomiaru = **NOT_MEASURED**, brak możliwości obserwacji = **NOT_OBSERVABLE**, czynność nie wystąpiła przez 20 minut = **NOT_REACHED_WITHIN_WINDOW**. Żadnego z tych stanów nie zastępujemy zerem. Jeśli cena jest widoczna, zapisać ją razem z datą, walutą i kontekstem oferty; nie ogłaszać jej uniwersalną ceną dla wszystkich kont.

FPS i użycie pamięci odnotowywać tylko wtedy, gdy narzędzie faktycznie je pokazuje. Subiektywne „płynnie” to obserwacja jakościowa, nie 60 FPS. Zrzut ze Studio nie zastępuje testu rzeczywistej gry na telefonie.

## 5. Rejestr 15 gier: stan początkowy

| ID | Gra | PC 20 min | Obserwacje 1/5/10/20 | Mobile | Kooperacja |
| --- | --- | --- | --- | --- | --- |
| G01 | Brookhaven RP | NOT_RUN | NOT_RECORDED | NOT_RUN, próba wybrana | Nie zaplanowano osobnej sesji |
| G02 | Adopt Me! | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | Nie zaplanowano osobnej sesji |
| G03 | Grow a Garden | NOT_RUN | NOT_RECORDED | NOT_RUN, próba wybrana | Nie zaplanowano osobnej sesji |
| G04 | Steal a Brainrot | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | Nie zaplanowano osobnej sesji |
| G05 | 99 Nights in the Forest | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | NOT_RUN, próba wybrana |
| G06 | Fisch | NOT_RUN | NOT_RECORDED | NOT_RUN, próba wybrana | Nie zaplanowano osobnej sesji |
| G07 | Fish It! | NOT_RUN | NOT_RECORDED | NOT_RUN, próba wybrana | Nie zaplanowano osobnej sesji |
| G08 | Blox Fruits | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | Nie zaplanowano osobnej sesji |
| G09 | RIVALS | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | NOT_RUN, próba wybrana |
| G10 | Dress To Impress | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | Nie zaplanowano osobnej sesji |
| G11 | Tower of Hell | NOT_RUN | NOT_RECORDED | NOT_RUN, próba wybrana | Nie zaplanowano osobnej sesji |
| G12 | Build A Boat For Treasure | NOT_RUN | NOT_RECORDED | NOT_RUN, próba wybrana | NOT_RUN, próba wybrana |
| G13 | Epic Minigames | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | Nie zaplanowano osobnej sesji |
| G14 | Work at a Pizza Place | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | NOT_RUN, próba wybrana |
| G15 | Find the Markers | NOT_RUN | NOT_RECORDED | Nie zaplanowano osobnej sesji | Nie zaplanowano osobnej sesji |

„Nie zaplanowano osobnej sesji” nie oznacza, że gra nie wspiera danego trybu. To wyłącznie wybór próby porównawczej. Puste obszary można rozszerzyć po pierwszych wynikach, zwłaszcza gdy rekomendacja MathCity mocno zależy od niezbadanego interfejsu.

## 6. Mobile i dwie osoby

**Sześć prób mobilnych po 10 minut:** G01/G03/G06/G07/G11/G12. Ten sam telefon i zbliżone ustawienia grafiki. Sprawdzić dosięgnięcie przycisków, zasłanianie celu palcem, jednoczesną obsługę kamery i czynności, cofanie oraz odczyt instrukcji. G06/G07 porównać bez zakładania, że większa liczba kliknięć oznacza lepszą zabawę.

**Cztery próby kooperacyjne po 15 minut:** G05/G09/G12/G14. Dwie osoby o znanym poziomie znajomości gry, bez przekazywania celu poza grą. Najpierw normalna runda, potem wyłączony czat, następnie opuszczenie stanowiska albo rozłączenie jednego uczestnika w kontrolowanym momencie. Nie szkodzić innym graczom publicznego serwera; zachowanie destrukcyjne oceniać tylko w dozwolonym, izolowanym teście. Jeśli izolacja wymaga zakupu, oznaczyć ograniczenie zamiast kupować samoczynnie.

Plan pełnej próby to **300 minut PC + 60 minut mobile + 60 minut wspólnych sesji = 420 minut okien obserwacji**, czyli 7 godzin bez uruchamiania, przygotowania, przerw i opracowania. Sesje wspólne wymagają czasu dwóch osób. To arytmetyka planu, nie termin dostarczenia ani obietnica wykonania bez udziału człowieka.

## 7. Formularz pojedynczego wyniku

Każdy rzeczywiście wykonany test zapisujemy w nowym pliku, np. `sessions/YYYY-MM-DD_G01_PC.md`. Katalog sessions powstaje dopiero z pierwszym realnym raportem. Szablon nie jest dowodem sesji.

```text
ID gry i Place ID:
Data, godzina, strefa:
Urządzenie, ekran, sterowanie, grafika:
Wcześniejszy postęp konta: TAK/NIE/NIEZNANY
Widoczna wersja gry: wartość albo NOT_OBSERVABLE
Status: COMPLETED / PARTIAL / BLOCKED
T-launch, T-play:
1 min: obserwacja / dowód / interpretacja
5 min: obserwacja / dowód / interpretacja
10 min: obserwacja / dowód / interpretacja
20 min: obserwacja / dowód / interpretacja
Metryki i jednostki:
Co da się przenieść do MathCity:
Czego nie przenosić:
Który wniosek z BENCHMARK_15_GAMES trzeba skorygować:
Ograniczenia i brakujące obserwacje:
```

Zrzuty z cudzych gier są materiałem dowodowym do odpowiedniego wykorzystania, nie assetami MathCity. Publiczne repo nie jest miejscem na nagrania dzieci, ich kont, czat, dane osobowe i prywatne ścieżki z komputera. W testach prototypu z dziećmi potrzebny jest opiekun i właściwe zgody; dziecko może przerwać w dowolnej chwili. Nie łączyć braku chęci do dalszej gry z oceną zdolności matematycznych.

## 8. Bramka kończąca C

Przeprowadzić co najmniej 12 z 15 sesji PC z wymaganych 12–15 w roadmapie, zachowując pokrycie pięciu najważniejszych rodzin interakcji. Brakujące trzy gry muszą być jawnie wskazane, a wnioski zależne wyłącznie od nich pozostają warunkowe. Preferowane pełne 15 sesji. Wymagane są również wybrane próby dotyku i współpracy albo jawne uzasadnienie zmienionej próby zatwierdzone przez właściciela.

Następnie skorygować ranking, odróżnić wyniki normalnej sesji od eventowych, spisać konflikty i poddać rekomendację właścicielowi. Playtest konkurencji nie potwierdza skuteczności dydaktycznej MathCity; tę trzeba zbadać na własnych zadaniach. **Obecnie: PLAYTEST_PENDING, Etap C PARTIAL.**
