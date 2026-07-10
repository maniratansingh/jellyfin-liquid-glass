import http.server
import socketserver

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

port = 8080
handler = CORSRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving with CORS at port {port}")
    httpd.serve_forever()
