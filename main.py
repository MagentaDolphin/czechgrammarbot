import telebot
import random
from telebot import types

bot = telebot.TeleBot('5246673155:AAG3hN08mtWUVSStY-uMJMfObPBx4psQhdM');

vzors = [[["pán"], ["pána"], ["pánovi", "pánu"], ["pána"], ["pane"], ["pánovi", "pánu"], ["pánem"]],
         [["muž"], ["muže"], ["mužovi", "mužu"], ["muže"], ["muži"], ["mužovi", "mužu"], ["mužem"]],
         [["předseda"], ["předssedy"], ["předsedovi"], ["předsedu"], ["předsedo"], ["předsedovi"], ["předsedou"]],
         [["soudce"], ["soudce"], ["soudcovi"], ["soudce"], ["soudce"], ["soudcovi"], ["soudcem"]],
         [["hrad"], ["hradu"], ["hradu"], ["hrad"], ["hrade"], ["hradu"], ["hradem"]],
         [["stroj"], ["stroje"], ["stroji"], ["stroj"], ["stroji"], ["stroji"], ["strojem"]],
         [["žena"], ["ženy"], ["ženě"], ["ženu"], ["ženo"], ["ženě"], ["ženou"]],
         [["růže"], ["růže"], ["růží"], ["růže"], ["růže"], ["růži"], ["růží"]],
         [["píseň"], ["písně"], ["písni"], ["píseň"], ["písni"], ["písní"], ["písní"]],
         [["kost"], ["kosti"], ["kosti"], ["kost"], ["kosti"], ["kosti"], ["kostí"]],
         [["město"], ["města"], ["městu"], ["město"], ["město"], ["městu"], ["městem"]],
         [["moře"], ["moře"], ["moři"], ["moře"], ["moře"], ["moři"], ["mořem"]],
         [["kuře"], ["kuřete"], ["kuřeti"], ["kuře"], ["kuře"], ["kuřeti"], ["kuřetem"]],
         [["stavení"], ["stavení"], ["stavení"], ["stavení"], ["stavení"], ["stavení"], ["stavením"]],
         [["páni"], ["pánů"], ["pánům"], ["pány"], ["páni"], ["pánech"], ["pány"]],
         [["muži"], ["mužů"], ["mužům"], ["muže"], ["muži"], ["mužích"], ["muži"]],
         [["předsedové"], ["předsedů"], ["předsedům"], ["předsedy"], ["předsedové"], ["předsedech"], ["předsedy"]],
         [["soudci"], ["soudců"], ["soudcům"], ["soudce"], ["soudci"], ["soudcích"], ["soudci"]],
         [["hrady"], ["hradů"], ["hradům"], ["hrady"], ["hrady"], ["hradech"], ["hrady"]],
         [["stroje"], ["strojů"], ["strojům"], ["stroje"], ["stroje"], ["strojích"], ["stroji"]],
         [["ženy"], ["žen"], ["ženám"], ["ženy"],["ženy"], ["ženách"], ["ženami"]],
         [["růže (pl.)"], ["růží"], ["růžím"], ["růže"], ["růže"], ["růžích"], ["růžemi"]],
         [["písně"], ["písní"], ["písním"], ["písně"], ["písně"], ["písních"], ["písněmi"]],
         [["kosti"], ["kosti"], ["kostem"], ["kosti"], ["kosti"], ["kostech"], ["kostmi"]],
         [["města"], ["měst"], ["městům"], "města", "města", "městech", "městy"],
         [["moře (pl.)"], ["moří"], ["mořím"], ["moře"], ["moře"], ["mořích"], ["moři"]],
         [["kuřata"], ["kuřat"], ["kuřatům"], ["kuřata"], ["kuřata"], ["kuřatech"], ["kuřaty"]],
         [["stavení (pl.)"], ["stavení"], ["stavením"], ["stavení"], ["stavení"], ["staveních"], ["staveními"]]]



padList = ["NOMINATIV", "GENITIV", "DATIV", "AKUZATIV", "VOKATIV", "LOKÁL", "INSTRUMENTÁL"]

vzorNum = int()

padNum = int()


def MessageVzor(message):

    def CheckVzor(message):
        print("For User: ", message.from_user.id, "Task: ",
              str(str(vzors[vzorNum][0]) + " in pad: " + str(padList[padNum])), " Correct: ",
              vzors[vzorNum][padNum])

        if message.text == "/stop":
            bot.send_message(message.from_user.id, str("Correct:\n" + " nebo ".join(vzors[vzorNum][0])))
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["/vzor", "/help"]
            keyboard.add(*buttons)
            bot.send_message(message.from_user.id, "Co chtete?", reply_markup=keyboard)
            return

        if message.text == "/skip":
            MessageVzor(message)
            return

        if message.text.lower().strip() in (vzors[vzorNum][padNum]):
            bot.send_message(message.from_user.id, "Correct!")
            print("User: ", message.from_user.id, " Print: ", message.text, " Result: Correct")
            MessageVzor(message)

        else:
            bot.send_message(message.from_user.id, "Incorrect!" + "\n" + "Try Again!")
            bot.register_next_step_handler(message, CheckVzor)
            print("User: ", message.from_user.id, " Print: ", message.text, " Result:  Not Correct")



    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/stop", "/skip"]
    keyboard.add(*buttons)
    vzorNum = random.randrange(0, 27)
    padNum = random.randrange(1, 6)

    bot.send_message(message.from_user.id,
                     str("Print vzor: \n" + " nebo ".join(vzors[vzorNum][0]) + "\n in pad: \n" + str(padList[padNum])), reply_markup=keyboard)
    bot.register_next_step_handler(message, CheckVzor)


@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    print(message.text, "\n", message.from_user.first_name, message.from_user.last_name, "(", message.from_user.id, ")")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/vzor", "/help"]
    keyboard.add(*buttons)

    if message.text == "/vzor":
        MessageVzor(message)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, " 1) /vzor pro opakovani padu" + "\n" + "2) ...")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Hello world)!", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Nemuzu pochopit. Pokusi se napsat /help.", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)

