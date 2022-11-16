import sqlite3
import json
from models import Soda


def get_all_inventory_count():
    # Open a connection to the database
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

        # Initialize an empty list to hold all soda representations
        sodas = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an soda instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Soda class above.
            soda = Soda(row['id'], row['cost'], row['soda_type_id'])

            sodas.append(soda.__dict__)

    inventory_count = len(sodas)
    # Use `json` package to properly serialize list as JSON
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

# this would work in MySQL
# apparently SQLite doesn't support LIMIT
# def delete_item(id):
#     with sqlite3.connect("./vending.db") as conn:
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         SELECT
#             s.id,
#             s.cost,
#             s.soda_type_id
#         FROM
#             soda s
#         WHERE
#             s.soda_type_id = ?
#         LIMIT 1;
#         """, ( id, ))

def get_all_inventory():
    # Open a connection to the database
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

        # Initialize an empty list to hold all soda representations
        sodas = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an soda instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Soda class above.
            soda = Soda(row['id'], row['cost'], row['soda_type_id'])

            sodas.append(soda.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(sodas)