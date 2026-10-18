# 🚀 Przewodnik Konfiguracji Roblox Studio & Gamepass 500 Robux

Ten poradnik wyjaśnia, jak poprawnie skonfigurować grę, włączyć zapis danych w chmurze oraz stworzyć i podłączyć **Gamepass za 500 Robux**!

---

## 1. Włączenie zapisu DataStore w Roblox Studio

Domyślnie Roblox Studio blokuje zapis danych w chmurze podczas testów na komputerze. Aby DataStore działał:

1. Otwórzcie Waszą grę w **Roblox Studio**.
2. W górnym menu kliknijcie **Home** ➡️ **Game Settings** (Ustawienia gry).
   *(Jeśli gra nie była jeszcze zapisana w chmurze, kliknijcie "Save to Roblox" i nadajcie jej nazwę, np. `Math City`)*.
3. W oknie ustawień przejdźcie do zakładki **Security** (Bezpieczeństwo).
4. Włączcie opcję:
   * ✅ **Enable Studio Access to API Services** (Zezwalaj Studio na dostęp do usług API).
5. Kliknijcie **Save** na dole okna. Od tej pory monety, kryształy i piętra będą zapisywać się na stałe!

---

## 2. Tworzenie Gamepassa Admin Panel za 500 Robux

1. Otwórzcie przeglądarkę internetową i wejdźcie na stronę:
   👉 **[create.roblox.com/dashboard/creations](https://create.roblox.com/dashboard/creations)**
2. Zalogujcie się na swoje konto Roblox.
3. Kliknijcie na Waszą grę (*Math City*).
4. W menu po lewej stronie wybierzcie: **Associated Items** (Powiązane przedmioty) ➡️ zakładka **Passes** (Przepustki).
5. Kliknijcie przycisk **Create a Pass** (Stwórz przepustkę).
6. Ustawienia przepustki:
   * **Image:** Wgrajcie grafikę (np. ikonę korony lub plik z folderu `assets`).
   * **Name:** `👑 Admin Panel`
   * **Description:** `Daje dostęp do Latania (Fly), Przenikania przez ściany (Noclip), Super Szybkości i Nieśmiertelności!`
7. Kliknijcie **Create Pass**.
8. Po utworzeniu kliknijcie na nowo powstałą przepustkę, a w menu po lewej wybierzcie **Sales** (Sprzedaż):
   * Zaznaczcie: ✅ **Item for Sale** (Przedmiot na sprzedaż).
   * **Price in Robux:** Wpiszcie `500`.
   * Kliknijcie **Save Changes**.

### 🔗 Jak podłączyć ID Gamepassa do skryptu:
1. W adresie przeglądarki podczas edycji Gamepassa skopiujcie ciąg cyfr, np.:
   `https://create.roblox.com/dashboard/creations/experiences/.../passes/`**`123456789`**`/details`
2. W Roblox Studio otwórzcie skrypt: [`src/server/AdminServer.luau`](file:///d:/gem/Matma%20roblox/src/server/AdminServer.luau)
3. Zmieńcie linijkę 12:
   ```lua
   local ADMIN_GAMEPASS_ID = 123456789 -- Wpiszcie Wasze skopiowane ID
   ```

---

## 3. Testowanie Gry w Roblox Studio

* **Test pojedynczy:** Wciśnijcie klawisz **F5** lub kliknijcie zielony przycisk **Play**.
* **Test z wieloma graczami:**
  1. Wejdźcie w zakładkę **Test** na górnym pasku.
  2. W sekcji *Clients and Servers* wybierzcie `2 Players`.
  3. Kliknijcie **Start** – otworzą się dwa okna, w których możecie sprawdzić, jak dwaj gracze widzą siebie nawzajem w wieży i na mieście!
