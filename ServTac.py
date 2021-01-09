#server side 

import socket
import sys
from _thread import *

#init global variables here
# --
board = [' ' for x in range(10)]
player_list = []
count = 0

#Server Initialization
def server_start():
	host = ''
	port = 8888

	# Create TCP socket
	ServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#Binding
	try: 
		ServerSocket.bind((host, port))
	except socket.error as e:
		print(str(e))
		sys.exit()
	#Listen for connections
	ServerSocket.listen(5)
	print("Listening for connections...")

	#Thread start
	while True:
		conn, address = ServerSocket.accept()
		print('Connected to:' + address[0] +':'+str(address[1]))
		start_new_thread(threaded_client, (conn, address))
		ThreadCount += 1
		print('Thread Number:' + str(ThreadCount))
	ServerSocket.close()


# send grid with number to user

#receive input from clients yes or no to play
def threaded_client(conn, addr):
    welcome = "**Welcome to the Tic Tac Toe Server! :D**\nDo you want to play the game?(yes,no) No to quit"
    player_list.append(conn)
    count = count + 1
    try:
    	#send welcome message to client
        conn.send(welcome.encode(encoding='UTF-8',errors='strict'))
        while True:
        	#receive input from client
            data = conn.recv(2048)
            #break if no input/error
            if not data:
                break
            #verify input
            if (data == "Y"):
            	initGame(conn, addr)
            #client quit
            else:
		#remove player_list latest data
		del player_list[-1]
		count=count -1
		goodbye_msg = "Goodbye"
		print("Client rejected game")
		conn.send(goodbye_msg.encode(encoding='utf-8', errors='strict'))
            	return

    except socket.error as e:
        print("Socket error: %s" % str(e))

    conn.close()




#generate board
def generateBoard():
    print('\t\t\t****************************')
    print('\t\t\t\t ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\t\t\t\t-----------')
    print('\t\t\t\t ' + board[4] + ' | ' +board[5] + ' | ' + board[6])
    print('\t\t\t\t-----------')
    print('\t\t\t\t ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\t\t\t****************************')
















#receive input from player whether X or O
def initGame(conn, addr):
	#first player 
	if count == 1
		msgXO = generateBoard() + "\n\nDo you want to be O or X? [O/X]: "
		conn.send(msgXO.encode())
		data = conn.recv(1024).decode()
		print(addr[0] +" is "+ str(data))
	if data == 'X'
		player1 = 2
		player2 = 4
	else
		player1 = 4
		player2 = 2

data = ""
#While no one has won yet
while checkWin() == 'Noone':
	#sends updated board
	update = generateBoard() + "\nEnter number: " 
	conn.send(update.encode())
	#receive input from client
	data = conn.recv(1024).decode()

	#convert the player move to int to occupy the space in pointer
	data = pointerEL[int(data)]
	playerMove(conn,player1,data)
	if checkWin()!="No"
		break

message = generateBoard() + '\n\n' + checkWin()
conn.send(message.encode()) 


if __name__ == "__main__":
	server_start()
