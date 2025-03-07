import telebot
import openai

# Подключаем токены
TELEGRAM_TOKEN = 'тут-вставь-твой-токен-из-BotFather'
OPENAI_API_KEY = 'тут-вставь-API-ключ-из-OpenAI'

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Светлячок — твой цифровой психолог. Напиши мне, как ты себя чувствуешь!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message.text,
            max_tokens=300
        )
        reply = response['choices'][0]['text'].strip()
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "Ой, что-то пошло не так. Попробуй снова!")

bot.polling()
