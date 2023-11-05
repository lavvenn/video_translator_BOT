from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, inline_keyboard_markup, inline_keyboard_button

user_main_kb= [
    [KeyboardButton(text='H1'),

    ],
    [KeyboardButton(text='H2'),
     
     ]
    
]

user_main = ReplyKeyboardMarkup(keyboard=user_main_kb, resize_keyboard=True, input_field_placeholder='')
