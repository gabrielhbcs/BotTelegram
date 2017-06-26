from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
chatId = ''
gruposCopiar = []
gruposColar = []
usuariosComandoPendente = []
boss = 0
ultimoUsuario = 0

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def photoReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    fileId = update.message.photo[0].file_id
    print(fileId)
    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendPhoto(gruposColar[i], fileId)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendPhoto(gruposColar[i], fileId)
            i += 1

def audioReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    fileId = update.message.audio.file_id
    print("audio")
    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendAudio(gruposColar[i], fileId)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendAudio(gruposColar[i], fileId)
            i += 1

def documentReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    fileId = update.message.document.file_id
    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendDocument(gruposColar[i], fileId)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendDocument(gruposColar[i], fileId)
            i += 1

def stickerReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    fileId = update.message.sticker.file_id
    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendSticker(gruposColar[i], fileId)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendSticker(gruposColar[i], fileId)
            i += 1

def videoReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    fileId = update.message.video.file_id

    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendVideo(gruposColar[i], fileId)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendVideo(gruposColar[i], fileId)
            i += 1

def voiceReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    fileId = update.message.voice.file_id
    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendVoice(gruposColar[i], fileId)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendVoice(gruposColar[i], fileId)
            i += 1

def locationReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendLocation(gruposColar[i], latitude, longitude)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendLocation(gruposColar[i], latitude, longitude)
            i += 1

def venueReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    latitude = update.message.venue.location.latitude
    longitude = update.message.venue.location.longitude
    title = update.message.venue.tittle
    endereco = update.message.venue.adress
    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendVenue(gruposColar[i], latitude, longitude, title, endereco)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendVenue(gruposColar[i], latitude, longitude, title, endereco)
            i += 1

def contactReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    chatId = update.message.chat.id
    userId = update.message.from_user.id
    numero = update.message.contact.phone_number
    nome = update.message.contact.first_name
    if (gruposCopiar and gruposColar):
        i = 0
        for grupo in gruposCopiar:
            if chatId == grupo:
                print("Match grupo, copiando")
                if (ultimoUsuario == userId):
                    bot.sendContact(gruposColar[i], numero, nome)
                else:
                    ultimoUsuario = userId
                    msgAux = str.format("*{0} {1}*: ", update.message.from_user.first_name,
                                        update.message.from_user.last_name)
                    bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                    bot.sendContact(gruposColar[i], numero, nome)
            i += 1

def textReceived(bot, update):
    global gruposCopiar
    global gruposColar
    global boss
    global ultimoUsuario

    msg = update.message.text
    chatId = update.message.chat.id
    userId = update.message.from_user.id
    print(str.format("{0}: {1}",update.message.chat.id, msg))
    if(boss != 0):
        if(msg.startswith("!copiar") and userId == boss):
            gruposCopiar.append(chatId)
            #usuariosComandoPendente.append(update.message)
            print("Copiando desse grupo")
        elif(msg.startswith("!colar") and userId == boss):
            gruposColar.append(chatId)
            print("Colando nesse grupo")
        i = 0
        if(gruposCopiar and gruposColar):
            for grupo in gruposCopiar:
                if chatId == grupo:
                    print("Match grupo, copiando")
                    if(ultimoUsuario == userId):
                        bot.sendMessage(gruposColar[i], msg)
                    else:
                        ultimoUsuario = userId
                        msgAux = str.format("*{0} {1}*: {2}", update.message.from_user.first_name, update.message.from_user.last_name, msg)
                        bot.sendMessage(gruposColar[i], msgAux, 'Markdown')
                i += 1
    elif(msg == "boss"):
        boss = userId
        bot.sendMessage(chatId ,"Você agora foi definido como boss")



def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():

    arq = open('token.txt', 'r')
    token = arq.readline()
    arq.close
    print(token)
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    #dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, textReceived))
    dp.add_handler(MessageHandler(Filters.photo, photoReceived))
    dp.add_handler(MessageHandler(Filters.audio, audioReceived))
    dp.add_handler(MessageHandler(Filters.document, documentReceived))
    dp.add_handler(MessageHandler(Filters.sticker, stickerReceived))
    dp.add_handler(MessageHandler(Filters.video, videoReceived))
    dp.add_handler(MessageHandler(Filters.voice, voiceReceived))
    #Video Note?
    dp.add_handler(MessageHandler(Filters.location, locationReceived))
    dp.add_handler(MessageHandler(Filters.venue, venueReceived))
    dp.add_handler(MessageHandler(Filters.contact, contactReceived))
    #Chat Action?

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()