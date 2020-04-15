from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import Bot_Key

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_fn(bot, update):
    """ГОВОРИМ ЧТОБЫ БОТ НАПИСАЛ ТЕКСТ"""
    update.message.reply_text('Привет, напиши Привет')

    """ГОВОРИМ ЧТОБЫ В ЛОГЕ ПРИ НАЖАТИИ НА КНОПКУ СТАРТ НАПИСАЛО СМС"""
    logging.info('Tap /start')

def talk_to_me(bot, update):
    """ПРИСВАИВАЕМ СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЯ ПЕРЕМЕННОЙ"""
    user_text = update.message.text 

    """ПРИСЫЛАЕМ В ЛОГ ИНФУ О ПОЛЬЗОВАТЕЛЕ"""
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, update.message.chat.id, update.message.text)

    if user_text == 'Привет':
        update.message.reply_text('Пока')
    else:
        update.message.reply_text('Пошел нахуй')

def main() :
    mybot = Updater(Bot_Key.API_KEY)

    logging.info('Bot Startet')

    dp =  mybot.dispatcher
    """СКАЗАЛИ ЧТО У НАС ЕСТЬ КНОПКА СТАРТ И ПРИ НАЖАТИИ ЗАПУСКАЕМ СТАРТ ФН"""
    dp.add_handler(CommandHandler('start', start_fn)) 

    """СКАЗАЛИ ЧТО КОГДА ПРИШЛО СМС ФИЛЬТРУЕМ ЧЕРЕЗ ТОЛК ТУ МИ"""
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) 

    """ЗАХОДИ В ТЕЛЕГРАММ"""
    mybot.start_polling() 
    
    """РАБОТАЙ НЕПРЕРЫВНО"""
    mybot.idle() 
main()
