import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()
env_variables = os.environ

bot_tokens = {key: value for key, value in env_variables.items() if key.startswith("BOT_TOKEN") if value}
MODERATOR_BOT = env_variables["MODERATOR_BOT"]

for key, value in bot_tokens.items():
    print(f"{key}: {value}")


async def pooling_bot(token: str):
    try:
        bot = Bot(token)
        dp = Dispatcher()
        from routers import react_router, start_router
        local_react_router = react_router.create_router()
        local_start_router = start_router.create_router()
        dp.include_router(local_start_router)
        dp.include_router(local_react_router)
        me = await bot.get_me()
        print(f"Bot {me.username} is polling now!")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Error with bot {token}: {e}")


async def pooling_moderator_bot(token: str):
    pass


async def main():
    tasks = [asyncio.create_task(pooling_bot(value)) for key, value in bot_tokens.items()]
    tasks.append(asyncio.create_task(pooling_moderator_bot(MODERATOR_BOT)))
    await asyncio.gather(*tasks)
    print("All bots are running!")


if __name__ == '__main__':
    asyncio.run(main())
