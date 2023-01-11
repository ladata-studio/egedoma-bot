from fastapi import FastAPI
from aiogram import types, Dispatcher, Bot
from bot import dp, bot, TOKEN


app = FastAPI()
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = "https://egedoma.deta.dev" + WEBHOOK_PATH


@app.get('/set/{TOKEN}')
async def set_webhook():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.delete_webhook()
        await bot.set_webhook(
            url=WEBHOOK_URL
        )
        return "Webhook is set successfully"
    return "Webhook is already set"


@app.get('/remove/{TOKEN}')
async def set_webhook():
    await bot.delete_webhook()
    return "Webhook is removed successfully"


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)
    return "ok"
