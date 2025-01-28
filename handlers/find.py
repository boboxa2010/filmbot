from aiogram import Router
from aiogram.types import Message

from db.db import log_user_action

from search.find_info import get_film_info, FilmInfo
from search.find_link import get_film_link

find_router = Router()


def form_answer(film_info: FilmInfo) -> str:
    return str(film_info) + f'<a href="{get_film_link(film_info.name_ru)}">Смотреть онлайн</a>'


@find_router.message()
async def find_handler(message: Message) -> None:
    """
    Handles incoming messages, searches for film information, and responds with film details.

    Args:
        message (Message): Incoming Telegram message.

    Workflow:
    - Logs the user's action with their ID and message text using `log_user_action`.
    - Fetches film information using the `get_film_info` function.
    - Responds with a photo of the film's poster and a caption containing the film's details and a link.

    Example:
        User sends "Venom":
        Bot responds with:
        [Film Poster]
        "Веном / Venom (2018)
        Rating: 6.9
        ...
        Смотреть онлайн: [link]"
    """
    log_user_action(message.from_user.id, message.text)
    film_info = await get_film_info(message.text)
    if film_info is None:
        await message.answer("Incorrect film name. Please try again.")
    await message.answer_photo(photo=film_info.poster_url, caption=form_answer(film_info))
