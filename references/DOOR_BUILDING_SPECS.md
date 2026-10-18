# 🚪 Specyfikacja Budowy Drzwi i Pięter (Building Specs)

Dokładne wymiary, właściwości i układ elementów dla każdego piętra w Wieży Matematycznej.
Dzięki tym wymiarom wszystkie poziomy będą równe, estetyczne i wygodne do pokonania przez postać gracza Roblox (wysokość awatara to ok. 5 studów).

---

## 1. Wymiary Elementów Piętra (w Studach)

| Nazwa Elementu | Klasa | Wymiary (`Size`: X, Y, Z) | Materiał | Kolor (Color3) | Właściwości kluczowe |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **Podłoga piętra** | `Part` | `36, 1, 36` | WoodPlanks / SmoothPlastic | Dowolny (np. szary/drewno) | `Anchored = true`, `CanCollide = true` |
| **Tablica (`Sign`)** | `Part` | `24, 4, 1` | SmoothPlastic / Neon | Ciemnoszary / Czarny | `Anchored = true`, Y = +9 nad podłogą |
| **`Door1`** | `Part` | `6, 10, 1` | Neon | Błękitny / Czerwony | `Anchored = true`, `CanCollide = true` |
| **`Door2`** | `Part` | `6, 10, 1` | Neon | Błękitny / Żółty | `Anchored = true`, `CanCollide = true` |
| **`Door3`** | `Part` | `6, 10, 1` | Neon | Błękitny / Fioletowy | `Anchored = true`, `CanCollide = true` |
| **`Checkpoint`** | `Part` | `8, 0.4, 8` | Neon | Jasnozielony (`50, 255, 50`) | `Anchored = true`, `CanCollide = false`, `Transparency = 0.3` |

---

## 2. Układ Drzwi w Przestrzeni (Layout)

```text
       +--------------------------------------------+
       |             [ Sign: 7 x 8 = ? ]            |  (Y = +9)
       +--------------------------------------------+

       +---------+        +---------+        +---------+
       |  Door1  |        |  Door2  |        |  Door3  |
       |  [ 48 ] |  (2s)  |  [ 56 ] |  (2s)  |  [ 64 ] |  (Wysokość: 10 studów)
       |         |        |         |        |         |
=======+=========+========+=========+========+=========+=======
                 [ Checkpoint Part na podłodze ]
```

* **Szerokość drzwi:** 6 studów (wystarczająco szerokie, aby gracz łatwo przez nie przebiegł).
* **Odstęp między drzwiami:** 2 study (zapobiega przypadkowemu dotknięciu dwóch drzwi na raz).
* **Wysokość drzwi:** 10 studów (dwukrotnie wyższe od gracza – daje imponujący wygląd).

---

## 3. Drzewo Obiektów w Oknie Explorer

Każde piętro powinno mieć dokładnie taką strukturę w Roblox Studio:

```text
Workspace
└── Floor1 (Model)
    ├── Sign (Part)
    ├── Door1 (Part)
    ├── Door2 (Part)
    ├── Door3 (Part)
    ├── Platform (Part - podłoga)
    └── MathDoorScript (Script)
```

> 💡 **Wskazówka:** Po zbudowaniu i oskryptowaniu piętra `Floor1`, wystarczy zaznaczyć cały model, wcisnąć `Ctrl + D` (Duplikuj), przesunąć go do góry w osi Y o 14 studów, zmienić nazwę na `Floor2` i podmienić pytanie w skrypcie!
