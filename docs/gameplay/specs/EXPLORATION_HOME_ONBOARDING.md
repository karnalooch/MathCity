# Miasto, paszport, pokój, podróż i pierwsze minuty

2026-10-19. Q01,Q03–Q04,Q08–Q14,Q21–Q23. Projekt bez implementacji. Koncepcja całego miasta pozostaje ambitna; poniższy mały scenariusz jest testem jakości, nie zamiennikiem masterplanu.

## 1. Osobisty paszport

Zakładki: Przygody, Miejsca, Nagrody, Moje umiejętności. Przygodę można znaleźć u mieszkańca albo na liście. Widoczne: krótki cel, spodziewana aktywność, możliwa nagroda i Solo/Zaproś/Znajdź ekipę. Nie pokazuj wszystkich questów jako znaczników na mapie. Na starcie sugeruj3 różne opcje jako TEST_DEFAULT, śledź maksymalnie1 wybraną. Przypięcie nagrody pokazuje powiązany cel, nie prowadzi do sklepu za Robux.

Moje umiejętności: prywatne Poznaję/Ćwiczę/Rozwiązuję samodzielnie. Cel szczegółowy, np. „Dzielę równo do 3 grup”, nie „matematyka ukończona”. Karta pokazuje przykład i link do ćwiczenia. Goście, party i tabele sportowe tego nie otrzymują.

## 2. Odkrycia i szybka podróż

Przy faktycznym dotarciu do oznaczonego punktu serwer potwierdza odkrycie raz. Od tego momentu można za darmo podróżować między poznanymi punktami. Nie wymaga odpowiedzi matematycznej, monet i ekonomicznego cooldownu. Krótka blokada techniczna na spam żądań nie może stać się licznikiem utrudniającym podróż.

Transakcja podróży: sprawdzenie prawa do celu i aktualnego stanu → przygotowanie/streaming miejsca docelowego → bezpieczne położenie → odblokowanie sterowania. Nigdy nie zaliczaj odległości teleportacji jako jazdy. Przy aktywnej próbie sportowej lub trasowej dostawie: jawne ostrzeżenie „Ta podróż przerwie próbę trasy”; potwierdzenie anuluje bieżący segment, nie wcześniejszą matematykę/medale. Błąd streamingu zostawia gracza w bezpiecznym punkcie źródła, nie w pustce.

Sekrety pozostają odkrywane spontanicznie. Nie blokuj wszystkich zwykłych misji w nieoznaczonych zaułkach ani nie wymagaj powrotu pieszo przez pół mapy do wznowienia historii.

## 3. Pokój od początku

`starterEntitlements` obejmuje podstawowy transport i prawo do prywatnego pokoju przed tutorialem. Prototyp pokoju: gotowy mały układ, ograniczona biblioteka dekoracji i proste sloty/siatka. Sklep oferuje podstawowe rzeczy, przygody pamiątki. Nie implementuj wolnego budowania całego bloku, gospodarki nieruchomościami, czynszu ani handlu gracz-gracz.

Zaproszenie do pokoju to odrębna zgoda, nie automatyczny skutek przystąpienia do drużyny. Gość tylko ogląda i porusza się; wszystkie mutacje układu serwer sprawdza względem ownerUserId. Dekoracje muszą pochodzić z inventory i mieścić się w legalnych slotach. Cofnięcie przez gospodarza nie modyfikuje cudzej kolekcji. Opuszczenie serwera nie kasuje pokoju. Renderuj tylko potrzebne wnętrza, nie wszystkie16 bogatych mieszkań przez całą sesję.

## 4. Onboarding bez obowiązkowego egzaminu

Cele czasowe to pomiary do pilota, nie presja dla dziecka. Najpierw wybór klasy z możliwością zmiany później; to nie weryfikacja wieku platformy. Potem krótki cel spacerowy w centrum, pokaz ruchu i interakcji, otwarcie paszportu i jedno proste zadanie na obiektach. Interakcja może używać tej samej mechaniki co M05, lecz nie udawać lokalizacji N06 pod ratuszem. Nie losuj od razu wymagającego zadania z ułamków.

Widoczne „Pomiń na razie” i „Wróć do wprowadzenia”. Stany samouczka zapisane po krokach. Po mini-zadaniu podziękowanie, jedna drobna pamiątka i3 sugerowane przygody. Wyjście przed końcem zachowuje pokój, pojazd i wszystkie uprawnienia startowe; resume nie przyznaje ich drugi raz. W kolejnych funkcjach pojawiają się krótkie kontekstowe wskazówki, nie drugi blok instrukcji całego miasta.

## 5. Osobista historia a wspólny efekt

Misje poboczne mają własne początki/końce i małe serie. Przykład roboczy: Pomost → Plażowe zamówienie → Przygotowanie rowerowej trasy. Konkretne nazwy, nagrody i długość serii są propozycją treści; uzgodniona jest jej modułowa forma. Ukończenie jednej serii nie wymaga EXP z innej. Odblokowanie rozdziału powiązane ze zbiorem jego wymaganych własnych etapów.

Efekt zadania: dekoracyjny własny fragment/pamiątka oraz lokalna prezentacja w czasie przygody. Nie usuwaj wspólnego pomostu całemu miastu, gdy dołączy początkujący, ani nie oznaczaj jego budowy jako ukończonej u wszystkich obecnych. Tymczasowy festyn ma osobny WorldEvent.

## 6. Testy

Skip tutorialu i pokoju dostępność;resume;start entitlements raz;jedna śledzona misja;zmiana celu;przypięta nagroda;odkrycie tej samej stacji20razy;podróż do odkrytego/nieodkrytego punktu;zła odpowiedź nie blokuje miasta;teleport nie nabija dostawy;nieudany streaming;gość próbuje przesunąć/zabrać dekorację;wyciszenie pełne i dotyk. Rzeczywiste wykonanie pozostaje NOT_RUN.
