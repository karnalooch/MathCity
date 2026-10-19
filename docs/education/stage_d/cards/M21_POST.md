# M21: Poczta i kurier

SPEC_READY / TEACHER_REVIEW_PENDING / CODE_NOT_STARTED. C14. ORDER, O:II.2.4; N:1.1, [źródła](../CURRICULUM_SOURCES.md). Numery domów i paczki są fikcyjne; nie zbieraj adresów dzieci.

## Zadanie i interakcja

„Ułóż paczki od najmniejszego numeru domu do największego.” Trzy paczki z dużymi liczbami35,12,21, trzy szerokie sloty kolejności. Dotknij paczki i slotu; zajęty slot zamienia miejscami, nie usuwa obiektu. Drag opcjonalny. Nie pokazuj wszystkich wejść już posortowanych. Strzałka „mały→duży” wyjaśnia kierunek bez podania kolejności konkretnych liczb.

## Walidator

Odpowiedź jest permutacją dokładnie trzech nadanychID paczek. Numery pobiera serwer z assignment, nie z payload. Warunek: numbers[1]≤numbers[2]≤numbers[3]. W głównej domenie wszystkie są różne, więc poprawna kolejność liczb to12,21,35. Inny porządek paczek z równymi numerami byłby dopuszczalny w przyszłym wariancie, ale generator pilota ich nie tworzy. PowtórzonyID nie jest poprawną permutacją nawet przy „dobrych” liczbach. Nie sortuj leksykograficznie stringów, bo100 może błędnie poprzedzić20.

## Domena

Sześć ręcznie zatwierdzanych zestawów liczbowych: {2,5,7}, {3,8,10}, {12,21,35}, {5,12,20}, {102,120,201}, {7,17,70}. Generator może wybierać dowolną z6permutacji każdej trójki, łącznie36 stanów. Dla pierwszego wejścia35,12,21. Łatwy band jednocyfrowy; dalej mieszane liczby i porównanie dziesiątek/jedności; trzycyfrowe tylko po właściwym review. Bandy nie są etykietą wieku na avatarze.

## Pomoc

UI_HELP demonstruje przeniesienie pustego pudełka i zamianę slotów. HINT1: „Poszukaj najmniejszego numeru.” HINT2: kolumny dziesiątek/jedności (przy trzycyfrowych też setek) jako pomoc matematyczna. GUIDED: porównaj pierwszą parę, wybierz mniejszy, porównaj z trzecią, ustaw pozostałe, przeczytaj wynik. Nie wykonuj serverSort na obiektach widocznych dziecku w trybie samodzielnym.

Po błędzie: „Kolejność nie rośnie. Porównaj sąsiednie numery.” Można od razu poprawić, bez utraty przygody i podstawowej nagrody. Błąd techniczny (drop poza UI, brak odpowiedzi serwera) nie liczy się jako złe porównanie.

## Powiązanie z dostawą i współpracą

Przygotowanie paczek jest ocenianą matematyką. Późniejszy przejazd może być częścią przygody, lecz sam teleport nie zalicza odcinków dostawy. W co-op każdy ma własną tacę lub partię; nie przechwyć prywatnej odpowiedzi kolegi. Może być wspólny znacznik liczby przygotowanych partii bez wyświetlania błędów uczniów. Dołączenie nowego uczestnika dopiero między sortowaniem a następnym etapem.

Kto pomaga przy ukończonej już własnej historii, uzyskuje nagrodę za realny wkład według kontraktu, ale nie ponowny firstGrant C14_POST_SORT_STORY. Wyjście zapisuje porządek obiektów; nowy seed nie zmienia starej próby i nie odnawia wyjątkowej nagrody.

## Odbiór

Wszystkie36 wejść kończą się prawidłową kolejnością. Test12/21/35,7/17/70 i102/120/201. Niepoprawne21/12/35, duplikatID, obceID i liczby podmienione po stronie klienta. Zapis w czasie zamiany nie może zgubić paczki. W dotyku każdy slot osiągalny bez zasłonięcia przez joystick lub systemową klawiaturę.
