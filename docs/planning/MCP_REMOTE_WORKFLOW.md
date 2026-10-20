# MathCity — zdalny workflow GitHub + Roblox Studio MCP

**Status 2026-10-20: PLAN_READY / OFFICIAL_MCP_CONFIRMED / LOCAL_MCP_NOT_CONNECTED_BY_THIS_COMMIT.**

Ten dokument odpowiada na pytanie: jak słabszy wykonawca ma korzystać z repozytorium na remote oraz lokalnego Roblox Studio MCP, bez rozwalenia sprawdzonej mapy.

## 1. Dwa osobne światy

**Remote GitHub jest źródłem specyfikacji i kodu.**  
**Studio MCP jest narzędziem inspekcji/edycji/testu otwartego miejsca.**

Agent nie może traktować zmian wykonanych tylko w Studio jako zakończonej pracy repo. Analogicznie commit kodu bez testu w Studio nie daje `STUDIO_PASS`.

## 2. Tryby pracy

### MODE-DOC
Dozwolone: `docs/**`, web research, GitHub.  
MCP Studio: niewymagane.  
Zakazane: zmiany mapy, kodu, publikacji.

### MODE-READ-STUDIO
Dozwolone: odczyt sceny/skryptów, dokumentacja, lista instancji.  
Warunek: właściciel zezwolił na lokalny odczyt, właściwe Studio wybrane jawnie.  
Zakazane: zapisy i publikacja.

### MODE-TEST-STUDIO
Dozwolone: mała zmiana w **kopii testowej** wynikająca z konkretnego Pxx, playtest, logi.  
Warunek: jawnie uruchomiony pakiet kodowy, osobna gałąź, zapisane SHA i studio_id.

### MODE-DEVICE
Dodatkowo fizyczne urządzenie zgodnie z `DEVICE_ACCEPTANCE.md`. MCP może przygotować scenę/test, ale samo nie daje `DEVICE_PASS`.

### MODE-PUBLISH
Domyślnie **DISABLED**. Publikacja wymaga osobnej decyzji właściciela oraz bramek prawnych, prywatności i Roblox Kids/Select.

## 3. Preflight

Wykonawca musi zapisać:
- packet id;
- bieżący branch i HEAD;
- `git status`;
- dozwolone ścieżki;
- hash `MathCity.rbxl`;
- czy Studio jest kopią testową;
- listę podłączonych Studio i wybrany `studio_id`;
- stan Edit/Play;
- czy DataStore/API services są wyłączone lub skierowane do testowego namespace.

Jeżeli któregokolwiek krytycznego punktu nie da się ustalić, STOP i `BLOCKED_PREFLIGHT`.

## 4. Zasada małego diffu

Jedno zlecenie = jedna funkcja lub jeden błąd. Preferowana granica:
- 1 moduł domenowy,
- 1 adapter/UI,
- testy,
- aktualizacja właściwej karty docs.

Przykład P01/M34: walidator równych grup bez systemu EXP, bez pokoju, bez wyścigów.

## 5. Procedura edycji przez MCP

1. Odczytaj skrypt przed zmianą.
2. Zapisz ścieżkę i zakres linii.
3. Zastosuj minimalną edycję.
4. Odczytaj zmieniony fragment.
5. Uruchom najwęższy test.
6. Sprawdź Output/error.
7. Wykonaj pełny przypadek akceptacyjny pakietu.
8. Przenieś/utrwal zmianę w repo w autorytatywnym pliku.
9. Sprawdź diff.
10. Raportuj warstwy testów osobno.

Nie wykonuj wielkiego `multi_edit` tylko dlatego, że narzędzie to umożliwia.

## 6. Synchronizacja z Git

Przed edycją Studio:
- aktualny branch ma odpowiadać bazie zadania;
- lokalne zmiany innych osób nie mogą być resetowane;
- równoległy autor nie może pisać w tej samej sesji Studio.

Po edycji:
- kod musi mieć odzwierciedlenie w repo;
- jeżeli Studio przechowuje zmianę w binarnym miejscu, przygotuj jawny eksport/build i opisz, co jest source-of-truth;
- nie commituj sekretów ani lokalnych konfiguracji MCP;
- przed push ponownie sprawdź remote HEAD i konflikt.

## 7. Dowody

Minimalny raport:
```text
packet_id:
base_sha:
final_sha:
studio_id:
place_name/place_id:
mode:
changed_paths:
studio_objects_changed:
tests:
  unit:
  studio:
  device:
  multiplayer:
not_run:
limitations:
next_allowed_packet:
```

Screenshot bez logu nie daje `UNIT_PASS`; log bez fizycznego urządzenia nie daje `DEVICE_PASS`.

## 8. Rozpoczęcie pierwszej sesji

Najpierw **MCP00_READONLY_SMOKE**:
- połączenie,
- lista Studio,
- odczyt jednego istniejącego skryptu,
- odczyt dokumentacji/skill,
- zero zmian.

Potem, dopiero po zgodzie na P00: **MCP01_EDIT_SMOKE** opisany w `ROBLOX_STUDIO_MCP.md`.

Następnie pierwszym realnym pilotem pozostaje **M34 Pomost Równych Desek**, zgodnie z dokumentacją Etapu D.
