# M35: Rowerowa Pętla Muchawki

SPEC_READY / TEACHER_REVIEW_PENDING / CODE_NOT_STARTED. N12, połączenie z N01. LENGTH/ADD_SUB O:II.5.2,II.3.4; N:2.2,N:1.9. [Źródła](../CURRICULUM_SOURCES.md). Długości to dane fikcyjnego planu, nie pomiar prawdziwej promenady.

## Rozdzielenie faz

PLAN: bez stopera i bez wymogu ruszania pojazdem. Polecenie: „Na planie odcinki mają 200 m, 150 m i 250 m. Ile metrów ma cała trasa?”. Trzy odcinki z etykietami i symbolami, spójna kolejność. Po zatwierdzeniu można rozpocząć przejazd przygodowy. Dobrowolny osobny wyścig na czas ma osobne zasady i nagrody; szybkość obliczenia600 nie poprawia czasu sportowego.

## Dane i wynik

EdgeIDs e1,e2,e3, lengths{200,150,250} w modelowych metrach. Wynik600m, nie600studów i nie600km. Do odpowiedzi wymagaj wskazania wszystkich trzech odcinków oraz właściwej sumy. Kolejność sumowania może być różna. Wirtualna siatka miasta używa skali i uproszczeń; nie wyliczaj zadania automatycznie z bieżącej pozycji każdego avatara. Zadanie ma podpis „Plan ćwiczeniowy”.

## Generator

Skończona domena pilota: [20,10,30]→60; [100,50,150]→300; [200,150,250]→600; [250,250,500]→1000. Każda tablica ma3dodatnie całkowite długości, nie przekracza1000 łącznie. Zakresy do recenzji indywidualnej. Pierwsza trudniejsza próbka200/150/250, łatwy band20/10/30. Zmiana liczby odcinków, prędkości lub skali to nowy recenzowany wariant, nie przypadkowy los.

## Opcjonalny wariant otwarty

Na osobnej karcie wariantu: „Wybierz trasę nie dłuższą niż600m i pokaż jej sumę.” A=200+150+250=600; B=100+200+250=550; C=300+200+200=700. A i B poprawne, C nie. Jeżeli instrukcja miałaby brzmieć „najkrótsza”, wtedy tylko B; wykonawca nie może zamieniać tych poleceń przy tym samym walidatorze. A/B mają równoważną nagrodę. Zmiana wybranej poprawnej trasy po ukończeniu nie tworzy drugiej wypłaty.

## UI i pomoc

Duże etykiety w panelu, nie mikroskopijne napisy na ziemi. Tap odcinek wyróżnia go w planie i w scenie; zaznaczony fragment nie może być pomylony z globalnym markerem questu. UI_HELP tłumaczy wybór odcinka. HINT1: „Dodaj długości wszystkich odcinków.” HINT2: „Możesz najpierw połączyć200 i250.” GUIDED: dziecko składa200+250=450, następnie+150=600 na blokach; jawne ASSISTED. Przed odpowiedzią nie pokazuj sumy w automatycznym GPS, która zdradziłaby całe zadanie.

## Przejazd i wspólna gra

Wspólny przejazd nie wymaga identycznej szybkości ani matematyki całej ekipy. Osobiste przygotowanie ma własny expected. Matematyczne zadanie już ukończone nie znika po wypadnięciu z roweru. Trasa jazdy zalicza kolejne legalne checkpointy, nie odległość teleportacji. Szybka podróż jest nadal dostępna po wyjściu z aktywnej dostawy; ostrzeż przed przerwaniem sportowej próby, bez odebrania poprzednich nagród.

Wznowienie matematyki przywraca te same długości. Rozłączenie podczas przejazdu ma osobny stan transportu; nie powoduje nowej wypłaty za liczenie. RewardObjective N12_ROUTE_PLAN_STORY nie jest tym samym co jednorazowy medal wyścigu.

## Odbiór

Suma600 i trzy poprawneID;550 błędne w wariancie sumy A, ale poprawne dla trasyB w wariancie otwartym. Nie akceptować700 przy limicie600 ani1000 bez jednostki w niezgodnym schemacie. Czas czytania=bez wpływu; teleport nie podbija dystansu; plansza nie zmienia się po streamingowej zmianie LOD. Kluczowe długości i checkpointy widoczne na niskiej grafice.
