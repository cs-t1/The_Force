# taken from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate server.pem with the following command:
#    openssl req -new -x509 -keyout key.pem -out server.pem -days 365 -nodes
# run as follows:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443


import http.server
import ssl

server_address = ('localhost', 8080)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
#ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)

httpd.socket = ctx.wrap_socket(sock=httpd.socket,
                               server_side=True,
                               do_handshake_on_connect=True,
                               #server_hostname="localhost",
                                )
httpd.serve_forever()
