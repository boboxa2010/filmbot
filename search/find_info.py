import dataclasses

import aiohttp
import os
import typing as tp

KINOPOISK_TOKEN = os.getenv("KINOPOISK_TOKEN")

KINOPOISK_URL = "https://kinopoiskapiunofficial.tech/"


@dataclasses.dataclass
class FilmInfo:
    film_id: int
    name_ru: str
    name_en: str | None
    year: int
    rating: float
    description: str
    poster_url: str

    def __str__(self) -> str:
        if self.name_en:
            return f'{self.name_ru} / {self.name_en} ({self.year})\nRating: {self.rating}\n{self.description}\n'
        return f'{self.name_ru} ({self.year})\nRating: {self.rating}\n{self.description}\n'


@dataclasses.dataclass
class FilmFact:
    type: str
    description: str
    spoiler: bool

    def __str__(self) -> str:
        if self.spoiler:
            return f'SPOILER!!!\n<b>{self.type}</b>\n<tg-spoiler>{self.description}</tg-spoiler>\n'
        return f'<b>{self.type}</b>\n{self.description}\n'


def form_search_url(name: str) -> str:
    return KINOPOISK_URL + f'api/v2.1/films/search-by-keyword?keyword={name}&page=1'


def form_fact_url(film_id: int) -> str:
    return KINOPOISK_URL + f'api/v2.2/films/{film_id}/facts'


async def get_film_json(name: str) -> dict[str, tp.Any] | None:
    async with aiohttp.ClientSession() as session:
        async with session.get(form_search_url(name),
                               headers={'X-API-KEY': KINOPOISK_TOKEN,
                                        'Content-Type': 'application/json'}) as resp:
            films = (await resp.json())['films']
            if not films:
                return None
            return films[0]


async def get_film_info(name: str) -> FilmInfo | None:
    film_json = await get_film_json(name)
    if not film_json:
        return None
    return FilmInfo(film_id=film_json['filmId'],
                    name_ru=film_json.get('nameRu'),
                    name_en=film_json.get('nameEn'),
                    year=int(film_json.get('year')),
                    rating=float(film_json.get('rating')),
                    description=film_json.get('description'),
                    poster_url=film_json.get('posterUrl'))


def form_fact(item: dict[str, tp.Any]) -> FilmFact:
    return FilmFact(type=item['type'],
                    description=item['text'],
                    spoiler=item['spoiler'])


async def get_facts(film: FilmInfo, k: int = 3) -> list[FilmFact]:
    async with aiohttp.ClientSession() as session:
        async with session.get(form_fact_url(film.film_id),
                               headers={'X-API-KEY': KINOPOISK_TOKEN,
                                        'Content-Type': 'application/json'}) as resp:
            json = await resp.json()
            return [form_fact(item) for item in json['items'][:k]]
