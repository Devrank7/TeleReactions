from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


def create_router():
    router = Router()

    @router.message(Command("start_gather"))
    async def start_router(message: Message) -> None:
        await message.answer("Start bot!")

    return router
