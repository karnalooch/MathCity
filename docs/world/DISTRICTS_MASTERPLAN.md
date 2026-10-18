# MathCity — dzielnice i masterplan otwartego miasta

**Status:** PROPOZYCJA, 2026-10-18. Nazwy dzielnic i lokalizacje są fikcyjne. Nie odnoszą się do granic administracyjnych Siedlec.

![Schemat świata — układ artystyczny, nie mapa geograficzna](../art/MATHCITY_WORLD_SCHEMATIC.svg)

## Docelowe doświadczenie

Duży, spójny świat z dalekimi sylwetkami ważnych obiektów, z miękkimi granicami między dzielnicami. Zawsze wiadomo, gdzie leży centrum; ratusz ma być wizualnym kompasem. Gracz może jechać przez miasto bez teleportacji co 30 sekund, a areny wymagające odrębnych budżetów ewentualnie trafią do osobnych Roblox Places.

## Koncepcja sześciu dzielnic

| # | Nazwa (robocza) | Tożsamość miejsca | Kolor / klimat | Charakter ruchu | Matematyka |
| --- | --- | --- | --- | --- | --- |
| 1 | **Jackowo: Serce Miasta** | Ratusz, kamienice, rynek | brzoskwinia, turkus, krem | pieszo, pojazdy miejskie | liczenie, pieniądze, sklep, Zegar Jacka |
| 2 | **Ogrody Aleksandrii** | Pałac, park, fontanny | mięta, róż, złoto | spacer, parkour | figury, symetria, układanki |
| 3 | **Kolejowo: Stacja Czasu** | Dworzec, stacja, fantastyczne estakady | błękit, fiolet | pociąg, autobusy | czas, bilety, dodawanie |
| 4 | **Muchawkowe Wyspy** | Zalew, plaża, mosty | morski turkus, żółty | rower, łodzie | dzielenie, ułamki, pomiary |
| 5 | **Neonowe Błonia** | Stadion, skatepark, tereny sportowe | koral, granat | wyścigi, skoki | pomiary, obwód, pole |
| 6 | **Aleja Kultury** | Teatr, muzea, zabytki | fiolet, złoto | pieszo, wycieczki | rytmy, wzory, kodowanie sekwencji |

Punkty historyczne są rozpoznawalne, ale fikcyjne elementy (wyspy, portale, estakady) mają być jasno odróżnione od geografii realnej.

## Makroukład (hipoteza)

- **Centrum:** Jackowo jako miejski hub, punkt startowy i miejsce odpoczynku.
- **Północ / północny zachód (artystycznie):** Ogrody i Aleja Kultury.
- **Wschód:** Kolejowo z szybkim transportem do centrum.
- **Południe:** Neonowe Błonia i przestrzeń wyścigów.
- **Zachód:** Muchawkowe Wyspy, promenady i spokojniejsza dzielnica wody.
- **Pierścień:** szerokie drogi i trasy rowerowe, krótki objazd do każdej atrakcji.
- **Oś widokowa:** sylwetka ratusza w zasięgu orientacyjnym w centrum, pałac widoczny zza parku, stadion jako duży punkt kierunkowy.

Schemat jest propozycją layoutu; po badaniach terenowych może zostać skorygowany. Nie należy mówić, że tak wygląda prawdziwy układ Siedlec.

## Hierarchia i rytm odkryć

- Co kilkadziesiąt sekund marszu: mały punkt interakcji.
- Co kilka minut: jedno większe miejsce lub aktywność.
- Między dzielnicami: charakterystyczne bramy krajobrazowe, zmiana roślinności i palety.
- Centralne landmarki: rozpoznawalne przy zredukowanym LOD i bardzo małej liczbie materiałów.
- Przy każdym ważnym zabytku: krótka, opcjonalna prawdziwa ciekawostka z linkiem do źródła.

To reguły koncepcyjne do walidacji użytkowej, nie wymagania techniczne.

## Skala do benchmarku, nie decyzja

Dwa kandydaty do prób: **8192 × 8192 studów** (ok. 2,29 × 2,29 km) i **16384 × 16384 studów** (ok. 4,59 × 4,59 km). Przelicznik orientacyjny 1 stud = 0,28 m wg Roblox Creator Hub. Rozmiar wynikać będzie z testów streamingu, telefonów i szybkości przemieszczania, nie z ambicji liczbowej.

## Kolejność projektowania

1. Atlas punktów i referencje zdjęciowe.
2. Trzy warianty topologii miasta w 2D.
3. Wybór makroukładu i skali dzielnic.
4. Blockout całej planowanej mapy (bez detalu).
5. Test sieci dróg i czasu przejazdu.
6. Dopiero potem reprezentatywny, pionowy wycinek jakości wizualnej do zatwierdzenia.
7. Produkcja sektorami, ale plan dla **całego świata** od początku.

**Nie wykonano jeszcze blockoutu, importu ani benchów.** Zob. [budżety](../tech/LARGE_WORLD.md), [roadmapę](../planning/RESEARCH_ROADMAP.md).
