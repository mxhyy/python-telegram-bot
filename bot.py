from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests  # 用于调用运势API

TOKEN = 7652176438:AAF7jHOraltNII5dgCdxe-pBF1Vbvb2g4lA

def start(update: Update, context: CallbackContext):
    update.message.reply_text('输入/setzodiac设置星座，输入/daily获取今日运势！')

def set_zodiac(update: Update, context: CallbackContext):
    # 存储用户选择的星座（如用数据库或字典）
    zodiac = context.args[0]
    context.user_data['zodiac'] = zodiac
    update.message.reply_text(f'已设置星座为：{zodiac}')

def send_daily(update: Update, context: CallbackContext):
    # 调用API或本地逻辑生成运势
    zodiac = context.user_data.get('zodiac', '未设置')
    fortune = get_fortune(zodiac)  # 自定义函数获取运势
    update.message.reply_text(fortune)

def get_fortune(zodiac: str) -> str:
    # 示例：调用API或随机生成
    return f"{zodiac}今日运势：★★★★☆，宜尝试新事物！"

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("setzodiac", set_zodiac))
updater.dispatcher.add_handler(CommandHandler("daily", send_daily))
updater.start_polling()
updater.idle()