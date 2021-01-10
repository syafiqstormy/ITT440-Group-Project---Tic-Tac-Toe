#Client Side code 

import socket
import sys
import os

# Client Initialization 
host = '192.168.0.66'
port = 8888
os.system('clear')

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
    print("Connection error")
    sys.exit()
# Input decision to send to the server whether client want to play or not 
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
    
    # If there is still no winner
    while "Win" not in data:
        print("\nBoard:\n" + data)
	# Input for the index number to send to the server
        while True:
            message = input('Please Enter number 1-9 for index, or enter <r> to display board\n')
            if message in [str(i+1) for i in range(9)] + ['r']:
                break
            # ??
        ClientSocket.send(message.encode())
        data = ClientSocket.recv(1024).decode()
    print(data)

	# Send input if the client want to play again
    print("\n===============================")
    print("Do you want to play again? Yes or No")
    message = input(" -> ")
	# Break if the client type in No
    if message == "No":
        print("Thanks for playing!")
        ClientSocket.close()
        sys.exit()

