> **Archiwalny bank przykładów dla Wieży v1:** 20 pięter przygotowanych dla klasy 3. Nie jest to zatwierdzony spis wymagań klas 2–4. Obecny kierunek, wersjonowanie podstaw MEN oraz dydaktyka minigier: [education/CURRICULUM_2_4.md](education/CURRICULUM_2_4.md).

# 📐 Baza Pytań Matematycznych dla 3. Klasy

Zestaw zadań przygotowany specjalnie pod program 3. klasy szkoły podstawowej (tabliczka mnożenia w zakresie do 100 oraz zasady kolejności działań).

Możecie skopiować te wartości bezpośrednio do zmiennych konfiguracyjnych w pliku [`src/server/MathDoorScript.luau`](file:///d:/gem/Matma%20roblox/src/server/MathDoorScript.luau) dla kolejnych pięter wieży!

---

## 🟢 Etap 1: Podstawowa Tabliczka Mnożenia (Piętra 1 – 5)

| Piętro | Pytanie (`QUESTION`) | Opcja 1 | Opcja 2 | Opcja 3 | Poprawne Drzwi (`CORRECT_DOOR_INDEX`) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | `"3 x 4 = ?"` | `10` | `12` | `14` | **2** |
| **2** | `"5 x 6 = ?"` | `30` | `25` | `35` | **1** |
| **3** | `"4 x 7 = ?"` | `24` | `26` | `28` | **3** |
| **4** | `"6 x 6 = ?"` | `32` | `36` | `40` | **2** |
| **5** | `"5 x 9 = ?"` | `45` | `40` | `50` | **1** |

---

## 🟡 Etap 2: Średnia Tabliczka Mnożenia (Piętra 6 – 10)

| Piętro | Pytanie (`QUESTION`) | Opcja 1 | Opcja 2 | Opcja 3 | Poprawne Drzwi (`CORRECT_DOOR_INDEX`) |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **6** | `"7 x 6 = ?"` | `40` | `44` | `42` | **3** |
| **7** | `"7 x 8 = ?"` | `48` | `56` | `64` | **2** |
| **8** | `"8 x 8 = ?"` | `64` | `58` | `72` | **1** |
| **9** | `"9 x 6 = ?"` | `52` | `54` | `58` | **2** |
| **10** | `"9 x 8 = ?"` | `81` | `68` | `72` | **3** |

---

## 🟠 Etap 3: Kolejność Działań bez Nawiasów (Piętra 11 – 15)
> 💡 **Zasada:** Mnożenie wykonujemy ZAWSZE przed dodawaniem i odejmowaniem!

| Piętro | Pytanie (`QUESTION`) | Opcja 1 | Opcja 2 | Opcja 3 | Poprawne Drzwi (`CORRECT_DOOR_INDEX`) | Wyjaśnienie |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **11** | `"2 + 3 x 4 = ?"` | `20` | `14` | `16` | **2** | $3 \times 4 = 12 \rightarrow 2 + 12 = 14$ |
| **12** | `"5 + 2 x 6 = ?"` | `17` | `42` | `19` | **1** | $2 \times 6 = 12 \rightarrow 5 + 12 = 17$ |
| **13** | `"10 - 2 x 3 = ?"` | `24` | `6` | `4` | **3** | $2 \times 3 = 6 \rightarrow 10 - 6 = 4$ |
| **14** | `"4 x 5 + 7 = ?"` | `27` | `48` | `25` | **1** | $4 \times 5 = 20 \rightarrow 20 + 7 = 27$ |
| **15** | `"20 - 3 x 5 = ?"` | `5` | `15` | `85` | **1** | $3 \times 5 = 15 \rightarrow 20 - 15 = 5$ |

---

## 🔴 Etap 4: Kolejność Działań z Nawiasami (Piętra 16 – 20)
> 💡 **Zasada:** Działanie w nawiasie wykonujemy ZAWSZE JAKO PIERWSZE!

| Piętro | Pytanie (`QUESTION`) | Opcja 1 | Opcja 2 | Opcja 3 | Poprawne Drzwi (`CORRECT_DOOR_INDEX`) | Wyjaśnienie |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **16** | `"(2 + 3) x 4 = ?"` | `14` | `20` | `24` | **2** | $2 + 3 = 5 \rightarrow 5 \times 4 = 20$ |
| **17** | `"(10 - 6) x 5 = ?"` | `20` | `44` | `15` | **1** | $10 - 6 = 4 \rightarrow 4 \times 5 = 20$ |
| **18** | `"3 x (2 + 5) = ?"` | `11` | `24` | `21` | **3** | $2 + 5 = 7 \rightarrow 3 \times 7 = 21$ |
| **19** | `"(4 + 4) x 8 = ?"` | `64` | `36` | `72` | **1** | $4 + 4 = 8 \rightarrow 8 \times 8 = 64$ |
| **20** | `"(12 - 3) x 9 = ?"` | `72` | `81` | `99` | **2** | $12 - 3 = 9 \rightarrow 9 \times 9 = 81$ |