import socket
import threading





PORT = 5050
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[NEW Connection] {addr} connected')
    connected= True
    while connected:
        msg = conn.recv(1024).decode('utf-8')
        if msg:
            print(msg)
            if str(msg) == 'DISCONNECT':
                print(f'disconnect message received form client, will close connection now.')
                connected= False 
    conn.close()

def start():
    server.listen()
    print(f"listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTION] {threading.activeCount() -1}')



print('Serer is starting...')
start()
