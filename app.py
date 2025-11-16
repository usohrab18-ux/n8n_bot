```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"سلام، پروژه‌ات با موفقیت اجرا شد!")

server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHandler)
print("سرور اجرا شد روی پورت 8000...")
httpd.serve_forever()
