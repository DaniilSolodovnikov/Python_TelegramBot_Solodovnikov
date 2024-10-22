import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# from main import create_note, read_note, edit_note, delete_note, display_notes, display_sorted_notes

updater = Updater(token="API_TOKEN")


# Создать обработчик для создания заметок create_handler
# def create_note_handler(update, context):
#     try:
#         note_text = update.message.text
#         note_name = update.message.chat_id
#         create_note(note_text, note_name)
#         context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} создана.")
#     except:
#         context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка с созданием заметки.")
#
#
# def read_note_handler(update, context):
#     try:
#         note_text = update.message.text
#         note_name = update.message.chat_id
#         read_note(note_name, note_text)
#         context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} прочитана.")
#     except:
#         context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка с прочтением заметки.")
#
#
# def edit_note_handler(update, context):
#     try:
#         note_text = update.message.text
#         note_name = update.message.chat_id
#         edit_note(note_name, note_text)
#         context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} обновлена.")
#     except:
#         context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка с редактированием заметки.")
#
#
# def delete_note_handler(update, context):
#     try:
#         note_text = update.message.text
#         note_name = update.message.chat_id
#         delete_note(note_name)
#         context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} удалена.")
#     except:
#         context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка с удалением заметки.")
#
#
# def display_notes_handler(update, context):
#     try:
#         note_text = update.message.text
#         note_name = update.message.chat_id
#         display_notes(note_name)
#         context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} удалена.")
#     except:
#         context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка с отображением заметок.")
#
#
# def display_sorted_notes_handler(update, context):
#     try:
#         note_text = update.message.text
#         note_name = update.message.chat_id
#         display_sorted_notes(note_name)
#         context.bot.send_message(chat_id=update.message.chat_id, text=f"Заметка {note_name} удалена.")
#     except:
#         context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка с сортировкой заметок.")


# updater.dispatcher.add_handler(CommandHandler('create', create_note_handler))
# updater.dispatcher.add_handler(CommandHandler('read', read_note_handler))
# updater.dispatcher.add_handler(CommandHandler('edit', edit_note_handler))
# updater.dispatcher.add_handler(CommandHandler('delete', delete_note_handler))
# updater.dispatcher.add_handler(CommandHandler('display', display_notes_handler))
# updater.dispatcher.add_handler(CommandHandler('display_sorted', display_sorted_notes_handler))


updater.start_polling()