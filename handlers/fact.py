from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from search.find_info import get_facts, get_film_info, FilmFact

fact_router = Router()


def form_answer(facts: list[FilmFact]) -> str:
    return "\n".join(str(fact) for fact in facts)


@fact_router.message(Command("facts"))
async def fact_handler(message: Message, command: CommandObject) -> None:
    """
    Handles incoming messages, searches for facts about film.

    Args:
        message (Message): Incoming Telegram message.
        command (CommandObject): Command object.
    Workflow:
    - Fetches film information using the `get_film_info` function.
    - Responds with facts from film.

    Example:
        User sends "/facts Venom":
        Bot responds with:
        FACT
        ...

        FACT
        ...

    """
    film_info = await get_film_info(command.args)
    if film_info is None:
        await message.answer("Incorrect film name. Please try again.")
    await message.answer(form_answer(await get_facts(film_info)))
