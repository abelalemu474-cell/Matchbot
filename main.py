import json, os
from datetime import date, datetime, timedelta
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ConversationHandler, CallbackQueryHandler, PreCheckoutQueryHandler,
    filters, ContextTypes
)

TOKEN = "8831721287:AAEvHDYsTeDcZS0kzIjvrhrx3WxkjPEeZn4"
BOT_USERNAME = "Jrmatchbot"
DAILY_LIMIT = 30
