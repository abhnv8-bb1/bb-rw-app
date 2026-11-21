import http.server, os
# collaborator (no Railway account) same-repo PR marker (researcher abhnv8, harmless): only reports whether the variable exists
print("COLLAB-PR-CODE-RUNNING secret_present=%s len=%d env=%s" % ("PR_TEST_SECRET" in os.environ, len(os.environ.get("PR_TEST_SECRET","")), os.environ.get("RAILWAY_ENVIRONMENT_NAME")), flush=True)
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"bb-rw-app COLLAB PR version\n")
http.server.ThreadingHTTPServer(("", int(os.environ.get("PORT", "8080"))), H).serve_forever()
