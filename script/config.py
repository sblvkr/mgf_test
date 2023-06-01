import logging
import os
from sys import stdout

import psycopg2

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s, %(name)s, %(levelname)s, %(message)s',
    handlers=(
        logging.StreamHandler(stream=stdout),
        logging.FileHandler('Log.log')
    ),
)


POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_PORT = os.getenv('DB_PORT', '5432')

NUMBER_ENTRY = 30
SLEEP_SEC = 60

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
)
cursor = conn.cursor()
