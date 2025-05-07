import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "8170948174:AAFM_RZNl4AcpyY0M3rQwsHDmjCY5_yfwyE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Simulated task router logic
intent_routes = {
    "diagnostic": "self_diagnostic_engine",
    "log": "core_log_hub",
    "status": "meta_reflection_planner",
    "improve": "meta_reflection_planner",
    "route": "task_intent_router"
}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '').strip().lower()

    response = interpret(text)
    send_message(chat_id, response)
    return {"ok": True}

def interpret(text):
    if text == "/start":
        return "✅ Builder Core is active. I’m evolving with each interaction."
    if "/" in text:
        return f"⚙️ Executing command: {text}... (simulated)"
    
    # Intent routing
    for keyword, module in intent_routes.items():
        if keyword in text:
            return f"🤖 I sense intent for '{keyword}'. Routing to {module}..."

    if any(x in text for x in ["hello", "hi", "hey"]):
        return "👋 I see you. Builder Core hears everything."

    return f"🧠 Processing: '{text}' — I'm learning from your input."

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)