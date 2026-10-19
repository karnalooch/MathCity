# Silne podpowiedzi UI: kontrakt dla PC, tabletu i telefonu

2026-10-19. Q07,Q13,Q15,Q22–Q27. **SPEC_READY / PLAYTEST_NOT_RUN.** Odczyt poleceń po polsku odłożony, nie wymagany teraz. Instrukcja dla wykonawcy: nie zastępować interakcji ścianą tekstu, migającą strzałką albo automatycznym rozwiązaniem.

## 1. Układ ekranu zadania

Góra: jedno krótkie polecenie i stabilne dane początkowe, widoczne przez całą próbę. Środek: obiekty do działania albo duża plansza. Dół: stałe przyciski „Cofnij”, „Pomoc”, „Sprawdź”; wyraźne „Wróć do miasta” dostępne bez ukończenia. Oddzielne, mniejsze „Jak sterować?” prowadzi do pomocy obsługowej. Ukończone etapy można pokazać ikonami, ale nie odliczać czasu matematycznego.

Nie zasłaniać treści joystickiem, palcem, paskiem systemowym, klawiaturą ani popupem nagrody. W wejściowym prototypie załóż poziomy układ rozgrywki jako TEST_DEFAULT; inne orientacje trzeba świadomie obsłużyć albo jasno zakomunikować przed użyciem, nie zostawić uciętego UI. W rzeczywistym kliencie sprawdź zmiany rozdzielczości i safe areas.

Rozmiary do pierwszej makiety: główne trafialne przyciski około48–64 jednostek ekranowych przy zastosowanej skali UI i odstęp co najmniej8. To własne ustawienia testowe, nie gwarancja fizycznego rozmiaru na każdym urządzeniu. Odbiór polega na wygodnym użyciu na iPadzie6 i obu telefonach, nie na samej liczbie w Properties. Tekst podstawowy czytelny bez przybliżania; nie zmniejszaj go w nieskończoność, żeby zmieścić długi opis.

## 2. Obsługa bez wymagania precyzyjnego drag

Każde zadanie z przeciąganiem ma równorzędny wariant „dotknij przedmiotu, dotknij celu”. Wybrany przedmiot ma obrys, symbol i krótki podpis; ponowny tap anuluje wybór. Sloty są duże i snapują obiekt. Wypadnięcie palca poza cel nie jest błędem matematycznym. Drag nie przenosi kamery, gdy dziecko próbuje układać zadanie. Po zamknięciu planszy przywróć sterowanie światem.

Nie wymagaj hover, prawego przycisku myszy, skrótów klawiaturowych, wielopalcowego gestu albo przytrzymania fizycznego klawisza, aby skończyć podstawowe zadanie. Klawiatura/mysz może mieć wygodne skróty, ale pokazują się tylko właściwe podpowiedzi dla bieżącego wejścia. Gra nie może wymagać klawiatury systemowej do ustawienia zegara czy rozdzielenia desek.

## 3. Stany UI i teksty

| Stan | Widoczny komunikat / akcja | Czego nie robić |
|---|---|---|
| INTRO | Krótki cel i „Zaczynam” / „Później” | nie uruchamiać quizowego timera |
| ACTIVE | Stałe dane, obiekty, przyciski | nie podmieniać liczb w tle |
| OBJECT_SELECTED | Obrys i dozwolone technicznie cele | nie wskazywać wyłącznie matematycznie poprawnego celu bez oznaczenia pomocy |
| CHECK_WAIT | „Sprawdzam…” i blokada powtórnego wysłania | nie pokazywać błędu odpowiedzi z powodu laga |
| INCOMPLETE | „Zostały przedmioty do ułożenia.” | nie usuwać poprawnych elementów |
| TRY_AGAIN | Krótkie wskazanie niespełnionego warunku | nie śmierć, utrata nagrody, publiczny wynik |
| UI_HELP | Pokaz gestu na neutralnym przykładzie | nie oznaczać automatycznie ASSISTED |
| MATH_HINT | Jawna podpowiedź matematyczna i powrót do działania | nie podszywać rozwiązania pod instrukcję obsługi |
| GUIDED | Jeden krok, własna akcja dziecka, następny krok | nie wykonać całego zadania bez uczestnictwa |
| SYNC_WAIT | „Zapisuję postęp. To może chwilę potrwać.” | nie dopisywać drugi raz punktów |
| COMPLETE | Rezultat, wyjaśnienie i należna nagroda | nie porównywać publicznie szybkości uczniów |
| PAUSED | „Wznowisz to zadanie później.” | nie kasować seedu i potwierdzonych etapów |

