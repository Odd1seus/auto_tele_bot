import telebot 
import tele_token
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton


bot = telebot.TeleBot(tele_token.token_num)

Gtr_r34 = "/GTR_R34"
Gtr_r35 = "/GTR_R35"
ms_6th = "/Mustang_6th_gen"
ms_5th = "/Mustang_5th_gen"
lb_aventador = "/Aventador"
lb_huracan = "/Huracan"
lb_veneno = "/Veneno"

nissan_nb_dict = {"/GTR_R35":"https://uk.wikipedia.org/wiki/Nissan_GT-R","/GTR_R34":"https://uk.wikipedia.org/wiki/Nissan_Skyline#R34"}
ford_nb_dict = {"/Mustang_6th_gen":"https://en.wikipedia.org/wiki/Ford_Mustang_(sixth_generation)",
"/Mustang_5th_gen":"https://en.wikipedia.org/wiki/Ford_Mustang_(fifth_generation)"}
lambo_nb_dict = {"/Aventador":"https://ru.wikipedia.org/wiki/Lamborghini_Aventador","/Huracan":"https://ru.wikipedia.org/wiki/Lamborghini_Hurac%C3%A1n","/Veneno":"https://ru.wikipedia.org/wiki/Lamborghini_Veneno"}



GTR_R35_buttons = {"/Объем_двигателя_Скайлайна":"3.8 литра V6","/Годы_выпуска_Скайлайна":"2008-2023","/Коль-во_сидений_Скайлайна":"2 передних и задний ряд,но там места слишком мало,очень тяжело высидеть поездку","/Цена_Скайлайна":" только б/у варианты стоят от $73 тыс долларов,а с завода и с полной комплектацией страшно представить"}
M_6th_buttons = {"/Объем_двигателя_Мустанга":"существует несколько версий v6,а именно:5 литров,3.7 литра и 2.3 литра Ecoboost","/Годы_выпуска_Мустанга":"Июль 2014 - наши дни","/Коль-во_сидений_Мустанга":"спереди 2 места и сзади ряд сидений,при желании можно и вптяером усестся","/Цена_Мустанга":"если брать с салона то цена стартует от $27.770"}
Veneno_buttons = {"/Объем_двигателя_Венено":"6,5 Литров V12","/Годы_выпуска_Венено":"2013 год","/Коль-во_сидений_Венено":"2","/Цена_Венено":"$4,500,000"}


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

def nissan_buttons():
  markup = ReplyKeyboardMarkup()
  V_buton = KeyboardButton("/Объем_двигателя_Скайлайна")
  year_button = KeyboardButton("/Годы_выпуска_Скайлайна")
  seat_button = KeyboardButton("/Коль-во_сидений_Скайлайна")
  price_button = KeyboardButton("/Цена_Скайлайна")
  markup.add(V_buton,year_button)
  markup.add(seat_button,price_button)
  return markup

def ford_buttons():
  markup = ReplyKeyboardMarkup()
  V_buton = KeyboardButton("/Объем_двигателя_Мустанга")
  year_button = KeyboardButton("/Годы_выпуска_Мустанга")
  seat_button = KeyboardButton("/Коль-во_сидений_Мустанга")
  price_button = KeyboardButton("/Цена_Мустанга")
  markup.add(V_buton,year_button)
  markup.add(seat_button,price_button)
  return markup

def lambo_buttons():
  markup = ReplyKeyboardMarkup()
  V_buton = KeyboardButton("/Объем_двигателя_Венено")
  year_button = KeyboardButton("/Годы_выпуска_Венено")
  seat_button = KeyboardButton("/Коль-во_сидений_Венено")
  price_button = KeyboardButton("/Цена_Венено")
  markup.add(V_buton,year_button)
  markup.add(seat_button,price_button)
  return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Привет,про какую машину хочешь узнать?",reply_markup = keyboard_buttons())


@bot.message_handler(commands=['Nissan_wiki'])
def nissan_message(message):
  bot.send_message(message.chat.id,f'Про какую модель хотите узнать?\n{Gtr_r34,Gtr_r35}')

