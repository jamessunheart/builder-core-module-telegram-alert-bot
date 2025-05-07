import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "8170948174:AAFM_RZNl4AcpyY0M3rQwsHDmjCY5_yfwyE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

intent_routes = {
    "diagnostic": "self_diagnostic_engine",
    "log": "core_log_hub",
    "status": "meta_reflection_planner",
    "optimize": "meta_reflection_planner",
    "improve": "meta_reflection_planner"
}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '').strip().lower()

    if text == "/start":
        reply = "✅ Builder Core is active and evolving. Ask me anything."
    elif "what are we optimizing" in text:
        reply = ("🧠 We're continuously optimizing clarity, responsiveness, and system intelligence. "
                 "I monitor feedback, adapt my behavior, and reflect on performance to improve the Builder Core experience. "
                 "Want me to run a diagnostic or surface recent learnings?")
    else:
        reply = interpret(text)

    send_message(chat_id, reply)
    return {"ok": True}

def interpret(text):
    for keyword, module in intent_routes.items():
        if keyword in text:
            return f"🔍 I sense you're focused on '{keyword}'. Routing that to {module}... (soon with real execution)"
    return f"📩 Message received: '{text}'. I'm learning and integrating."

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)