import socket
import os
import sys
import re

# Client program
def client_program():
    host = '192.168.0.66'
    port = 8888
    os.system('clear')
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
        sys.exit()
    # Receive input to send to server whether to play or not.
    while True:
        #initOpt = input('Play? Enter Y or N :')
        # // if Input == '': // print("Invalid input!") Input =
        # input('Play?Enter Y or N :') Converts input to uppercase and
        # removes whitespaces
        #initOpt = initOpt.upper().strip()
        initOpt = ClientSocket.recv(1024).decode()
        print(initOpt)
        cliOpt = input('>')
        while cliOpt != 'N':
            ClientSocket.send(cliOpt.encode('utf-8'))
            Response = ClientSocket.recv(1024).decode()
            while True:
            # If response exists
                if len(Response) != 0:
                    print(Response)
                    x = re.search("Do", (str(Response)))
                    # if message contains option X or O do
                    if x:
                        playerOpt = input("->")
                        playerOpt = playerOpt.upper()
                        ClientSocket.send(playerOpt.encode())
                        Response = ClientSocket.recv(1024).decode()
                    while "Win" or "Tie" not in Response:
                        print("\nBoard:\n"+ Response)
                        while True:
                            index = input("Enter index [1-9]")
                            if Response in [str(i+1) for i in range(9)]:
                                break
                            print("vreak code")
                        ClientSocket.send(index.encode())
                        data = ClientSocket.recv(1024).decode()
                    print(data)
                #if response doesnt exit
                else:
                    print("****Server has unexpectedly closed connection****")
                    ClientSocket.close()
                    sys.exit(0)
        print("Thanks for entering. Goodbye")
        sys.exit()
if __name__ == '__main__':
    client_program()

