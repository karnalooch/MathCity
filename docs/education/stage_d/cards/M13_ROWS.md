# M13: Stadion, rzędy krzeseł i kilka rozwiązań

SPEC_READY / TEACHER_REVIEW_PENDING / CODE_NOT_STARTED. S01. MULTIPLY_GROUPS + OPEN_CONSTRAINT; O:II.3.3,II.4.1–2; N:1.10,N:6.3. [Źródła](../CURRICULUM_SOURCES.md). Liczby opisują fikcyjny mały sektor, nie rzeczywistą pojemność stadionu.

## Wariant zamknięty

„Ustaw 6 rzędów po 4 krzesła. Ile miejsc będzie razem?” 24 obiekty,6 oznaczonych rzędów. Expected6×4=24, każdy rząd ma4. Dziecko wybiera/umieszcza krzesła; pełny rząd można zapełnić zatwierdzanym krokiem, ale nie automatycznie rozwiązać całego problemu. Mnożenie może być przedstawione przez dodawanie grup. Nie wymagaj zapisu jednej metody.

## Wariant otwarty, główny cel eksperymentu

„Rozstaw wszystkie 12 krzeseł w równych rzędach. Zrób od 2 do 6 rzędów. W każdym ma być od 2 do 6 miejsc.” Plansza6×6, układ prostokątny, bez dziur. Poprawne pary (rzędy,miejsca) to (2,6),(3,4),(4,3),(6,2). Układy1×12 i12×1 nie spełniają JAWNYCH ograniczeń planszy. Nie odrzucaj ich na podstawie ukrytej preferencji projektanta; instrukcja musi wskazywać ograniczenia przed rozpoczęciem.

## Walidator otwarty

Wszystkie12 unikalnychID krzeseł użyte raz. Zajęte sloty tworzą pełny prostokąt r×c wewnątrz siatki;2≤r≤6,2≤c≤6,r×c=12. Translation do innego legalnego narożnika jest dozwolone; normalizuj minimalny rząd/kolumnę. Permutacja identycznych krzeseł i obrót prostokąta nie zmienia nagrody. Cztery powyższe pary opisują rozmiary, nie całą liczbę położeń na planszy. [3,3,3,3] jest poprawne jako4×3; [5,4,3] nie mimo sumy12.

## Domena kontrolowana

Wariant otwarty wybiera n z{6,8,10,12,15,16,18,20,24}; rozmiary boków2…6. Generator wylicza zbiór par spełniających iloczyn; dopiero gdy niepusty, publikuje zadanie. Dla n7 brak rozwiązań w domenie, więc dane są odrzucone i użyty ręczny zapas n12. Pierwszy pokaz zamknięty4×3 lub6×4, potem otwarte12. Pozostałe wartości wymagają pedagogicznego dobrania kolejności; nie mnożymy obiektów do setek na iPadzie.

## Mocne UI

Dotknij krzesła/partii, potem slotu; wolno wybrać liczbę rzędów przyciskami, ale system nie wskazuje automatycznie poprawnego ilorazu. „Cofnij” oraz „Wyczyść mój układ” z potwierdzeniem; nie usuwa innych stanowisk. Podświetlenie granic legalnej planszy = UI_HELP; wyróżnienie jednego poprawnego wymiaru = MATH_HINT. Informacja „W drugim rzędzie jest inna liczba miejsc” pomaga sprawdzić warunek; nie daje finalnej liczby bez jawnej wskazówki.

HINT1: „Rzędy mają być równe. Sprawdź, czy wykorzystujesz wszystkie krzesła.” HINT2: „Spróbuj rozdzielać po jednym do wybranych rzędów.” GUIDED: dziecko wybiera np.3 rzędy, rozdziela porcje, sprawdza4 w każdym, widzi12=3×4. W drugim przykładzie pokazujemy możliwość2×6, nie wymuszamy jej do odbioru nagrody. Osiągnięcie z pomocą nie jest niezależnym mastery.

## Multiplayer i nagroda

Każdy przygotowuje swój mini-sektor, z parametrami per skill. Wspólny efekt to fikcyjna gotowość widowni; nie współdzielą klocków roboczych. Nagroda S01_SEATING_STORY ma tę samą wartość dla wszystkich poprawnych rozwiązań i nie odnawia się po przejściu3×4→2×6. Zapis obejmuje dane i zajęte sloty; powrót po przerwie nie losuje innych12 krzeseł.

## Odbiór

Akceptacja4par dla n12 i wszystkich tłumaczeń wewnątrz6×6; odrzucenie1×12,3×3,5/4/3, dziury i duplikatu ID. Dla9 wartości n istnieje co najmniej1para. Zmiana rozwiązania po grant nic nie wypłaca. Dotyk i duże sloty działają na iPadzie oraz telefonie. Nie przerabiaj tego na płatne projektowanie trybun.
