#server side 

import socket
import sys
from _thread import *

#init global variables here
# --



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




#generate grid
def generateGrid():
    g = ''
    for i in range(5):
        g += ' '
        for j in range(3):
            if i % 2 == 0:
                g += '   '
                if j == 0 or j == 1: g += '|'
            else:
                g += '--- '
        g += '\n'
    return (g)


#generate grid with numbers
def generateGridNum():
    g = ''
    for i in range(5):
        g += ' '
        for j in range(3):
            if i % 2 == 0:
                g += ' ' + str(((i // 2) * 3) + j + 1) + ' '
                if j == 0 or j == 1: g += '|'
            else:
                g += '--- '
        g += '\n'
    return (g)


#receive input from player whether X or O
def initGame(conn, addr):

#check if win


#check if tie



if __name__ == "__main__":
	server_start()
