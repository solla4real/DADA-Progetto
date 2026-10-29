# Configurazione Claude Code (skill e agenti pubblici)

Raccolta delle skill e degli agenti elencati in `INVENTARIO_CLAUDE_CODE.md`, scaricati dai **repository pubblici originali su GitHub** (non dal PC di Davide: sono le versioni ufficiali, che possono differire leggermente dalle sue).

## Come installarli

Copia le cartelle nella tua configurazione di Claude Code:

- **Windows:** `C:\Users\<tuo-utente>\.claude\skills\` e `C:\Users\<tuo-utente>\.claude\agents\`
- **Mac/Linux:** `~/.claude/skills/` e `~/.claude/agents/`

```bash
cp -r skills/* ~/.claude/skills/
cp agents/*.md ~/.claude/agents/
```

Poi riavvia Claude Code. Le skill si richiamano con `/nome` (es. `/caveman`).

## Da dove viene cosa

| Cartella | Fonte | Licenza |
|---|---|---|
| 25 skill di sviluppo (`spec-driven-development`, `interview-me`, `idea-refine`, `context-engineering`, …) + agenti `code-reviewer`, `security-auditor`, `test-engineer`, `web-performance-auditor` | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| Skill UI/animazioni (`emil-design-eng`, `apple-design`, `animate`, `break-ui`, `prototype`, `write-swift`, …) | [emilkowalski/skills](https://github.com/emilkowalski/skills) | MIT |
| `ponytail`, `ponytail-audit`, `ponytail-review`, `ponytail-debt`, `ponytail-gain`, `ponytail-help` | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| `caveman` | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Apache-2.0 |
| `last30days` (senza la cartella `assets` con immagini/audio di esempio) | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | MIT |
| `graphify` | [safishamsi/graphify](https://github.com/safishamsi/graphify) | Apache-2.0 / MIT |
| `find-skills` | [vercel-labs/skills](https://github.com/vercel-labs/skills) | MIT |
| `teach-me` | [matheuszambonin/teach-me](https://github.com/matheuszambonin/teach-me) | MIT |
| `secondo-parere` | scritta per questo repository (ispirata a [hiroro-work/claude-plugins `ask-codex`](https://github.com/hiroro-work/claude-plugins)) | — |
| `hrtem-fft-zone-axis-indexing` | di Davide (condivisa da lui) | — |
| `marketing-psychology` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | MIT |

I testi delle licenze sono in `licenze/`.

### Note importanti

- **graphify** funziona solo con il suo programma Python installato: `pip install graphifyy` (con due "y"), poi `graphify install`, che rimette anche la skill al posto giusto.
- **last30days** usa script Python (cartella `scripts/`) e alcune fonti richiedono chiavi API: leggi il suo `SKILL.md`.
- **teach-me** si usa in una cartella vuota con `/teach-me`: prima cerca le fonti più affidabili sull'argomento (le salva in `RESOURCES.md`, due per ogni area), poi ti insegna a lezioni con ripassi a distanza. Potrebbe non essere identica alla versione di Davide.
- **secondo-parere** richiede la CLI di Codex: `npm install -g @openai/codex` e poi `codex login` (con account ChatGPT o chiave OpenAI). Si avvia solo con `/secondo-parere`.
- **ponytail** e **caveman** esistono anche come plugin completi (con hook): `/plugin marketplace add DietrichGebert/ponytail` e `/plugin marketplace add JuliusBrussee/caveman`.

## Cosa NON è stato trovato (personali di Davide)

Queste non esistono pubblicamente con quel nome: vanno chieste a Davide.

- Agenti: `data-analyst`, `latex-writer`
- Skill: `chief-of-staff`, tutte le `founder-*`
- Plugin `research-desk`, `scientific-coding`, `task-observer`, `social-media-skills`: vanno installati dal marketplace dei plugin.
- Connettori (alphaXiv, Wiley, Canva, …): si collegano dall'account su https://claude.ai/customize/connectors.

Alternative pubbliche simili alle `founder-*`: [ognjengt/founder-skills](https://github.com/ognjengt/founder-skills) e le altre skill di [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills).
