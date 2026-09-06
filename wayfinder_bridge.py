"""
Wayfinder local sync bridge.

This tiny local server is the "bridge" between the Wayfinder browser page
and a real file on your computer. It does two things only:
  - GET  /data  -> reads wayfinder-data.json from DATA_DIR and returns it
  - POST /data  -> writes the request body to wayfinder-data.json in DATA_DIR

It only ever listens on your own machine (127.0.0.1) — nothing outside
your computer can reach it.

HOW TO SET THE SAVE LOCATION
-----------------------------
Change DATA_DIR below to the folder you want the data file kept in.

Note on "C:\\Program Files\\...": Windows blocks normal (non-admin)
programs from writing inside Program Files. If you point DATA_DIR there,
you must run this script from an Administrator Command Prompt every
time, or it will fail to save. A folder you already own — like the one
below, or anywhere under your user profile — avoids that problem
entirely and is what most people should use.
"""

import http.server
import json
import os

# ---- CHANGE THIS to where you want the data file saved ----
DATA_DIR = r"C:\Users\Rahul Deb Roy\Documents\Wayfinder\Data"
# Example without admin headaches:
# DATA_DIR = r"C:\Users\YOUR_USERNAME\Documents\Wayfinder\Data"

DATA_FILE = os.path.join(DATA_DIR, "wayfinder-data.json")
PORT = 8765


class BridgeHandler(http.server.BaseHTTPRequestHandler):
    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path != "/data":
            self.send_response(404)
            self._cors_headers()
            self.end_headers()
            return
        try:
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    body = f.read()
            else:
                body = "{}"
            payload = body.encode("utf-8")
            self.send_response(200)
            self._cors_headers()
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        except Exception as e:
            self.send_response(500)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(str(e).encode("utf-8"))

    def do_POST(self):
        if self.path != "/data":
            self.send_response(404)
            self._cors_headers()
            self.end_headers()
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            raw = self.rfile.read(length)
            data = json.loads(raw.decode("utf-8"))  # validate it's real JSON

            os.makedirs(DATA_DIR, exist_ok=True)
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)

            self.send_response(200)
            self._cors_headers()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"ok": true}')
        except PermissionError:
            self.send_response(500)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(
                b'{"error": "Permission denied writing to DATA_DIR. '
                b'Run this script as Administrator, or change DATA_DIR '
                b'to a folder you own (e.g. under Documents)."}'
            )
        except Exception as e:
            self.send_response(500)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))

    def log_message(self, fmt, *args):
        print("[wayfinder-bridge]", fmt % args)


if __name__ == "__main__":
    print(f"Wayfinder bridge running at http://127.0.0.1:{PORT}")
    print(f"Saving data to: {DATA_FILE}")
    print("Keep this window open while using Wayfinder. Press Ctrl+C to stop.")
    server = http.server.HTTPServer(("127.0.0.1", PORT), BridgeHandler)
    server.serve_forever()
