import sys
import socket
import time

from websocket import *
import websocket_helper

listen_s = None
client_s = None
ws = None

def setup_server(port, accept_handler):
    global listen_s

    listen_s = socket.socket()
    listen_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    ai = socket.getaddrinfo("0.0.0.0", port)
    addr = ai[0][4]

    listen_s.bind(addr)
    listen_s.listen(1)
    if accept_handler:
        listen_s.setsockopt(socket.SOL_SOCKET, 20, accept_handler)
    return listen_s

def stop():
    global listen_s, client_s, ws
    if client_s:
        client_s.close()
    if listen_s:
        listen_s.close()
    if ws:
        ws.close()

def data_in(sock):
    global ws
    data = ws.read()
    print(data)
    data = data.decode('UTF-8')
    print(data)
    ws.write("cool")
    if data == 'close':
        stop()

def handle_conn(listen_sock):
    global ws
    global client_s
    cl, remote_addr = listen_sock.accept()
    cl.setblocking(False)
    client_s = cl
    websocket_helper.server_handshake(cl)
    ws = websocket(cl)

    cl.setsockopt(socket.SOL_SOCKET, 20, data_in)
    ws.write("connected to server")

def start():
    s = setup_server(8888, handle_conn)
