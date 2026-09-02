#!/usr/bin/env python3
"""Validate generated Everyday English packages using only the standard library."""

from pathlib import Path
import py_compile
import re
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PACKAGES = {
    "everyday-english-agent-skill.zip": [
        "everyday-english/SKILL.md",
        "everyday-english/references/scenarios.md",
    ],
    "everyday-english-codex.zip": [
        "everyday-english/SKILL.md",
        "everyday-english/agents/openai.yaml",
        "everyday-english/INSTALL.md",
    ],
    "everyday-english-claude.zip": [
        "everyday-english/SKILL.md",
        "everyday-english/INSTALL.md",
    ],
    "everyday-english-deepseek.zip": [
        "INSTALL.md",
        "api/api-example.py",
        "api/system-prompt.md",
        "harness/.agents/skills/everyday-english/SKILL.md",
    ],
    "everyday-english-doubao.zip": [
        "SKILL.md",
        "INSTALL.md",
        "system-prompt.md",
        "opening-message.md",
    ],
    "everyday-english-workbuddy.zip": [
        "everyday-english/skill.yml",
        "everyday-english/implementation/prompt.md",
        "everyday-english/INSTALL.md",
    ],
}


def main() -> None:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert re.match(r"^---\n.*?\n---", skill, re.DOTALL), "SKILL.md frontmatter missing"
    assert "name: everyday-english" in skill
    assert "Hi! 👋 I’m your everyday English coach." in skill
    assert all(f"### {level}" in skill for level in ("Beginner", "Intermediate", "Advanced"))

    with tempfile.TemporaryDirectory() as temp_name:
        temp = Path(temp_name)
        py_compile.compile(
            str(ROOT / "scripts/build_packages.py"),
            cfile=str(temp / "build_packages.pyc"),
            doraise=True,
        )
        py_compile.compile(
            str(ROOT / "adapters/deepseek/api-example.py"),
            cfile=str(temp / "api_example.pyc"),
            doraise=True,
        )

    for package_name, required in PACKAGES.items():
        package = DIST / package_name
        assert package.is_file(), f"Missing package: {package_name}"
        with zipfile.ZipFile(package) as archive:
            assert archive.testzip() is None, f"Corrupt ZIP: {package_name}"
            names = set(archive.namelist())
            missing = [name for name in required if name not in names]
            assert not missing, f"{package_name} missing: {missing}"
            assert not any("__pycache__" in name or name.endswith(".DS_Store") for name in names)

    checksums = (DIST / "SHA256SUMS.txt").read_text(encoding="utf-8")
    assert checksums.count(".zip") == len(PACKAGES)
    print(f"Validated {len(PACKAGES)} installation packages.")


if __name__ == "__main__":
    main()