@bot.message_handler(commands=['GTR_R35'])
def GTR_R35(message):
  bot.send_message(message.chat.id,nissan_nb_dict["/GTR_R35"])

@bot.message_handler(commands=['GTR_R34'])
def GTR_R34(message):
  bot.send_message(message.chat.id,nissan_nb_dict["/GTR_R34"])

@bot.message_handler(commands=['Nissan_button'])
def nissan_message(message):
  bot.send_message(message.chat.id,"Модель GTR R35",reply_markup = nissan_buttons())

@bot.message_handler(commands=['Объем_двигателя_Скайлайна'])
def GTR_R35_V(message):
  bot.send_message(message.chat.id,GTR_R35_buttons["/Объем_двигателя_Скайлайна"])

@bot.message_handler(commands=['Годы_выпуска_Скайлайна'])
def GTR_R35_YR(message):
  bot.send_message(message.chat.id,GTR_R35_buttons["/Годы_выпуска_Скайлайна"])

@bot.message_handler(commands=['Коль-во_сидений_Скайлайна'])
def GTR_R35_seats(message):
  bot.send_message(message.chat.id,GTR_R35_buttons["/Коль-во_сидений_Скайлайна"])

@bot.message_handler(commands=['Цена_Скайлайна'])
def GTR_R35_price(message):
  bot.send_message(message.chat.id,GTR_R35_buttons["/Цена_Скайлайна"])

#####################################################################################################################

@bot.message_handler(commands=['Ford_wiki'])
def ford_message(message):
  bot.send_message(message.chat.id,f'Про какую модель хотите узнать?\n{ms_5th,ms_6th}')

@bot.message_handler(commands=['Mustang_6th_gen'])
def M_6th_gen(message):
  bot.send_message(message.chat.id,ford_nb_dict["/Mustang_6th_gen"])

@bot.message_handler(commands=['Mustang_5th_gen'])
def M_5th_gen(message):
  bot.send_message(message.chat.id,ford_nb_dict["/Mustang_5th_gen"])

@bot.message_handler(commands=['Ford_button'])
def ford_message(message):
  bot.send_message(message.chat.id,"Модель Mustang 6th gen",reply_markup = ford_buttons())

@bot.message_handler(commands=['Объем_двигателя_Мустанга'])
def M_6th_V(message):
  bot.send_message(message.chat.id,M_6th_buttons["/Объем_двигателя_Мустанга"])

@bot.message_handler(commands=['Годы_выпуска_Мустанга'])
def M_6th_YR(message):
  bot.send_message(message.chat.id,M_6th_buttons["/Годы_выпуска_Мустанга"])

@bot.message_handler(commands=['Коль-во_сидений_Мустанга'])
def M_6th_seats(message):
  bot.send_message(message.chat.id,M_6th_buttons["/Коль-во_сидений_Мустанга"])

@bot.message_handler(commands=['Цена_Мустанга'])
def M_6th_price(message):
  bot.send_message(message.chat.id,M_6th_buttons["/Цена_Мустанга"])

#####################################################################################################################

@bot.message_handler(commands=['Lamborghini_wiki'])
def lambo_message(message):
  bot.send_message(message.chat.id,f'Про какую модель хотите узнать?\n{lb_aventador,lb_huracan,lb_veneno}')

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
  bot.send_message(message.chat.id,"Модель Lamborghini Veneno",reply_markup = lambo_buttons())

@bot.message_handler(commands=['Объем_двигателя_Венено'])
def Veneno_V(message):
  bot.send_message(message.chat.id,Veneno_buttons["/Объем_двигателя_Венено"])

@bot.message_handler(commands=['Годы_выпуска_Венено'])
def Veneno_YR(message):
  bot.send_message(message.chat.id,Veneno_buttons["/Годы_выпуска_Венено"])

@bot.message_handler(commands=['Коль-во_сидений_Венено'])
def Veneno_seats(message):
  bot.send_message(message.chat.id,Veneno_buttons["/Коль-во_сидений_Венено"])

@bot.message_handler(commands=['Цена_Венено'])
def Veneno_price(message):
  bot.send_message(message.chat.id,Veneno_buttons["/Цена_Венено"])




bot.polling(non_stop=True)