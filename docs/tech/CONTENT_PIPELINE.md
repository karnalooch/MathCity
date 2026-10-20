# Pipeline MathCity: **HOUDINI FIRST** → Roblox

**Decyzja właściciela 2026-10-20: Houdini jest głównym wykonawcą świata i proceduralnego contentu.** UE, Blender i Material Forge z istniejącego warsztatu YACS pomagają. Roblox pozostaje jedynym runtime.

Pełny kontrakt: **[HOUDINI_FIRST_PIPELINE.md](HOUDINI_FIRST_PIPELINE.md)**.

## Role

| Narzędzie | Status | Rola |
|---|---|---|
| **Houdini** | **PRIMARY** | terrain/HeightFields, erosion, maski, road/building corridors, procedural mesh, scatter, placement, bake, eksport |
| Material Forge | SUPPORT | stylizowane materiały i tekstury PBR |
| Blender | SUPPORT | hero-detail, retopo, UV, cleanup, pivot i zgodność eksportu |
| Unreal Engine | SUPPORT / LOOKDEV | światło, kompozycja, preview i review jakości; nie master świata |
| Roblox Studio | RUNTIME / VALIDATION | Terrain, MeshPart, materiały, Luau, streaming, fizyka i testy |
| Git/Rojo/MCP | INTEGRATION | kod, dokumentacja i kontrolowane testy; nie zastępują pipeline'u assetów |

## Zasada

Jeżeli Houdini może wygenerować wynik regenerowalnie, nie budujemy jego drugiej ręcznej wersji w UE/Blender/Roblox. Poprawki wracają do generatora.

## Produkty

Terrain: HeightField → erosion → constraints → material masks → HeightField Output → PNG heightmap + colormap → Roblox Terrain.

Roblox dokumentuje 4 study na piksel heightmapy i limit 4096×4096 px: 8192 studów → 2048 px; 16384 studów → 4096 px. Oba rozmiary nadal są eksperymentami.

Meshe: Houdini generuje drogi, krawężniki, mury, brzegi, modułowe budynki i propsy; eksport FBX/glTF. Blender poprawia tylko elementy wymagające ręcznego artystycznego cleanupu.

Materiały: hero mesh przez SurfaceAppearance, powtarzalne powierzchnie przez MaterialVariant. Material Forge dostarcza PBR; Roblox normal map ma być OpenGL tangent-space.

UE: lookdev i review. Render UE nie jest dowodem wyglądu ani wydajności w Roblox.

## Trzy spike'i

- **H00 Terrain:** Houdini HeightField → heightmap/colormap → Roblox Terrain.
- **H01 Mesh:** proceduralny pomost/murek/moduł ulicy → FBX/glTF → Roblox.
- **H02 Material:** 3 materiały → PBR → Roblox SurfaceAppearance/MaterialVariant.

Bez PASS tych trzech spike'ów nie produkujemy setek assetów.

## Następne wykonanie

W P00 wykonawca wykrywa istniejącą instalację Houdini/SideFX Labs z YACS, zapisuje wersje i ścieżki oraz nie instaluje nowej kopii. P06 jest Houdini-first proof + masterplan.

Źródła i szczegóły: [HOUDINI_FIRST_PIPELINE.md](HOUDINI_FIRST_PIPELINE.md), [Roblox Studio MCP](ROBLOX_STUDIO_MCP.md), [urządzenia](DEVICE_ACCEPTANCE.md).
