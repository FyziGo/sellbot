import telebot
import requests
import json
from telebot import types
  #Привязка бота
bot = telebot.TeleBot('TOKEN')
#Start
@bot.message_handler(commands=['start'])
def send_message(message):
        name = message.from_user.first_name
        print(name)
        bot.send_message(message.chat.id, 'Привет,' + name + '!', parse_mode= "Markdown")

#Кнопки
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.add('Заказать', 'Доставка', 'Скидки и акции', 'Отзыв', 'Support', 'Подарок', 'Мы в Instagram')

    #Помощь
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

    #Заказать
@bot.message_handler(commands=['zakaz'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

    #Инстаграм
@bot.message_handler(commands=['Instagram'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

    #Не доработано
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Заказать':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Доставка':
        bot.send_message(message.chat.id, 'Прощай, создатель') 


        #Данные 

bot.polling()
