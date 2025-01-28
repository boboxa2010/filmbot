from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.db import get_user_history

history_router = Router()


@history_router.message(Command('history'))
async def history_handler(message: Message) -> None:
    """
    Handles the /history command, fetching and displaying the user's history.

    Args:
        message (Message): Incoming Telegram message.

    Workflow:
    - Retrieves the user's ID and fetches history using `get_user_history`.
    - Sends a message with the history in a formatted list or informs the user if no history is found.

    Example:
        "Your history (last 10):
        Venom at 2024-12-01
        Matrix at 2024-12-05"
        ...
    """
    history = get_user_history(message.from_user.id)

    if not history:
        await message.answer("You have no history yet.")
    else:
        history_text = "\n".join([f"{row[0]} at {row[1]}" for row in history])
        await message.answer(f"Your history (last 10):\n{history_text}")
