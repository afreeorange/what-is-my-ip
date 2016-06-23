import sys
from http.server import HTTPServer, BaseHTTPRequestHandler


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        client_ip = self.client_address[0]

        if client_ip == '127.0.0.1' and 'X-Real-IP' in self.headers:
            client_ip = self.headers['X-Real-IP']

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes(client_ip + '\n', 'utf8'))

        return


def run(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) == 2 else 9000)
