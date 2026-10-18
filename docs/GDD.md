# MathCity — Game Design Document v2 (research / concept)

**Data:** 2026-10-18. **Status:** koncepcja, nie specyfikacja wdrożona.

Historyczny opis istniejącej Wieży Matematycznej: [legacy/GDD_TOWER_V1.md](legacy/GDD_TOWER_V1.md). Nie usuwamy jej ani nie zmieniamy pliku MathCity.rbxl na etapie researchu.

## 1. Wysoka koncepcja

**MathCity: Siedlce Unlimited** (tytuł roboczy): kolorowe, wielkie, otwarte miasto zbudowane na rozpoznawalnych atrakcjach Siedlec. Swoboda przemieszczania się i zabawy jak w miejskich grach społecznościowych, projekt poziomów i czytelność 3D jak w przygodowej platformówce. Matematyka klas 2–4 jest naturalną częścią zadań, usług miejskich, eksploracji i kooperacji.

**USTALONE:** świat osadzony w Siedlcach, ale nie 1:1; mocna promocja miasta; eksponowanie ważnych miejsc; matematyka zgodna z polską podstawą programową dla klas 2–4; research popularnych mechanik Roblox bez kopiowania; użycie UE, Blendera i Material Forge z zaplecza YACS do przygotowania treści; wygodne sprawdzanie w Roblox Studio; estetyczne inspiracje: klimat Vice City i energia Super Mario Odyssey.

**NIEUSTALONE:** liczba dzielnic, docelowe wymiary mapy, ekonomia, model monetyzacji, pełna fabuła, kamienie milowe, wersja pierwszej publicznej gry.

## 2. Gracz, platforma, sesja

- Odbiorca projektowy: dzieci uczące się w klasach 2–4, z uwzględnieniem wymagań wiekowych platformy i potrzeb opiekunów.
- Roblox PC i urządzenia mobilne jako priorytety testów; inne platformy do decyzji po testach.
- Proponowana sesja: 5–15 minut, z możliwością dłuższej eksploracji.
- Dwa tryby zaangażowania: swobodna zabawa w mieście oraz wyprawy i minigry matematyczne.
- Brak kar za błędne odpowiedzi; wskazówki i próby ponowne. Mechanika śmierci za złe drzwi z prototypu wymaga przebudowy przed użyciem w nowym trybie edukacyjnym.

## 3. Core loop (PROPOZYCJA)

**Odkrywaj → Weź udział w aktywności → Rozwiąż problem → Zdobądź nagrodę i wiedzę → Personalizuj / odblokuj → Odkrywaj dalej.**

Exploracja i roleplay muszą działać także pomiędzy zadaniami. Nie wolno wymuszać nieustannych quizów.

## 4. Świat

Proponowane dzielnice:
1. **Jackowo – Serce Miasta** (ratusz, plac startowy i sklepy).
2. **Ogrody Aleksandrii** (park, pałac, geometria i labirynty).
3. **Kolejowo – Stacja Czasu** (dworzec, rozkłady i podróże).
4. **Muchawkowe Wyspy** (**Zalew Muchawka jako flagowa atrakcja**: kąpielisko, plaża, pomost, promenady rowerowe, realna grobla i odrębny chroniony teren Doliny; fantastyczne wyspy oraz matematykę ułamków, czasu, odległości, rowerów i sportu). [Pełna karta N01](world/atlas/MUCHAWKA_FEATURE.md).
5. **Neonowe Błonia** (sport, obwody, pola, pomiary).
6. **Aleja Kultury** (muzyka, sekwencje, sztuka, muzea).
7. **Sekuła: Leśna Ekspedycja** (Las Sekulski, trasy narciarstwa biegowego N05, ścieżka N06, hipoteza Górka Grześ N07). *Nowa propozycja z Etapu A, nie zatwierdzona; miejsca pamięci bez aktywności sportowych.*

Dzielnice i ich nazwy są fikcyjne. Budynki mają być rozpoznawalne, ale drogi, odległości i funkcje są podporządkowane grywalności. Szczegóły: [atlas](world/SIEDLCE_LANDMARK_ATLAS.md), [masterplan](world/DISTRICTS_MASTERPLAN.md).

