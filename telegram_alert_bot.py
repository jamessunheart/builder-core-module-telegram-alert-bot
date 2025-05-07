import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "{{CLARITY_COMPANION_BOT_TOKEN}}"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    if text == "/start":
        send_message(chat_id, "✅ Builder Core bot connected. Your alerts are now active!")
        # Log chat_id securely (simulated)
        print(f"Captured chat_id: {chat_id}")

    return {"ok": True}

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=payload)

# Flask app to listen for Telegram updates (mocked locally here)
if __name__ == "__main__":
    print("Telegram bot webhook listening (mock mode)")