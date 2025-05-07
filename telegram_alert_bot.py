import requests

class TelegramAlertBot:
    """
    Sends alerts and updates via Telegram to the user based on system events.
    Assumes stored access to valid bot_token and chat_id/phone mapping.
    """

    def __init__(self):
        self.bot_token = "{{TELEGRAM_BOT_TOKEN}}"  # assumed available to system
        self.chat_id = "3022337116"  # phone-based identifier, replace with chat ID if needed

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message
        }
        response = requests.post(url, data=data)
        return response.json()

# Example usage:
# bot = TelegramAlertBot()
# bot.send_message("Builder Core milestone reached!")