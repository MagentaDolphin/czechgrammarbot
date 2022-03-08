import telebot
import random
from telebot import types

#bot = telebot.TeleBot('5246673155:AAG3hN08mtWUVSStY-uMJMfObPBx4psQhdM')
bot = telebot.TeleBot('5288395945:AAFLWZLrcqIHrbjM-wwdgxL1F4zLegwgs6g')

vzors = [[["pán (sg.)"], ["pána"], ["pánovi", "pánu"], ["pána"], ["pane"], ["pánovi", "pánu"], ["pánem"]],
         [["muž (sg.)"], ["muže"], ["mužovi", "mužu"], ["muže"], ["muži"], ["mužovi", "mužu"], ["mužem"]],
         [["předseda (sg.)"], ["předssedy"], ["předsedovi"], ["předsedu"], ["předsedo"], ["předsedovi"], ["předsedou"]],
         [["soudce (sg.)"], ["soudce"], ["soudcovi"], ["soudce"], ["soudce"], ["soudcovi"], ["soudcem"]],
         [["hrad (sg.)"], ["hradu"], ["hradu"], ["hrad"], ["hrade"], ["hradu"], ["hradem"]],
         [["stroj (sg.)"], ["stroje"], ["stroji"], ["stroj"], ["stroji"], ["stroji"], ["strojem"]],
         [["žena (sg.)"], ["ženy"], ["ženě"], ["ženu"], ["ženo"], ["ženě"], ["ženou"]],
         [["růže (sg.)"], ["růže"], ["růží"], ["růže"], ["růže"], ["růži"], ["růží"]],
         [["píseň (sg.)"], ["písně"], ["písni"], ["píseň"], ["písni"], ["písní"], ["písní"]],
         [["kost (sg.)"], ["kosti"], ["kosti"], ["kost"], ["kosti"], ["kosti"], ["kostí"]],
         [["město (sg.)"], ["města"], ["městu"], ["město"], ["město"], ["městu"], ["městem"]],
         [["moře (sg.)"], ["moře"], ["moři"], ["moře"], ["moře"], ["moři"], ["mořem"]],
         [["kuře (sg.)"], ["kuřete"], ["kuřeti"], ["kuře"], ["kuře"], ["kuřeti"], ["kuřetem"]],
         [["stavení (sg.)"], ["stavení"], ["stavení"], ["stavení"], ["stavení"], ["stavení"], ["stavením"]],
         [["páni (pl.)"], ["pánů"], ["pánům"], ["pány"], ["páni"], ["pánech"], ["pány"]],
         [["muži (pl.)"], ["mužů"], ["mužům"], ["muže"], ["muži"], ["mužích"], ["muži"]],
         [["předsedové (pl.)"], ["předsedů"], ["předsedům"], ["předsedy"], ["předsedové"], ["předsedech"], ["předsedy"]],
         [["soudci (pl.)"], ["soudců"], ["soudcům"], ["soudce"], ["soudci"], ["soudcích"], ["soudci"]],
         [["hrady (pl.)"], ["hradů"], ["hradům"], ["hrady"], ["hrady"], ["hradech"], ["hrady"]],
         [["stroje (pl.)"], ["strojů"], ["strojům"], ["stroje"], ["stroje"], ["strojích"], ["stroji"]],
         [["ženy (pl.)"], ["žen"], ["ženám"], ["ženy"], ["ženy"], ["ženách"], ["ženami"]],
         [["růže (pl.)"], ["růží"], ["růžím"], ["růže"], ["růže"], ["růžích"], ["růžemi"]],
         [["písně (pl.)"], ["písní"], ["písním"], ["písně"], ["písně"], ["písních"], ["písněmi"]],
         [["kosti (pl.)"], ["kostí"], ["kostem"], ["kosti"], ["kosti"], ["kostech"], ["kostmi"]],
         [["města (pl.)"], ["měst"], ["městům"], "města", "města", "městech", "městy"],
         [["moře (pl.)"], ["moří"], ["mořím"], ["moře"], ["moře"], ["mořích"], ["moři"]],
         [["kuřata (pl.)"], ["kuřat"], ["kuřatům"], ["kuřata"], ["kuřata"], ["kuřatech"], ["kuřaty"]],
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

##

posesivAdjektiv = [[["otcovo (n) (sg.)"], ["otcova"], ["otcovu"], ["otcovo"], ["otcovo"], ["otcově"], ["otcovým"]],
                  [["otcova (f) (sg.)"], ["otcovy"], ["otcově"], ["otcovu"], ["otcova"], ["otcově"], ["otcovou"]],
                  [["otcův (m.i.) (sg.)"], ["otcova"], ["otcovu"], ["otcův"], ["otcův"], ["otcově"], ["otcovým"]],
                  [["otcův (m.a.) (sg.)"], ["otcova"], ["otcovu"], ["otcova"], ["otcův"], ["otcově"], ["otcovým"]],
                  [["matčino (n) (sg.)"], ["matčina"], ["matčinu"], ["matčino"], ["matčino"], ["matčině"], ["matčiným"]],
                  [["matčina (f) (sg.)"], ["matčiny"], ["matčině"], ["matčinu"], ["matčina"], ["matčině"], ["matčinou"]],
                  [["matčin (m.i.) (sg.)"], ["matčina"], ["matčinu"], ["matčin"], ["matčin"], ["matčině"], ["matčiným"]],
                  [["matčin (m.a.) (sg.)"], ["matčina"], ["matčinu"], ["matčina"], ["matčin"], ["matčině"], ["matčiným"]],
                  [["otcova (n) (pl.)"], ["otcových"], ["otcovým"], ["otcova"], ["otcova"], ["otcových"], ["otcovými"]],
                  [["otcovy (f) (pl.)"], ["otcových"], ["otcovým"], ["otcovy"], ["otcovy"], ["otcových"], ["otcovými"]],
                  [["otcovy (m.i.) (pl.)"], ["otcových"], ["otcovým"], ["otcovy"], ["otcovy"], ["otcových"], ["otcovými"]],
                  [["otcovi (m.a.) (pl.)"], ["otcových"], ["otcovým"], ["otcovy"], ["otcovi"], ["otcových"], ["otcovými"]],
                  [["matčina (n) (pl.)"], ["matčiných"], ["matčiným"], ["matčina"], ["matčina"], ["matčiných"], ["matčinými"]],
                  [["matčiny (f) (pl.)"], ["matčiných"], ["matčiným"], ["matčiny"], ["matčiny"], ["matčiných"], ["matčinými"]],
                  [["matčiny (m.i.) (pl.)"], ["matčiných"], ["matčiným"], ["matčiny"], ["matčiny"], ["matčiných"], ["matčinými"]],
                  [["matčini (m.a.) (pl.)"], ["matčiných"], ["matčiným"], ["matčiny"], ["matčini"], ["matčiných"], ["matčinými"]]]

ukazniZajmeno = [[["ten (sg.) (m)"], ["toho"], ["tomu"], ["toho","ten"], ["NONE"], ["tom"], ["tím"]],
                [["ta (sg.) (f)"], ["té"], ["té"], ["tu"], ["NONE"], ["té"], ["tou"]],
                [["to (sg.) (n)"], ["toho"], ["tomu"], ["to"], ["NONE"], ["tom"], ["tím"]],
                [["tí(ty) (pl.) (m)"], ["těch"], ["těm"], ["ty"], ["NONE"], ["těch"], ["těmi"]],
                [["ty (pl.) (f)"], ["těch"], ["těm"], ["ty"], ["NONE"], ["těch"], ["těmi"]],
                [["ta (pl.) (n)"], ["těch"], ["těm"], ["ta"], ["NONE"], ["těch"], ["těmi"]]]


osobniZajmeno = [[["já (sg.)"], ["mne","mě"], ["mně","mi"], ["mne","mě"], ["NONE"], ["mně"], ["mnou"]],
                [["ty (sg.)"], ["tebe","tě"], ["tobě","ti"], ["tebe","tě"], ["NONE"], ["tobě"], ["tebou"]],
                [["on (sg.)"], ["jeho","ho"], ["jemu","mu"], ["jeho","ho","jej"], ["NONE"], ["něm"], ["jím"]],
                [["ona (sg.)"], ["jí"], ["jí"], ["jí"], ["NONE"], ["ní"], ["jí"]],
                [["ono (sg.)"], ["jeho","ho"], ["jemu","mu"], ["je"], ["NONE"], ["něm"], ["jím"]],
                [["já (pl.)"], ["nás"], ["nám"], ["nás"], ["NONE"], ["nás"], ["námi"]],
                [["ty (pl.)"], ["vás"], ["vám"], ["vás"], ["NONE"], ["vás"], ["vámi"]],
                [["on (pl.)"], ["jich"], ["jim"], ["je"], ["NONE"], ["nich"], ["jimi"]],
                [["ona (pl.)"], ["jich"], ["jim"], ["je"], ["NONE"], ["nich"], ["jimi"]],
                [["ono (pl.)"], ["jich"], ["jim"], ["je"], ["NONE"], ["nich"], ["jimi"]]]

privlastneZajmeno = [[["můj (m) (sg.)"], ["mého"], ["mému"], ["mého","můj"], ["NONE"], ["mém"], ["mým"]],
                    [["moje(má) (f) (sg.)"], ["mé"], ["mé"], ["mou"], ["NONE"], ["mé"], ["mou"]],
                    [["moje(mé) (n) (sg.)"], ["mého"], ["mému"], ["moje","mé"], ["NONE"], ["mém"], ["mým"]],
                    [["náš (m) (sg.)"], ["našeho"], ["našemu"], ["našeho","náš"], ["NONE"], ["našem"], ["naším"]],
                    [["naše (f) (sg.)"], ["naší"], ["naší"], ["naší"], ["NONE"], ["naší"], ["naší"]],
                    [["naše (n) (sg.)"], ["našeho"], ["našemu"], ["naše"], ["NONE"], ["našem"], ["naším"]],
                    [["moji(moje) (m) (pl.)"], ["mých"], ["mým"], ["moje","mé"], ["NONE"], ["mých"], ["mými"]],
                    [["moje(mé) (f) (pl.)"], ["mých"], ["mým"], ["moje","mé"], ["NONE"], ["mých"], ["mými"]],
                    [["moje(mé) (n) (pl.)"], ["mých"], ["mým"], ["moje","mé"], ["NONE"], ["mých"], ["mými"]],
                    [["naši(naše) (m) (pl.)"], ["našich"], ["našim"], ["naše"], ["NONE"], ["našich"], ["našimi"]],
                    [["naše (f) (pl.)"], ["našich"], ["našim"], ["naše"], ["NONE"], ["našich"], ["našimi"]],
                    [["naše (n) (pl.)"], ["našich"], ["našim"], ["naše"], ["NONE"], ["našich"], ["našimi"]]]

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
            bot.send_message(message.from_user.id, str("Correct:\n" + " nebo ".join(vzor[vzorNum][padNum])))
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
    if ["NONE"] in vzor[vzorNum]:
        if random.random() > 0.5:
            padNum = random.randint(5, len(vzor[vzorNum])-1)
        else:
            padNum = random.randint(1, 3)
    else:
        padNum = random.randrange(1, len(vzor[vzorNum])-1)

    bot.send_message(message.from_user.id,
                     str("Print vzor: \n" + " nebo ".join(vzor[vzorNum][0]) + "\n in pad: \n" + str(padList[padNum])), reply_markup=keyboard)
    bot.register_next_step_handler(message, CheckVzor)

def CheangeVzorVariant(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Substantiv", "Adjektiv", "Zajmeny", "Posesiv"]
    keyboard.add(*buttons)
    bot.send_message(message.from_user.id, "Vyberte jednu z možností", reply_markup=keyboard)
    bot.register_next_step_handler(message, GetVzorVarriant)

def CheangeZajmVariant(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Ukazni", "Osobni", "Privlastne"]
    keyboard.add(*buttons)
    bot.send_message(message.from_user.id, "Vyberte jednu z možností", reply_markup=keyboard)
    bot.register_next_step_handler(message, GetZajmVariant)

def GetZajmVariant(message):
    if message.text == "Ukazni":
        MessageVzor(message, ukazniZajmeno)
    elif message.text == "Osobni":
        MessageVzor(message, osobniZajmeno)
    elif message.text == "Privlastne":
        MessageVzor(message, privlastneZajmeno)
    else:
        return


def GetVzorVarriant(message):
    if message.text == "Substantiv":
        MessageVzor(message, vzors)
    elif message.text == "Adjektiv":
        MessageVzor(message, adjektiv)
    elif message.text == "Posesiv":
        MessageVzor(message, posesivAdjektiv)
    elif message.text == "Zajmeny":
        CheangeZajmVariant(message)
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
        bot.send_message(message.from_user.id, " 1) /vzor pro opakovani padu" + "\n" + "2) /stop pro zastavení tréninku" + "\n" + "3) /skip pro přeskočení vzoru")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Co chtete?", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Nemuzu pochopit. Pokusite se napsat /help.", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)

