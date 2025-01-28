import sqlite3
import typing as tp

from datetime import datetime

__created = False


def create_table() -> None:
    global __created
    if __created:
        return
    conn = sqlite3.connect("db/user_history.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_history (
        user_id INTEGER,
        film TEXT,
        timestamp TEXT
    )
    """)
    conn.commit()
    conn.close()
    __created = True


def log_user_action(user_id: int, film: str) -> None:
    conn = sqlite3.connect("db/user_history.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO user_history (user_id, film, timestamp) VALUES (?, ?, ?)",
        (user_id, film, timestamp)
    )
    conn.commit()
    conn.close()


def get_user_history(user_id: int, limit: int = 10) -> list[tp.Any]:
    conn = sqlite3.connect("db/user_history.db")
    cursor = conn.cursor()
    cursor.execute(
        """SELECT film, timestamp
        FROM user_history
        WHERE user_id = ?
        ORDER BY timestamp DESC
        LIMIT ?""",
        (user_id, limit)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_user_stats(user_id: int, limit: int = 5) -> list[tp.Any]:
    conn = sqlite3.connect("db/user_history.db")
    cursor = conn.cursor()
    cursor.execute(
        """SELECT film, COUNT(*) as count
        FROM user_history
        WHERE user_id = ?
        GROUP BY film
        ORDER BY count DESC, timestamp
        LIMIT ?""",
        (user_id, limit)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
