from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# router = Router()
#
#
# @router.message(Command("start"))
# async def start_router(message: Message) -> None:
#     await message.answer("Start bot!")


def create_router():
    router = Router()

    @router.message(Command("start"))
    async def start_router(message: Message) -> None:
        await message.answer("Start bot!")

    return router
