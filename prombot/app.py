from flask import Flask
from . import appblueprint
import logging
from .senders import TelegramBotSender


def _create_app():
    app = Flask(__name__)
    app.config.from_object('prombot.config.Config')
    app.register_blueprint(appblueprint)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(app.config['LOG_FILE'])
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)
    return app


def main():
    app = _create_app()

    appblueprint.prombot_sender = TelegramBotSender(
        app.config['TELEGRAM_BOT_TOKEN'],
        app.config['TELEGRAM_BOT_CHAT_ID'],
    )
    app.logger.info("Starting prombot")
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])


if __name__ == '__main__':
    main()
