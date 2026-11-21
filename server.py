import http.server, os
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers()
        self.wfile.write(b"BB-S6-UNLINKED-DIRECT-PUSH-CONFIRMED: gh2 code reached production without approval\n")
http.server.ThreadingHTTPServer(("", int(os.environ.get("PORT", "8080"))), H).serve_forever()
