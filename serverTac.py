import socket
import sys
from threading import Thread

# Defining variables
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
# dictionary for when player = 1 is O, then player = 4 is X.
num2Eng = {0: ' ', 1: 'O', 4: 'X'}
# points which index is available
available = [(i, j) for i in range(3) for j in range(3)]
# Event Listener for each box
pointerEL = {(i * 3) + j + 1: (i, j) for i in range(3) for j in range(3)}
# keeps ports
player_list = []
#keeps client sockets
player_socket = []

# Server Initialization
def start_server():
    host = ""
    port = 8888

    # Create socket
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")


    # Binding
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print("Bind failed. Error : " + str(e))
        sys.exit()

    # Listening
    ServerSocket.listen(5)
    print("Socket now listening")

    while True:
        connection, address = ServerSocket.accept()
        ip, port = str(address[0]), str(address[1])
        player_socket.append(connection)
        #broadcastMessage("This is a broadcast message!")
        print("Connected with " + ip + ":" + port)
        try:
            Thread(target=threaded_client, args=(connection, ip, port)).start()
        except socket.error as e:
            print("Thread did not start." + str(e))
            ServerSocket.close()


# Receive  message from client to determine either they want to play or not
def threaded_client(c, ip, port):
    global board, num2Eng, available
    player_list.append(port)
    print("Player " + str(len(player_list)) + " port: " + str(port))

    while True:
	# Receive Yes or No input from client
        data = c.recv(1024).decode()
	# Break if there is no input or error
        if not data:
            print('break')
            break
	# Verify input
        print("from connected user: " + str(data))
        if (data == "Yes"):
            # Initialise/reset board and event listeners
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            num2Eng = {0: ' ', 1: 'O', 4: 'X'}
            available = [(i, j) for i in range(3) for j in range(3)]
            initGame(c, ip)
	# Break if client want to quit
        elif (data == "No"):
            break

# prints board containing indexes
def genBoardMessage():
    s = ''
    for i in range(5):
        s += ' '
        for j in range(3):
            if i % 2 == 0:
                s += ' ' + num2Eng[board[i // 2][j]] + ' '
                if j == 0 or j == 1: s += '|'
            else:
                s += '--- '
        s += '\n'
    return s
# prints plain board with numbers JUST to display initially
def genBoardIndex():
    s = ''
    for i in range(5):
        s += ' '
        for j in range(3):
            if i % 2 == 0:
                s += ' ' + str(((i // 2) * 3) + j + 1) + ' '
                if j == 0 or j == 1: s += '|'
            else:
                s += '--- '
        s += '\n'
    return s


# To check the result for the client
def checkWin():
    if len(available) == 0:
        return "Draw"

    # check all rows for O
    for i in range(3):
        if sum(board[i]) == 3:
            return 'O Wins!'
        # check all rows for X
        elif sum(board[i]) == 12:
            return 'X Wins!'
# check all columns
    for kolum in range(3):
        sumKol=0
        for row in range(3):
            sumKol = sumKol + board[row][kolum]
            if sumKol == 3:
                return 'O Wins!'
            elif sumKol == 12:
                return 'X Wins!'
    # check first diagonal that looks like \
    if ((board[0][0])+(board[1][1])+(board[2][2]))== 3:
        return 'O Wins!'
    elif ((board[0][0])+(board[1][1])+(board[2][2]))== 12:
        return 'X Wins!'
    # check second diagonal that looks like /
    if ((board[0][2])+(board[1][1])+(board[2][0]))== 3:
        return 'O Wins!'
    elif ((board[0][2])+(board[1][1])+(board[2][0]))== 12:
        return 'X Wins!'
    # return when there is no winner or draw.
    return 'No'


 # Determine the client's moves and removes from the avaiable spots in the grid
def playerMove(player, data):
    i = int(data[0])
    j = int(data[1])
    if player == 4:
        print("X at(", i, j,")")
    else:
        print("O at(", i, j,")")

    # send index to board.
    board[i][j] = player
    # removes available slots on "board" when inserted
    available.pop(available.index((i, j)))

# sends message to all clients simultaneously
def broadcastMessage(msg):
    for x in player_socket:
        x.send(msg.encode())

# Receive input from the client whether they want to be X or O
def initGame(conn, ip):
    message = genBoardIndex() + "\n\nDo you want to be O or X? [O/X]: "
    conn.send(message.encode())
    #receives X or O from client
    data = conn.recv(1024).decode()
    print(ip + " is", data)
    if data.upper() == 'X':
        player1 = 4
        player2 = 1
    else:
        player2 = 4
        player1 = 1

   # loops while there is no winner
    data = ""

    while checkWin() == 'No':
   # checks if client wants to quit
        if (data != 'quit'):
            firstup = genBoardMessage()
            broadcastMessage(firstup)
            #conn.send(firstup.encode())
            data = conn.recv(1024).decode()
            # sends inputted index to grid when client inputs index 
            data = pointerEL[int(data)]
            playerMove(player1, data)
            if checkWin() != 'No':
                break
            # generates updated board n broadcasts.
            #updated = genBoardMessage()
            #broadcastMessage(updated)
            # if checkWin returns Yes
        if data == 'quit':
            sys.exit()
            if checkWin() != 'No':
                break
    #    else:
   #         data = pointerEL[int(data)]
  #          playerMove(player1,data)
 #           if checkWin() != 'No':
#                break
    # when checkWin == Yes
    message = genBoardMessage() + '\n\n' + checkWin()
    broadcastMessage(message)


if __name__ == "__main__":
    start_server()
