import threading 
import http
import socketserver
from logger import logger

def start_server():
  """
  This is to run a simple webserver to use with uptimerobot. Add https://[Project name].[Replit Username].repl.co to https://uptimerobot.com
  """
  logger.log("Starting webserver", "THREAD")
  server_thread = threading.Thread(target=run_server)
  server_thread.start()


def run_server(PORT=8000, logging=False):
  class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
      pass
      
    def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(b"200 OK")


  with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    logger.log(f"Webserver serving at port {PORT}", "THREAD")
    httpd.serve_forever()
