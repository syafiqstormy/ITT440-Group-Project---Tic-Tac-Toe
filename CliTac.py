#Client Side code 

import socket
import sys
import os


host = '192.168.0.136'
port = 8888
os.system('clear')

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
    print("Connection error")
    sys.exit()

print("\n===============================")
print("Do you want to play? Yes or No")
while True:
    message = input(' -> ').strip()
    if message in ('Yes', 'No'):
        break

while message.lower().strip() != 'No':
    ClientSocket.send(message.encode())
    data = ClientSocket.recv(1024).decode()
    while True:
        print("\n" + data)
        player = input().strip()
        if player.upper() in ('O', 'X'):
            break
        print('Please Enter O or X')
    ClientSocket.send(player.encode())
    data = ClientSocket.recv(1024).decode()
    while "Win" not in data:
        print("\nBoard:\n" + data)
        while True:
            message = input('Please Enter number 1-9 for index, or enter <r> to display board\n')
            if message in [str(i+1) for i in range(9)] + ['r']:
                break
           
        ClientSocket.send(message.encode())
        data = ClientSocket.recv(1024).decode()
    print(data)

    print("\n===============================")
    print("Do you want to play again? Yes or No")
    message = input(" -> ")
    if message == "No":
        print("Thanks for playing!")
        ClientSocket.close()
        sys.exit()

