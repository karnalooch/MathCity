# 🛠️ Poradnik: Jak złożyć Waszą grę w Roblox Studio krok po kroku!

**Gotowy projekt:** otwórzcie `Roblox.rbxl` i naciśnijcie Play. Mapa zawiera 3 etapy, 9 drzwi, 4 checkpointy, 6 kryształów i panel administratora. Poniższe kroki ręczne są potrzebne tylko przy przenoszeniu gry do innej mapy.

W nieopublikowanym projekcie Studio działa lokalny tryb testowy: statystyki resetują się po zatrzymaniu Play. W opublikowanej grze używany jest DataStore; awaria odczytu nie przełącza gry na dane tymczasowe. ID Gamepassa nadal wymaga uzupełnienia.

Witajcie! Przygotowaliśmy kompletny zestaw skryptów. Poniżej znajduje się prosta instrukcja dla Was dwojga, jak w kilka minut uruchomić działającą grę w **Roblox Studio**.

---

## 🏁 KROK 1: Przygotowanie nowego miejsca (Baseplate)
1. Otwórzcie **Roblox Studio**.
2. Kliknijcie **New** (Nowa gra) ➡️ Wybierzcie szablon **Baseplate** (Pusta plansza).

---

## 📊 KROK 2: Wklejenie statystyk i zapisu gry (Leaderstats)
1. W oknie **Explorer** (po prawej stronie) znajdźcie folder **`ServerScriptService`**.
2. Kliknijcie na niego prawym przyciskiem myszy ➡️ **Insert Object** ➡️ **Script**.
3. Zmieńcie nazwę skryptu na: `LeaderstatsAndDataStore`.
4. Otwórzcie go podwójnym kliknięciem, skasujcie `print("Hello world!")` i wklejcie zawartość z pliku:
   👉 [`src/server/LeaderstatsAndDataStore.luau`](file:///d:/gem/Matma%20roblox/src/server/LeaderstatsAndDataStore.luau)

---

## 🚪 KROK 3: Zbudowanie pierwszego piętra Wieży z Drzwiami
1. Stwórzcie 4 klocki (Part) za pomocą przycisku **Part** na górnym pasku:
   * **Klocek 1 (Tablica)**: Nazwijcie go **`Sign`** (powieście go wyżej nad drzwiami).
   * **Klocek 2 (Pierwsze drzwi)**: Nazwijcie go **`Door1`**.
   * **Klocek 3 (Drugie drzwi)**: Nazwijcie go **`Door2`**.
   * **Klocek 4 (Trzecie drzwi)**: Nazwijcie go **`Door3`**.
2. Zaznaczcie wszystkie 4 klocki, upewnijcie się, że mają włączoną opcję **Anchored** (Zakotwiczone – żeby nie spadały).
3. Kliknijcie na nie prawym przyciskiem myszy ➡️ **Group as Model** (Zgrupuj jako model) i nazwijcie model: **`Floor1`**.
4. Kliknijcie na model `Floor1` prawym przyciskiem ➡️ **Insert Object** ➡️ **Script** i nazwijcie go: `MathDoorScript`.
5. Wklejcie do niego zawartość z pliku:
   👉 [`src/server/MathDoorScript.luau`](file:///d:/gem/Matma%20roblox/src/server/MathDoorScript.luau)

> 💡 **Jak to działa?**
> W skrypcie na samej górze możecie zmieniać pytania i wyniki:
> ```lua
> local QUESTION = "7 x 8 = ?"
> local OPTION_1 = "48"
> local OPTION_2 = "56" -- Dobre drzwi!
> local OPTION_3 = "64"
> local CORRECT_DOOR_INDEX = 2 -- Numer 2 wygrywa!
> ```

---

## 📍 KROK 4: Checkpointy (Respawny po śmierci)
1. W **Workspace** kliknijcie prawym przyciskiem ➡️ **Insert Object** ➡️ **Folder**.
2. Zmieńcie nazwę folderu na dokładnie: **`Checkpoints`**.
3. Wstawcie do tego folderu klocek (Part) i nazwijcie go **`1`** (będzie to respawn przed drzwiami piętra 1).
4. Dla kolejnego piętra dodacie tam klocek o nazwie **`2`** za drzwiami. Upewnijcie się, że klocki mają włączone **Anchored**!

---

## 👑 KROK 5: Admin Panel (Latanie, Noclip, Monety)
1. **Część serwerowa**:
   * W **`ServerScriptService`** dodajcie nowy **Script** i nazwijcie go: `AdminServer`.
   * Wklejcie do niego kod z:
     👉 [`src/server/AdminServer.luau`](file:///d:/gem/Matma%20roblox/src/server/AdminServer.luau)
2. **Część wizualna (Panel gracza)**:
   * W oknie Explorer znajdźcie **`StarterPlayer`** ➡️ **`StarterPlayerScripts`**.
   * Kliknijcie prawym przyciskiem ➡️ **Insert Object** ➡️ **LocalScript**.
   * Nazwijcie go: `AdminPanelGui`.
   * Wklejcie do niego kod z:
     👉 [`src/client/AdminPanelGui.luau`](file:///d:/gem/Matma%20roblox/src/client/AdminPanelGui.luau)

---

## 💎 KROK 6: Zbieranie kryształów na mapie
1. Stwórzcie w Workspace mały klocek, np. kulkę lub diament.
2. Zmieńcie mu kolor na błękitny.
3. Wstawcie do niego **Script** i wklejcie kod z:
   👉 [`src/server/CollectibleCoin.luau`](file:///d:/gem/Matma%20roblox/src/server/CollectibleCoin.luau)
4. Teraz możecie powielać ten klocek (`Ctrl + D`) i rozstawiać po całym mieście!

---

## 🎮 KROK 7: Testowanie gry!
1. Naciśnijcie klawisz **F5** lub kliknijcie zielony przycisk **Play** w Roblox Studio.
2. Zobaczcie:
   * W prawym górnym rogu macie: **Stage (1)**, **Coins (0)**, **Gems (0)**.
   * Uprawniony gracz po wczytaniu danych widzi żółty przycisk **👑 ADMIN**. W nieopublikowanym miejscu w Studio dostęp mają wszyscy testerzy; w opublikowanej grze właściciel, wskazane konta i posiadacze Gamepassa.
   * Podejdźcie do złych drzwi – postać natychmiast zginie i odrodzi się na checkpoincie `1`!
   * Przejdźcie przez dobre drzwi (`56`) – dostaniecie **50 monet**, a Wasze piętro zmieni się na **Stage 2**!

## Konfiguracja przed uruchomieniem

* Aby sprawdzić trwały zapis, opublikujcie oddzielną grę testową i włączcie **Enable Studio Access to API Services** w jej ustawieniach bezpieczeństwa. Studio może zapisywać rzeczywiste dane. Nie jest to potrzebne do lokalnego testu nieopublikowanej mapy.
* W `AdminServer` wpiszcie własny `ADMIN_GAMEPASS_ID`. Wartość `0` wyłącza dostęp przez Gamepass; cena 500 Robux jest ustawiana w Creator Dashboard, nie w skrypcie. Panel nie zawiera przycisku zakupu.
* Dla gry należącej do grupy wpiszcie identyfikatory uprawnionych użytkowników w `ADMIN_USER_IDS`, np. `{[12345678] = true}`. ID grupy nie jest ID administratora.
* Wszystkie pięć skryptów należy zaktualizować razem. Drzwi, kryształy i panel czekają na serwerowy atrybut `DataLoaded`.
* Zapis odbywa się co 60 sekund, przy wyjściu i zamknięciu serwera. Błąd odczytu lub aktywna sesja na innym serwerze powoduje odmowę wejścia, zamiast nadpisania postępów. Po awarii serwera blokada sesji może pozostać aktywna do 180 sekund. Nie uruchamiajcie równocześnie starej i nowej wersji skryptu zapisu.
* Po odrodzeniu tryby administratora są wyłączane. Fly obsługuje WASD, spację i Shift; na telefonie używa joysticka oraz przycisków ↑/↓, a na padzie kierunku ruchu i A/B.
* Kontrola dostępu zabezpiecza funkcje dostarczonego panelu. Nie jest pełnym systemem wykrywania zmodyfikowanych klientów ani teleportowania postaci.

## Sprawdzenie poprawek

Testy logiki z symulowanymi usługami Roblox: `python tests/run.py ŚCIEŻKA_DO_LUAU.EXE` (interpreter z oficjalnego projektu luau-lang/luau).

W Roblox Studio sprawdźcie również:

1. Zapis postępu, ponowne wejście i pierwsze pojawienie się na zapisanym checkpoincie.
2. Dwóch graczy z różnymi uprawnieniami: zwykły gracz nie widzi panelu, administrator może używać funkcji.
3. Fly i Noclip włączone przed śmiercią, ich wyłączenie po odrodzeniu i przywracanie kolizji po Noclip OFF.
4. Powrót pierwotnego koloru drzwi po trzech sekundach od ostatniego dotknięcia.
5. Sterowanie na telefonie/padzie oraz zapis podczas zamykania serwera. Testy lokalne nie odtwarzają fizyki, replikacji ani usług Roblox.
