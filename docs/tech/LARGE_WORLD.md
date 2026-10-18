# Ogromny świat w Roblox — architektura i budżet wydajności

**Status:** hipotezy inżynierskie, 2026-10-18. „Maksymalnie wielka mapa” jest celem eksploracyjnym, a nie znanym z góry rozmiarem.

## Dwa zakresy do pierwszego benchmarku

| Parametr | Próba A | Próba B |
| --- | --- | --- |
| Bok mapy | 8192 studów | 16 384 studów |
| Odpowiednik fizyczny (0,28 m/stud) | około 2,29 km | około 4,59 km |
| Powierzchnia geometryczna | około 5,26 km² | około 21,05 km² |
| Status | **DO ZMIERZENIA** | **DO ZMIERZENIA** |

Wartości nie są gwarantowaną ani rekomendowaną maksymalną granicą Roblox. Przeliczenie: [Roblox units](https://create.roblox.com/docs/physics/units). Dla porównania każda próba wymaga pomiarów „czas do zabawy”, pamięci, FPS, teleporterów, pojazdów i fizyki.

## Architektura hipotetyczna

- Jeden spójny **Place** obejmujący centrum i dzielnice, jeśli testy mobilne potwierdzą płynność.
- Opcjonalne osobne Places dla dużych aren/odległych wysp, gdy streaming jednego Place jest niewystarczający. Decyzja dopiero po benchmarkach.
- Logiczne sektory; streaming zależny od pozycji i potrzeb danej sceny.
- SLIM dla odległych modeli i uproszczony RenderFidelity / LOD.
- Mniejsza liczba unikalnych siatek: jedna biblioteka fasad, dachów, roślin, latarni, słupków.
- Tekstury łączone / trim sheets, rozsądne rozdzielczości, tinty i ograniczenie światła dynamicznego.
- Kolizje prostsze niż wizualna siatka. Nie symulować zasięgiem całej mapy.
- Lekkie odległe landmarki muszą zachować sylwetkę; nie dociągać pełnego wnętrza z drugiego końca miasta.

Źródła: [Roblox — Improve performance](https://create.roblox.com/docs/performance-optimization/improve) oraz [Design for performance](https://create.roblox.com/docs/performance-optimization/design).

## Cele do potwierdzenia

| Pomiar | Proponowany próg |
| --- | --- |
| PC docelowy | 60 FPS |
| Telefon średniej klasy | >=30 FPS |
| Sensowna pierwsza interakcja | w 2–3 min od wejścia (preferencyjnie szybciej) |
| Jazda po mieście | bez niespodziewanych dziur w kolizji i geometrii |
| Multiplayer | podstawowe minigry i transport bez widocznych desynchronizacji |
| Streaming | bez utknięcia gracza w niegotowym sektorze |

To **kryteria aspiracyjne**, nie wyniki pomiarów. Progi pamięci i loadingu uzależniamy od faktycznych modeli urządzeń.

## Plan prób skali

1. Stworzyć **syntetyczny** szkielet sześciu sektorów z uproszczonymi bryłami, a nie finalny krajobraz.
2. Przygotować A i B z identyczną gęstością obiektów na km².
3. Ustawić streaming i przetestować spacer, pojazd, teleport, respawn.
4. Przetestować 1, 2, 4 i więcej klientów; wysoki i niski preset grafiki.
5. Zmierzyć FPS medianę i spadki, pamięć, czas ładowania, dławienie sieci, obciążenie serwera.
6. Wprowadzić landmarki testowe i trzy typy roślin/elewacji. Powtórzyć pomiary.
7. Zmniejszyć złożoność lub przejść na wiele Places, jeśli problem systemowy.

**Ważne:** sam pusty teren o rozmiarze B nie dowodzi, że pełne miasto o tym wymiarze będzie działać. Zasymulować docelową gęstość obiektów i zachowań.

## Warunek Go / No-Go

Wybieramy największą mapę, która **spełnia testy przy realistycznej zawartości i normalnych urządzeniach dzieci**, zamiast maksymalnej wartości z edytora. Budowa pełnego świata nie może ruszyć bez takiego testu.

Zob. [testowanie](PLAYTESTING.md), [masterplan](../world/DISTRICTS_MASTERPLAN.md).
