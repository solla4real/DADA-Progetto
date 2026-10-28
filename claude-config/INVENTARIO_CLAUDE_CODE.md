# Inventario Claude Code di Davide (gaett)

> **Per l'altro Claude Code che legge questo file.**
> Qui sono elencati gli agenti, le skill, i plugin e i connettori (MCP) che ho installati nella mia configurazione di Claude Code (Windows, utente `gaett`), con cosa fa ciascuno.
> Usalo per sapere quali strumenti posso avere a disposizione, o per replicare la configurazione.
> I file degli agenti sono in `C:\Users\gaett\.claude\agents\`, le skill personali in `C:\Users\gaett\.claude\skills\` (una cartella per skill, ognuna con `SKILL.md`).
> Inventario aggiornato al 28/10/2026.

Contesto: sono un dottorando (UniMoRe). Lavoro soprattutto su analisi di dati scientifici in Python, scrittura della tesi in LaTeX, microscopia elettronica (HRTEM) e qualche progetto web/marketing.
Rispondimi in **italiano**.

---

## 1. Agenti personalizzati (subagent)

Si invocano con il tool `Agent` indicando `subagent_type`. File: `~/.claude/agents/<nome>.md`.

| Agente | Cosa fa |
|---|---|
| `code-reviewer` | Revisore di codice Python per l'analisi di dati scientifici del dottorato. Da usare in modo proattivo dopo ogni modifica al codice Python: cerca bug, controlla la coerenza delle unità di misura, la riproducibilità e i test mancanti, e propone correzioni ordinate per gravità. |
| `data-analyst` | Analista di dati sperimentali (pandas, numpy, scipy, matplotlib). Carica ed esplora i dati, fa fit con stima e propagazione delle incertezze, produce grafici da pubblicazione (etichette con unità, salvataggio in PDF e PNG a 300 dpi). |
| `latex-writer` | Esperto di scrittura scientifica in LaTeX per tesi e articoli. Scrive o revisiona capitoli; controlla notazione, unità, riferimenti incrociati (`\label`/`\ref`/`\eqref`/`\cite`), bibliografia BibTeX e l'inglese accademico. **Propone sempre le modifiche e non tocca i file senza approvazione esplicita.** |
| `security-auditor` | Ingegnere di sicurezza: individua vulnerabilità, fa threat modeling, review del codice orientata alla sicurezza e consigli di hardening. |
| `test-engineer` | Ingegnere QA: strategia di test, scrittura di test per codice esistente, analisi della copertura e della qualità dei test. |
| `web-performance-auditor` | Ingegnere di performance web: Core Web Vitals, caricamento, rendering, rete, anti-pattern strutturali di performance. |

Agenti integrati di Claude Code (sempre presenti): `general-purpose`, `Explore` (ricerca in sola lettura nel codice), `Plan` (piani di implementazione), `claude-code-guide` (domande su Claude Code, API e SDK), `statusline-setup`.

---

## 2. Skill personali (`~/.claude/skills/`)

Si invocano con il tool `Skill` (o dall'utente con `/nome`).

### 2.1 Ricerca, dottorato e studio
| Skill | Cosa fa |
|---|---|
| `hrtem-fft-zone-axis-indexing` | Indicizza le macchie di FFT di immagini HRTEM o di pattern SAED (d-spacing, angoli, ampiezze) trovando l'asse di zona e gli indici hkl rispetto a una struttura cristallina candidata. Da usare ogni volta che si indicizza un pattern di diffrazione elettronica. |
| `graphify` | Trasforma qualsiasi input (codice, documenti, cartelle) in un knowledge graph e permette di interrogarlo. Si attiva con `/graphify` o quando esiste già una cartella `graphify-out/`. **Istruzione globale: quando scrivo `/graphify`, usare questa skill prima di ogni altra cosa.** |
| `teach-me` | Tutoraggio strutturato: spiega concetti, fa quiz, crea piani di studio e mini-corsi. |
| `last30days` | Ricerca cosa si dice su un tema negli ultimi 30 giorni (Reddit, X, YouTube, TikTok, Hacker News, GitHub, Polymarket…). |
| `secondo-parere` | Chiede un parere indipendente a OpenAI Codex (ChatGPT) su un file, un codice o un testo e lo confronta con la review di Claude. Solo su richiesta esplicita (`/secondo-parere`). Risponde in italiano. |
| `interview-me` | Mi intervista una domanda alla volta finché non è chiaro (al ~95%) cosa voglio davvero. |
| `idea-refine` | Affina un'idea vaga con pensiero divergente e convergente e ne mette alla prova le assunzioni. |

### 2.2 Organizzazione e produttività
| Skill | Cosa fa |
|---|---|
| `chief-of-staff` | Modalità "capo di gabinetto": coordina, filtra il rumore, tiene un registro delle decisioni e prepara brief giornalieri o settimanali. Solo con `/chief-of-staff` o su richiesta esplicita. In italiano. |
| `caveman` | Stile telegrafico: prima la risposta, niente fronzoli, tutti i fatti tecnici. Resta attivo fino a "stop caveman". |
| `find-skills` | Cerca e installa nuove skill o plugin, solo su richiesta esplicita. |
| `using-agent-skills` | Meta-skill: aiuta a decidere quale skill usare per un certo lavoro. |
| `context-engineering` | Ottimizza il contesto dell'agente (file di regole, CLAUDE.md, inizio sessione, cambio di task). |

### 2.3 Sviluppo software: processo e qualità
| Skill | Cosa fa |
|---|---|
| `spec-driven-development` | Scrive specifiche o PRD prima di programmare. |
| `planning-and-task-breakdown` | Divide il lavoro in task ordinati e implementabili. |
| `incremental-implementation` | Implementa a piccoli passi verificabili. |
| `test-driven-development` | Ciclo red-green-refactor: i test guidano lo sviluppo. |
| `debugging-and-error-recovery` | Debug sistematico alla ricerca della causa radice. |
| `code-review-and-quality` | Code review su più assi prima del merge. |
| `code-simplification` | Semplifica il codice senza cambiarne il comportamento. |
| `doubt-driven-development` | Sottopone ogni decisione non banale a una revisione avversariale con contesto fresco. |
| `constraint-driven-development` | Mette per iscritto gli standard di qualità (`CONSTRAINTS.md`) e impedisce agli agenti di abbassarli (test saltati, soppressioni…). |
| `source-driven-development` | Basa ogni scelta sulla documentazione ufficiale. |
| `api-and-interface-design` | Progettazione di API e interfacce stabili (REST/GraphQL, contratti tra moduli). |
| `git-workflow-and-versioning` | Buone pratiche git: commit, branch, conflitti. |
| `ci-cd-and-automation` | Configurazione di pipeline CI/CD e controlli di qualità automatici. |
| `documentation-and-adrs` | Documentazione e Architecture Decision Records. |
| `deprecation-and-migration` | Deprecazioni e migrazioni (anche di schemi di database senza downtime). |
| `security-and-hardening` | Rafforzamento del codice contro le vulnerabilità. |
| `performance-optimization` | Ottimizzazione delle prestazioni di frontend, backend e query. |
| `observability-and-instrumentation` | Logging, metriche, tracing, alerting. |
| `shipping-and-launch` | Checklist prima del rilascio in produzione. |
| `browser-testing-with-devtools` | Test in un browser reale tramite Chrome DevTools MCP. |
| `ponytail` | "Senior dev pigro": la modifica più piccola che risolve davvero, con una risposta che si capisce in una lettura. Solo su richiesta ("ponytail", "yagni"). |
| `ponytail-audit` | Audit di qualità di un intero repo (bug, sicurezza, carico, test mancanti, cosa eliminare). Report, non modifica nulla. |
| `ponytail-review` | Review di qualità di una singola modifica. |
| `ponytail-debt` | Elenca tutti i commenti `shortcut:` e `ponytail:` come registro del debito tecnico. |
| `ponytail-gain` | Mostra i risparmi misurati di ponytail (codice, costo, velocità). |
| `ponytail-help` | Aiuto sulla famiglia di skill ponytail. |
| `write-swift` | Swift moderno (Swift 6, concorrenza, tipi valore). |

### 2.4 Frontend, UI e animazioni
| Skill | Cosa fa |
|---|---|
| `frontend-ui-engineering` | Interfacce di qualità da produzione, accessibili e responsive. |
| `pick-ui-library` | Sceglie la libreria frontend giusta da una lista curata (grafici, toast, drag and drop, virtualizzazione…). |
| `prototype` | Costruisce più versioni davvero diverse di un pezzo di UI, con un selettore visivo per sceglierne una. |
| `break-ui` | Mette alla prova la UI con i dati peggiori possibili (nomi lunghissimi, emoji, zero elementi…) e riporta cosa si rompe. |
| `emil-design-eng` | Filosofia di Emil Kowalski su rifinitura della UI, componenti e animazioni. |
| `apple-design` | Approccio di Apple a interfaccia e movimento (spring, gesti, materiali), applicato al web. |
| `mobile-native` | Fa sembrare nativa su telefono una web app (meta tag, CSS). |
| `ask-sonner` | Guida alla libreria di toast React Sonner. |
| `animate` | Crea un'animazione da zero, prendendo le decisioni nell'ordine giusto. |
| `animate-expo` | Animazioni in React Native/Expo (Reanimated, Gesture Handler). |
| `animation-performance` | Mantiene le animazioni web fluide (proprietà composite, `will-change`, jank). |
| `animation-vocabulary` | Glossario: da una descrizione vaga di un effetto al suo nome tecnico. |
| `find-animation-opportunities` | Trova i punti di una UI che dovrebbero essere animati (solo proposte). |
| `improve-animations` | Audit delle animazioni di un codebase, con piani di miglioramento. |
| `review-animations` | Review severa del codice di animazione. |

### 2.5 Business e startup (famiglia `founder-*`)
| Skill | Cosa fa |
|---|---|
| `founder-board` | Un "consiglio di amministrazione" di 3 sub-agenti (lenti di Hormozi, Thiel e Steve Jobs) che valuta un'idea di business e vota. |
| `founder-competitors` | Mappa i concorrenti diretti e indiretti da fonti pubbliche e individua lo spazio libero nel mercato. |
| `founder-consumer` | Panel simulato di acquirenti (100 sub-agenti, o 20 con `--quick`) che reagiscono al pitch. |
| `founder-pricing` | Trova il prezzo giusto (Van Westendorp + concorrenza). |
| `founder-offer` | Costruisce un'offerta irresistibile (problemi → soluzioni, bonus, garanzia). |
| `founder-cfo` | Unit economics, margini, break-even, cassa necessaria, scenari. |
| `founder-marketing` | Posizionamento, canali, campagna di lancio di 30 giorni, hook, budget. |
| `founder-brand` | Nome, voce, tagline e linee guida visive del brand. |
| `founder-ops` | Operatività del giorno 1: fornitori, turni, routine, strumenti, licenze. |
| `founder-launch` | Piano di lancio con date: test reale, countdown, giorno del lancio, primi 30 giorni. |
| `founder-plan` | Riunisce l'output di tutte le skill founder in un unico business plan. |
| `marketing-psychology` | Applica principi di psicologia e scienze comportamentali al marketing. |

---

## 3. Plugin installati

| Plugin | Cosa fornisce |
|---|---|
| `anthropic-skills` | Skill ufficiali Anthropic: `pdf`, `docx`, `xlsx`, `pptx` (creare e modificare documenti Office e PDF), `deep-research`, `docs`, `google-workspace`, `chrome-browser`, `built-in-browser`, `computer-use`, `skill-creator`, `consolidate-memory`, `import-memory`, `morning`, `explain-usage`, `setup-claude`, `hrtem-fft-zone-axis-indexing`. |
| `research-desk` | Strumenti per la ricerca accademica: `citation-check` (verifica che i riferimenti esistano e supportino la frase), `related-work` (bozza dello stato dell'arte dalle fonti fornite), `paper-critique`, `paper-compare`, `research-litnote`, `decision-matrix`, `llm-council`; più un server MCP `reference-lookup` (verifica dei riferimenti su OpenAlex e arXiv, controllo dei file BibTeX). |
| `scientific-coding` | Skill `scientific-coding` per scrivere codice scientifico. |
| `frontend-design` | Skill `frontend-design` per il design di interfacce frontend. |
| `task-observer` | `task-observer`, `learn`, `preferences`: osserva il lavoro e salva o ordina le preferenze di lavoro in CLAUDE.md. |
| `social-media-skills` | Circa 100 skill per i social media: strategia, calendario editoriale, script per Reels/TikTok/YouTube, caption, hook, caroselli, LinkedIn, Instagram, Pinterest, Threads, X, newsletter, analytics, A/B test, e prompt per strumenti di AI generativa (Canva, CapCut, Runway, Kling, Veo 3, Suno, HeyGen, Synthesia, Flux, Ideogram…). |
| `playwright` | Server MCP per automatizzare un browser (navigare, cliccare, compilare form, screenshot). |

Skill e comandi integrati in Claude Code: `code-review`, `simplify`, `security-review`, `init`, `run`, `loop`, `schedule`, `claude-api`, `update-config`, `keybindings-help`, `fewer-permission-prompts`, `plugin-authoring`, `dataviz`, `artifact-design`, `artifact-diagramming`, `artifact-capabilities`.

---

## 4. Connettori e server MCP

| Connettore | Cosa fa |
|---|---|
| alphaXiv | Ricerca e lettura di articoli arXiv; gestione della mia libreria di paper, delle note e dei ricercatori seguiti. |
| Wiley | Ricerca nel testo completo delle pubblicazioni Wiley. |
| Ricerca nella letteratura scientifica (due connettori) | Ricerca di paper, revisioni sistematiche, report, ricerca di trial clinici, librerie di fonti. |
| Canva | Creare, modificare ed esportare design Canva; generare immagini. |
| Claude Docs | Documenti condivisi su claude.ai, modificabili insieme a Claude. |
| Claude in Chrome | Controllo del mio Chrome reale tramite estensione. |
| Browser integrato (desktop app) | Browser interno all'app Claude, per leggere pagine e vedere anteprime di siti. |
| Scheduled tasks | Attività pianificate e ricorrenti. |
| Playwright | Vedi la sezione 3. |
| research-desk reference-lookup | Vedi la sezione 3 (OpenAlex e arXiv). |

---

## 5. Istruzioni globali attive (`~/.claude/CLAUDE.md`)

- **graphify**: quando l'utente scrive `/graphify`, usare la skill installata (`~/.claude/skills/graphify/SKILL.md`) prima di fare qualsiasi altra cosa.

## 6. Come replicare la configurazione su un'altra macchina

1. Copiare `C:\Users\gaett\.claude\agents\` e `C:\Users\gaett\.claude\skills\` nella cartella `~/.claude/` di destinazione.
2. Copiare `C:\Users\gaett\.claude\CLAUDE.md`.
3. Reinstallare i plugin (sezione 3) dal marketplace dei plugin e riconnettere i connettori (sezione 4) dall'account claude.ai: richiedono il login, quindi non si copiano come file.
