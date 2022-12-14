import telebot

bot = telebot.TeleBot(token="YOUR_TOKEN")


@bot.message_handler(commands=["hello", "hi", "whatsup"])
def hello_handler(message: telebot.types.Message):
    bot.send_message(chat_id=message.chat.id, text="И тебе привет!")


@bot.message_handler(content_types=telebot.util.content_type_media)
def echo_message_handler(message: telebot.types.Message):
    if message.text:
        bot.send_message(chat_id=message.chat.id, text=message.text)
    elif message.photo:
        bot.send_message(chat_id=message.chat.id, text="Классная фотка!")


if __name__ == "__main__":
    bot.polling(non_stop=True)

