import telebot
import random
import time

# Замените 'YOUR_API_TOKEN' на токен вашего бота
bot = telebot.TeleBot('8410098899:AAHR08sPpnuq7JKgIk1zU3ltRK7OlgEQBVs')


# 1. Генератор комплиментов
@bot.message_handler(commands=['комплимент'])
def send_compliment(message):
    nouns = ["котик", "супергерой", "король кода", "мастер Python"]
    adjectives = ["крутой", "невероятный", "гениальный", "очаровательный"]
    phrases = ["Ты просто {0}!", "Как же ты {1}!", "Я в восторге от твоего {0}"]
    compliment = random.choice(phrases).format(random.choice(adjectives), random.choice(nouns))
    bot.send_message(message.chat.id, compliment)


# 2. Калькулятор настроения
@bot.message_handler(commands=['настроение'])
def mood_calculator(message):
    bot.send_message(message.chat.id, "Как настроение? (1–10):")

    @bot.message_handler(func=lambda m: True)
    def handle_mood(message):
        try:
            mood = int(message.text)
            if mood >= 8:
                bot.send_message(message.chat.id, "Ого! Ты просто сияешь 🌟")
            elif mood >= 5:
                bot.send_message(message.chat.id, "Нормалёк! Держи позитивный смайл 😊")
            else:
                bot.send_message(message.chat.id, "Пора взбодриться! 😯 Вот котик для поднятия настроения 🐱")
        except ValueError:
            bot.send_message(message.chat.id, "Пожалуйста, введите число от 1 до 10.")


# 3. Бегущая строка (имитация)
@bot.message_handler(commands=['бегущая'])
def running_text(message):
    text = "Ты — гений кода! 🎉"
    for char in text:
        bot.send_message(message.chat.id, char)
        time.sleep(0.2)


# 4. Шутка с input
@bot.message_handler(commands=['сыр'])
def cheese_joke(message):
    bot.send_message(message.chat.id, "Скажи 'сыр' для фото! 🏞️:")

    @bot.message_handler(func=lambda m: True)
    def handle_cheese(message):
        if message.text.lower() == "сыр":
            bot.send_message(message.chat.id, "📸 Щёлк! Фото готово. Ты — звезда! 🌟")
        else:
            bot.send_message(message.chat.id, "Не сработало! Фотоаппарат обиделся 😤")


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! Я прикольный бот. Попробуй команды:\n/комплимент — получить комплимент\n/настроение — проверить настроение\n/бегущая — бегущая строка\n/сыр — шутка с фото")


# Запуск бота
bot.polling(none_stop=True, interval=0)
