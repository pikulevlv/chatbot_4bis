from aiogram.types import ContentTypes, ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('/menu')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(button_hi)

inline_btn_1 = InlineKeyboardButton('Узнать статус обращения',
                                    callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Оставить заявку на обратный звонок',
                                    callback_data='button2')
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(inline_btn_2)