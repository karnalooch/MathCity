# Pakiety wykonawcze: od 33 decyzji do działającej gry

Wersja 1, 2026-10-19. **Plan przyszłej pracy.** Dokumenty w repo nie oznaczają wykonania pakietu. Czytaj [START HERE](WEAK_LLM_START_HERE.md). Wszystkie nazwy przyszłych modułów są proponowaną strukturą: przed ich dodaniem sprawdź, czy odpowiednik już istnieje.

## Kolejność i bramki

`D00 → D01 → D02 → D03 → D04 → D05 → D06` to domknięcie edukacyjnej dokumentacji. `P00 → P01 → P02 → P03 → P04 → P05 → P06 → P07 → P08 → P09 → P10` to przyszłe eksperymenty po osobnym upoważnieniu. Część badań A/B/C/G może przebiegać równolegle, ale nie należy ogłaszać ich PASS. Wybór dokładnych 8 pilotów jest rekomendacją techniczną, nie nowym zakresem zatwierdzonym przez właściciela.

**Aktualizacja 2026-10-20:** właściciel uruchomił teraz **P00 + sam H00 z P06**, przed implementacją gameplayu. Wykonywalne wejście, izolacja i dowody: [P00_H00_RUNBOOK](../tech/P00_H00_RUNBOOK.md). H01/H02 oraz pozostałe pakiety nie są automatycznie uruchomione. Dostarczony kod nie oznacza wykonanego testu Windows/Houdini/Studio.

## D00: synchronizacja źródła prawdy

**Wejście:** OWNER_DECISIONS, aktualny GDD, decyzje historyczne. **Zakres:** tylko docs. **Czynności:** sprawdź komplet Q01–Q33; wykryj sprzeczności: płatny admin, śmierć za błędne drzwi, dzielnica=klasa, min poziomu do misji, głos wymagany na starcie, nieskończone pieniądze z rekordów. Oznacz starsze opisy jako historyczne, nie usuwaj ich bez potrzeby. **Wyjście:** lista rozstrzygnięć i linki w głównych indeksach. **Odbiór:** zero aktywnych wymagań przeciwnych Qxx; pliki gry niezmienione. **STOP:** niejednoznaczna nowa wypowiedź właściciela; nie dotyczy znanych i rozstrzygniętych 33 odpowiedzi.

## D01: źródła dydaktyczne i roczniki

**Wejście:** CURRICULUM_SOURCES. **Czynności:** odczytaj oficjalny tekst z właściwymi zmianami; potwierdź §4 oraz mapowanie roczników; dla każdej umiejętności zapisz konkretny punkt, etap I–III albo IV–VI, datę i stronę. Osobno wypełniaj propozycję klasy, bo dokument etapowy nie wyznacza automatycznie klasy 4. Sprawdź późniejsze zmiany aktu. **Wyjście:** zatwierdzony przez recenzenta wykaz źródeł; brakujący fragment = SOURCE_PENDING, nie MEN_VERIFIED. **Odbiór:** każdy pilot ma punkt źródła i jawny status klasy; pedagog nie jest zastępowany przez drugą odpowiedź LLM.

## D02: audyt M01–M40

**Wejście:** audit + oryginalna MECHANICS_MATRIX. **Czynności:** dla każdego ID sprawdź dane, wynik, jednostkę, instrukcję, ograniczenia wieku, zależność od zręczności i miejsca; nie dodawaj M41. Popraw M02/M28: sama liczba elementów nie sprawdza symetrii. Rozdziel obwód/pole M39. Dla M08 nie zgaduj geografii. **Wyjście:** 40 kompletnych wierszy i lista korekt z uzasadnieniem. **Odbiór:** wszystkie wiersze mają disposition i source anchor; replika lokalnego miejsca nie wynika z liczb ćwiczenia.

## D03: osiem kart pilotowych

**Wejście:** PILOT_INDEX, kontrakt UI i task model. **Czynności:** pracuj po jednej karcie: instrukcja, stan obiektów, walidator, co najmniej 3 kontrolowane warianty, typowe błędy, demonstracja obsługi, pomoc matematyczna, kroki wspólnego rozwiązania, nagrody, tryby 1–4 osób, poprawne i negatywne przykłady. **Wyjście:** karta kompletna bez pola „LLM wymyśli później”. **Odbiór:** drugi czytelnik potrafi ręcznie przewidzieć wynik każdego przypadku; materiał nie otrzymuje etykiety recenzji nauczyciela bez faktycznego review.

## D04: rejestr przykładów i kontrola generatorów

**Wejście:** osiem kart i TEST_VECTORS. **Czynności:** przelicz wszystkie przykłady deterministycznie. Dla skończonych zakresów wylicz wszystkie kombinacje, nie tylko losową próbkę. Udowodnij konstrukcyjnie, że generator daje rozwiązanie; osobno generuj kontrprzykłady. Dla zadań otwartych wylicz cały dopuszczony zbiór. Błędny generator kończy się znanym przykładem zapasowym, nie nieskończoną pętlą losowania. **Wyjście:** wyniki kontrolne dokumentacji. **Odbiór:** brak dzielenia przez zero, reszt nieprzewidzianych w karcie, sprzecznych zakresów i nieokreślonych zegarów. Nie nazywaj tych obliczeń testami Luau/Studio.

