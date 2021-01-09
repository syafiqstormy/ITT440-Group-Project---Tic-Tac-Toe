#server side 

import socket
import sys
from _thread import *

#init global variables here
# --
board = [' ' for x in range(10)]
player_list = []
count = 0
num2Eng = {0:' ',1:'0',4:'X'}
available = [(i,j) for i in range(3) for j in range(3)] 
pointerEL = {(i*3)+j+1:(i,j) for i in range(3) for j in range(3)}



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
		remove player_list latest data
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
    b = ''
    for i in range(5):
        b += ' '
        for j in range(3):
            if i % 2 == 0:
                b += ' ' + num2Eng[board[i // 2][j]] + ' '
                if j == 0 or j == 1: b += '|'
            else:
                b += '--- '
        b += '\n'
    return b

#player moves
def playerMove(conn,player,data)
    i = int(data[0])
    j = int(data[1])

    if player == 4:
        print("X at", i, j)
    else:
        print("O at", i, j)
    board[i][j] = player
    available.pop(available.index((i, j)))



#check if win
def checkWin()
    #checks if the board is full or not 
    if len(available) == 0:
    #returns draw if board is full
        return "Draw"
    column = [0, 0, 0]
    diagonal = [0, 0]
    for i in range(3):
        if sum(board[i]) == 3:
            return 'O Win!'
        elif sum(board[i]) == 12:
            return 'X Win!'
        for j in range(3):
            if i == j:
                diagonal[0] += board[i][j]
            if i + j == 2:
                diagonal[1] += board[i][j]
            column[j] += board[i][j]
    for i in range(3):
        if column[i] == 3:
            return 'O Win!'
        elif coloumn[i] == 12:
            return 'X Win!'
    for i in range(2):
        if diagonal[i] == 3:
            return 'O Win!'
        elif diagonal[i] == 12:
            return 'X Win!'
    return 'Noone'


#receive input from player whether X or O
def initGame(conn, addr):
	#first player 
	if count == 1
		msgXO = generateBoard() + "\n\nDo you want to be O or X? [O/X]: "
		conn.send(msgXO.encode())
		data = conn.recv(1024).decode()
		print(addr[0] +" is "+ str(data))
	if count == 2
		if data == 'X'
			msgXO = generateBoard() +"\n\nYou are O!"
		else
			msgXO = generateBoard() +"\n\nYou are X!"


	if data == 'X'
		player1 = 4
		player2 = 1
	else
		player1 = 1
		player2 = 4


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
	if checkWin()!="Noone"
		break

message = generateBoard() + '\n\n' + checkWin()
conn.send(message.encode()) 


if __name__ == "__main__":
	server_start()
