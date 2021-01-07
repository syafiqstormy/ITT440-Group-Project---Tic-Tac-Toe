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
	soc.listen(5)
	print("Listening for connections...")

	#Thread start
	while True:
		conn, address = ServerSocket.accept()
		print('Connected to:' + address[0] +':'+str(address[1]))
		start_new_thread(threaded_client, (conn, address))
		ThreadCount += 1
		print('Thread Number:' + str(ThreadCount))
	ServerSocket.close()


# fx send prompt to client to receive input to play game [yes or no]
# send  table with 1-9 visible also

def threaded_client(conn, addr):

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


#generate grid index
def generateGridIndex():


#receive input from player whether X or O


#check if win


#check if tie



if __name__ == "__main__":
	server_start()
