# Osiem kart pilotowych: indeks i sposób użycia

2026-10-19. Wybór pilotów jest **rekomendacją planu**, nie stwierdzeniem wykonania albo osobnym zatwierdzeniem całej zawartości przez właściciela. Klasy i warianty mają TEACHER_REVIEW_PENDING. Każdą kartę czytaj z [modelem zadania](TASK_MODEL_AND_ADAPTATION.md), [UI](../../ux/LEARNING_UI_CONTRACT.md) i [regułami nagród](../../gameplay/specs/PROGRESSION_AND_REWARDS.md).

| Karta | Główna umiejętność | Co sprawdza technicznie |
|---|---|---|
| [M01 Zegar Jacka](cards/M01_CLOCK.md) | CLOCK | czas jako dane, dwie wskazówki, brak presji |
| [M02 Pałac Lustrzanych Okien](cards/M02_SYMMETRY.md) | SYMMETRY | walidacja pozycji zamiast samej liczebności |
| [M05 Osiem Stacji Sekuły](cards/M05_STATIONS.md) | COUNT/ADD_SUB | unikalne odkrycia, nie licznik dotknięć |
| [M13 Stadion: układ krzesełek](cards/M13_ROWS.md) | MULTIPLY_GROUPS/OPEN_CONSTRAINT | kilka poprawnych rozwiązań |
| [M21 Poczta i kurier](cards/M21_POST.md) | ORDER | sortowanie obiektów i role |
| [M33 Plażowy Sklep](cards/M33_SHOP.md) | MONEY | wirtualny budżet odrębny od portfela gry |
| [M34 Pomost Równych Desek](cards/M34_PIER.md) | EQUAL_SHARING | generator, drag/tap, guided, co-op |
| [M35 Rowerowa Pętla](cards/M35_ROUTE.md) | LENGTH/ADD_SUB | mapa danych vs geometria, teleport a trasa |

Pierwszy test implementacji: M34 bez pełnego świata. Pierwszy onboarding może używać prostej interakcji z odkrywaniem i ikonami w centrum, bez teleportowania nowego gracza na Sekułę; nie przemianowuj w tym celu M05 ani nie udawaj, że las leży przy ratuszu. Ośmiu pilotów nie implementuje się w jednym PR.

## Wspólne wymagania każdej karty

Podstawowa nagroda przychodzi po rzeczywistym ukończeniu roli i jednokrotnym zapisie niezależnie od pomocy. Zadania można zostawić i wznowić. Wspólny efekt artystyczny nie narusza cudzej prywatnej wersji zadania. Prywatne warianty matematyczne nie rywalizują o te same fizyczne przedmioty. Typowe błędy w karcie to kontrprzykłady walidatora, nie tekst do zawstydzania dziecka.

Tryb 1–4: ta sama mechanika instancjonuje oddzielne małe porcje pracy, np. sekcje pomostu albo stoliki z paczkami. Każdy ukończony zestaw ma sensowny efekt; nie dziel głównego EXP przez liczbę graczy. Dodatkowe role nie muszą być czterema osobnymi rodzajami minigier. Przy 1 osobie realizuje się minimalny pełny zestaw; przy 2–4 analogiczne porcje są równoległe. Dokładny koszt pracy podlega testowi, by solo nie wymagało czterokrotnie dłuższej sesji.

## Kolejność review

Parametry → rozwiązanie → negatywne przykłady → UI → pomoc → warianty → prywatność → współpraca → nagrody. Dopiero potem finalny wygląd. Nie zastępować walidatora animacją domyślnie pokazującą sukces. Wszystkie przykłady oraz skończone domeny mają kontrolę w [TEST_VECTORS](TEST_VECTORS.md).
