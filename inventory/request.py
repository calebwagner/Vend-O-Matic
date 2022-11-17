import sqlite3
import json
from models import Soda

# The following functions are:
# get_all_inventory_objects
# get_total_inventory_count
# get_single_inventory_type_count
# delete_item

# leaving this here for testing purposes
def get_all_inventory_objects():
    with sqlite3.connect("./vending.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.cost,
            s.soda_type_id
        FROM soda s
        """)

        sodas = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            soda = Soda(row['id'], row['cost'], row['soda_type_id'])
            sodas.append(soda.__dict__)

    return json.dumps(sodas)


def get_total_inventory_count():
    with sqlite3.connect("./vending.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.cost,
            s.soda_type_id
        FROM soda s
        """)

        sodas = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            soda = Soda(row['id'], row['cost'], row['soda_type_id'])
            sodas.append(soda.__dict__)

    inventory_count = len(sodas)

    return json.dumps(inventory_count)


def get_single_inventory_type_count(soda_type_id):
    with sqlite3.connect("./vending.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.cost,
            s.soda_type_id
        FROM soda s
        WHERE s.soda_type_id = ?
        """, ( soda_type_id, ))

        sodas = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            soda = Soda(row['id'], row['cost'], row['soda_type_id'])
            sodas.append(soda.__dict__)

        soda_count = len(sodas)

        return json.dumps(soda_count)


def delete_item(id):
    with sqlite3.connect("./vending.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM
            soda
        WHERE
            id = (
                SELECT
                    MIN(soda.id)
                FROM
                    soda
                WHERE
                    soda.soda_type_id = ?
            )
        """, (id, ))
    get_single_inventory_type_count(id)

