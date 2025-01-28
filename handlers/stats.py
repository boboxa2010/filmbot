from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.db import get_user_stats

stats_router = Router()


@stats_router.message(Command('stats'))
async def stats_handler(message: Message) -> None:
    """
    Handles the /stats command, fetching and displaying the user's stats.

    Args:
        message (Message): Incoming Telegram message.

    Workflow:
    - Retrieves the user's ID and fetches stats using `get_user_stats`.
    - Sends a message with the stats or informs the user if no stats are found.

    Example:
        "Top 5 movies by your requests:
        Venom: asked 19 times
        Matrix: asked 5 times"
    """
    stats = get_user_stats(message.from_user.id)

    if not stats:
        await message.answer("You have no stats yet.")
    else:
        stats_text = "\n".join([f"{row[0]}: searched {row[1]} times" for row in stats])
        await message.answer(f"Top 5 movies by your requests:\n{stats_text}")
