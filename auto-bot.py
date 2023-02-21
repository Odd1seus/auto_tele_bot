import telebot 
import tele_token
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton


bot = telebot.TeleBot(tele_token.token_num)

nissan_nb_dict = {"/GTR_R35":"https://uk.wikipedia.org/wiki/Nissan_GT-R","/GTR_R34":"https://uk.wikipedia.org/wiki/Nissan_Skyline#R34"}
ford_nb_dict = {"/Mustang_6th_gen":"https://en.wikipedia.org/wiki/Ford_Mustang_(sixth_generation)",
"/Mustang_5th_gen":"https://en.wikipedia.org/wiki/Ford_Mustang_(fifth_generation)"}
lambo_nb_dict = {"/Aventador":"https://ru.wikipedia.org/wiki/Lamborghini_Aventador","/Huracan":"https://ru.wikipedia.org/wiki/Lamborghini_Hurac%C3%A1n","/Veneno":"https://ru.wikipedia.org/wiki/Lamborghini_Veneno"}

GTR_R35_buttons = {"/Объем_двигателя":"3.8 литра V6","/Годы_выпуска":"2008-2023","/Коль-во_сидений":"2 передних и задний ряд,но там места слишком мало,очень тяжело высидеть поездку","/Цена":" только б/у варианты стоят от $73 тыс долларов,а с завода и с полной комплектацией страшно представить"}
M_6th_buttons = {"/Объем_двигателя":"существует несколько версий v6,а именно:5 литров,3.7 литра и 2.3 литра Ecoboost","/Годы выпуска":"Июль 2014 - наши дни","/Коль-во_сидений":"спереди 2 места и сзади ряд сидений,при желании можно и вптяером усестся","/Цена":"если брать с салона то цена стартует от $27.770"}
Veneno_buttons = {"/Объем_двигателя":"6,5 Литров V12","/Годы_выпуска":"2013 год","/Коль-во_сидений":"2","/Цена":"$4,500,000"}


def keyboard_buttons():
    markup = ReplyKeyboardMarkup()
    itembtn1 = KeyboardButton('/Nissan_wiki')
    itembtn2 = KeyboardButton('/Ford_wiki')
    itembtn3 = KeyboardButton('/Lamborghini_wiki')
    itembtn4 = KeyboardButton('/Nissan_button')
    itembtn5 = KeyboardButton('/Ford_button')
    itembtn6 = KeyboardButton('/Lamborghini_button')
    markup.add(itembtn1, itembtn2,itembtn3)
    markup.add(itembtn4, itembtn5,itembtn6)
    return markup

def interactive_buttons():
  markup = ReplyKeyboardMarkup()
  V_buton = KeyboardButton("/Объем_двигателя")
  year_button = KeyboardButton("/Годы_выпуска")
  seat_button = KeyboardButton("/Коль-во_сидений")
  price_button = KeyboardButton("/Цена")
  markup.add(V_buton,year_button)
  markup.add(seat_button,price_button)
  return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Привет,про какую машину хочешь узнать?",reply_markup = keyboard_buttons())


@bot.message_handler(commands=['Nissan_wiki'])
def nissan_message(message):
  bot.send_message(message.chat.id,f'Про какую модель хотите узнать?,{nissan_nb_dict.keys()}')

@bot.message_handler(commands=['GTR_R35'])
def GTR_R35(message):
  bot.send_message(message.chat.id,nissan_nb_dict["/GTR_R35"])

@bot.message_handler(commands=['GTR_R34'])
def GTR_R34(message):
  bot.send_message(message.chat.id,nissan_nb_dict["/GTR_R34"])

@bot.message_handler(commands=['Nissan_button'])
def nissan_message(message):
  bot.send_message(message.chat.id,"Модель GTR R35",reply_markup = interactive_buttons())

@bot.message_handler(commands=['Объем_двигателя'])
def GTR_R35_V(message):
  bot.send_message(message.chat.id,GTR_R35_buttons["/Объем_двигателя"])

