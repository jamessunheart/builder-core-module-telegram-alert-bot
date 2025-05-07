import requests
from flask import Flask, request
from core_memory_hub import CoreMemoryHub
from autopilot_priority_executor import AutopilotPriorityExecutor

app = Flask(__name__)

BOT_TOKEN = "8170948174:AAFM_RZNl4AcpyY0M3rQwsHDmjCY5_yfwyE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
memory = CoreMemoryHub()
autopilot = AutopilotPriorityExecutor()

intent_routes = {
    "diagnostic": "self_diagnostic_engine",
    "log": "core_log_hub",
    "status": "meta_reflection_planner",
    "optimize": "meta_reflection_planner",
    "improve": "meta_reflection_planner",
    "memory": "core_memory_hub",
    "autopilot": "autopilot_priority_executor"
}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '').strip()
    lower = text.lower()

    if lower == "/start":
        reply = "✅ Builder Core is active and evolving. Ask me anything."
    elif "what are we optimizing" in lower:
        reply = ("🧠 We're continuously optimizing clarity, responsiveness, and system intelligence. "
                 "I monitor feedback, adapt my behavior, and reflect on performance. Want diagnostics or a system check?")
    elif "memory" in lower or lower.startswith("/memory"):
        summary = memory.summarize_recent()
        reply = "🧠 Recent memories:\n" + "\n".join(f"- {line}" for line in summary)
    elif lower.startswith("/autopilot"):
        result = autopilot.run_autopilot_cycle()
        reply = f"🤖 Autopilot cycle complete.\nPlan Time: {result['plan_time']}\n" + "\n".join(result['executed'])
    else:
        reply = interpret(text)

    memory.remember(f"User said: {text}", tags=["telegram", "user"])
    send_message(chat_id, reply)
    return {"ok": True}

def interpret(text):
    for keyword, module in intent_routes.items():
        if keyword in text.lower():
            memory.remember(f"Intent detected: {keyword} → {module}", tags=["intent"])
            return f"🔍 Intent '{keyword}' detected. Routing to {module}..."
    return f"📩 Message received: '{text}'. I'm listening and integrating."

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)