Komunikaty to przykłady redakcyjne; sprawdzić czytelność i długość na docelowych ekranach. Po sukcesie wyjaśnienie może pokazać wynik, ale ten ekran nie jest nową próbą samodzielną.

## 4. Drabina pomocy

Po wejściu: pokaż cel i możliwość działania, nie podawaj odpowiedzi. Na żądanie: UI_HELP objaśnia gest. Przy matematycznej trudności użytkownik wybiera „Podpowiedź”; hint wskazuje relację. Następna podpowiedź przedstawia strategię. Tryb „Zróbmy razem” dzieli zadanie na kroki i pozwala dziecku wykonywać je samodzielnie w obrębie prowadzenia.

Po dwóch świadomych błędach UI może zaproponować pomoc, ale nie wymusza jej. Po dłuższym bezruchu może wskazać przycisk pomocy obsługowej; brak ruchu nie obniża umiejętności i nie odbiera nagrody. Nie trzeba pytać o pomoc na czacie ani pisać zdania własnymi słowami.

W M34 podświetlenie wszystkich legalnych sekcji jest obsługowe; wskazanie tej, w której brakuje deski do równego rozdziału, jest już pomocą matematyczną. W M02 prowadnica do konkretnego odbitego okna jest MATH_HINT. W M01 demonstrowanie przesunięcia wskazówki na innej, neutralnej tarczy może być UI_HELP, ale pokazanie trzech potrzebnych kroków bieżącego zadania jest MATH_HINT.

## 5. Informacja o błędzie bez kar

Warunki rozwiązania mają być jawne przed próbą. Przy błędzie pokazuj konkretnie: nierówne grupy, brak elementu, niezgodna jednostka, zły kierunek porządkowania. Nie pokazuj „Źle!” jako całego wyjaśnienia i nie oceniaj osoby. Pozostaw prawidłowo ułożone elementy; cofnięcie czy poprawka nie wymagają restartu. Awaria sieci ma osobny stan techniczny, nigdy „Nie umiesz”.

Samodzielnie zauważona poprawka po sprawdzeniu może zakończyć zadanie bez użytej wskazówki. Nie jest jednak wystarczającym pojedynczym dowodem całej umiejętności. Wysokość podstawowej nagrody jest taka sama po guided i bez guided. Pomoc nie kasuje poprzednich osiągnięć w paszporcie.

## 6. Czytelność i prywatność

Kolor + kształt/symbol + podpis, nie sam czerwony/zielony. Ograniczone miganie i kamera; można wyłączyć nadmiarowe efekty. Dźwięk nie jest konieczny do zrozumienia zadania, rytmu ani alarmu przeszkody. Wyniki matematyczne i statusy pomocy widzi właściciel, nie gość pokoju ani członkowie drużyny. Wspólna tablica pokazuje gotowość stanowiska, nie ocenę ucznia.

Śledzenie misji dotyczy jednego celu i jest odrębne od instrukcji bieżącej planszy. Duże popupy level-up, zaproszenia oraz sklep nie mogą przerywać trwającego zadania; odłóż je do bezpiecznego miejsca, nie blokuj odpowiedzi.

## 7. Odbiór jednej minigry

Nagraj: rozpoczęcie → działanie tap–tap → działanie drag → nietrafiony drop → błędny wynik → UI_HELP → MATH_HINT → GUIDED → poprawne ukończenie → potwierdzony zapis → wyjście i wznowienie innej próby. Powtórz na czterech urządzeniach z [DEVICE_ACCEPTANCE](../tech/DEVICE_ACCEPTANCE.md). Bez mikrofonu, dźwięku i fizycznej klawiatury na urządzeniach mobilnych. Screen z emulacji nie zastępuje tego nagrania.
