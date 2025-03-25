from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from param_parser import parse_param
from logger import log_json
import json
import time

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path != "/":
            self.send_error(404, "Not Found")
            return

        query = parse_qs(parsed_url.query)

        wait = parse_param(query.get("wait", ["0"])[0], "float", 0.0)
        status = parse_param(query.get("status", ["200"])[0], "int", 200)
        response_size = parse_param(query.get("response_size", ["100"])[0], "int", 100)

        if wait > 0:
            time.sleep(wait)

        payload = "X" * response_size
        response = {
            "status": status,
            "wait": wait,
            "response_size": response_size,
            "payload": payload
        }

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

        log_json({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "ip": self.client_address[0],
            "method": self.command,
            "path": self.path,
            "params": query,
            "status": status,
            "wait": wait,
            "response_size": response_size
        })

    def log_message(self, format, *args):
        pass  # Disable default logging