@bot.message_handler(commands=['Годы_выпуска'])
def GTR_R35_YR(message):
  bot.send_message(message.chat.id,GTR_R35_buttons["/Годы_выпуска"])

@bot.message_handler(commands=['Коль-во_сидений'])
def GTR_R35_seats(message):
  bot.send_message(message.chat.id,GTR_R35_buttons["/Коль-во_сидений"])

@bot.message_handler(commands=['Цена'])
def GTR_R35_price(message):
  bot.send_message(message.chat.id,GTR_R35_buttons["/Цена"])

#####################################################################################################################

@bot.message_handler(commands=['Ford_wiki'])
def ford_message(message):
  bot.send_message(message.chat.id,f'Про какую модель хотите узнать?,{ford_nb_dict.keys()}')

@bot.message_handler(commands=['Mustang_6th_gen'])
def M_6th_gen(message):
  bot.send_message(message.chat.id,ford_nb_dict["/Mustang_6th_gen"])

@bot.message_handler(commands=['Mustang_5th_gen'])
def M_5th_gen(message):
  bot.send_message(message.chat.id,ford_nb_dict["/Mustang_5th_gen"])

@bot.message_handler(commands=['Ford_button'])
def ford_message(message):
  bot.send_message(message.chat.id,"Модель Mustang 6th gen",reply_markup = interactive_buttons())

@bot.message_handler(commands=['Объем_двигателя'])
def M_6th_V(message):
  bot.send_message(message.chat.id,M_6th_buttons["/Объем_двигателя"])

@bot.message_handler(commands=['Годы_выпуска'])
def M_6th_YR(message):
  bot.send_message(message.chat.id,M_6th_buttons["/Годы_выпуска"])

@bot.message_handler(commands=['Коль-во_сидений'])
def M_6th_seats(message):
  bot.send_message(message.chat.id,M_6th_buttons["/Коль-во_сидений"])

@bot.message_handler(commands=['Цена'])
def M_6th_price(message):
  bot.send_message(message.chat.id,M_6th_buttons["/Цена"])

#####################################################################################################################

@bot.message_handler(commands=['Lamborghini_wiki'])
def lambo_message(message):
  bot.send_message(message.chat.id,f'Про какую модель хотите узнать?,{lambo_nb_dict.keys()}')

@bot.message_handler(commands=['Aventador'])
def aventador(message):
  bot.send_message(message.chat.id,lambo_nb_dict["/Aventador"])

@bot.message_handler(commands=['Huracan'])
def Huracan(message):
  bot.send_message(message.chat.id,lambo_nb_dict["/Huracan"])

@bot.message_handler(commands=['Veneno'])
def Veneno(message):
  bot.send_message(message.chat.id,lambo_nb_dict["/Veneno"])


@bot.message_handler(commands=['Lamborghini_button'])
def veneno_message(message):
  bot.send_message(message.chat.id,"Модель Lamborghini Veneno",reply_markup = interactive_buttons())

@bot.message_handler(commands=['Объем_двигателя'])
def Veneno_V(message):
  bot.send_message(message.chat.id,Veneno_buttons["/Объем_двигателя"])

@bot.message_handler(commands=['Годы_выпуска'])
def Veneno_YR(message):
  bot.send_message(message.chat.id,Veneno_buttons["/Годы_выпуска"])

@bot.message_handler(commands=['Коль-во_сидений'])
def Veneno_seats(message):
  bot.send_message(message.chat.id,Veneno_buttons["/Коль-во_сидений"])

@bot.message_handler(commands=['Цена'])
def Veneno_price(message):
  bot.send_message(message.chat.id,Veneno_buttons["/Цена"])

@bot.message_handler(content_types=['text'])
def choose_car(message):
  if message.text == "/Ford_button":
    M_6th_V(message)













bot.polling(non_stop=True)