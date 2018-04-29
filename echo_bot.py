import telebot


TOKEN = "asdasdag"

bot = telebot.TeleBot(TOKEN)

@bot.message_nadler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "How are you?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
