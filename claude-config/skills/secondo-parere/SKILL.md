---
name: secondo-parere
description: Chiede un parere indipendente a OpenAI Codex (ChatGPT) su un file, un codice o un testo tramite la CLI `codex`, poi lo confronta con la review di Claude e indica su cosa concordano e su cosa no. Da usare SOLO quando l'utente lo chiede esplicitamente (`/secondo-parere`, "chiedi un secondo parere", "senti cosa dice ChatGPT/Codex"). Risponde sempre in italiano.
argument-hint: "File, cartella o testo da far valutare (e cosa controllare)"
disable-model-invocation: true
allowed-tools: Bash(codex *), Read, Glob, Grep
---

# Secondo parere (Claude + Codex)

L'utente vuole due revisioni **indipendenti** dello stesso materiale: la tua e quella di Codex. Il valore sta nell'indipendenza: nessuno dei due deve vedere il parere dell'altro prima di aver scritto il proprio.

## Requisiti

- CLI `codex` installata e autenticata (`npm install -g @openai/codex`, poi `codex login`).
- Se `codex --version` fallisce, fermati e spiega all'utente come installarla. Non inventare la risposta di Codex.

## Procedura

1. **Chiarisci l'oggetto.** Dagli argomenti ricava cosa va valutato (file, cartella, selezione di testo, diff) e su quale aspetto (bug, chiarezza, correttezza scientifica, stile, inglese accademico…). Se non è chiaro, chiedi una sola volta.

2. **Scrivi prima la TUA review**, senza mostrarla ancora all'utente. Leggi il materiale con `Read`/`Grep`, poi annota i punti in ordine di gravità, ognuno con posizione (file:riga o paragrafo) e motivo.

3. **Chiedi a Codex, in sola lettura**, con lo stesso compito e senza la tua review:

   ```bash
   codex exec --sandbox read-only -C "<cartella del progetto>" "Sei un revisore indipendente. Valuta <oggetto> concentrandoti su <aspetto>. Elenca i problemi in ordine di gravità, ognuno con posizione esatta (file:riga o paragrafo) e motivo. Non modificare nessun file. Rispondi in italiano."
   ```

   - Per un testo che non è in un file, salvalo prima in un file temporaneo e indica a Codex quel percorso.
   - Non usare mai `--full-auto` o sandbox in scrittura: il secondo parere non tocca i file.
   - Se il comando va in errore o supera il tempo, riprova una volta; poi riporta l'errore così com'è.

4. **Verifica le affermazioni di Codex** sul materiale vero: un problema citato esiste davvero a quella riga? Segna quelli che non reggono.

5. **Presenta il confronto** in italiano, in questo formato:

   ```md
   ## Secondo parere su <oggetto>

   ### Concordano entrambi
   - <problema> — <posizione> (gravità)

   ### Solo Claude
   - <problema> — <posizione> — perché è rilevante

   ### Solo Codex
   - <problema> — <posizione> — ✅ verificato / ❌ non regge, perché

   ### In disaccordo
   - <punto>: Claude dice …, Codex dice … → mio giudizio: …

   ### Cosa farei
   1. <azione prioritaria>
   ```

## Regole

- Non modificare file: proponi soltanto. Le modifiche si fanno dopo, se l'utente le approva.
- Riporta il parere di Codex fedelmente; se lo riassumi, non cambiarne il senso.
- Non dare ragione a Codex per cortesia né a te stesso per principio: decide la verifica sul materiale.
- Non inviare a Codex dati che l'utente ha indicato come riservati senza chiederglielo prima.
