import sqlite3
import json
from models import Coin

def create_coin(new_coin):
    with sqlite3.connect("./vending.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Coin
            ( coin )
        VALUES
            ( ? );
        """, (new_coin['coin'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the coin dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_coin['id'] = id


    return json.dumps(new_coin)

def get_coins():
    # Open a connection to the database
    with sqlite3.connect("./vending.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.coin
        FROM coin c
        """)

        # Initialize an empty list to hold all coin representations
        coins = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an coin instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Coin class above.
            coin = Coin(row['id'], row['coin'])

            coins.append(coin.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(coins)

def get_num_of_coins():
    # Open a connection to the database
    with sqlite3.connect("./vending.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.coin
        FROM coin c
        """)

        # Initialize an empty list to hold all coin representations
        coins = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an coin instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Coin class above.
            coin = Coin(row['id'], row['coin'])

            coins.append(coin.__dict__)

    coin_count = len(coins)
    # Use `json` package to properly serialize list as JSON
    return json.dumps(coin_count)

def delete_coin():
    with sqlite3.connect("./vending.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM coin
        """)