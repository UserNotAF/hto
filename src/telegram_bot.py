import requests


class TelegramBot:

    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.url = f"https://api.telegram.org/bot{token}/sendMessage"

    def send(self, text: str) -> bool:

        if not self.token or not self.chat_id:
            return False

        try:
            response = requests.post(
                self.url,
                json={
                    "chat_id": self.chat_id,
                    "text": text,
                    "parse_mode": "HTML"
                },
                timeout=10
            )

            return response.status_code == 200

        except Exception:
            return False
