
import telebot

bot = telebot.TeleBot('6372147419:AAFkFTx7bedr29Ts93xLglNZxiLn-ZoGsm8')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Дякую що завітали до наc\n \nВведіть команду /pricelist_pedikur - щоб дізнатися ціни на послуги педикюра\n \nВедіть команду /pricelist_manikur щоб дізнатися ціни на послуги манікюра")

@bot.message_handler(commands=['pricelist_manikur'])
def main(message):
    bot.send_message(message.chat.id, "Стандарнтий манікюр-200грн\n \nМанікюр з покриттям-300грн\n \nКорекція нарощених-350грн\n \nНарощення до 5мм-400грн\n \nНарощення від 6 до 9мм-500грн")

@bot.message_handler(commands=['pricelist_pedikur'])
def main(message):
    bot.send_message(message.chat.id, "Cтандартний педикюр-200грн\n \nПедикюр з покриттям-300грн\n \nПоверхнева чистка п'ят-200грн")

bot.polling(none_stop=True)