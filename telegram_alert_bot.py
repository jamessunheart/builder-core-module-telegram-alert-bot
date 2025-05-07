import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "8170948174:AAFM_RZNl4AcpyY0M3rQwsHDmjCY5_yfwyE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route(f"/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '').strip().lower()

    if text == "/start":
        send_message(chat_id, "✅ Builder Core is online and listening.")
    elif "hello" in text or "hi" in text:
        send_message(chat_id, "👋 Hello from Builder Core. How can I assist?")
    else:
        send_message(chat_id, f"📩 Got your message: '{text}'. I'm listening.")

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