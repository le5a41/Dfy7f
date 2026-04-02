import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')  # Токен возьмём из переменных окружения
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот на Amvera')

print('Бот запущен')
bot.infinity_polling()
