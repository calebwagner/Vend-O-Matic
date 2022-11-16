INVENTORY = [
    {
        "id": 1, "name": "coke", "cost": 2
    },
    {
        "id": 2, "name": "sprite", "cost": 2
    },
    {
        "id": 3, "name": "pepsi", "cost": 2
    }
]

def get_all_inventory():
    return INVENTORY

def get_single_inventory_item(id):
    requested_item = None

    for item in INVENTORY:
        if item["id"] == id:
            requested_item = item

    return requested_item