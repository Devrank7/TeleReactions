import asyncio
import random

from aiogram import Router
from aiogram.types import Message, ReactionTypeEmoji


def get_react():
    random_number = int(round(random.randrange(0, 5)))
    match random_number:
        case 0:
            return "👍"
        case 1:
            return "❤"
        case 2:
            return "🔥"
        case 3:
            return "💯"
        case 4:
            return "🍾"


def get_timeout(start_time, end_time):
    timeout = random.uniform(start_time, end_time)
    return round(timeout, 5)


async def react(message: Message):
    print(message.text)
    me = await message.bot.get_me()
    await asyncio.sleep(get_timeout(24, 118))
    print(f"Text: {message.text} / I am {me.username}")
    await message.react([ReactionTypeEmoji(emoji=get_react())])


def create_router() -> Router:
    router = Router()

    @router.channel_post()
    async def react_chanel(message: Message):
        await react(message)

    @router.message()
    async def react_message(message: Message):
        await react(message)

    return router
