from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = int(os.environ.get("PORT", 8080))
ENVIRONMENT = os.environ.get("ENVIRONMENT", "Development")

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Docker Practice App</title>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                    background: #f0f4f8;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .card {{
                    background: white;
                    padding: 40px;
                    border-radius: 12px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                    text-align: center;
                    max-width: 500px;
                }}
                h1 {{ color: #2496ED; margin-bottom: 10px; }}
                .tag {{
                    display: inline-block;
                    background: #e1f0fc;
                    color: #0d6efd;
                    padding: 6px 14px;
                    border-radius: 20px;
                    font-size: 14px;
                    font-weight: bold;
                }}
                p {{ color: #555; line-height: 1.6; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🐳 Hello from Inside Docker!</h1>
                <p>Congratulations, your container is running successfully!</p>
                <div class="tag">Environment: {ENVIRONMENT}</div>
                <p style="margin-top: 20px; font-size: 13px; color: #888;">
                    Host Port 8080 &rarr; Container Port {PORT}
                </p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    print(f"🚀 Server started at http://0.0.0.0:{PORT}")
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()
