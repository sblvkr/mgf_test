import logging
import random
import time
from datetime import datetime

from config import NUMBER_ENTRY, SLEEP_SEC, cursor
from exceptions import MainError


def generate_data() -> str:
    return "generated text " + str(random.randint(1, 100))


def insert_data(data) -> None:
    try:
        cursor.execute(
            "INSERT INTO test_data_tbl (data, date) VALUES (%s, %s);",
            (data, datetime.now())
        )
        logging.info('Данные внесены')
    except MainError:
        logging.error('Ошибка при внесении данных')


def clear_table() -> None:
    try:
        cursor.execute(
            "DELETE FROM test_data_tbl;"
        )
        logging.info('Таблица девственно чиста')
    except MainError:
        logging.error('Ошибка при отчистке таблицы')


def create_table() -> None:
    try:
        cursor.execute("""
            CREATE TABLE test_data_tbl (
                id SERIAL PRIMARY KEY,
                data TEXT,
                date TIMESTAMP);
        """)
        logging.info('Таблица создана')
    except MainError:
        logging.error('Ошибка при создании таблицы')


def main():
    create_table()
    while True:
        time.sleep(SLEEP_SEC)

        logging.info('Начата генерация данных и отправка в БД')
        data = generate_data()
        insert_data(data)

        cursor.execute("SELECT COUNT(*) FROM test_data_tbl;")
        count = cursor.fetchone()[0]

        if count >= NUMBER_ENTRY:
            logging.info('Начинаем отчистку таблицы')
            clear_table()

        logging.info('Успех! Сон %s секунд', SLEEP_SEC)


if __name__ == "__main__":
    main()
