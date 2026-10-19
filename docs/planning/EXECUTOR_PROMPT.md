# Gotowy prompt startowy dla wykonawcy

Użyj poniższego po otwarciu repozytorium. To prompt do wykonania **jednego pakietu**, nie zgoda na wszystkie prace jednocześnie. Domyślnie praca dokumentacyjna. Zmianę na pakiet kodowy Pxx musi zlecić właściciel.

```text
Pracujesz w karnalooch/MathCity. Najpierw przeczytaj:
1. docs/planning/WEAK_LLM_START_HERE.md
2. docs/planning/OWNER_DECISIONS_20261019.md
3. docs/planning/EXECUTION_PACKETS.md
4. Dokumenty wejściowe wyłącznie dla aktualnego pakietu.

Aktualny zakres: sprawdź D00, następnie wykonaj D01. Jeżeli D00 jest już
udokumentowany, nie przepisuj całego repo; przejdź do brakujących dowodów D01.
Nie uruchamiaj kolejnego pakietu Pxx bez osobnego zlecenia.

Zadanie właściciela teraz dotyczy dokumentacji. Nie zmieniaj MathCity.rbxl,
src/, tests/, tools/, assets/, ustawień Roblox ani produkcyjnych danych.
Nie merge PR #1. Nie usuwaj wcześniejszych badań i nie twórz nowych M41+.
Nie dopisuj nowych pytań A/B/C do rozstrzygniętych decyzji Q01–Q33.

Wymagania krytyczne:
- Wspólne miasto, matematyka dopasowana osobno do umiejętności.
- XP przygody nie oznacza opanowania matematyki i nie blokuje misji.
- Podpowiedzi UI i pomoc matematyczna to różne zdarzenia.
- Pomoc nie odbiera podstawowej nagrody, ale nie daje samodzielności.
- Głos PL później; mocne UI i pełny dotyk teraz.
- 1–4 osoby na przygodę, cel16 osób w mieście, iPad6 obowiązkowy.
- Dołączenie tylko między etapami i bez retroaktywnych nagród.
- Otwarty problem oceniamy warunkami, nie jednym wzorcowym obrazkiem.
- Wszystkie wartości TEST_DEFAULTS są do sprawdzenia, nie zostały wybrane
  przez właściciela jako ostateczny balans.

Przed zmianą: odczytaj aktualny HEAD i git status. Nie resetuj cudzej pracy.
Zapisz bazowy SHA i hash mapy. Sprawdź rzeczywiste pliki, nie ufaj pamięci.
W D01 odczytaj oficjalne źródła i przypisz konkretne punkty programu.
Odróżnij etap IV–VI od klasy4; uwzględnij przepisy przejściowe i zmiany.
Brakujący dowód zaznacz SOURCE_PENDING/TEACHER_REVIEW_PENDING, nie wymyślaj.

Wykonaj tylko brakujące kroki pakietu, zachowując poprawne istniejące treści.
Na koniec sprawdź odnośniki, komplet IDs i czy zmiany są wyłącznie w docs/.
Nie twierdź, że uruchomiłeś Roblox, testy na iPadzie, review nauczyciela albo
sesje z dziećmi, jeśli nie masz rzeczywistych wyników i dowodów.

Raport: packet_id; base_sha; final_sha; ścieżki; Qxx; wykonane sprawdzenia;
wyniki PASS/FAIL/BLOCKED/NOT_RUN z zakresem; linki do dowodów; ograniczenia;
następny dozwolony pakiet. Zakończ po tym raporcie.
```

Dla przyszłego pakietu kodowego zmień wyłącznie aktualny zakres zgodnie ze zleceniem i wczytaj odpowiednie kontrakty. Nie wolno automatycznie usunąć zakazów bezpieczeństwa dotyczących oryginalnej mapy, cudzych zmian i publikacji. Najpierw kopia testowa oraz jawnie dozwolone ścieżki danego pakietu.
