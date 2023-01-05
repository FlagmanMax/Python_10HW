from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("hello", command_hello))
app.add_handler(CommandHandler("time", command_time))
app.add_handler(CommandHandler("date", command_date))
app.add_handler(CommandHandler("sum", command_sum))
app.add_handler(CommandHandler("diff", command_diff))
app.add_handler(CommandHandler("mult", command_mult))
app.add_handler(CommandHandler("div", command_div))
app.add_handler(CommandHandler("help", command_help))
# app.add_handler(CommandHandler("sum", command_sum))

print("Server started!")

app.run_polling()