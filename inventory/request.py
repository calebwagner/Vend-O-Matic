# INVENTORY = [
#     {
#         "id": 1,
#         "coke":
#     [
#         {
#             "id": 1, "cost": 2
#         },
#         {
#             "id": 2, "cost": 2
#         },
#         {
#             "id": 3, "cost": 2
#         },
#         {
#             "id": 4, "cost": 2
#         },
#         {
#             "id": 5, "cost": 2
#         }
#     ]
#     },
#     {
#         "id": 2,
#         "sprite":
#     [
#         {
#             "id": 1, "cost": 2
#         },
#         {
#             "id": 2, "cost": 2
#         },
#         {
#             "id": 3, "cost": 2
#         },
#         {
#             "id": 4, "cost": 2
#         }
#     ]
#     },
#     {
#         "id": 3,
#         "pepsi":
#     [
#         {
#             "id": 1, "cost": 2
#         },
#         {
#             "id": 2, "cost": 2
#         },
#         {
#             "id": 3, "cost": 2
#         }
#     ]
#     }
# ]

import sqlite3
import json
from models import Soda

# todo
# response body should be an array of remaining item quantities
# aka an array of integers
def get_all_inventory_old():
    inventory_count = 0
    for sodas in INVENTORY:
        # print("soda --> ", sodas)
        for items in sodas:
            # print("items --> ", len(sodas[items]))
            inventory_count += len(sodas[items])
    # inventory_count = len(INVENTORY)
    print("inventory_count --> ", inventory_count)
    return inventory_count

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

    inventory_count = len(sodas)
    # Use `json` package to properly serialize list as JSON
    return json.dumps(inventory_count)

def get_single_inventory_item_old(id):
    id_minus_one = id - 1
    requested_inventory_count = None

    # print("inventory item --> ", INVENTORY.id)

    for sodas in INVENTORY:
        soda_id = sodas.get("id")
        # print("soda_id --> ", soda_id)
        # soda = sodas.get("coke")
        # print("sodas -------> ", len(soda))
        # if soda_id == id_minus_one:
        if id_minus_one == 0:
            print("soda_id --> ", len(INVENTORY[id_minus_one].get("coke")))
            requested_inventory_count = len(INVENTORY[id_minus_one].get("coke"))

        if id_minus_one == 1:
            print("soda_id --> ", len(INVENTORY[id_minus_one].get("sprite")))
            requested_inventory_count = len(INVENTORY[id_minus_one].get("sprite"))

        if id_minus_one == 2:
            print("soda_id --> ", len(INVENTORY[id_minus_one].get("pepsi")))
            requested_inventory_count = len(INVENTORY[id_minus_one].get("pepsi"))


    return requested_inventory_count

def get_single_inventory_item(soda_type_id):
    with sqlite3.connect("./vending.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
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

def delete_inventory_item(id):
    # Initial -1 value for item index, in case one isn't found
    item_index = -1

    # Iterate the INVENTORY list, but use enumerate() so that you
    # can access the index value of each item
    for index, soda in enumerate(INVENTORY):
        if soda["id"] == id:
            # Found the soda. Store the current index.
            item_index = index

    # If the item was found, use pop(int) to remove it from list
    if item_index >= 0:
        INVENTORY.pop(item_index)

def update_inventory_item(id, new_item):
    # Iterate the INVENTORY list, but use enumerate() so that
    # you can access the index value of each item.
    for index, soda in enumerate(INVENTORY):
        if soda["id"] == id:
            # Found the soda. Update the value.
            INVENTORY[index] = new_item
            break