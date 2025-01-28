from googlesearch import search


def form_query(name: str) -> str:
    return f"смотреть {name} онлайн без регистрации и смс"


def get_film_link(name: str) -> str:
    return next(search(form_query(name), num_results=1, lang='ru'))
