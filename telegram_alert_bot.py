import requests

class TelegramAlertBot:
    def __init__(self):
        # Token assumed stored securely in Builder Core for claritycompanion_bot
        self.bot_token = "{{CLARITY_COMPANION_BOT_TOKEN}}"  # placeholder for secure system-side token
        self.chat_id = "3022337116"  # replace with real chat_id if mapped

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message
        }
        try:
            response = requests.post(url, data=data)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

# Trigger real alert
bot = TelegramAlertBot()
result = bot.send_message("🚨 Builder Core Alert: This is a live test from @claritycompanion_bot.")
print("Telegram Send Result:", result)