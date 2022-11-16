from http.server import BaseHTTPRequestHandler, HTTPServer
from inventory import get_all_inventory, get_single_inventory_item, delete_item
from coins import create_coin, get_coins, get_num_of_coins, delete_coin
import json


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def _set_headers(self, status, num_of_coins_returned_accepted, remaining_inventory):
        self.send_response(status)
        self.send_header('X-Coins', num_of_coins_returned_accepted)
        self.send_header('X-Inventory-Remaining', remaining_inventory)
        self.end_headers()

    def do_GET(self):
        self._set_headers(200, None, None)

        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "inventory":
            if id is not None:
                response = f"remaining item quantity: {get_single_inventory_item(id)}"
            else:
                response = f"remaining item quantities: {[get_all_inventory()]}"
        elif resource == "":
                response = f"{get_coins()}"

        self.wfile.write(f"{response}".encode())

    def do_POST(self):
        # todo:
        # add dynamic value
        self._set_headers(204, 1, None)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_coin = None

        if resource == "":
            new_coin = create_coin(post_body)

        self.wfile.write(f"{new_coin}".encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        remaining_inventory = get_single_inventory_item(id)
        coin_count = get_num_of_coins()
        coin_count_minus_cost = int(coin_count) - 2

        if resource == "inventory":
            if int(remaining_inventory) > 0 and int(coin_count) >= 2:
                delete_item(id)
                delete_coin()
                self._set_headers(200, coin_count_minus_cost, remaining_inventory)
                self.wfile.write(f"[quantity: {1}]".encode())
            elif int(coin_count) < 2:
                self._set_headers(403, coin_count, None)
            else:
                coin_count = 0
                self._set_headers(404, coin_count, None)

        if resource == "":
            # todo:
            # I know this isn't a dynamic value but the machine
            # only accepts one coin at a time so I think this works
            self._set_headers(204, 1, None)
            create_coin(post_body)

        # Encode the new inventory item and send in response
        # todo:
        # self.wfile.write(f"[quantity: {1}]".encode())

    def do_DELETE(self):
        num_of_coins_returned = get_num_of_coins()
        self._set_headers(204, num_of_coins_returned, None)

        (resource, id) = self.parse_url(self.path)

        if resource == "":
            delete_coin()

        self.wfile.write("".encode())



def main():
    """Starts the server on port 8000 using the HandleRequests class
    """
    host = ''
    port = 8000
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
