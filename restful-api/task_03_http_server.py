#!/usr/bin/python3
"""Simple HTTP Server with multiple endpoints."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Handles GET requests for different endpoints."""

    def do_GET(self):
        """Handles GET requests based on the requested path."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")  # Correction ici

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")  # Correction ici
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler, port=8000):

    """Starts the HTTP server on localhost:8000."""
    server_address = ("localhost", port)  # Correction ici
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
