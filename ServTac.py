import socket
import sys
from threading import Thread

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
num2Eng = {0: ' ', 1: 'O', 4: 'X'}
# points which index is available
available = [(i, j) for i in range(3) for j in range(3)]
# Event Listener for each box
pointerEL = {(i * 3) + j + 1: (i, j) for i in range(3) for j in range(3)}
player_list = []


def start_server():
    host = ""
    port = 8888

    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket created")

    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print("Bind failed. Error : " + str(e))
        sys.exit()

    ServerSocket.listen(5)
    print("Socket now listening")

    while True:
        connection, address = ServerSocket.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=threaded_client, args=(connection, ip, port)).start()
        except socket.error as e:
            print("Thread did not start." + str(e))
            ServerSocket.close()


def threaded_client(c, ip, port):
    global board, num2Eng, available
    player_list.append(port)
    print("Player " + str(len(player_list)) + " port: " + str(port))

    while True:
        data = c.recv(1024).decode()
        if not data:
            print('break')
            break
        print("from connected user: " + str(data))
        if (data == "Yes"):
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            num2Eng = {0: ' ', 1: 'O', 4: 'X'}
            available = [(i, j) for i in range(3) for j in range(3)]
            initGame(c, ip)
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


# prints board with numbers to display initially
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


def checkWin():
    if len(available) == 0:
        return "Draw"
    col = [0, 0, 0]
    diag = [0, 0]
    for i in range(3):
        if sum(board[i]) == 3:
            return 'O Win!'
        elif sum(board[i]) == 12:
            return 'X Win!'
        for j in range(3):
            if i == j:
                diag[0] += board[i][j]
            if i + j == 2:
                diag[1] += board[i][j]
            col[j] += board[i][j]
    for i in range(3):
        if col[i] == 3:
            return 'O Win!'
        elif col[i] == 12:
            return 'X Win!'
    for i in range(2):
        if diag[i] == 3:
            return 'O Win!'
        elif diag[i] == 12:
            return 'X Win!'
    return 'No'


def playerMove(player, data):
    i = int(data[0])
    j = int(data[1])

    if player == 4:
        print("X at", i, j)
    else:
        print("O at", i, j)
    board[i][j] = player
    available.pop(available.index((i, j)))


def initGame(conn, ip):
    message = genBoardIndex() + "\n\nDo you want to be O or X? [O/X]: "
    conn.send(message.encode())
    data = conn.recv(1024).decode()
    print(ip[0] + " is", data)
    if data.upper() == 'X':
        player1 = 4
        player2 = 1
    else:
        player2 = 4
        player1 = 1

    data = ""
    while checkWin() == 'No':
        if (data != 'r'):
            s = genBoardMessage()
            conn.send(s.encode())
        data = conn.recv(1024).decode()

        if data == 'r':
            conn.send(genBoardMessage().encode())
            if checkWin() != 'No':
                break
        else:
            data = pointerEL[int(data)]
            playerMove(player1, data)
            if checkWin() != 'No':
                break

    message = genBoardMessage() + '\n\n' + checkWin()
    conn.send(message.encode())


if __name__ == "__main__":
    start_server()

