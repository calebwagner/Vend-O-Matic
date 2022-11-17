from http.server import BaseHTTPRequestHandler, HTTPServer
from inventory import get_single_inventory_item, delete_item, get_all_inventory_count, inventory_num_tracker
from coins import create_coin, get_coins, get_num_of_coins, delete_coin
import json

# The following functions in HandleRequests are:
# parse_url
# _set_headers
#
# do_GET
# do_POST
# do_PUT
# do_DELETE

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
                response = f"remaining item quantities: {[int(get_all_inventory_count())]}"
        elif resource == "":
                response = f"{get_coins()}"

        self.wfile.write(f"{response}".encode())


    def do_POST(self):
        # TODO: add dynamic value
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

        print("----------------------------")
        print("post_body: ", post_body)
        print("resource: ", resource)
        print("id: ", id)
        print("----------------------------")

        remaining_inventory = get_single_inventory_item(id)
        coin_count = get_num_of_coins()
        coin_count_minus_cost = int(coin_count) - 2

        print("----------------------------")
        convert_inventory_to_num = int(remaining_inventory)
        remaining_inventory_minus_one = convert_inventory_to_num -1
        print("remaining_inventory: ", remaining_inventory_minus_one - 1)
        print("----------------------------")

        # inventory_num_tracker(remaining_inventory)

        if resource == "inventory":
            if int(remaining_inventory) > 0 and int(coin_count) >= 2:
                delete_item(id)
                delete_coin()
                inventory_num_tracker(remaining_inventory)
                # remaining_inventory_min_deleted = int(remaining_inventory - 1)
                self._set_headers(200, coin_count_minus_cost, remaining_inventory_minus_one)
                self.wfile.write(f"[quantity: {1}]".encode())
            elif int(coin_count) < 2:
                self._set_headers(403, coin_count, None)
            else:
                coin_count = 0
                self._set_headers(404, coin_count, None)

        if resource == "":
            # TODO:
            # I know this (1) isn't a dynamic value but the machine
            # only accepts one coin at a time so I think this works
            self._set_headers(204, 1, None)
            create_coin(post_body)

        # self.wfile.write(f"[quantity: {1}]".encode())


    def do_DELETE(self):
        num_of_coins_returned = get_num_of_coins()
        self._set_headers(204, num_of_coins_returned, None)

        (resource, id) = self.parse_url(self.path)

        if resource == "":
            delete_coin()

        self.wfile.write("".encode())



def main():
    host = ''
    port = 8000
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
