# B7 — MathCity UI: dzieci 2–4, PC i mobile

## Zobacz UI, zanim narysujesz własne

![PC i telefon: ekran wyzwania i obszary sterowania](concepts/REF12_UI_PC_MOBILE_SAFEAREA.svg)

![Matematyka na obiektach, nie tylko na formularzu](concepts/REF13_MATH_MINIGAME_VISUALS.svg)

**To makiety.** Safe area i przyciski dotykowe wymagają sprawdzenia na prawdziwym kliencie Roblox; treści matematyczne konsultacji pedagogicznej.

**Status:** UI DESIGN, nie zrealizowany HUD i nie testowane UI Roblox. Dzieci mogą odczytywać liczby i symbole, ale nie projektuj „dorosłego” ekranu wypchanego informacjami. Źródła: [R13,R14,R15,R16,R17](SOURCE_REGISTER.md).

## Priorytet wyświetlania

1. Teraz: **jedno** bieżące zadanie w maksymalnie dwóch krótkich zdaniach.
2. Interakcja: duży widoczny przycisk, odrębny od skoku/joysticka.
3. Nawigacja: prosty kierunek lub minimapa; informacja „Gdzie jestem” na żądanie.
4. Postęp: ikona paszportu odkrywcy, nie wyskakująca reklama.
5. Ekonomia/kolekcje: tylko w odpowiednim panelu, nigdy nad celem matematycznym.

## Trzy rozkłady ekranu do makiet

| Breakpoint testu | Orientacja | Zasada | Status |
|---|---|---|---|
| PC 1920×1080 | pozioma 16:9 | cel u góry, minimapa w narożniku, centrum 3D niezasłonięte | CONCEPT_ONLY |
| telefon ~19.5:9 | pozioma szeroka | lewy dolny pod joystick; prawy dolny pod skok; interakcja obok, ale nie koliduje; góra unika wycięcia | CONCEPT_ONLY |
| tablet 4:3 | pozioma | proporcje zautomatyzowane, karta minigry nie wykracza poza safe area | CONCEPT_ONLY |

To formaty testowe, nie deklaracja, że gra wspiera wyłącznie takie rozdzielczości. Nie narzucaj orientacji ekranu bez testu produktu.

## Warstwy UI

### U1 — Free Roam HUD
- Góra (safe zone): nazwa miejsca, jedna ikona bieżącego celu, ikona paszportu; brak tekstowego spamowania.
- Minimapka: prosty schemat stref, gracz / droga / punkt, nie pseudo-Google Maps pełne danych.
- Lewy i prawy dół: zarezerwowany pod domyślne mobilne sterowanie; własne przyciski nie powinny utrudniać ruchu.
- Interakcja: etykieta + ikona, np. „Zegar Jacka” + zegar; zawsze dostępne wyjście.
- Nie pokazywać oceny gracza ani porównania „gorszych uczniów”.

### U2 — Paszport odkrywcy
- Karty siedmiu proponowanych stref, odwiedzone landmarki z prawdziwymi nazwami, odznaki i cele poznawcze.
- Oddziel tab: „Miejsca Siedlec” i „Matematyka”, bez mieszania fikcyjnych atrakcji z faktami.
- Kolor + ikona + nazwa, uniknąć wyłącznie kolorowych kwadracików.
- Proponowany dobrowolny tryb rodzica/nauczyciela dopiero po audycie danych i etapu edukacji.

### U3 — Wyzwanie matematyczne
- Krótkie polecenie, obiekt 3D w centrum; przyciski „Pokaż wskazówkę”, „Spróbuj ponownie”, „Wyjdź”.
- Przy odpowiedzi: pokaż, dlaczego jest prawidłowa, a przy błędzie konkretną wskazówkę wizualną.
- Bez kar monetarnych/utraty życia za niepoprawną odpowiedź (projekt, do potwierdzenia).
- Sprawdzić poprawne wyświetlanie polskich znaków, różnych długości tekstu i skalowania.

## Tokeny UI (propozycje, bez narzucania pikseli silnikowi)

| Token | Zastosowanie | Zasada |
|---|---|---|
| UIC-BG | karta zadania | kremowe tło z wysokim kontrastem tekstu |
| UIC-TEXT | tekst | ciemny grafit, nie sam kolor akcentowy |
| UIC-ACTION | zatwierdzanie / pomoc | turkus + ikona i etykieta |
| UIC-STOP | wyjście/przerwanie | ramka + tekst, bez agresywnej czerwieni |
| UIC-HINT | podpowiedź | słoneczny żółty i symbol żarówki |
| UIC-INFO | lokalna ciekawostka | fiolet i ikona książki |

**Dostępność:** tekst + ikona + kształt, podpisy do kluczowych dźwięków, opcja ograniczenia ruchu/migotania, czytelny stan focus i brak drobnych dekoracyjnych mikrotekstów [R15].

## Roblox 2026: interfejs bezpieczny względem wycięć i systemowego UI

- `ScreenGui.ScreenInsets` może używać `CoreUISafeInsets` do omijania cutoutów i systemowego top baru; nie przejmuj ich samym absolutnym pixel offsetem [R14].
- `Device Simulator` w aktualnych docs jest w beta, warto testować nim wstępnie, ale to NIE wynik rzeczywistego telefonu [R16].
- Projektuj wokół mobilnych joystick/jump reserved zones i stref kciuków [R13].
- Dane telemetrii UI i ich testy w Roblox to odrębny etap, nie deklaruj działania na samym mockupie.

## Ujęcia i dowody

V-09 obejmuje **minimum dwa koncepty** tego samego UI (desktop/telefon) i jedną minigrę U3. Przy każdych makietach:
- podaj rozdzielczość mockupu, orientację, bezpieczne obszary i informację `IMAGE_CONCEPT`;
- bez prawdziwego screen capture wpisz `NOT_TESTED_IN_ROBLOX`;
- sprawdź czy przy rozmiarze telefonu można przeczytać zadanie i czy pasek Roblox nie zasłania menu.

## FAIL
- joystick, przycisk skoku lub notch zasłaniają grę;
- UI wymaga dźwięku do wykonania zadania;
- kolory są jedyną informacją;
- ważny tekst na jasnym tle ma brak kontrastu;
- mockup przedstawiony jako implementacja;
- paszport wyświetla dzieciom oceny innych graczy.
