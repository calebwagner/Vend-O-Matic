import sqlite3
import json
from models import Coin

# The following functions are:
# create_coin
# get_coins
# get_num_of_coins
# delete_coin


def create_coin(new_coin):
    with sqlite3.connect("./vending.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Coin
            ( coin )
        VALUES
            ( ? );
        """, (new_coin['coin'], ))

        id = db_cursor.lastrowid
        new_coin['id'] = id

    return json.dumps(new_coin)


def get_coins():
    with sqlite3.connect("./vending.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.coin
        FROM coin c
        """)

        coins = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            coin = Coin(row['id'], row['coin'])
            coins.append(coin.__dict__)

    return json.dumps(coins)


def get_num_of_coins():
    with sqlite3.connect("./vending.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.coin
        FROM coin c
        """)

        coins = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            coin = Coin(row['id'], row['coin'])
            coins.append(coin.__dict__)

    coin_count = len(coins)

    return json.dumps(coin_count)


def delete_coin():
    with sqlite3.connect("./vending.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM coin
        """)