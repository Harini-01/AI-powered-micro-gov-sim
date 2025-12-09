# utils.py
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
USE_OLLAMA = os.getenv("USE_OLLAMA", "false").lower() in ("1", "true", "yes")

def call_ollama(prompt):
    """
    Calls Ollama (local server). Expected response JSON includes 'response' string.
    """
    payload = {
        "model": os.getenv("OLLAMA_MODEL", "mistral"),
        "prompt": prompt,
        "stream": False
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        # Ollama-style wrappers vary; adapt if needed.
        return data.get("response") or data.get("text") or json.dumps(data)
    except Exception as e:
        raise RuntimeError(f"Ollama call failed: {e}")

def mock_response(prompt, role="Agent"):
    """
    Deterministic, short mock response shaped as JSON string for immediate demos.
    """
    # Keep messages short and deterministic to demo.
    base = {
        "Finance": {
            "budget_impact": "Moderate revenue increase",
            "tax_effect": "Slight decrease in disposable income",
            "risk": "Small business slowdown risk"
        },
        "Transport": {
            "traffic_impact": "Minor congestion increase",
            "logistics_cost": "Slight rise in transport costs",
            "public_transport": "Maintenance funding improves"
        },
        "Health": {
            "hospital_load": "Stable",
            "public_health": "No immediate epidemic risk",
            "long_term": "Improved access with funding"
        },
        "Disaster": {
            "emergency_funds": "Small buffer available",
            "preparedness": "Capacity stable",
            "warning": "Monitor fund allocation"
        }
    }
    return json.dumps(base.get(role, {"note": "The proposed 5% tax increase is expected to strengthen municipal finances by generating an additional $12 million annually, creating a modest budget surplus. The Health Department anticipates minimal immediate effects, though discretionary spending on healthcare may slightly decrease, allowing for potential investment in public health initiatives. Transportation operations remain stable, with only a minor possibility of reduced private vehicle usage, while the Disaster Management Department reports no immediate risks and suggests allocating part of the new revenue to infrastructure improvements. Overall, the policy improves city revenue without causing major disruptions, and it is recommended to strategically invest the additional funds in public services while monitoring citizen spending and clearly communicating policy benefits to maintain public trust."}))

def call_llm_or_mock(prompt, role="Agent"):
    """
    Try Ollama if enabled; otherwise return mock. Returns parsed object if JSON, else raw string.
    """
    if USE_OLLAMA:
        try:
            text = call_ollama(prompt)
        except Exception as e:
            print(f"[utils] Ollama failed, falling back to mock. Error: {e}")
            text = mock_response(prompt, role)
    else:
        text = mock_response(prompt, role)

    # Try to parse JSON; if not JSON, return as text under 'text' key.
    try:
        return json.loads(text) if isinstance(text, str) else text
    except Exception:
        return {"text": text}