## D05: review pedagogiczne i UI

**Wejście:** D01–D04. **Czynności:** recenzent edukacji I–III i matematyki IV sprawdza adekwatność, słownictwo, progresję, błędy i granice adaptacji. Porównaj łamigłówkę otwartą z jej warunkami. Przeprowadź ocenę instrukcji i plan sesji z opiekunem. **Wyjście:** podpis/identyfikator recenzji, data, zakres i uwagi; bez danych dzieci w publicznym repo. **Odbiór:** TEACHER_APPROVED dla konkretnych wersji kart, nie dla całej gry z automatu. **STOP:** brak recenzenta pozostawia stan PENDING; wolno kontynuować test techniczny z syntetycznymi danymi i dorosłymi.

## D06: zamknięcie etapu D

**Wejście:** weryfikacja źródeł, 40 audytów, 8 kart, testy danych, review. **Czynności:** sprawdź spójność Qxx, brak nowych identyfikatorów i fałszywych PASS. Zapisz co wolno przenieść do prototypu. **Wyjście:** decyzja D_ACCEPTED albo lista otwartych punktów. **Odbiór:** warunki z STAGE_D_README; brak implementacji nie jest błędem tego etapu.

## P00: bezpieczny warsztat i izolacja

Zlecenie P00/H00 zostało uruchomione 2026-10-20. Sprawdź istniejące skrypty i mapę, źródło prawdy `.rbxl` vs Luau, backup i rollback. Wykryj Houdini/SideFX Labs oraz pomocnicze UE/Blender/Material Forge; nie instaluj ponownie warsztatu YACS. Dla H00 użyj nowego, nieopublikowanego lokalnego miejsca bez skryptów gry i bez DataStore. Przyszłe testy gameplayu mogą wymagać odrębnego testowego magazynu danych; H00 go nie tworzy. Nie zastępuj całego Workspace istniejącej gry. **Dowód:** otwarcie sceny testowej, Play, stop, ponowne otwarcie, zgodność mapy bazowej; rzeczywiste wersje narzędzi. **Bramka:** oryginał i produkcyjne dane nietknięte. [Komenda i kontrola](../tech/P00_H00_RUNBOOK.md).

## P01: czysty model zadania i generator M34

**Wejście:** M34, task model, test vectors. Proponowane pliki: `src/shared/education/TaskTypes.luau`, `EqualGroups.luau`, `tests/education/EqualGroups.spec.luau`. Najpierw walidator danych i funkcja wyniku, bez UI, sieci, DataStore, monetyzacji i fizyki tratwy. Enumeruj zakres; odrzuć duplikaty przedmiotów, obce ID, niecałkowite wartości, NaN/Inf. **Odbiór:** D04 w natywnym środowisku testu logiki; testy faktycznie uruchomione, interpreter/narzędzie wykryte zamiast wymyślonej komendy.

## P02: interakcja M34 + mocne UI na czterech urządzeniach

**Wejście:** P01 i kontrakt UI. Użyj prostych zakotwiczonych elementów. Zbuduj wybierz–dotknij celu jako pełnoprawną alternatywę drag; duże sloty, cofnięcie, pomoc obsługowa, pomoc matematyczna, guided steps, powrót. Bez głosu. **Dowód:** surowy screenshot i nagranie działań na iPadzie 6, G54, Note14 4G i PC. Emulator jest dodatkiem. **Odbiór:** poprawne/złe rozwiązanie, zamknięcie UI i wznowienie bez zmiany danych. To mała próbka interakcji, nie gotowa mapa.

## P03: serwer i trwały, jednokrotny zapis postępu

**Wejście:** kontrakt danych i nagród. Dodaj przydział zadania na serwerze, walidację intencji oraz bezpieczny ledger. Walidator nie ufa liczbie punktów z klienta. Zapisuj completion i grant w tej samej operacji profilu; nie modyfikuj wspólnego starego DataStore v1. **Testy:** duplikat remote, retriable write, crash przed/po zapisie, błąd odczytu, dwa jednoczesne żądania, reconnect. **Odbiór:** jedna nagroda i jeden completion, żadnego zerowania istniejącego profilu.

## P04: przygoda solo, pierwsze wejście, paszport i prywatny pokój

Zaimplementuj jedną krótką serię używając M34/M33; nie zamieniaj jej w całą główną fabułę. Tutorial opcjonalny. Pokój i podstawowy transport przyznane idempotentnie przed tutorialem. Jedna odznaka, jedna dekoracja, zakup za walutę z gry, prywatna mapa umiejętności. Dodaj darmowe odkrywane punkty podróży i ochronę przed zaliczaniem teleportem tras. **Odbiór:** skip/resume, osobiste completion, brak wejścia gościa w edycję i brak wycieku mastery.

## P05: 1–4 osoby i wznowienie

