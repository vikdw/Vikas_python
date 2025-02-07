import socket

PORT= 5050
SERVER = "0.0.0.0"
ADDR= SERVER,PORT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    msg = msg.encode('utf-8')
    client.send(msg)
send("test")