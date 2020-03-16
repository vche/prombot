class Config(object):
    """This is the basic configuration class for BorgWeb."""

    #: builtin web server configuration
    HOST = '0.0.0.0'  # use 0.0.0.0 to bind to all interfaces
    PORT = 9087  # ports < 1024 need root
    DEBUG = True  # if True, enable reloader and debugger
    LOG_FILE = 'prombot.log'

    # Telegram bot config
    TELEGRAM_BOT_TOKEN = "1110478838:AAGZVZaDmjUPffFTIxpgLVIKI5r7yg5h_8g"
    TELEGRAM_BOT_CHAT_ID = "-489291168"
