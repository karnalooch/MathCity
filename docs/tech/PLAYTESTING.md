# MathCity — szybkie testowanie Roblox z Wojtkiem

**Status:** plan procesu pracy. Nie wdrożono Rojo ani nowego pipeline'u.

## Stan wyjściowy

- Obecny, działający plik mapy: **MathCity.rbxl** na gałęzi main. Nie nadpisywać go przypadkowym buildem.
- Aktualne skrypty w repo: katalogi src/server i src/client.
- Pliki .luau nie synchronizują się automatycznie z istniejącą mapą Roblox Studio.
- Stare instrukcje [ROBLOX_SETUP_GUIDE](../ROBLOX_SETUP_GUIDE.md) i [PORADNIK](../../PORADNIK_ROBLOX_STUDIO.md) nadal opisują prototyp.

## Docelowy cykl

1. Zmiana skryptu w repozytorium; Git weryfikuje diff.
2. W fazie wdrożenia konfigurujemy Rojo tak, by tylko wybrane części kodu synchronizowały się ze Studio. Nie nadpisujemy automatycznie świata ani Terrain.
3. Test **F5 (Play)** w Studio; po każdej zmianie głównych mechanik test **Server & Clients** (2 klientów).
4. Test importowanego modelu: prosty poziom testowy, kontrola materiałów, osi, proporcji, kolizji.
5. Test urządzenia mobilnego i rzeczywistej rozdzielczości.
6. Dopiero po PASS backup .rbxl i dokumentacja dowodowa (zrzuty, logi, FPS, SHA).

Oficjalne informacje: [Studio testing modes](https://create.roblox.com/docs/studio/testing-modes); [Rojo](https://github.com/rojo-rbx/rojo); [Rojo sync details](https://github.com/rojo-rbx/rojo.space/blob/master/docs/sync-details.md).

## Testy ryzykowne

- Nie przełączać istniejącej mapy na nowy schemat Rojo bez kopii i uzgodnionego source-of-truth.
- Dwuosobowe testy: gracz A/B, drzwi, checkpoint, pojazd, minigra, nagroda.
- Dane trwałe: osobna gra testowa i osobny namespace, aby nie uszkodzić postępów produkcyjnych.
- Bezpieczeństwo serwera: nagrody i poprawność odpowiedzi weryfikuje serwer.
- Rozłączenie gracza, częściowe ładowanie, jednoczesne wejścia na minigrę, telefony.
- Współpraca Team Create: sprawdzić aktualne wymagania wieku i uprawnień obu kont, zanim zaplanujemy wspólną sesję: [Roblox Collaboration](https://create.roblox.com/docs/projects/collaboration).

## Artefakty późniejszego testu

W przyszłym etapie każde potwierdzenie techniczne powinno mieć: numer zadania, commit, wariant grafiki, urządzenie, datę, logi, pomiary i screenshot. Teraz tylko ustalamy definicję dowodu.
