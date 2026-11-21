import http.server, os, hashlib
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        v = os.environ.get("PR_TEST_SECRET")
        d = hashlib.sha256(v.encode()).hexdigest()[:16] if v else "absent"
        self.send_response(200); self.end_headers()
        self.wfile.write(("BB-RV-GH2-UNLINKED-PUSH-20261121 present=%s sha256_16=%s\n" % (bool(v), d)).encode())
http.server.ThreadingHTTPServer(("", int(os.environ.get("PORT", "8080"))), H).serve_forever()
