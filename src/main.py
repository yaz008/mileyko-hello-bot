from telebot import TeleBot
from telebot.types import Message

from project.cfg.configs.telebot import BotConfig
from project.env import Env


bot: TeleBot = TeleBot(
    token=Env.TELEGRAM_BOT_TOKEN,
    parse_mode=BotConfig.parse_mode,
    skip_pending=True,
    threaded=BotConfig.threaded,
)


@bot.message_handler(commands=['start'])  # type: ignore
def on_start(message: Message) -> None:
    bot.send_message(chat_id=message.from_user.id, text='<b>Hello</b>')


if __name__ == '__main__':
    bot.infinity_polling()
