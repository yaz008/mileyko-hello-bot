from typing import Literal

from project.cfg.decorator import config


ParseMode = Literal['HTML', 'Markdown', 'MarkdownV2']


@config(filename='telebot')
class BotConfig:
    parse_mode: ParseMode = 'HTML'
    threaded: bool = False
