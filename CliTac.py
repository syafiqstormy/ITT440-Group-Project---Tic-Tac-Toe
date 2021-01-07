import socket
import os


# Client program
def client_program():
	host = '192.168.0.66'
	port = 8080


	os.system('clear')
	ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	try:
		ClientSocket.connect((host,port))
	except socket.error as e:
		print(str(e))
		sys.exit()

	#Receive input to send to server whether to play or not.
	while True:
		Input = input('Play? Enter Y or N :')
		if Input == '':
			print("Invalid input!")
			Input = input('Play?Enter Y or N :')
	#Converts input to uppercase and removes whitespaces
	while Input.upper().strip() != 'N':
		ClientSocket.send(Input.encode('utf-8'))
		data = ClientSocket.recv(1024).decode('utf-8')

		Response = ClientSocket.recv(1024)
		if len(Response)!=0:
			print(Response.decode('utf-8')



if __name__ == '__main__':
	client_program()


	ClientSocket.close()
