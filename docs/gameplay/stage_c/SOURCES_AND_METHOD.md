# Etap C: źródła, identyfikacja gier i metoda badania

**Odczyt: 2026-10-19. Zakres: research źródłowy, nie zdalny playtest.**

## 1. Klasy dowodu

- **F:** informacja odczytana w materiale pierwotnym. Zawsze podać ID źródła. Opis autora jest deklaracją funkcji, nie testem poprawności.
- **I:** interpretacja mechaniki lub hipoteza projektanta. Nie opisywać jej jako wyniku eksperymentu.
- **MC:** autorska propozycja dla MathCity. Nie jest elementem analizowanej gry ani zatwierdzonym zakresem implementacji.
- **N:** niezmierzone lub niezweryfikowane. W metrykach zapisywać NOT_MEASURED, nigdy 0.
- **O:** własna obserwacja sesji z urządzeniem, datą i dowodem. **W tej wersji nie ma rekordów O.**

## 2. Dobór próby

To próba celowa 15 porównywalnych doświadczeń, **nie ranking 15 najpopularniejszych gier w dniu odczytu**. G01/G03/G04/G05/G09 mają sygnał szerokiego zainteresowania w oficjalnym podsumowaniu Roblox za 2025 (S01). Adopt Me! i Grow a Garden pojawiają się także w oficjalnym wydarzeniu z września 2026 (S02). Pozostałe gry dodano dla pokrycia konkretnych wzorców: sterowanie, konstrukcja, krótkie rundy, praca zespołowa, wyszukiwanie i ekspresja.

Nie potwierdzono bieżącej pozycji każdej gry ani aktualnych CCU. Popularność z 2025 nie jest przedstawiana jako ranking października 2026. Wydarzenie The Hunt opisane w S02 odbywało się 17–28 września 2026 i nie jest obecnie trwającym eventem.

## 3. Gry: potwierdzony adres, ID i autor z karty Roblox

