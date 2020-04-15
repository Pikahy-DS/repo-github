import telebot
import config
import random
from telebot import types, TeleBot
import datetime
import COVID19Py
import pyowm
bot: TeleBot = telebot.TeleBot(config.TOKEN)
owm = pyowm.OWM(config.TOKEN2, language = "ru")
covid19 = COVID19Py.COVID19()
smiles = [
	'❤','😘','😂','☺','😳','😚','😅','🙊','😐','😋','😆','😃','🤣','😍','🥰','😘','😝','🧐','🤬','😡','🤯'
]
hello = [
	'Good morning', 'Good evening, i"m the dispatcher ', 'Good night', 'You are welcome', 'Thanks', 'Доброе утро', 'Hello', 'Hi', 'Привет','Добрый вечер, я диспетчер'
]
@bot.message_handler(commands = ['start'])
def welcome(message):

    #keybroad
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("🤒 COVID19")
    item3 = types.KeyboardButton('♠ Игра')
    item5 = types.KeyboardButton('🕰 Время')
    item4 = types.KeyboardButton('📓 Расписание пар')
    item6 = types.KeyboardButton('⛅️Погода')
    markup.add(item1, item2, item3)
    markup.add(item4,item5,item6)
    bot.send_message(message.chat.id,
                     f"{random.choice(hello)}" + ", {0.first_name}!\nЯ - <b>{1.first_name}</b>, а ты нет, бот созданный чтобы упростить тебе жизнь ".format(
                         message.from_user, bot.get_me()) + f"{random.choice(smiles)}",
                     parse_mode='html', reply_markup = markup)
    print(message.from_user)
