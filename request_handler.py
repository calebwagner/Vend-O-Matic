from http.server import BaseHTTPRequestHandler, HTTPServer
from inventory import get_all_inventory, get_single_inventory_item
from coins import get_all_coins


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
                response = f"{get_single_inventory_item(id)}"
            else:
                response = f"{get_all_inventory()}"
        if self.path == "/coins":
            response = get_all_coins()
        else:
            response = []

        self.wfile.write(f"received get request:<br>{response}".encode())

    def do_POST(self):
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = f"received post request:<br>{post_body}"
        self.wfile.write(response.encode())


    def do_PUT(self):
        self.do_POST()



def main():
    """Starts the server on port 8000 using the HandleRequests class
    """
    host = ''
    port = 8000
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
