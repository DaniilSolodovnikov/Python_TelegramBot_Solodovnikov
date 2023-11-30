import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token="6737933348:AAGpe7GRoxIDf96aNHUGXP8tVGlithuFjwI")

from main3 import create_note, read_note, edit_note, delete_note


def create_note_handler(update, context):
    try:
        note_text = update.message.text
        note_name = update.message.chat_id
        create_note(note_text, note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} создана.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")


updater.dispatcher.add_handler(CommandHandler('create', create_note_handler))


def read_note_handler(update, context):
    try:
        note_name = update.message.chat_id
        read_note(note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} прочитана.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

updater.dispatcher.add_handler(CommandHandler('read', create_note_handler))


def edit_note_handler(update, context):
    try:
        note_name = update.message.chat_id
        edit_note(note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} обновлена.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

updater.dispatcher.add_handler(CommandHandler('edit', create_note_handler))


def delete_note_handler(update, context):
    try:
        note_name = update.message.chat_id
        delete_note(note_name)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} удалена.")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка.")

updater.dispatcher.add_handler(CommandHandler('delete', create_note_handler))


updater.start_polling()
