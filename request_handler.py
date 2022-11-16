from http.server import BaseHTTPRequestHandler, HTTPServer
from inventory import get_all_inventory, get_single_inventory_item, delete_inventory_item, update_inventory_item
from coins import get_all_coins, create_coin
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

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()


    def do_GET(self):
        self._set_headers(200)

        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "inventory":
            if id is not None:
                response = f"remaining item quantity: {get_single_inventory_item(id)}"
            else:
                response = f"remaining item quantities: {get_all_inventory()}"
        elif resource == "coins":
                response = f"{get_all_coins()}"

        self.wfile.write(f"{response}".encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new coin
        new_coin = None

        # Add a new coin to the list
        if resource == "coins":
            new_coin = create_coin(post_body)

        # Encode the new coin and send in response
        self.wfile.write(f"{new_coin}".encode())


def do_PUT(self):
    self._set_headers(204)
    content_len = int(self.headers.get('content-length', 0))
    post_body = self.rfile.read(content_len)
    post_body = json.loads(post_body)

    # Parse the URL
    (resource, id) = self.parse_url(self.path)

    # Delete a single inventory item from the list
    if resource == "inventory":
        update_inventory_item(id, post_body)

    # Encode the new inventory item and send in response
    self.wfile.write("".encode())



def main():
    """Starts the server on port 8000 using the HandleRequests class
    """
    host = ''
    port = 8000
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
