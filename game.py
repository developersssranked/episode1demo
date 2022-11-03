import telebot
from telebot import types
bot = telebot.TeleBot("5693058882:AAFh8E8dLgZeqCmvcqQeaPPR_DSugFlcCqU")

inventory = []


@bot.message_handler(commands=['start'])
def start(message):
    inventory.clear()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать")
    markup.add(btn1)
    mes = bot.send_message(
        message.chat.id, "Хотите начать игру", reply_markup=markup)
    bot.register_next_step_handler(mes, epiz1)


bot.message_handler(content_types=["text"])


def epiz1(message):
    mrk1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrk1.add(types.KeyboardButton("встать и осмотреться"),
             types.KeyboardButton("осмотреться не вставая"))
    mes = bot.send_message(
        message.chat.id, "вы просыпаетесь в темной комнате, лежа на полу", reply_markup=mrk1)

    bot.register_next_step_handler(mes, walk)


def walk(message):
    if message.text == "встать и осмотреться":
        mrk1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk1.add(types.KeyboardButton("Кровать"), types.KeyboardButton(
            "Шкаф"), types.KeyboardButton("Тумбочка"), types.KeyboardButton("Дверь"))
        mes = bot.send_message(
            message.chat.id, "Вы осматриваете темную комнату.В ней вы видите: кровать, шкаф, дверь, тумбочка. выберите что хотите осмотреть", reply_markup=mrk1)

        bot.register_next_step_handler(mes, choise)

    elif message.text == "осмотреться не вставая":
        mrk1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk1.add(types.KeyboardButton("Кровать"), types.KeyboardButton(
            "Шкаф"), types.KeyboardButton("Тумбочка"), types.KeyboardButton("Дверь"))
        mes = bot.send_message(
            message.chat.id, "вы лежа осматриваете темную комнату.В ней вы видите: кровать, шкаф, дверь, тумбочка. выберите что хотите осмотреть", reply_markup=mrk1)

        bot.register_next_step_handler(mes, choise)
    else:
        mrk1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mrk1.add(types.KeyboardButton("Кровать"), types.KeyboardButton(
            "Шкаф"), types.KeyboardButton("Тумбочка"), types.KeyboardButton("Дверь"))
        mes = bot.send_message(
            message.chat.id, "выберите то  что хотите просмотреть", reply_markup=mrk1)

        bot.register_next_step_handler(mes, choise)


def choise(message):
    if "Кровать" == message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("дальше")
        markup.add(btn1)
        mess = bot.send_message(
            message.chat.id, "Вы идете к кровати", reply_markup=markup)

        bot.register_next_step_handler(mess, bed)
    elif "Дверь" == message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("дальше")
        markup.add(btn1)
        mess = bot.send_message(
            message.chat.id, "Вы идете к двери", reply_markup=markup)

        bot.register_next_step_handler(mess, door)
    elif "Тумбочка" == message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("дальше")
        markup.add(btn1)
        mess = bot.send_message(
            message.chat.id, "Вы идете к тумбочке", reply_markup=markup)

        bot.register_next_step_handler(mess, box)
    elif "Шкаф" == message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("дальше")
        markup.add(btn1)
        mess = bot.send_message(
            message.chat.id, "Вы идете к Шкафу", reply_markup=markup)

        bot.register_next_step_handler(mess, shelf)


def door(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("вернуться к выбору")
    markup.add(btn1)
    if "Ключ" in inventory:
        bot.send_message(message.chat.id, "Вы успешно выбрались из комнаты")
    else:
        mess = bot.send_message(
            message.chat.id, "Осмотрев дверь вы понимаете, что она закрыта на ключ", reply_markup=markup)
        bot.register_next_step_handler(mess, walk)


def shelf(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("вернуться к выбору")
    markup.add(btn1)
    inventory.append("Молоток")
    mess = bot.send_message(
        message.chat.id, "Осмотрев шкаф вы находите там кучу одежды и молоток. Вы забираете молоток", reply_markup=markup)
    bot.register_next_step_handler(mess, walk)


def bed(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("вернуться к выбору")
    markup.add(btn1)
    mes = bot.send_message(
        message.chat.id, "просто обычная старая кровать, простыня которой пропитанна ужасным запахом", reply_markup=markup)
    bot.register_next_step_handler(mes, walk)


def box(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("вернуться к выбору")
    markup.add(btn1)
    if "Молоток" in inventory:
        inventory.append("Ключ")
        mess = bot.send_message(
            message.chat.id, "Вы открываете тумбочку и находите там ключ", reply_markup=markup)
        bot.register_next_step_handler(mess, walk)
    else:
        mess = bot.send_message(
            message.chat.id, "Тумбочка оказывается закрытой, нужно ее чем то выломать", reply_markup=markup)
        bot.register_next_step_handler(mess, walk)


bot.infinity_polling()
