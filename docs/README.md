# 📚 Dokumentacja Projektu: Math City

Witaj w oficjalnej dokumentacji gry **Math City** tworzonej w Roblox Studio!
Gra łączy wspinaczkę po **Wieży Matematycznej** (zadaniach z tabliczki mnożenia i kolejności działań dla 3. klasy) z **Otwartym Światem (Miastem)**, w którym za zarobione pieniądze kupuje się domy, samochody i jedzenie.

---

## 🗂️ Spis Treści Dokumentacji

| Dokument | Opis |
| :--- | :--- |
| 📖 [**GDD.md**](file:///d:/gem/Matma%20roblox/docs/GDD.md) | **Game Design Document** – pełny opis mechaniki gry, pętli rozgrywki, celów gracza i monetyzacji. |
| 🏗️ [**ARCHITECTURE.md**](file:///d:/gem/Matma%20roblox/docs/ARCHITECTURE.md) | **Architektura Techniczna** – schemat klient-serwer, zapis `DataStore`, obsługa respawnów i komunikacja `RemoteEvents`. |
| 📐 [**MATH_CURRICULUM.md**](file:///d:/gem/Matma%20roblox/docs/MATH_CURRICULUM.md) | **Baza Pytań dla 3. Klasy** – gotowe zestawy zadań z mnożenia i kolejności działań na kolejne 20 pięter wieży. |
| 🚀 [**ROBLOX_SETUP_GUIDE.md**](file:///d:/gem/Matma%20roblox/docs/ROBLOX_SETUP_GUIDE.md) | **Instrukcja Konfiguracji** – jak dodać Gamepass za 500 Robux na create.roblox.com, jak opublikować grę i testować. |
| 🚪 [**DOOR_BUILDING_SPECS.md**](file:///d:/gem/Matma%20roblox/references/DOOR_BUILDING_SPECS.md) | **Specyfikacja Budowy Drzwi** – dokładne wymiary klocków, koordynaty, kolory, oświetlenie i struktura modeli. |
| ⚖️ [**ECONOMY_BALANCE.md**](file:///d:/gem/Matma%20roblox/references/ECONOMY_BALANCE.md) | **Balans Ekonomii** – ceny samochodów, domów, jedzenia oraz zbalansowane nagrody za piętra i zbieranie kryształów. |
| ⌨️ [**SHORTCUTS_AND_TOOLS.md**](file:///d:/gem/Matma%20roblox/references/SHORTCUTS_AND_TOOLS.md) | **Ściągawka Roblox Studio** – skróty klawiszowe, sterowanie kamerą, obsługa właściwości i narzędzi. |

---

## 📁 Struktura Folderów w Projekcie

```text
d:\gem\Matma roblox\
├── assets\                     # Grafiki koncepcyjne i tekstury
│   ├── math_city_concept.jpg
│   └── math_city_doors.jpg
├── docs\                       # Główna dokumentacja projektowa i techniczna
│   ├── README.md
│   ├── GDD.md
│   ├── ARCHITECTURE.md
│   ├── MATH_CURRICULUM.md
│   └── ROBLOX_SETUP_GUIDE.md
├── references\                 # Ściągawki, specyfikacje wymiarów i balans gry
│   ├── DOOR_BUILDING_SPECS.md
│   ├── ECONOMY_BALANCE.md
│   └── SHORTCUTS_AND_TOOLS.md
├── src\                        # Gotowe kody źródłowe Luau do wklejenia w Studio
│   ├── server\                 # Skrypty serwerowe (ServerScriptService / Workspace)
│   │   ├── LeaderstatsAndDataStore.luau
│   │   ├── MathDoorScript.luau
│   │   ├── AdminServer.luau
│   │   └── CollectibleCoin.luau
│   └── client\                 # Skrypty klienckie (StarterPlayerScripts / StarterGui)
│       └── AdminPanelGui.luau
├── PORADNIK_ROBLOX_STUDIO.md   # Skrócony przewodnik startowy
└── MathCity.rbxl               # Aktualny projekt Math City w Roblox Studio
```
