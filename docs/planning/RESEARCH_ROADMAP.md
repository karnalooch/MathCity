# MathCity — plan badań, dowody i bramki decyzji

**Stan na 2026-10-18.** To plan researchu, **nie** zgoda na wdrażanie świata do Roblox. Obecny MathCity.rbxl pozostaje bez zmian.

## Aktualizacja stanu Etapu A — 2026-10-18

**Desk research zakończony, Stage A PARTIAL (NIE PASS).** Dokumentacja: [world/STAGE_A_README.md](../world/STAGE_A_README.md). Katalog liczy 41 punktów (10×A, 23×B, 8×C), 41 kart opisowych i 40 wstępnych minigier. Wśród priorytetów: Las Sekulski, biegówki na Sekule, Górka Grześ (wymaga potwierdzenia miejsca), stadion piłkarski oraz Park Wodny. Do bramki pozostają licencjonowane zdjęcia dla A, mapy tras i stref pamięci, potwierdzona lokalizacja Grześ oraz aprobata właściciela co do 7-strefowej koncepcji. Zatwierdzenie **NIE** następuje automatycznie po commicie dokumentacji.

### Zalew Muchawka: specjalny pakiet researchowy (2026-10-19)

**Dostarczono w docs**: [pełny brief N01](../world/atlas/MUCHAWKA_FEATURE.md), uzupełnienie [CURRICULUM_2_4](../education/CURRICULUM_2_4.md) oraz osiem nowych pomysłów `M33…M40`. Obecnie **40** kandydatów minigier łącznie. Muchawka pozostaje **priorytetem A**, a nie plażą dekoracyjną. Gate otwarte: 10 referencji z prawami, czytelny obrys miejsc, odpowiednio wersjonowana podstawa, odbiór przez mieszkańca, wybór rzeczywistych atrakcji do budowy. Nie uznawać Etapu A za PASS.

## Etap A: Atlas Siedlec

**Zadania:** wybrać 15–20 reprezentacyjnych punktów ze źródeł oficjalnych, zebrać własne/licencjonowane zdjęcia, nadać priorytety A/B/C, opracować karty landmarków. **Deliverables:** atlas, mapa logiczna, 3 kompletne karty ratusz/pałac/zalew. **Gate:** zatwierdzone miejsca i brak niesprawdzonych praw do materiałów.

## Etap B: Art bible i wizualizacje

**Aktualizacja 2026-10-19:** wykonano również **17 graficznych referencji SVG** i przypisano je do V01–V23 w [galerii](../art/VISUAL_REFERENCE_ATLAS.md). Stan wizualny: `SVG_GUIDES_READY / FINAL_RENDERS_NOT_DONE`; nie zatwierdzono jeszcze stylu. Przygotowano dokumentację researchową, scenariusze 3 stylów S1–S3, lookdev 7 proponowanych stref (Sekuła osobno), 23 karty ujęć, promptery, UI i procedury dla słabszych modeli. Stan `STAGE_B_DOCUMENTATION_READY / STAGE_B_VISUALS_NOT_DONE / REVIEW_REQUIRED`, bez końcowego PASS. Realne obrazy porównawcze i zatwierdzenie ownera nadal OPEN. [Indeks B](../art/STAGE_B_README.md), [runbook](../art/STAGE_B_WEAK_LLM_RUNBOOK.md), [B8 QA](../art/VISUAL_REVIEW.md).



**Zadania:** trzy warianty stylistyczne, te same kadry porównawcze, dzień/zachód/noc, model postaci i pojazdów, czytelność z poziomu dziecka. **Deliverables:** 10 ujęć z art briefs, porównanie, paleta i reguły modułowego modelowania. **Gate:** Siedlce są rozpoznawalne i wizualizacje wyglądają jak spójna gra, nie jak kopia GTA/Mario.

## Etap C: Mechaniki Roblox

**Zadania:** zagrać w 12–15 współcześnie popularnych gier; obserwować onboarding, pętlę w 1/5/10/20 minut, interakcje społeczne, mobile, nagrody i monetyzację. **Deliverables:** ranking wzorców + pięć antywzorców i propozycja core loop. **Gate:** rozwiązania oparte na obserwacji, nie samej liczbie graczy.

## Etap D: Dydaktyka klas 2–4

**Zadania:** zebrać oficjalne teksty podstaw obowiązujących klasy II/III oraz nową IV, przypisać umiejętności do minigier, napisać podpowiedzi, alternatywne ścieżki i ocenę. **Deliverables:** macierz z odsyłaczami do punktów programu, co najmniej 8 kart minigier, przykładowy bank. **Gate:** pozytywna recenzja nauczyciela i brak kar za pomyłki.

## Etap E: Proof-of-pipeline YACS → Roblox

**Zadania:** sprawdzić realne instalacje UE/Blender/Material Forge, prawa do przykładowego assetu, jeden stylizowany fragment Ratusza, eksport, import i porównanie. **Deliverables:** raport wersji i ścieżek, ustawienia skali, PBR, kolizje, pamięć, zrzuty i czas wykonania. **Gate:** w pełni odtwarzalny import w Roblox; mapy i skrypty gry pozostają nienaruszone na tym etapie.

## Etap F: Masterplan i skala mapy

**Zadania:** trzy warianty układu dzielnic, testowe trasy, syntetyczna makieta sześciu dzielnic, benchmark 8192 vs 16384 studów, symulacja docelowej gęstości budynków, FPS i streaming. **Deliverables:** wybrany schemat, raport urządzeń PC/mobile oraz konsekwencje one Place vs multiple Places. **Gate:** rozmiar wynika z pomiarów, nie z maksimum edytora.

## Etap G: Zgody, bezpieczeństwo i publikacja

**Zadania:** spis licencji YACS, zasady używania znaków Siedlec, wymagania Roblox Kids/Select, zgodność współpracy Team Create, dane dzieci, bezpieczna ekonomia. **Deliverables:** wykaz praw, plan publikacji, polityka bezpieczeństwa, testy odbiorców 16+. **Gate:** realistyczna i zgodna z platformą droga premiery.

## Etap H: Decyzja o produkcji (dopiero później)

Zatwierdzić cel MVP, układ i skalę całego miasta, listę pierwszych minigier, sposób synchronizacji i pierwszy pionowy fragment. Produkcja sektorami jest możliwa, ale plan obejmuje **cały docelowy świat od początku**, nie mały wycinek podszywający się pod całość.

## Reguły pracy

- Po każdym etapie: zapis w docs, źródła, data i status PASS/FAIL.
- Wnioski do decyzji: [DECISION_LOG.md](DECISION_LOG.md).
- Otwarte problemy: [RISKS_AND_OPEN_QUESTIONS.md](../research/RISKS_AND_OPEN_QUESTIONS.md).
- Nie edytujemy .rbxl, src i nie importujemy assetów podczas tej fazy dokumentacyjnej.
