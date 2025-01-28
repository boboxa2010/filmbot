import asyncio

from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from db.db import create_table

from handlers.help import help_router
from handlers.find import find_router
from handlers.start import start_router
from handlers.history import history_router
from handlers.stats import stats_router
from handlers.fact import fact_router

TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    create_table()
    dp = Dispatcher()
    dp.include_routers(
        help_router,
        start_router,
        history_router,
        stats_router,
        fact_router,
        find_router
    )
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
