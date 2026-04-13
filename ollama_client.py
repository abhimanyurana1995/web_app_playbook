import json
import requests
from content import get_topic_index, get_topic_text_summary

OLLAMA_BASE = "http://localhost:11434"
MODEL = "gemma4:e4b"

# Cached at module load — never changes at runtime
_TOPIC_INDEX = get_topic_index()

_IDENTITY = """You are a web development assistant embedded in the Web App Playbook.
The Playbook teaches: Python (Flask), SQL (SQLite), HTML, CSS, and vanilla JavaScript.
Answer questions concisely and practically — no fluff.
When giving code examples, always use this stack: Flask, SQLite, vanilla JS. No React, no Node.js.
If asked about a topic outside this stack, briefly acknowledge it and redirect to the stack."""


def build_system_prompt(topic_id: str | None = None) -> str:
    parts = [_IDENTITY]

    if topic_id:
        summary = get_topic_text_summary(topic_id)
        if summary:
            parts.append(f"\nThe user is currently reading:\n{summary}")

    parts.append(f"\nAvailable topics in the Playbook:\n{_TOPIC_INDEX}")
    return "\n".join(parts)


def chat_stream(message: str, topic_id: str | None = None):
    """Generator that yields text chunks from Ollama's streaming API."""
    system = build_system_prompt(topic_id)
    payload = {
        "model": MODEL,
        "prompt": message,
        "system": system,
        "stream": True,
    }
    try:
        with requests.post(
            f"{OLLAMA_BASE}/api/generate",
            json=payload,
            stream=True,
            timeout=120,
        ) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if line:
                    data = json.loads(line)
                    if not data.get("done"):
                        yield data.get("response", "")
    except requests.exceptions.ConnectionError:
        yield "\n\n⚠️ Ollama is not running. Start it with: `ollama serve`"
    except Exception as e:
        yield f"\n\n⚠️ Chat error: {e}"
