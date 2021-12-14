import time
import telebot
from core import token
from crud import crud_user, crud_medicine
from models.user import User
from schemas.medicine import MedicineCreate
from services import UserService
import json

user_service = UserService()
bot = telebot.TeleBot(token)
user_logged = User


@bot.message_handler(commands=["start"])
def greet(message):
    msg = f""" Hello, welcome to my bot, you're not welcome {message.chat.first_name}. \n - To add new user: /add """
    bot.reply_to(message, msg)


@bot.message_handler(commands=["add"])
def add(message):
    user = User(name=message.chat.first_name, chat_id=message.chat.id)
    try:
        user_service.create_user(user)
        bot.reply_to(message, "Ok")
    except Exception as exc:
        bot.reply_to(message, exc.args)


@bot.message_handler(commands=["get_user"])
def get(message):
    try:
        value = user_service.get_user_by_id(message.chat.id)
        bot.send_message(message.chat.id, value.__str__())
    except Exception as exc:
        bot.send_message(message.chat.id, exc.args)


@bot.message_handler(commands=["get_user_medicine"])
def get_medicine(message):
    try:
        value = user_service.get_user_medicines(message.chat.id)
        bot.send_message(message.chat.id, value)
    except Exception as exc:
        bot.send_message(message.chat.id, exc.args)


@bot.message_handler(commands=["create_user_medicine"])
def create_medicine(message):
    try:
        txt = (message.text).replace("/create_user_medicine", "").replace(" ", "")
        med = json.loads(txt)
        medicine = MedicineCreate(name=med["name"], dosage=med["dosage"])
        value = crud_medicine.create(medicine)
        bot.send_message(message.chat.id, value)
    except Exception as exc:
        bot.send_message(message.chat.id, exc.args)
        bot.send_message(message.chat.id, "Use the following model:")
        m = MedicineCreate(name="Name Here", dosage="""[{"time":"10:00"}]""")
        bot.send_message(message.chat.id, m.json())
    # bot.register_next_step_handler(message, create_m(message))


@bot.message_handler(commands=["teste"])
def teste(message):
    v = True
    while v:
        time.sleep(5)

        def t(message):
            if message.text:
                v = False
                bot.send_message(message.chat.id, "V false")

    bot.send_message(message.chat.id, "Saiu loop")


@bot.message_handler(commands=["get_user_agenda"])
def get_agenda(message):
    try:
        value = user_service.get_user_agenda(message.chat.id)
        bot.send_message(message.chat.id, value)
    except Exception as exc:
        bot.send_message(message.chat.id, exc.args)


def main():
    bot.polling()


if __name__ == "__main__":
    main()
