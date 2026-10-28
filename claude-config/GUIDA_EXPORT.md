# Da Claude Code a Claude "normale" (claude.ai e app)

Cosa si può portare, cosa no, e come.

| Cosa | Si esporta? | Come |
|---|---|---|
| **Skill** (53) | ✅ Sì | Una alla volta, come zip (cartella `skill/`) |
| **Agenti** (`code-reviewer`, `security-auditor`, `test-engineer`, `web-performance-auditor`) | ⚠️ Convertiti | Su claude.ai i subagent non esistono: sono diventati skill `agente-…` |
| **CLAUDE.md / preferenze** | ✅ Sì | Copia e incolla `PREFERENZE_PER_CLAUDE.txt` nel profilo |
| **Connettori** (alphaXiv, Wiley, Canva, …) | ✅ Già condivisi | Sono legati all'account: quelli collegati su claude.ai valgono ovunque |
| **Plugin** | ❌ No | Funzionano solo in Claude Code (e nell'app desktop per chi la usa con Claude Code) |
| **Hook, permessi, `settings.json`** | ❌ No | Esistono solo in Claude Code |

## 1. Caricare le skill

1. Su claude.ai apri **Impostazioni → Funzionalità** e attiva **Esecuzione di codice e creazione di file** (le skill la richiedono).
2. Nella sezione **Skill**, clicca **Carica skill** e scegli uno zip dalla cartella `skill/`.
3. Ripeti per ogni skill che ti serve: conviene caricare solo quelle che usi davvero, perché sono tante.

Le skill caricate valgono per il tuo account su claude.ai, app desktop e app mobile.

**Cosa è stato adattato nell'export:**
- Dal frontmatter sono state tolte le opzioni che esistono solo in Claude Code (`argument-hint`, `disable-model-invocation`, …).
- Le skill che in Claude Code partono solo con `/nome` (es. `teach-me`, `secondo-parere`, `ponytail`) hanno nella descrizione "Usala SOLO quando l'utente la chiede esplicitamente": su claude.ai le richiami scrivendo per esempio *"usa la skill teach-me"*.

**Skill che su claude.ai funzionano male o per niente:**
- `secondo-parere`: ha bisogno della CLI di Codex installata sul tuo PC → **non funziona** su claude.ai, solo in Claude Code.
- `graphify`: ha bisogno del programma `graphifyy` installato in locale → **non funziona** su claude.ai.
- `last30days`: usa script Python che scaricano dati da internet; nella sandbox di claude.ai la rete è limitata → **funziona solo in parte**.
- `browser-testing-with-devtools`, `git-workflow-and-versioning`, `ci-cd-and-automation`: pensate per lavorare su un progetto locale → su claude.ai danno solo consigli.

## 2. Preferenze (equivalente di CLAUDE.md)

Apri **Impostazioni → Profilo**, e incolla il testo di `PREFERENZE_PER_CLAUDE.txt` nel campo delle preferenze personali.

In alternativa, per un argomento specifico (es. la tesi) crea un **Progetto** e incolla le istruzioni nelle *Istruzioni del progetto*.

## 3. Rigenerare l'export

Se aggiungi o modifichi skill nella cartella `claude-config/skills/`:

```bash
pip install pyyaml
python esporta_per_claude_ai.py
```

Ricrea `export-claude-ai/` e il file unico `export-claude-ai.zip`.
