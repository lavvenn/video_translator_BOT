#подключение aiogram
from aiogram import  Router, F      
from aiogram.types import Message

#подключение переводчика

import argostranslate.package
import argostranslate.translate

from_code = "ru"
to_code = "en"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())
                  

#создание обекта класса Router
router = Router()

#подключение клавиатур
import app.keybords as kb

#функция обновления спска сообщений для GPT3.5
def update(messages, role, content):                            
    messages.append({'role': role, 'content': content})
    return messages

def list_to_str(list):
    output_str = ''
    for i in range(0,len(list)) :
          output_str = output_str + str(i + 1) + '.' + ' ' + list[i] + ' '
    return output_str
    



vac_list = ['HR menger','frontend developer']


#handler команды  "start"
@router.message(F.text == '/start')                             
async def start_comand(message: Message):
    await message.answer("""
BOT is STARTED
""", reply_markup= kb.user_main)
   

@router.message(F.text == "H2")
async def vac(message: Message):
        await message.answer(f"""
TEXT               
                             """)

#handler команды  "/help"
@router.message(F.text == 'H2')
async def help_comand(message: Message):
    await message.answer(
        """
TEXT
"""
    )

#handler который принемает все сообщения и возврощяет ответ от переводчика
@router.message()                                              
async def all_message(message: Message):

    print (f'имя пользователя : {message.from_user.first_name}')
    print(f'написал : {message.text}')

    output = argostranslate.translate.translate(message.text, from_code, to_code)

    print(output)

    await message.answer(output)