from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command

    Args:
        message (Message): Incoming Telegram message.

    Example:
        "Hello, user_name!"
    """
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")
