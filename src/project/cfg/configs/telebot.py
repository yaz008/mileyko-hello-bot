from project.cfg.decorator import config


@config(filename='telebot')
class BotConfig:
    parse_mode: str = 'HTML'
    threaded: bool = False
