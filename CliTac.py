import socket


def cli_prog():
	host = '192.168.0.66'
	port = 8080

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))


	s.close()


if __name__ == '__main__':
	cli_prog()

