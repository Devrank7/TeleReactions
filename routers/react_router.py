import asyncio
import random

from aiogram import Router
from aiogram.types import Message, ReactionTypeEmoji


# router = Router()


async def react(message: Message):
    print(message.text)
    me = await message.bot.get_me()
    wait_for_time = round(float(random.randrange(1000) / random.randrange(400, 600)), 7)
    await asyncio.sleep(wait_for_time)
    print(f"Text: {message.text} / I am {me.username}")
    react_type = "👍" if random.randrange(3) == 0 else "❤" if random.randrange(2) == 1 else "🍾"
    await message.react([ReactionTypeEmoji(emoji=react_type)])


# @router.channel_post()
# async def react_text(message: Message):
#     await react(message)
#
#
# @router.message()
# async def react_text(message: Message):
#     await react(message)


def create_router() -> Router:
    router = Router()

    @router.channel_post()
    async def react_chanel(message: Message):
        await react(message)

    @router.message()
    async def react_message(message: Message):
        await react(message)

    return router
