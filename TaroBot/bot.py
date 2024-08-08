# bot.py
import asyncio
from telethon import TelegramClient, events
from tarot_data import tarot_deck
import random

api_id = '29183496'
api_hash = '989aa18a720a4ba746d5087d8c809e26'
bot_token = '7496291307:AAF4QsnCBxvGGMbxEYMvDPGck6HhpRyN91I'

client = TelegramClient('tarot_bot', api_id, api_hash).start(bot_token=bot_token)

# Список доступных раскладов
readings = {
    "love": "Любовь и отношения",
    "decision": "Принятие решений",
    "past_future": "Прошлое и будущее",
    "money": "Деньги и бизнес"
}

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "Привет! Я Таро-бот. Выберите тип расклада:\n"
        "/love - Любовь и отношения\n"
        "/decision - Принятие решений\n"
        "/past_future - Прошлое и будущее\n"
        "/money - Деньги и бизнес"
    )

@client.on(events.NewMessage(pattern='/love'))
async def love_reading(event):
    await tarot_reading(event, "love")

@client.on(events.NewMessage(pattern='/decision'))
async def decision_reading(event):
    await tarot_reading(event, "decision")

@client.on(events.NewMessage(pattern='/past_future'))
async def past_future_reading(event):
    await tarot_reading(event, "past_future")

@client.on(events.NewMessage(pattern='/money'))
async def money_reading(event):
    await tarot_reading(event, "money")

async def tarot_reading(event, reading_type):
    cards = random.sample(list(tarot_deck.keys()), 3)
    message = f"Расклад: {readings[reading_type]}\n"
    for i, card in enumerate(cards):
        message += f"\nКарта {i+1}: {card}\nОписание: {tarot_deck[card]['description']}\n"

    await event.respond(message)

def main():
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
