import telebot
import random
from telebot import types

#bot = telebot.TeleBot('5246673155:AAG3hN08mtWUVSStY-uMJMfObPBx4psQhdM')
bot = telebot.TeleBot('5288395945:AAFLWZLrcqIHrbjM-wwdgxL1F4zLegwgs6g')

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
         [["ženy"], ["žen"], ["ženám"], ["ženy"], ["ženy"], ["ženách"], ["ženami"]],
         [["růže (pl.)"], ["růží"], ["růžím"], ["růže"], ["růže"], ["růžích"], ["růžemi"]],
         [["písně"], ["písní"], ["písním"], ["písně"], ["písně"], ["písních"], ["písněmi"]],
         [["kosti"], ["kosti"], ["kostem"], ["kosti"], ["kosti"], ["kostech"], ["kostmi"]],
         [["města"], ["měst"], ["městům"], "města", "města", "městech", "městy"],
         [["moře (pl.)"], ["moří"], ["mořím"], ["moře"], ["moře"], ["mořích"], ["moři"]],
         [["kuřata"], ["kuřat"], ["kuřatům"], ["kuřata"], ["kuřata"], ["kuřatech"], ["kuřaty"]],
         [["stavení (pl.)"], ["stavení"], ["stavením"], ["stavení"], ["stavení"], ["staveních"], ["staveními"]]]

adjektiv = [[["mladý (m.a.) (sg.)"], ["mladého"], ["mladému"], ["mladého"], ["mladý"], ["mladém"], ["mladým"]],
         [["mladý (m.i.) (sg.)"], ["mladého"], ["mladému"], ["mladý"], ["mladý"], ["mladém"], ["mladým"]],
         [["mladá (f) (sg.)"], ["mladé"], ["mladé"], ["mladou"], ["mladá"], ["mladé"], ["mladou"]],
         [["mladé (n) (sg.)"], ["mladého"], ["mladému"], ["mladé"], ["mladé"], ["mladém"], ["mladým"]],
         [["jarní (m.a.) (sg.)"], ["jarního"], ["jarnímu"], ["jarního"], ["jarní"], ["jarním"], ["jarním"]],
         [["jarní (m.i.) (sg.)"], ["jarního"], ["jarnímu"], ["jarní"], ["jarní"], ["jarním"], ["jarním"]],
         [["jarní (f) (sg.)"], ["jarní"], ["jarní"], ["jarní"], ["jarní"], ["jarní"], ["jarní"]],
         [["jarní (n) (sg.)"], ["jarního"], ["jarnímu"], ["jarní"], ["jarní"], ["jarním"], ["jarním"]],
         [["mladí (m.a.) (pl.)"], ["mladých"], ["mladým"], ["mladé"], ["mladí"], ["mladých"], ["mladými"]],
         [["mladé (m.i.) (pl.)"], ["mladých"], ["mladým"], ["mladé"], ["mladé"], ["mladých"], ["mladými"]],
         [["mladé (f) (pl.)"], ["mladých"], ["mladým"], ["mladé"], ["mladé"], ["mladých"], ["mladými"]],
         [["mladá (n) (pl.)"], ["mladých"], ["mladým"], ["mladá"], ["mladá"], ["mladých"], ["mladými"]],
         [["jarní (m.a.) (pl.)"], ["jarních"], ["jarním"], ["jarní"], ["jarní"], ["jarních"], ["jarními"]],
         [["jarní (m.i.) (pl.)"], ["jarních"], ["jarním"], ["jarní"], ["jarní"], ["jarních"], ["jarními"]],
         [["jarní (f) (pl.)"], ["jarních"], ["jarním"], ["jarní"], ["jarní"], ["jarních"], ["jarními"]],
         [["jarní (n) (pl.)"], ["jarních"], ["jarním"], ["jarní"], ["jarní"], ["jarních"], ["jarními"]]]


padList = ["NOMINATIV", "GENITIV", "DATIV", "AKUZATIV", "VOKATIV", "LOKÁL", "INSTRUMENTÁL"]

vzorNum = int()

padNum = int()


def MessageVzor(message, vzor: vzors):

    def CheckVzor(message):
        print("For User: ", message.from_user.id, "Task: ",
              str(str(vzor[vzorNum][0]) + " in pad: " + str(padList[padNum])), " Correct: ",
              vzor[vzorNum][padNum])

        if message.text == "/stop":
            bot.send_message(message.from_user.id, str("Correct:\n" + " nebo ".join(vzor[vzorNum][padNum])))
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["/vzor", "/help"]
            keyboard.add(*buttons)
            bot.send_message(message.from_user.id, "Co chtete?", reply_markup=keyboard)
            return

        if message.text == "/skip":
            MessageVzor(message, vzor)
            return

        if message.text.lower().strip() in (vzor[vzorNum][padNum]):
            bot.send_message(message.from_user.id, "Correct!")
            print("User: ", message.from_user.id, " Print: ", message.text, " Result: Correct")
            MessageVzor(message, vzor)

        else:
            bot.send_message(message.from_user.id, "Incorrect!" + "\n" + "Try Again!")
            bot.register_next_step_handler(message, CheckVzor)
            print("User: ", message.from_user.id, " Print: ", message.text, " Result:  Not Correct")



    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/stop", "/skip"]
    keyboard.add(*buttons)
    vzorNum = random.randrange(0, len(vzor))
    padNum = random.randrange(1, 6)

    bot.send_message(message.from_user.id,
                     str("Print vzor: \n" + " nebo ".join(vzor[vzorNum][0]) + "\n in pad: \n" + str(padList[padNum])), reply_markup=keyboard)
    bot.register_next_step_handler(message, CheckVzor)

def CheangeVzorVariant(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Substantiv", "Adjektiv", "Zajmeny"]
    keyboard.add(*buttons)
    bot.send_message(message.from_user.id, "Vyberte jednu z možností", reply_markup=keyboard)
    bot.register_next_step_handler(message, GetVzorVarriant)


def GetVzorVarriant(message):
    if message.text == "Substantiv":
        MessageVzor(message, vzors)
    elif message.text == "Adjektiv":
        MessageVzor(message, adjektiv)
  #  elif message.text == "Zajmeny":
   #     MessageVzor(message, zaymeny)
    else:
        return



@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    print(message.text, "\n", message.from_user.first_name, message.from_user.last_name, "(", message.from_user.id, ")")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/vzor", "/help"]
    keyboard.add(*buttons)

    if message.text == "/vzor":
        CheangeVzorVariant(message)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, " 1) /vzor pro opakovani padu" + "\n" + "2) ...")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Co chtete?", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Nemuzu pochopit. Pokusite se napsat /help.", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)

