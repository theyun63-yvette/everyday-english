#!/usr/bin/env python3
"""Minimal DeepSeek API chat example for Everyday English."""

import json
import os
import urllib.request
from pathlib import Path

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")


def main() -> None:
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise SystemExit("Set DEEPSEEK_API_KEY before running this example.")

    prompt_path = Path(__file__).with_name("system-prompt.md")
    system_prompt = prompt_path.read_text(encoding="utf-8")
    user_message = input("You: ").strip() or "Let's practise everyday English."

    payload = json.dumps(
        {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            "stream": False,
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.load(response)
    print("Coach:", result["choices"][0]["message"]["content"])


if __name__ == "__main__":
    main()