| ID | Tytuł i źródło pierwotne | Place ID | Autor widoczny w odczycie |
| --- | --- | --- | --- |
| G01 | [Brookhaven RP](https://www.roblox.com/games/4924922222/Brookhaven-RP) | 4924922222 | Brookhaven by Voldex |
| G02 | [Adopt Me!](https://www.roblox.com/games/920587237/Adopt-Me) | 920587237 | Uplift Games |
| G03 | [Grow a Garden](https://www.roblox.com/games/126884695634066/Grow-a-Garden) | 126884695634066 | The Garden Game |
| G04 | [Steal a Brainrot](https://www.roblox.com/games/109983668079237/Steal-a-Brainrot) | 109983668079237 | BRAZILIAN SPYDER |
| G05 | [99 Nights in the Forest](https://www.roblox.com/games/79546208627805/99-Nights-in-the-Forest) | 79546208627805 | Grandma's Favourite Games |
| G06 | [Fisch](https://www.roblox.com/games/16732694052/Fisch) | 16732694052 | Fisching |
| G07 | [Fish It!](https://www.roblox.com/games/121864768012064/Fish-It) | 121864768012064 | Fish Atelier |
| G08 | [Blox Fruits](https://www.roblox.com/games/2753915549/Blox-Fruits) | 2753915549 | Gamer Robot Inc |
| G09 | [RIVALS](https://www.roblox.com/games/17625359962/RIVALS) | 17625359962 | Nosniy Games |
| G10 | [Dress To Impress](https://www.roblox.com/games/15101393044/Dress-To-Impress) | 15101393044 | Dress To Impress Group |
| G11 | [Tower of Hell](https://www.roblox.com/games/1962086868/Tower-of-Hell) | 1962086868 | YXceptional Studios |
| G12 | [Build A Boat For Treasure](https://www.roblox.com/games/537413528/Build-A-Boat-For-Treasure) | 537413528 | Chillz Studios |
| G13 | [Epic Minigames](https://www.roblox.com/games/277751860/Epic-Minigames) | 277751860 | Typical Games |
| G14 | [Work at a Pizza Place](https://www.roblox.com/games/192800/Work-at-a-Pizza-Place) | 192800 | Dued1 |
| G15 | [Find the Markers](https://www.roblox.com/games/7896264844/Find-the-Markers) | 7896264844 | markers epic memers |

**Identyfikator Place nie jest Universe ID.** Nie podstawiać go bez konwersji do endpointów wymagających Universe ID. Wyszukiwarka zwracała kopie o identycznych nazwach; zostały odrzucone. W szczególności alternatywne 99 Nights od Middle Games i Brookhaven od pojedynczych kont nie są korpusem G05/G01.

### Ograniczenia kart Roblox

Warstwa wyszukiwarki oznaczała otwarte karty gier jako indeksowane około dwa miesiące wcześniej. Data odczytu nie dowodzi daty aktualizacji gry. Tytułów eventów i notatek o patchach z kart nie oznaczamy jako najnowszych. Komunikat strony o braku działających instancji bez JavaScript **nie jest dowodem zerowej liczby graczy**. Publiczny odczyt Charts dał szkielet wymagający JS. Próba endpointu `apis.roblox.com/universes/v1/places/4924922222/universe` była niedostępna w użytym narzędziu. Z tego powodu nie wpisano liczników graczy, przychodów, retencji ani nowych rekordów popularności.

## 4. Dokumentacja i materiały twórców

| ID | Źródło | Data publikacji, jeśli podana | Wykorzystanie |
| --- | --- | --- | --- |
| S01 | [Roblox Replay: Search and Style](https://about.roblox.com/newsroom/2025/12/roblox-replay-decoded-search-style) | 2025-12-16 | Historyczny sygnał zainteresowania: roleplay, symulacje, współpraca i różnorodność gatunków |
| S02 | [The Hunt: Roblox 20](https://about.roblox.com/newsroom/2026/09/join-the-hunt-roblox-20) | 2026-09-16 | Wzorzec hubu i wypraw przez różne doświadczenia, nie aktualny ranking |
| S03 | [Adopt Me: strona twórców](https://www.playadopt.me/) | strona aktualizowana | Opieka, wspólna zabawa i personalizacja domu |
| S04 | [Roblox: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding) | dokumentacja, brak daty w odczycie | Szybkie pokazanie podstaw i wartość pierwszej sesji |
| S05 | [Roblox: Core loops](https://create.roblox.com/docs/production/game-design/core-loops) | dokumentacja | Czynność, powtarzalna sekwencja i progresja |
| S06 | [Roblox: Discovery](https://create.roblox.com/docs/discovery) | dokumentacja | Sygnały zachowania, powrotów i współpracy; brak gwarancji dystrybucji |
| S07 | [Roblox: Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items) | dokumentacja | Obowiązki przy losowości opłacanej bezpośrednio i pośrednio |
| S08 | [Kids and Select globally available](https://about.roblox.com/newsroom/2026/06/age-based-roblox-kids-and-select-accounts-now-globally-available) | 2026-06-16 | Czat zależny od wieku, sprawdzenia i ustawień; dodatkowa ocena gier |
| S09 | [Content maturity and compliance](https://create.roblox.com/docs/production/promotion/content-maturity) | dokumentacja | Rozróżnienie roleplay i social hangout, tworzenie treści przez graczy |
| S10 | [Create Your Game-Specific Quick Words](https://devforum.roblox.com/t/create-your-game-specific-quick-words/4932108) | 2026-10-13 | Bieżąca informacja o własnych moderowanych frazach, kategoriach i tłumaczeniu |
| S11 | [Roblox Kids and Select: wymagania](https://create.roblox.com/docs/production/publishing/kids-and-select) | dokumentacja | Bramki publikacji, nie instrukcja obchodzenia kwalifikacji |
| S12 | [Adopt Me: Profiles](https://www.playadopt.me/news/profiles) | 2024-04-19 | Album kolekcji, personalizacja; również przykład losowych paczek, których nie przenosimy |
| S13 | [Adopt Me: Jukebox and Quality of Life](https://www.playadopt.me/news/jukebox-and-quality-of-life) | 2025-03-07 | Waga potwierdzania kosztownych zakupów i poprawiania UI mobilnego |

Źródła są pierwotne: autor gry, platforma lub oficjalne ogłoszenie. Społecznościowe komentarze pod forum nie stanowią zasad Roblox. Ogłoszenie S10 jest nowsze od zapowiedzi Quick Words z marca i września 2026; nie traktujemy starszych limitów niestandardowych presetów jako aktualnej specyfikacji.

## 5. Co wolno wywnioskować

Można porównać zadeklarowane podstawowe czynności i zaproponować ich adaptację. Nie można na tej podstawie twierdzić, że wskazany przycisk jest wygodny, dziecko rozumie cel w minutę, gra jest bezpieczna w każdej sytuacji ani że konkretny mechanizm spowodował sukces rynkowy.

Przy każdym późniejszym pomiarze zapisać osobno czas odczytu danych, czas aktualizacji źródła i czas sesji. Nie utożsamiać odwiedzin z unikalnymi osobami ani szczytu eventowego z typowym CCU. W tym etapie nie zbierano danych dzieci ani nie uruchamiano gry z ich kont.

## 6. Powiązanie z MathCity

Źródła repozytorium: [bank M01–M40](../../world/atlas/MECHANICS_MATRIX.md), [Muchawka](../../world/atlas/MUCHAWKA_FEATURE.md), [Etap A](../../world/STAGE_A_README.md), [program klas 2–4](../../education/CURRICULUM_2_4.md). Odczyt bazowy: `ac942dd85f599b095af7d0922e88288175402a08`. Nie przenosić fikcyjnych parametrów eksperymentów do kart prawdziwych miejsc.
