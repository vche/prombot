"""
Reference for telegram bot api:
https://core.telegram.org/bots/api#available-methods
"""

import requests
from flask import current_app


class TelegramBotSender():
    TELEGRAM_BOT_API_BASEURL = "https://api.telegram.org/bot"
    TELEGRAM_BOT_API_SENDMSG = "sendMessage"

    def __init__(self, username, token, dest):
        self._endpoint = f"{self.TELEGRAM_BOT_API_BASEURL}{token}"
        self._dest = dest

    def _cmd_url(self, cmd):
        return f"{self._endpoint}/{cmd}"

    def _post(self, cmd, data):
        current_app.logger.info(f"sent {data} to {self._cmd_url(cmd)}")
        return requests.post(self._cmd_url(cmd), data=data)

    def _build_message(self, message_data):
        return {'chat_id': self._dest, 'text': message_data}

    def send(self, message):
        payload = self._build_message(message)
        resp = self._post(self.TELEGRAM_BOT_API_SENDMSG, payload)
        current_app.logger.debug(f"Response {resp}: {resp.content}")
        if resp.status_code == 200:
            jrsesp = resp.json()
            if jrsesp['ok']:
                return {'ok': True}
            else:
                return {'ok': False, 'error': jrsesp['description']}
        else:
            return {'ok': False, 'error': resp.status_code}
