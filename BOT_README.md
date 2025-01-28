# Cinemabot

## Overview

This is a telegram bot searches for film information and links to watch it for free, and responds with film details.

The bot was created using python `aiogram` library

For searching information about films was used [`kinopoisk_api`](https://kinopoiskapiunofficial.tech) and `googlesearch`


Data about users history is stored in `sqlite` database, connection to the database was created via python's `sqlite3`
library

## Initialising and running the project

Install dependencies

```
pip install -r ./requirements.txt
``` 

Run the bot:

```
BOT_TOKEN=<...> KINOPOISK_TOKEN=<...> python bot.py
```

## Functionality

The bot supports the following commands:

- /start: Start the bot.
- /help: Get assistance with using the bot.
- /stats: View the top 5 movies based on your requests.
- /history: See your request history.
- /facts film: Facts about this film.
- film: Searches for film information and links to watch it.