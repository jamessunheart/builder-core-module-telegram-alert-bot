import requests

class TelegramAlertBot:
    def __init__(self):
        self.bot_token = "{{CLARITY_COMPANION_BOT_TOKEN}}"
        self.username = "jsunheart"
        self.chat_id = self.resolve_chat_id()

    def resolve_chat_id(self):
        # In practice, this requires prior interaction and possibly a database
        # Here we simulate or require pre-mapped chat ID
        known_ids = {
            "jsunheart": "USER_CHAT_ID_PLACEHOLDER"  # Replace with actual ID once known
        }
        return known_ids.get(self.username, None)

    def send_message(self, message):
        if not self.chat_id:
            return {"error": "Chat ID not found for user."}
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

# Attempt to send real message now
bot = TelegramAlertBot()
print("Sending message to jsunheart...")
result = bot.send_message("⚡ Builder Core alert test to @jsunheart.")
print("Telegram result:", result)