import sqlite3
import json
from models import Soda

# The following functions are:
# get_all_inventory
# get_all_inventory_count
# get_single_inventory_item
#
# delete_item
# delete_item_deprecated


def get_all_inventory():
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


def get_all_inventory_count():
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


def get_single_inventory_item(soda_type_id):
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
        DELETE FROM soda
        WHERE id = ?
        """, (id, ))

def inventory_num_tracker(remaining_inventory):
    hash_table = {}
    inventory_num_list = []
    last_num = 0

    num_remaining_inventory = int(remaining_inventory)
    inventory_num_list.append(num_remaining_inventory)
    if (len(inventory_num_list) > 1):
        last_num = (len(inventory_num_list)-1) -1
    else:
        last_num = inventory_num_list[0] - 1

    print("----------- H E R E -----------------")
    print("last_num: ", last_num)
    return last_num




# this would work in MySQL
# apparently SQLite doesn't support LIMIT
def delete_item_deprecated(id):
    with sqlite3.connect("./vending.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.cost,
            s.soda_type_id
        FROM
            soda s
        WHERE
            s.soda_type_id = ?
        LIMIT 1;
        """, ( id, ))