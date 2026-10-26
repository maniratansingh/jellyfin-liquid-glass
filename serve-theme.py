#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

PORT = 8085

class ThreadedCORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, HEAD')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Liquid Glass Theme Server</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0c1022; color: #fff; padding: 30px; line-height: 1.6; }
        .card { background: rgba(255,255,255,0.08); border-radius: 16px; padding: 24px; max-width: 650px; margin: 0 auto; backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.15); box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
        h1 { margin-top: 0; color: #5eb5f7; font-size: 1.6rem; }
        .status { display: inline-block; padding: 4px 12px; background: #10b981; color: #fff; border-radius: 999px; font-weight: 600; font-size: 0.85rem; margin-bottom: 16px; }
        a { color: #60a5fa; text-decoration: none; word-break: break-all; }
        a:hover { text-decoration: underline; }
        ul { padding-left: 20px; }
        li { margin-bottom: 12px; }
        code { background: rgba(255,255,255,0.15); padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="card">
        <span class="status">&#10003; Active &amp; Serving</span>
        <h1>Liquid Glass Live Dev Server</h1>
        <p>Zero-cache CORS enabled theme server for Jellyfin testing.</p>
        <h3>Direct CSS Links:</h3>
        <ul>
            <li><strong>Main Theme (dist):</strong><br><a href="/dist/jellyfin-liquid-glass.css">/dist/jellyfin-liquid-glass.css</a></li>
            <li><strong>Bundle Theme:</strong><br><a href="/liquid-glass-bundle.css">/liquid-glass-bundle.css</a></li>
        </ul>
        <h3>Interactive Mock Previews:</h3>
        <ul>
            <li><a href="/tests/fixtures/mock-jellyfin-detail.html">Movie Detail View (Mobile)</a></li>
            <li><a href="/tests/fixtures/mock-jellyfin-nowplaying.html">Now Playing / Audio Player (Mobile)</a></li>
            <li><a href="/tests/fixtures/mock-jellyfin-login.html">Login Screen</a></li>
            <li><a href="/tests/fixtures/mock-jellyfin-redesign.html">Home &amp; Library View</a></li>
        </ul>
    </div>
</body>
</html>"""
            self.wfile.write(html.encode('utf-8'))
            return
        super().do_GET()

def run():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", PORT), ThreadedCORSRequestHandler) as httpd:
        print(f"Serving Liquid Glass Theme with Multi-Threaded CORS at http://0.0.0.0:{PORT}", flush=True)
        httpd.serve_forever()

if __name__ == '__main__':
    run()
