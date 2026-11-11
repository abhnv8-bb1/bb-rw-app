import http.server, os
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers()
        self.wfile.write(b"bb-rw-app OWNER PR branch (control)\n")
http.server.ThreadingHTTPServer(("", int(os.environ.get("PORT", "8080"))), H).serve_forever()
