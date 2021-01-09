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
		#if Input == '':
		#	print("Invalid input!")
		#	Input = input('Play?Enter Y or N :')
	#Converts input to uppercase and removes whitespaces
	Input = Input.upper().strip()
	while Input != 'N':
		ClientSocket.send(Input.encode('utf-8'))
		While True:
		Response = ClientSocket.recv(1024).decode()
		#Receive input Do you want to be X or O?
		if len(Response)!=0:
			print(Response.decode())
		x = re.search("Do",(str(Response)))
		#if message contains option X or O do
		if x:
			playeropt = input("->")
			playeropt = playeropt.upper()
			ClientSocket.send(playeropt.encode())
			Response= ClientSocket.recv(1024).decode()
		while "Win" or "Tie" not in Response:
			print("\nBoard:\n+ Response)
			while True:
				prompt = input("Enter index [1-9]")
				if message in [str(i+1) for in range(9)]:
					break
				print("Please enter index [1-9]")
			ClientSocket.send(prompt.encode())
			data = s.recv(1024).decode()
			print(data)



if __name__ == '__main__':
	client_program()


	ClientSocket.close()
