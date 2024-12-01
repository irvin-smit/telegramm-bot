import telebot

bot = telebot.TeleBot('7012335808:AAGVp8SbcFRZ2KQ9HxZn4NWQlmetUJ8fbmI')


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(text="Авторизация на сайте", url="https://drkuznetsovpavel.ru/user/my/profile")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми кнопку для авторизации на сайте:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Авторизация на сайте")
def handle_auth(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    for course in COURSES:
        keyboard.add(telebot.types.KeyboardButton(course[0]))

    bot.send_message(message.chat.id, "Выберите курс из списка:", reply_markup=keyboard)    


@bot.message_handler(func=lambda message: message.text in [course[0] for course in COURSES])
def handle_course(message):
    for course in COURSES:
        if course[0] == message.text:
            course_name, course_link, course_price = course
            keyboard = telebot.types.InlineKeyboardMarkup()
            course_button = telebot.types.InlineKeyboardButton(text="Оплатить", url=course_link)
            keyboard.add(course_button)
            bot.send_message(message.chat.id, f"Название: {course_name}\nСтоимость: {course_price}\nСсылка для оплаты:", reply_markup=keyboard)
            break

COURSES = [('Демо-доступ Сам Себе Тренер','https://drkuznetsovpavel.ru/teach/control/stream/view/id/837258751'),
           ('Сам Себе Тренер', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/837259111', 990),
           ('Сам Себе Тренер(7 Потоков)', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/837290237', 1990),
           ('Сам Себе Тренер Самостоятельное прохождение', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/838104401', 990),
           ('Стопы', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/838104401', 2990),
           ('Ягодицы', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/839495024', 2990),
           ('Поясница', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/840941434', 2990),
           ('Поясница 2.0', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/840941434', 2990),
           ('Грудной, шейный хондроз', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/840740981', 2990),
           ('Практика из курса Грудной. шейный хондроз', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/862539460', 990),
           ('Домашние тренировки+Диета', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/840740976', 2990),
           ('Пресс', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/840740840', 2990),
           ('Персональная диагностика', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/839596284', 3000),
           ('Забудь про боль!', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/841038930', 0),
           ('Стопы курс №1', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/841065554', 0),
           ('Пробные занятия из авторских курсов', 'https://drkuznetsovpavel.ru/teach/control/stream/view/id/846892682', 0),
        ]


bot.polling()
