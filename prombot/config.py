class Config(object):
    """This is the basic configuration class for BorgWeb."""

    #: builtin web server configuration
    HOST = '0.0.0.0'  # use 0.0.0.0 to bind to all interfaces
    PORT = 9087  # ports < 1024 need root
    DEBUG = True  # if True, enable reloader and debugger
    LOG_FILE = 'prombot.log'

    # Telegram bot config
    TELEGRAM_BOT_TOKEN = "XXXX"
    TELEGRAM_BOT_CHAT_ID = "-XXXX"
