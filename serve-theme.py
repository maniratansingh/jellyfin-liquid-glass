import http.server
import socketserver

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

port = 8085
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", port), CORSRequestHandler) as httpd:
    print(f"Serving Liquid Glass Theme with CORS at http://0.0.0.0:{port}")
    httpd.serve_forever()