@bot.callback_query_handler(func = lambda call: True) #Отвечает за виртуальные кнопки
def callback_woker(call):
	try:
	    if call.data == 'yes':
	        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True )
	        item1 = types.KeyboardButton("Да ")
	        item2 = types.KeyboardButton("Нет")
	        markup.add(item1, item2)
	        bot.send_message(call.message.chat.id, 'А я доверяю тебе 😏')
	        bot.send_message(call.message.chat.id, 'Ты приготовился к игре? 😈 ', reply_markup = markup )
	    elif call.data == 'no':
	        bot.send_message(call.message.chat.id, 'И Я ТЕБЕ НЕ ДОВЕРЯЮ')
	    elif call.data == 'one':
	        bot.send_message(call.message.chat.id, 'И так, у тебя ровно одна попытка')
	    elif call.data == 'two':
	        bot.send_message(call.message.chat.id, 'И так, у тебя ровно две попытки')
	    elif call.data == 'Russia':
	        location = covid19.getLocationByCountryCode("RU")
	        date = location[0]['last_updated'].split('T')
	        time = date[1].split(".")
	        final_message = f"<u>Данные по стране Россия:</u>\nНаселение: {location[0]['country_population']:,}\n" \
	                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
	                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
	                        f"{location[0]['latest']['deaths']:,}"
	        bot.send_message(call.message.chat.id, final_message, parse_mode='html')
	    elif call.data == 'Usa':
	        location = covid19.getLocationByCountryCode("US")
	        date = location[0]['last_updated'].split('T')
	        time = date[1].split(".")
	        final_message = f"<u>Данные по стране США:</u>\nНаселение: {location[0]['country_population']:,}\n"\
	                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>"\
	                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
	                        f"{location[0]['latest']['deaths']:,}"
	        bot.send_message(call.message.chat.id, final_message, parse_mode='html')

	    elif call.data == 'Ukraine':
	        location = covid19.getLocationByCountryCode("UA")
	        date = location[0]['last_updated'].split('T')
	        time = date[1].split(".")
	        final_message = f"<u>Данные по стране Украина:</u>\nНаселение: {location[0]['country_population']:,}\n" \
	                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
	                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
	                        f"{location[0]['latest']['deaths']:,}"
	        bot.send_message(call.message.chat.id, final_message, parse_mode='html')
	    elif call.data == 'All':
	        location = covid19.getLatest()
	        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"
	        bot.send_message(call.message.chat.id, final_message, parse_mode = 'html')

	    elif call.data == 'Numerator':

	        keyboard = types.InlineKeyboardMarkup()
	        Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='Monday')
	        keyboard.add(Monday)
	        Tuesday = types.InlineKeyboardButton(text="Вторник", callback_data='Tuesday')
	        keyboard.add(Tuesday)
	        Wednesday = types.InlineKeyboardButton(text="Среда", callback_data='Wednesday')
	        keyboard.add(Wednesday)
	        Thursday = types.InlineKeyboardButton(text="Четверг", callback_data='Thursday')
	        keyboard.add(Thursday)
	        Friday = types.InlineKeyboardButton(text="Пятница", callback_data='Friday')
	        keyboard.add(Friday)
	        bot.send_message(call.message.chat.id, "Выбери день недели: ", reply_markup = keyboard)
	        #bot.edit_message_reply_markup(call.message.chat.id, message_id = call.message.message_id-1, reply_markup = '')
	        # remove inline buttons

	       # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
	        #                          text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
	    elif call.data == 'Monday':
	        bot.send_message(call.message.chat.id, 'Понедельник - Числитель \n1 пара: ТАУ (Практика) \n2 пара: ФИЗ - РА \n3 пара: Электротехника (Лекция) ')
	    elif call.data == 'Tuesday':
	        bot.send_message(call.message.chat.id, 'Вторник - Числитель \n1 пара: Алгоритмизация и программирование (Лекция) \n2 пара: Электробезопасность (Лекция) \n3 пара: Электротехика (Курсовая) ')
	    elif call.data == 'Wednesday':
	        bot.send_message(call.message.chat.id, 'Среда - Числитель \n1 пара: ТАУ (Лекция) \n2 пара: ТАУ (Лабораторная) \n  ')
	    elif call.data == 'Thursday':
	        bot.send_message(call.message.chat.id, 'Четверг - Числитель \n1 пара: Электроника (Лекция) \n2 пара: Прикладная Механика (Лекция) \n  ')
	    elif call.data == 'Friday':
	        bot.send_message(call.message.chat.id, 'Пятница - Числитель \n1 пара: Электроника (Лабораторная) \n2 пара: Базы Данных (Лабораторная) \n3 пара: Электротехника (Практика) ')
	    elif call.data == 'Monday1':
	        bot.send_message(call.message.chat.id,  'Понедельник - Знаменатель \n2 пара: ФИЗ - РА \n3 пара: Электротехника (Лекция) ')
	    elif call.data == 'Tuesday1':
	        bot.send_message(call.message.chat.id, 'Вторник - Знаменатель \n1 пара: Алгоритмизация и программирование (Практика) \n2 пара: Электробезопасность (Пратика) \n3 пара: Электротехника (Курсовая) ')
	    elif call.data == 'Wednesday1':
	        bot.send_message(call.message.chat.id, 'Среда - Знаменатель \n1 пара: Датчики (Лекция) \n2 пара: Датчики (Практика) \n3 пара: Электротехника (Лабораторная) ')
	    elif call.data == 'Thursday1':
	        bot.send_message(call.message.chat.id, 'Четверг - Знаменатель \n1 пара: Электроника (Лекция) \n2 пара: Прикладная Механика (Лекция) \n 3 пара: Прикладная Механика (Практика)')
	    elif call.data == 'Friday1':
	      	bot.send_message(call.message.chat.id, 'Пятница - Знаменатель \n1 пара: Алгоритмизция и программирование (Лабораторная) \n2 пара: Базы Данных (Лабораторная) \n3 пара: Базы Данных (Лекция) ')
	    elif call.data == 'Denominator':

	        keyboard = types.InlineKeyboardMarkup()
	        Monday1 = types.InlineKeyboardButton(text='Понедельник', callback_data='Monday1')
	        keyboard.add(Monday1)
	        Tuesday1 = types.InlineKeyboardButton(text="Вторник", callback_data='Tuesday1')
	        keyboard.add(Tuesday1)
	        Wednesday1 = types.InlineKeyboardButton(text="Среда", callback_data='Wednesday1')
	        keyboard.add(Wednesday1)
	        Thursday1 = types.InlineKeyboardButton(text="Четверг", callback_data='Thursday1')
	        keyboard.add(Thursday1)
	        Friday1 = types.InlineKeyboardButton(text="Пятница", callback_data='Friday1')
	        keyboard.add(Friday1)
	        bot.send_message(call.message.chat.id, 'Выбери день недели: ', reply_markup=keyboard)

	    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= call.message.text,
                          reply_markup='')
	except Exception:
		bot.edit_message_text(call.message.chat.id, 'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')
