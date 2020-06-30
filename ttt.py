def react(board,a,b,turns):
    if turns == 9:
        return board
    for i in range(3):
        val,val2 = countrow(i)
        if val2 == 2 and val == 0:
            s,d = counterow(i)
            board[s][d] = "O"
            return board
        val,val2 = countdown(i)
        if val2 == 2 and val == 0:
            s,d = countedown(i)
            board[s][d] = "O"
            return board
    diaga,diagb,i,j = countright()
    if diaga == 0 and diagb == 2:
        board[i][j] = "O"
        return board
    diaga,diagb,i,j = countleft()
    if diaga == 0 and diagb == 2:
        board[i][j] = "O"
        return board
    #####
    if turns == 1:
        if board[1][1] != "X":
            board[1][1] = "O"
            return board
        else:
            board[0][0] = "O"
            return board
    rowa,rowb = countrow(a)
    if (rowa == 2 and rowb == 0):
        i,j = counterow(a)
        board[i][j] = "O"
        return board
    downa, downb = countdown(b)
    if (downa == 2 and downb == 0):
        i,j = countedown(b)
        board[i][j] = "O"
        return board
    if (a == 0 and b == 0) or (a == 2 and b == 2) or (a == 1 and b == 1):
        diaga,diagb,i,j = countright()
        if (diaga == 2 and diagb == 0):
            board[i][j] = "O"
            return board
    if (a == 2 and b == 0) or (a == 1 and b== 1) or (a == 0 and b == 2):
        diaga,diagb,i,j = countleft()
        if (diaga == 2 and diagb == 0):
            board[i][j] = "O"
            return board
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                return board
def countright():
    cntx,cnto,empty = 0,0,[None,None]
    for i in range(3):
        if board[i][i] == "O":
            cnto += 1
        elif board[i][i] == "X":
            cntx += 1
        else:
            empty = [i,i]
    return cntx,cnto,empty[0],empty[1]
def countleft():
    cntx,cnto,empty = 0,0,[None,None]
    for i in range(3):
        if board[i][2-i] == "O":
            cnto += 1
        elif board[i][2-i] == "X":
            cntx += 1
        else:
            empty = [i,2-i]
    return cntx,cnto,empty[0],empty[1]
def countrow(a):
    cntx = 0
    cnto = 0
    for val in board[a]:
        if val == "X":
            cntx += 1
        if val == "O":
            cnto += 1
    return cntx,cnto
def countdown(b):
    cntx = 0
    cnto = 0
    for i in range(3):
        if board[i][b] == "X":
            cntx += 1
        if board[i][b] == "O":
            cnto += 1
    return cntx,cnto
def counterow(a):
    for i in range(3):
        if board[a][i] == "":
            return a,i
def countedown(b):
    for i in range(3):
        if board[i][b] == "":
            return i,b
def check(board):
    for i in range(3):
        val,val2 = countrow(i)
        if (val2 == 3 and val == 0) or (val2 == 0 and val == 3):
            return True
        val,val2 = countdown(i)
        if (val2 == 3 and val == 0) or (val == 3 and val2 == 0):
            return True
    diaga,diagb,i,j = countright()
    if (diaga == 0 and diagb == 3) or (diagb == 0 and diaga == 3):
        return True
    diaga,diagb,i,j = countleft()
    if (diaga == 0 and diagb == 3) or (diagb == 0 and diaga == 3):
        return True
    return False
board = [["","",""],
         ["","",""],
         ["","",""]]
turns = 0
while turns < 9:
    print(board[0])
    print(board[1])
    print(board[2])
    while True:
        pair = input("Choose an empty position ")
        if int(pair[0]) in range(0,3) and int(pair[2]) in range(0,3) and board[int(pair[0])][int(pair[2])] == "":
            board[int(pair[0])][int(pair[2])] = "X"
            break
    turns += 1
    board = react(board,int(pair[0]),int(pair[2]),turns)
    if check(board):
        break
    turns += 1
print(board[0])
print(board[1])
print(board[2])
    
    