**Aktualizacja 2026-10-19:** Zalew Muchawka jest osobnym pełnym hubem rekreacji i matematyki, z 6 podstrefami fantasy `MW-01…MW-06`, 12 pomysłami minigier `M24–M27` i `M33–M40` oraz 10 fotoreferencjami do pozyskania. Nie mylić z krytym Parkiem Wodnym Siedlce `S02`; [specyfikacja](world/atlas/MUCHAWKA_FEATURE.md) i [edukacja](education/CURRICULUM_2_4.md). Zalew musi pełnić funkcję głównej atrakcji i znaczącego obszaru rozgrywki, nie tylko dekoracji. Jest to wymóg koncepcyjny, a nie istniejąca scena.

**Aktualizacja Etapu A:** pełne źródła 41 miejsc, 41 kart, w tym stadion/basen/Sekuła/Grześ, i 40 przykładów minigier: [world/STAGE_A_README.md](world/STAGE_A_README.md). To materiały badawcze, **nie nowa wersja gry**.

## 5. Mechaniki do walidacji

- Ułatwiające eksplorację: pieszo, hulajnogi/rowery, pojazdy, publiczny transport fikcyjny.
- Społeczne: bezpieczne wspólne wyzwania, wycieczki, spotkania i roleplay.
- Odkrywanie: ukryte kolekcje, punkty widokowe, paszport odkrywcy.
- Przygodowe: obby, parkour, interaktywne obiekty, logiczne łamigłówki.
- Długoterminowe: kosmetyka postaci i pojazdów, nieszkodliwe towarzyszące stworki.
- Minigry: co najmniej 8 kandydatów opisanych w [CORE_LOOP_AND_MINIGAMES.md](gameplay/CORE_LOOP_AND_MINIGAMES.md).

Bez kopiowania rozpoznawalnych elementów cudzych gier i bez pay-to-win w edukacji.

## 6. Edukacja

Treści matematyczne mają etykiety: obszar umiejętności, przewidywana klasa, wersja podstawy, trudność, rodzaj pomocy. Z uwagi na reformę MEN 2026 zakres trzeba wersjonować i konsultować z nauczycielem. Patrz [education/CURRICULUM_2_4.md](education/CURRICULUM_2_4.md).

Zadania preferują manipulowanie obiektami 3D, pomiary, zakupy, planowanie i współpracę. Pisemny quiz jest opcją, nie jedyną formą nauki. Poprawność wyniku i sugestie potwierdza serwer.

## 7. Art direction

Pastelowe kamienice, turkus, brzoskwinia, różowe zachody słońca, czytelne bryły i miękka stylizacja. Siedlce muszą pozostać czytelne; nie tworzymy kopii Miami ani gry Nintendo. Zob. [art/ART_BIBLE.md](art/ART_BIBLE.md).

## 8. Zasada budowania wielkiego świata

Roblox jest **platformą wykonawczą**. UE służy do wizualizacji i planowania, Blender do modelowania oraz optymalizacji, Material Forge do przygotowania kolorów/PBR. Świat importujemy modułowo, testujemy streaming, LOD, pamięć i wydajność mobilną. Zob. [tech/LARGE_WORLD.md](tech/LARGE_WORLD.md).

Nie wybieramy maksymalnego rozmiaru mapy na podstawie samej liczby studów. Kandydaci 8192 i 16384 studów na bok to **hipotezy do benchmarku**, nie obietnice.

## 9. Ochrona dzieci i publikacja

Przyjazna informacja zwrotna, dostępność UI, możliwość wyłączenia nadmiarowych efektów, ochrona danych, weryfikacja wieku i zasad współpracy/publikacji Roblox. Historia płatnego panelu administratora z v1 **nie oznacza, że tę monetyzację akceptujemy dla nowej gry**. Zob. [legal/RIGHTS_AND_COMPLIANCE.md](legal/RIGHTS_AND_COMPLIANCE.md).

## 10. Definition of success na etap badań

- Jest atlas najważniejszych miejsc i plan rozmieszczenia siedmiu **proponowanych** stref (wcześniej 6; teraz osobna Sekuła).
- Są warianty stylu: dzień, zmierzch, noc; zatwierdzony styl czytelny dla dzieci.
- Jest macierz mechanik z testów ręcznych minimum 12–15 gier Roblox.
- Jest mapa treści klas 2–4 zweryfikowana dydaktycznie.
- Jest lokalny test jednego assetu: Material Forge / Blender → Roblox, z pomiarami.
- Jest benchmark skali dużego świata.
- **Zero zmian gameplayu i mapy**, dopóki etap researchu nie przejdzie bramek w [planning/RESEARCH_ROADMAP.md](planning/RESEARCH_ROADMAP.md).
