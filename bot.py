from telebot import telebot, types
from config import TOKEN
from parsing import get_response, parse, parse_objects
# from models import Course


from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,

)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome_message(message):
    text = """Здравствуйте! Здесь вы можете посмотреть все наши курсы ."""
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    course_list = InlineKeyboardButton("Нажмите сюда чтобы посмотреть курсы ", callback_data="course_list")
    markup.add(course_list)
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "course_list")
def course_menu(call):
    text = "СПИСОК КУРСОВ"
    parsing = parse('https://coursive.id/api/v1/courses')
    course_list = f'{text} \n {parsing} klk'
    bot.send_message(call.message.chat.id, course_list)


bot.infinity_polling()

# from telebot import TeleBot, types
#
# # local imports
# from data import TOKEN
#
# from parser import Parsing
#
# from db.models import Course
#
#
# bot = TeleBot(TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def start(message: types.Message):
#     buttons = types.InlineKeyboardMarkup()
#     buttons.add(
#         types.InlineKeyboardButton(
#             'Посмотреть все курсы',
#             callback_data='show_courses',
#         )
#     )
#
#     bot.send_message(message.chat.id, 'Привет!', reply_markup=buttons)
#
#
# @bot.callback_query_handler(lambda c: c.data == 'show_courses')
# def show_course_list(callback: types.CallbackQuery):
#     list_of_data = Parsing().parse()
#     Course.create_from_list(list_of_data)
#
#     text = ''
#     for data in list_of_data:
#         text += data['title'] + '\n'
#
#     bot.send_message(callback.message.chat.id, text)