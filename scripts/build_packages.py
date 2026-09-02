#!/usr/bin/env python3
"""Build portable Everyday English packages without external dependencies."""

from __future__ import annotations

import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
CORE_FILES = [
    Path("SKILL.md"),
    Path("README.md"),
    Path("references/scenarios.md"),
    Path("references/grammar-guide.md"),
    Path("references/progress-template.md"),
    Path("references/correction-examples.md"),
]


def copy_files(destination: Path, files: list[Path]) -> None:
    for relative in files:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)


def skill_body() -> str:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip()
    return text


def combined_prompt() -> str:
    sections = [
        "# Everyday English — Portable System Prompt\n\n",
        "Follow the instructions below as the system-level behavior for this English-learning assistant.\n\n",
        skill_body(),
    ]
    for relative in CORE_FILES[2:]:
        title = relative.stem.replace("-", " ").title()
        sections.extend(
            [
                f"\n\n---\n\n# Supporting Reference: {title}\n\n",
                (ROOT / relative).read_text(encoding="utf-8"),
            ]
        )
    return "".join(sections).rstrip() + "\n"


def write_zip(source: Path, output: Path) -> None:
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file in sorted(p for p in source.rglob("*") if p.is_file()):
            info = zipfile.ZipInfo(file.relative_to(source).as_posix())
            info.date_time = (2026, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, file.read_bytes())


def build() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    prompt = combined_prompt()

    with tempfile.TemporaryDirectory() as temp_name:
        temp = Path(temp_name)

        generic = temp / "generic" / "everyday-english"
        copy_files(generic, CORE_FILES)
        write_zip(temp / "generic", DIST / "everyday-english-agent-skill.zip")

        codex = temp / "codex" / "everyday-english"
        copy_files(codex, CORE_FILES + [Path("agents/openai.yaml")])
        shutil.copy2(ROOT / "docs/codex.md", codex / "INSTALL.md")
        write_zip(temp / "codex", DIST / "everyday-english-codex.zip")

        claude = temp / "claude" / "everyday-english"
        copy_files(claude, CORE_FILES)
        shutil.copy2(ROOT / "docs/claude.md", claude / "INSTALL.md")
        write_zip(temp / "claude", DIST / "everyday-english-claude.zip")

        deepseek = temp / "deepseek"
        harness_skill = deepseek / "harness/.agents/skills/everyday-english"
        copy_files(harness_skill, CORE_FILES)
        api = deepseek / "api"
        api.mkdir(parents=True)
        (api / "system-prompt.md").write_text(prompt, encoding="utf-8")
        shutil.copy2(ROOT / "adapters/deepseek/api-example.py", api / "api-example.py")
        shutil.copy2(ROOT / "docs/deepseek.md", deepseek / "INSTALL.md")
        write_zip(deepseek, DIST / "everyday-english-deepseek.zip")

        doubao = temp / "doubao"
        copy_files(doubao, CORE_FILES)
        (doubao / "system-prompt.md").write_text(prompt, encoding="utf-8")
        shutil.copy2(ROOT / "adapters/doubao/opening-message.md", doubao / "opening-message.md")
        shutil.copy2(ROOT / "docs/doubao.md", doubao / "INSTALL.md")
        write_zip(doubao, DIST / "everyday-english-doubao.zip")

        workbuddy = temp / "workbuddy" / "everyday-english"
        (workbuddy / "implementation").mkdir(parents=True)
        shutil.copy2(ROOT / "adapters/workbuddy/skill.yml", workbuddy / "skill.yml")
        (workbuddy / "implementation/prompt.md").write_text(prompt, encoding="utf-8")
        copy_files(workbuddy, CORE_FILES[2:])
        shutil.copy2(ROOT / "README.md", workbuddy / "README.md")
        shutil.copy2(ROOT / "docs/workbuddy.md", workbuddy / "INSTALL.md")
        write_zip(temp / "workbuddy", DIST / "everyday-english-workbuddy.zip")

    checksum_lines = []
    for package in sorted(DIST.glob("*.zip")):
        digest = hashlib.sha256(package.read_bytes()).hexdigest()
        checksum_lines.append(f"{digest}  {package.name}")
    (DIST / "SHA256SUMS.txt").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")

    print(f"Built Everyday English {VERSION} packages:")
    for path in sorted(DIST.iterdir()):
        print(f"- {path.name}")


if __name__ == "__main__":
    build()
