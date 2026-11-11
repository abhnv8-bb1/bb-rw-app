import http.server, os
# outside-contributor fork PR marker (researcher abhnv8, harmless): only reports whether the variable exists
print("FORK-PR-CODE-RUNNING secret_present=%s len=%d" % ("PR_TEST_SECRET" in os.environ, len(os.environ.get("PR_TEST_SECRET",""))), flush=True)
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"bb-rw-app FORK PR version (outside contributor)\n")
http.server.ThreadingHTTPServer(("", int(os.environ.get("PORT", "8080"))), H).serve_forever()
# touch 1794377863
