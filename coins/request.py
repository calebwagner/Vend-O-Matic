COINS = [
    {
        "id": 1, "coin": 1
    },
    {
        "id": 2, "coin": 1,
    }
]

def get_all_coins():
    return COINS

def create_coin(coin):
    # Get the id value of the last animal in the list
    max_id = COINS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the coin dictionary
    coin["id"] = new_id

    # Add the coin dictionary to the list
    COINS.append(coin)

    # Return the dictionary with `id` property added
    return coin