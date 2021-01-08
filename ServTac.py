#server side 

import socket
import sys
from _thread import *

#init global variables here
# --
board = [' ' for x in range(10)]


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
    welcome = "**Welcome to the Tic Tac Toe Server! :D**

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
            	sys.exit()

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

#check if win


#check if tie



if __name__ == "__main__":
	server_start()