Dodaj role per-stage, części własne per-player, kolejkę wolnych miejsc na bieżącym serwerze. Człowiek dołącza tylko w bezpiecznej granicy etapów. Rozłączanie i odłączanie od grupy pozostawia osobisty postęp. Dodaj nagrody co-op i catch-up tylko po prawdziwym wkładzie. **Testy:** 1/2/3/4 graczy; wejście 5.; zmiana lidera; odejście przed nagrodą; uzupełnienie składu; brak czatu; ponowne dołączenie. **Odbiór:** żadnych ghost rewards i obowiązkowych czterech stanowisk.

## P06: **HOUDINI FIRST** — H00/H01/H02 i masterplan całego świata

**Wejście:** [HOUDINI_FIRST_PIPELINE](../tech/HOUDINI_FIRST_PIPELINE.md), pipeline, Art Bible, atlas i audyt licencji. Najpierw wykryj istniejący Houdini/SideFX Labs z YACS; nie instaluj nowego DCC.

**H00 Terrain:** mały HeightField z pagórkiem/doliną/brzegiem/building pad → erosion/constraints → heightmap + colormap → Roblox Terrain.

**H01 Mesh:** proceduralny pomost/murek/moduł ulicy → UV/pivot → FBX/glTF → Roblox, z kontrolą ponownego cooku po zmianie parametru.

**H02 Material:** trzy materiały z Material Forge/Houdini → PBR → SurfaceAppearance/MaterialVariant; normal map OpenGL.

UE wolno użyć do lookdev/review, Blender do hero-detail/retopo/UV/cleanup, Material Forge do PBR. **Nie wolno przenieść source-of-truth świata z Houdiniego do UE/Blendera.**

Po H00/H01/H02: makieta WSZYSTKICH roboczych stref. Warianty 8192/16384 studów pozostają eksperymentami. Dla Terrain odpowiadają im odpowiednio heightmapy 2048 i 4096 px przy 4 studach/piksel. Dobierz realistyczną gęstość instancji, granice streamingu i widoczne ikony Siedlec.

**Odbiór:** regenerowalność, porównanie przed/po recook, aktualizacja bez ręcznej rekonstrukcji, skala, materiały, kolizja, ruch i streaming; potem obowiązkowy iPad gate. Zmniejszenie skali, obejście Houdiniego przez ręczne budowanie albo usunięcie iPada wymaga decyzji właściciela.

## P07: czysta jazda i porównywalne rekordy

Najpierw jedna trasa, pomiar postępu/checkpointów i serwerowy czas. Rekomendacja testu TT: jeden profil referencyjny albo osobne tablice per profile; nie mieszać. Start bez zadań matematycznych na czas. Nagrody ukończenia i progów po jednym razie. **Odbiór:** skrót legalny/nielegalny, teleport, zmiana kierunku, disconnect, powtórka progu, wersja zasad i fizyki.

## P08: wyścig festynowy, profile, boty, trzy gadżety

Dodaj profile dostępne wszystkim, potem czytelne boty, dopiero potem banan/turbo/osłona jako roboczy zestaw. Testuj oddzielnie każdy efekt i powrót do sterowania. Catch-up zmienia tylko wagi przedmiotów. **Odbiór:** odrębne wyniki od TT, odporność na serię trafień, brak działania poza dobrowolnym wyścigiem, boty bez teleportów, brak bonusu co-op za sam fakt PvP. Liczba uczestników eksperymentu nie jest liczbą mieszkańców miasta.

## P09: kolejne karty i wydarzenie miejskie

Rozszerz do ośmiu recenzowanych kart; reużyj rendererów i generatorów. Jedno powtarzalne wydarzenie na serwerze daje wspólny efekt, ale nie cudze osobiste completion. Nie produkuj 40 minigier przed testem 8; zachowaj cały backlog. **Odbiór:** ścieżka solo i co-op, prywatność, równoważne nagrody, warianty otwarte, brak farmy waluty.

## P10: skalowanie, regresja, decyzja o premierze

Próby 2,4,8,16 prawdziwych klientów, także w jednym punkcie. Narzędzie lokalnej symulacji ma udokumentowany limit 8 klientów; 16 wymaga odpowiedniej sesji testowej, nie 16 NPC. Obowiązkowe urządzenia z DEVICE_ACCEPTANCE. Sprawdź wersje programu, prawa do assetów, publikację dla właściwych grup, komunikację, prywatność. **Odbiór:** rozdzielone wyniki techniczne, edukacyjne, wizualne i platformowe. Brak jednego wymagania to NO_GO dla pełnej premiery, nie powód do ukrywania wyniku.

## Czego nie wykonywać razem

Nie łączyć P02 (UI) z wymianą systemu zapisu; P05 z wdrożeniem pełnych wyścigów; nowej biblioteki materiałów z migracją istniejącej mapy. Jeden eksperyment ma jedną hipotezę. Dodatkowe prace zapisywać jako backlog, nie wykonywać poza zakresem. Każdy pakiet kończyć formatem raportu ze START HERE.
