from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

help_router = Router()


@help_router.message(Command('help'))
async def help_handler(message: Message) -> None:
    """
    This handler responds to the `/help` command.

    Args:
        message (Message): Incoming Telegram message containing the `/help` command.

    Example:
        User input: "/help"
        Bot response: "I'm here to help you! Just type the name of a film,
        and I'll provide a link where you can watch it for free."
    """
    await message.answer(
        "I'm here to help you!\n"
        "Just type the name of a film, and I'll provide a link where you can watch it for free.\n\n"
        "Other available commands:\n"
        "- /start: Start the bot.\n"
        "- /help: Get assistance with using the bot.\n"
        "- /stats: View the top 5 movies based on your requests.\n"
        "- /history: See your request history.\n"
        "- /facts <film>: Provide facts about film.\n"
    )
