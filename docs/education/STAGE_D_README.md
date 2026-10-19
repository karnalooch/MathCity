# Etap D: edukacja klas 2–4 i kontrakty wykonawcze

2026-10-19. **DESIGN_SPEC_READY / SOURCE_ANCHORS_IDENTIFIED / TEACHER_REVIEW_PENDING / IMPLEMENTATION_NOT_STARTED.** Jest to audyt projektu i plan wykonania, nie oświadczenie pełnej zgodności gry z całym programem szkolnym.

## Dostarczone i niedostarczone

Dostarczono wiążący zapis [33 decyzji](../planning/OWNER_DECISIONS_20261019.md), wstępne przypisanie źródłowe i audyt M01–M40, osiem szczegółowych kart, model generatorów i adaptacji, silne UI, przypadki testowe oraz kolejność małych pakietów. Nie wykonano recenzji nauczyciela, sesji z dziećmi, testu Luau, testu w Studio ani na wskazanych urządzeniach. Żadna z tych pozycji nie ma domyślnego PASS.

## Nawigacja

| Dokument | Funkcja |
|---|---|
| [CURRICULUM_SOURCES](stage_d/CURRICULUM_SOURCES.md) | Właściwe roczniki, identyfikatory dokumentów, konkretne punkty, granice przypisania do klasy |
| [M01_M40_AUDIT](stage_d/M01_M40_AUDIT.md) | 40 decyzji o zakresie i poprawkach; nie 40 gotowych implementacji |
| [TASK_MODEL_AND_ADAPTATION](stage_d/TASK_MODEL_AND_ADAPTATION.md) | Dane zadania, walidatory, niezależna adaptacja, rozróżnienie podpowiedzi |
| [PILOT_INDEX](stage_d/PILOT_INDEX.md) | Osiem kart M01/M02/M05/M13/M21/M33/M34/M35 |
| [TEST_VECTORS](stage_d/TEST_VECTORS.md) | Dane i spodziewane wyniki do ręcznej i późniejszej programowej kontroli |
| [Kontrakt UI](../ux/LEARNING_UI_CONTRACT.md) | Instrukcja, silne podpowiedzi, stany ekranu i dotyk |
| [Pakiety D00–D06](../planning/EXECUTION_PACKETS.md) | Jak wykonać i odebrać następne kroki |

## Definicja minimum edukacyjnego

Dziecko może odkrywać wszystkie dzielnice. Wybór klasy nie określa jego tożsamości ani wieku do celów platformy. Każda umiejętność ma własny poziom gotowości; EXP przygody, sport, zakupy i pomoc innym nie zaliczają matematyki. Praca z UI i pomoc matematyczna są różnymi zdarzeniami. Matematyka nie ma odliczania. Zadanie wykonane z pomocą kończy przygodę i daje podstawową nagrodę; nie dowodzi samodzielności.

Szablon ma mieć skończony, kontrolowany zakres danych, zaplanowaną informację zwrotną i przynajmniej jedno rozwiązanie. Słabszy LLM nie generuje treści w trakcie gry. Klasa 4 nie oznacza automatycznie wszystkich treści z etapu IV–VI. Pierwsze zadania w karcie są celowo małe i konkretne; trudniejsze warianty wymagają przeglądu.

## Bramka D: kiedy wolno napisać PASS

- 40 ID ma przypisane umiejętności, disposition, przykład, wynik i status właściwej wersji programu.
- Każdy z ośmiu pilotów ma źródłowy punkt, granice wariantów, walidator, dwa rodzaje pomocy i przypadki błędne.
- Nauczyciel zatwierdził konkretne wersje oraz rozkład poziomów; imię i dane kontaktowe recenzenta nie muszą być publiczne.
- Kontrola danych potwierdziła poprawność przykładów i kompletność rozwiązań otwartych.
- Plan pomocy nie odbiera nagród; nie ma obowiązkowej szybkości liczenia, publicznej oceny i płatnej przewagi.
- Właściciel otrzymał raport zakresu, a nie slogan o pełnym pokryciu podstawy.

Nauczyciel podpisuje wersję karty, umiejętność i zakres; zmiana zakresu albo walidatora unieważnia tę część recenzji. Samo poprawienie literówki nie wymaga ponownej oceny całej gry. Pełny edukacyjny pilotaż i runtime testy są odrębnymi bramkami przed premierą.

## Otwarte braki programowe

Obecne M01–M40 nie pokrywają wszystkich tematów szkoły. Brakuje m.in. pełnego planu dla masy/pojemności, kalendarza, zapisu pozycyjnego, wybranych reprezentacji liczb i szerszej geometrii. To backlog umiejętności, nie zgoda na dodanie M41+. Nie podawać procentu pokrycia bez zdefiniowanego mianownika wymagań i review. Ścieżka adaptacyjna nie przenosi automatycznie dziecka poza wybrany zakres.
