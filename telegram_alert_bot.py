import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "8170948174:AAFM_RZNl4AcpyY0M3rQwsHDmjCY5_yfwyE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '').strip().lower()

    if text == "/start":
        reply = "✅ Builder Core is active. Use commands like /status, /help, or just ask a question."
    elif text == "/status":
        reply = "🧠 Builder Core Status: All systems operational. Modules responsive."
    elif text == "/help":
        reply = ("🤖 Available commands:\n"
                 "/status - Check system status\n"
                 "/log - Show recent activity\n"
                 "/whoami - Identity of this bot\n")
    elif text == "/log":
        reply = "📜 Log: Last diagnostics run, 1 task executed, no errors."
    elif text == "/whoami":
        reply = "I'm Builder Core's alert companion. I listen, log, and notify."
    elif "diagnostic" in text:
        reply = "🔍 Running diagnostics... (simulated response: system stable)"
    elif any(greet in text for greet in ["hi", "hello", "hey"]):
        reply = "👋 Hello! I'm always here."
    else:
        reply = f"📩 Got your message: '{text}'. I'm logging it."

    send_message(chat_id, reply)
    return {"ok": True}

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)