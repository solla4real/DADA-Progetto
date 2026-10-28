"""Prepara skill e agenti di questa cartella per caricarli su Claude (claude.ai / app).

Su claude.ai le skill si caricano una alla volta come file .zip
(Impostazioni > Funzionalità > Skill). Gli agenti non esistono su claude.ai,
quindi vengono convertiti in skill.

Uso:  python esporta_per_claude_ai.py
Crea: export-claude-ai/  (uno zip per skill + GUIDA + preferenze)
      export-claude-ai.zip (tutto in un unico file)
"""

import shutil
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "export-claude-ai"
# Chiavi del frontmatter accettate dal formato Agent Skills; le altre
# (argument-hint, disable-model-invocation, …) sono solo di Claude Code.
CHIAVI_OK = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
SOLO_SU_RICHIESTA = "Usala SOLO quando l'utente la chiede esplicitamente. "


def leggi(md: Path):
    _, fm, corpo = md.read_text(encoding="utf-8").split("---", 2)
    return yaml.safe_load(fm), corpo


def scrivi(md: Path, meta: dict, corpo: str):
    fm = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=10_000)
    md.write_text(f"---\n{fm}---{corpo}", encoding="utf-8")


def pulisci(meta: dict) -> dict:
    nuovo = {k: v for k, v in meta.items() if k in CHIAVI_OK}
    if meta.get("disable-model-invocation") or meta.get("user-invocable") is False:
        nuovo["description"] = (SOLO_SU_RICHIESTA + str(nuovo["description"]))[:1024]
    return nuovo


def zippa(cartella: Path, destinazione: Path):
    with zipfile.ZipFile(destinazione, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(cartella.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(cartella.parent))


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    lavoro = OUT / "_tmp"
    (OUT / "skill").mkdir(parents=True)
    nomi = []

    for cartella in sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").exists()):
        copia = lavoro / cartella.name
        shutil.copytree(cartella, copia)
        meta, corpo = leggi(copia / "SKILL.md")
        scrivi(copia / "SKILL.md", pulisci(meta), corpo)
        zippa(copia, OUT / "skill" / f"{cartella.name}.zip")
        nomi.append(cartella.name)

    for agente in sorted((ROOT / "agents").glob("*.md")):
        meta, corpo = leggi(agente)
        nome = f"agente-{meta['name']}"
        copia = lavoro / nome
        copia.mkdir(parents=True)
        meta = {"name": nome, "description": str(meta["description"])[:1024]}
        nota = "\n> Convertito da un agente (subagent) di Claude Code: segui queste istruzioni come ruolo per la richiesta corrente.\n"
        scrivi(copia / "SKILL.md", meta, nota + corpo)
        zippa(copia, OUT / "skill" / f"{nome}.zip")
        nomi.append(nome)

    shutil.rmtree(lavoro)
    for f in ("GUIDA_EXPORT.md", "PREFERENZE_PER_CLAUDE.txt"):
        shutil.copy(ROOT / f, OUT / f)

    tutto = ROOT / "export-claude-ai.zip"
    tutto.unlink(missing_ok=True)
    zippa(OUT, tutto)
    print(f"{len(nomi)} skill pronte in {OUT}\nFile unico: {tutto}")


if __name__ == "__main__":
    main()
