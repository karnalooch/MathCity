# Roblox Studio MCP — oficjalna integracja dla MathCity

**Data weryfikacji źródeł: 2026-10-20. Status: OFFICIAL_FEATURE_CONFIRMED / LOCAL_CONNECTION_NOT_YET_TESTED.**

Roblox Studio ma **wbudowany serwer Model Context Protocol (MCP)**. Po połączeniu z klientem AI może on bezpośrednio pracować z **otwartą sesją Studio**: eksplorować model danych, czytać i edytować skrypty, uruchamiać Luau, używać playtestu i korzystać z dokumentacji/skills udostępnianych przez Studio.

Źródła pierwszej strony:
- [Roblox Creator Hub — Connect to the Roblox Studio MCP server](https://create.roblox.com/docs/studio/mcp)
- [Roblox Creator Hub — AI on Roblox / accelerated workflows](https://create.roblox.com/docs/ai/accelerated-workflows)

To zmienia plan wykonawczy MathCity: Studio MCP jest preferowaną drogą do lokalnej inspekcji i testowania gry. Nie zastępuje GitHub, testów urządzeń ani kontroli zakresu.

## 1. Włączenie MCP w Studio

W aktualnym Roblox Studio:
1. Otwórz **Assistant**.
2. Wybierz menu **…**.
3. Otwórz **Manage MCP Servers**.
4. Włącz **Enable Studio as MCP server**.
5. Po połączeniu klienta sprawdź zielony wskaźnik liczby połączonych klientów.

Przed próbą używaj najnowszej wersji Studio. Jeśli przełącznik lub nazwy menu różnią się, sprawdź bieżącą dokumentację zamiast zgadywać.

## 2. Windows — oficjalne wejście

Roblox dokumentuje na Windows transport przez lokalny skrypt:

```text
cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat
```

Przykładowa konfiguracja klienta MCP:

```json
{
  "mcpServers": {
    "Roblox_Studio": {
      "command": "cmd.exe",
      "args": [
        "/c",
        "%LOCALAPPDATA%\\Roblox\\mcp.bat"
      ]
    }
  }
}
```

Kopia do użycia jako wzór znajduje się w [examples/roblox_studio_mcp.windows.json](examples/roblox_studio_mcp.windows.json).

**Nie commitować lokalnych plików konfiguracyjnych zawierających inne serwery, tokeny, ścieżki prywatne lub sekrety.** Do repo trafia wyłącznie neutralny wzór.

## 3. Quick Connect

Oficjalna dokumentacja wymienia szybkie połączenie m.in. dla:
- Codex CLI,
- Claude Code,
- Claude Desktop,
- Cursor,
- Gemini CLI,
- Visual Studio Code,
- Antigravity.

Jeżeli klient jest wykryty lokalnie, preferuj **Quick Connect** w Studio zamiast ręcznego przepisywania JSON. Brak klienta na liście nie oznacza, że MCP jest niedostępne; każdy klient wspierający transport **stdio** może zostać skonfigurowany zgodnie z dokumentacją.

## 4. Narzędzia i zachowanie sesji

Oficjalny przewodnik wymienia m.in.:
- `script_read` — czytanie skryptu z gry;
- `multi_edit` — wielokrotne edycje skryptów; może utworzyć nowy skrypt;
- `script_search` — wyszukiwanie skryptów;
- `http_get` — dostęp do dozwolonych stron dokumentacji Roblox;
- `skill` — referencje/best practices, np. debugowanie, symulacja urządzeń i wyszukiwanie dokumentacji;
- `list_roblox_studios` — lista podłączonych instancji Studio.

Lista może się rozszerzać. **Wykonawca ma odkryć faktycznie dostępne narzędzia w swojej wersji Studio, a nie korzystać z wymyślonego API.**

Każde wywołanie jest kierowane do konkretnego `studio_id`. Przy wielu otwartych oknach Studio najpierw użyj listy instancji, zapisz nazwę/place id i jawnie wybierz właściwą sesję.

## 5. Zasady MathCity

### 5.1. Testowa kopia, nie autorytatywna mapa

Dopóki właściciel nie uruchomi pakietu kodowego Pxx:
- MCP wolno użyć do **odczytu i demonstracji** wyłącznie po osobnym zleceniu;
- nie edytować `MathCity.rbxl`;
- nie publikować miejsca;
- nie zmieniać DataStore;
- nie uruchamiać masowych edycji;
- nie importować cudzych assetów.

Po uruchomieniu pakietu Pxx:
1. Utwórz osobną gałąź Git.
2. Otwórz **kopię testową** miejsca.
3. Zapisz `studio_id`, place id/nazwę, SHA repo i hash pliku bazowego.
4. Wprowadź tylko zmiany wynikające z pakietu.
5. Zrób playtest i zachowaj dowody.
6. Kod i dokumentację commituj do gałęzi; oryginalnego `.rbxl` nie zastępuj bez osobnego kroku akceptacji.

### 5.2. Jedno okno = jeden autor zmian

Nie uruchamiaj dwóch agentów edytujących tę samą instancję Studio jednocześnie. Drugi agent może przeglądać repo lub dokumentację, ale nie może równolegle zapisywać tych samych skryptów/sceny.

### 5.3. MCP nie zastępuje testów sprzętowych

Symulacja urządzenia w Studio pomaga z UI, ale:
- nie jest fizycznym iPadem 6;
- nie dowodzi stabilnych 30 FPS;
- nie zastępuje Motoroli G54 ani Redmi Note 14 4G;
- nie zastępuje testu 16 rzeczywistych klientów.

Statusy pozostają osobne: `MCP_CONNECTED`, `STUDIO_PASS`, `DEVICE_PASS`, `16_CLIENT_PASS`.

## 6. Pierwszy bezpieczny smoke test MCP

Po skonfigurowaniu połączenia, ale **bez edycji projektu**, wykonawca:
1. Otwiera Studio z kopią testową.
2. Wywołuje listę instancji i zapisuje właściwy `studio_id`.
3. Wyszukuje istniejący skrypt po nazwie.
4. Odczytuje 10–30 linii bez edycji.
5. Pobiera stronę dokumentacji Roblox przez narzędzie dokumentacyjne, jeśli jest dostępne.
6. Sprawdza dostępne `skill`/referencje.
7. Kończy bez zapisu do miejsca.

PASS: właściwe Studio wskazane jawnie, odczyt się zgadza, brak modyfikacji mapy i repo.

## 7. Pierwszy smoke test edycji — dopiero po P00

Po jawnej zgodzie właściciela na kodowy pakiet P00/P01:
1. W testowej kopii utwórz izolowany `ServerScriptService.MathCityMcpProbe`.
2. Wstaw minimalny skrypt w `--!strict`, który nie dotyka DataStore i tylko zapisuje stały komunikat do Output.
3. Uruchom test.
4. Odczytaj Output.
5. Usuń probe w tej samej testowej kopii.
6. Udokumentuj: `studio_id`, SHA, ścieżkę skryptu, wynik, czas, screenshot/log.
7. Nie publikuj.

Celem jest sprawdzenie kanału edycja → playtest → log, nie wdrożenie mechaniki gry.

## 8. Workflow docelowy dla słabszego LLM

```text
GitHub: wybierz jeden packet Pxx
        ↓
WEAK_LLM_START_HERE + kontrakt + karta minigry
        ↓
Studio MCP: list_roblox_studios → jawny studio_id
        ↓
READ-ONLY inspekcja
        ↓
mała zmiana Luau
        ↓
playtest + Output + ewentualny screenshot
        ↓
testy repo / diff
        ↓
raport PASS/FAIL/NOT_RUN per warstwa
```

**Zakaz:** `multi_edit` nie jest zgodą na szeroki refactor. Liczba narzędzi MCP nie zmienia zakresu pakietu.

## 9. Diagnostyka połączenia

Jeżeli MCP nie jest widoczne:
1. uruchom ponownie Studio i klienta;
2. sprawdź, czy Studio ma włączony serwer MCP;
3. potwierdź istnienie `%LOCALAPPDATA%\Roblox\mcp.bat`;
4. sprawdź poprawność JSON;
5. sprawdź, czy klient obsługuje stdio;
6. ponownie wylistuj instancje Studio.

Nie pobieraj losowego „Roblox MCP server” z internetu, jeżeli wbudowany serwer Studio jest dostępny.

## 10. Co trafia do dowodów

Dla każdej operacji przez MCP raportuj:
- klient AI i wersję, jeśli znana;
- Studio version / data testu;
- `studio_id`, nazwę miejsca i place id, jeśli istnieje;
- bazowy i końcowy SHA repo;
- zmienione skrypty/instancje;
- typ dowodu: odczyt / edit / playtest / device emulation;
- wynik oraz jawne `NOT_RUN`;
- czy test był na kopii lokalnej, opublikowanym test place czy produkcji.

Nigdy nie raportuj `DEVICE_PASS` tylko dlatego, że Studio MCP działa.
