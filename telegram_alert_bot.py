import requests

class TelegramAlertBot:
    def __init__(self):
        self.bot_token = "{{CLARITY_COMPANION_BOT_TOKEN}}"
        self.chat_id = "1759822075"

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

# Send confirmation message
bot = TelegramAlertBot()
bot.send_message("✅ Builder Core is now connected to your Telegram! Alerts will flow from here.")