@bot.message_handler(content_types = ['text'])
def main(message): #Отвечает за кнопки на клавиатуре
	try:
	    if message.chat.type == 'private':
	        if message.text == '🎲 Рандомное число':
	            bot.send_message(message.chat.id, str(random.randint(0,100)))
	        elif message.text == '♠ Игра':
	            keyboard = types.InlineKeyboardMarkup()
	            key_yes = types.InlineKeyboardButton(text=' Да', callback_data='yes')
	            keyboard.add(key_yes)
	            key_no = types.InlineKeyboardButton(text="Нет", callback_data='no')
	            keyboard.add(key_no)
	            bot.send_message(message.chat.id, 'Ты доверяешь мне?', reply_markup = keyboard)
	        elif message.text == 'Нет':
	            bot.register_next_step_handler(message, welcome)
	            bot.send_message(message.chat.id, 'Напиши любое сообщение')
	        elif message.text == 'Да':
	            keyboard = types.InlineKeyboardMarkup()
	            key_yes = types.InlineKeyboardButton(text='Бесконечность не предел (-♾: ♾+)', callback_data='one')
	            keyboard.add(key_yes)
	            key_no = types.InlineKeyboardButton(text="Попытки стремятся к нулю 🔜", callback_data='two')
	            keyboard.add(key_no)
	            bot.send_message(message.chat.id, 'Как ты думаешь, сколько у тебя попыток?) 🙀 ', reply_markup=keyboard)
	        elif message.text == '📓 Расписание пар':
	            keyboard = types.InlineKeyboardMarkup()
	            key_yes = types.InlineKeyboardButton(text='Числитель', callback_data='Numerator')
	            keyboard.add(key_yes)
	            key_no = types.InlineKeyboardButton(text="Знаменатель", callback_data='Denominator')
	            keyboard.add(key_no)
	            bot.send_message(message.chat.id, 'Числитель или Знаменатель?', reply_markup=keyboard)
	        elif message.text == '🕰 Время':
	            date2 = datetime.datetime(2020, 6, 1)
	            ic = datetime.datetime.now().isocalendar()
	            b = 'Числитель' if ic[1] % 2 != 0 else 'Знаменатель'
	            date_time = datetime.datetime.now(tz = None)
	            date_t = date2 - date_time
	            bot.reply_to(message, "Сейчас:  " + date_time.strftime("%d-%m-%Y %H:%M") + f"- {b}" + f"\nДо сессии: {str(date_t.days)} дней")
	            #bot.reply_to(message, f"До сессии: {str(date_t.days)} дней\nСейчас: {b}")
	        elif message.text == "🤒 COVID19":
	            keyboard = types.InlineKeyboardMarkup()
	            key_yes = types.InlineKeyboardButton(text='Россия', callback_data='Russia')
	            keyboard.add(key_yes)
	            key_no = types.InlineKeyboardButton(text="США", callback_data='Usa')
	            keyboard.add(key_no)
	            key_go = types.InlineKeyboardButton(text="Украина", callback_data='Ukraine')
	            keyboard.add(key_go)
	            key_mo = types.InlineKeyboardButton(text="Во всем мире", callback_data='All')
	            keyboard.add(key_mo)
	            bot.send_message(message.chat.id, 'По какой стране вывести информацию?', reply_markup=keyboard)
	        elif message.text == '⛅️Погода':
	        	observation = owm.weather_at_place('Старый Оскол')
	        	w = observation.get_weather()
	        	temp = w.get_temperature('celsius')['temp']
	        	clothes = 'Одевайся теплее' if temp < 20 else 'Надевай легкую одежду'
	        	bot.send_message(message.chat.id, 'На улице сейчас ' + w.get_detailed_status() + '\nТемпература сейчас в районе '+ str(int(temp)) + ' °C\n' + clothes)
	        else:
	            bot.send_message(message.chat.id, f'Я не знаю, что ответить {random.choice(smiles)}')

	except Exception:
		bot.send_message(message.chat.id, 'Это что еще за покемон?\nОшибка на сервер, сейчас кабанчики подскочат и порешают!')
# def games(message):
#     bot.send_message(message.chat.id, 'Hello')
#     bot.register_next_step_handler(message, welcome)

bot.polling(none_stop = True)
 