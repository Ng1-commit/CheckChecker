import random

def generateRandomPieceSet():
    whitepieces = ['R', 'N', 'B', 'Q', 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    blackpieces = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
    
    
    #blackpieces = [item.lower() for item in whitepieces]

    wP = ["K"]
    bP = ["k"]

    numBP = random.randint(1, 15)
    numWP = random.randint(1, 15)

    for i in range(numBP):
        bP.append(blackpieces.pop(random.randint(0, len(blackpieces) - 1)))

    for i in range(numWP):
        wP.append(whitepieces.pop(random.randint(0, len(whitepieces) - 1)))

    return wP, bP

def generateboard():

    board = {}
    for i in range(1, 9):
        for j in range(1, 9):
            board[(i, j)] = ''
    return board

def getrandomcoordinates():
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    return x, y

def placepieces(board, pieces):

    for colour in pieces:
       for piece in colour:
            while True:
                x, y = getrandomcoordinates()
                if board[(x, y)] == '':
                    if piece == 'P' or piece == 'p':
                        if y == 1 or y == 8:
                            continue
                    board[(x, y)] = piece
                    break
                else:
                    continue
    return board

def isWhiteKingInCheck(board):
    colour = 'w'
    isKingInCheck = False
    for i in range(1,9):
        for j in range(1,9):
            if board[(i, j)] == 'K':
                WKing = (i, j)
            else:
                continue

    print(chr(WKing[0] +96) + ',' + str(WKing[1]))
    #print(WKing)

    file = isKingInCheckOnFile(board, WKing, colour) 
    if file == True:
    	print('Rank')
    	return file
    rank = isKingInCheckOnRank(board, WKing, colour)
    if rank == True:
    	print('File')
    	return rank
    diagonal = isKingInCheckOnDiagonal(board, WKing, colour) 
    if diagonal == True:
    	print('Diagonal')
    	return diagonal
    knight = isKingInCheckFromKnight(board, WKing, colour)
    if knight == True:
    	print('Knight')
    	return knight
    return isKingInCheck

def isKingInCheckOnFile(board, kingPos, colour):
    currentKingPos = list(kingPos)
    if colour == 'w':
        #check to left
        while currentKingPos[0] - 1 > 0:
            currentKingPos[0] -= 1
            if board[(currentKingPos[0], currentKingPos[1])] == '': 
                continue
            elif board[(currentKingPos[0],  currentKingPos[1])] in [ 'q', 'r']:
                return True
            else:
                return False
        #check to right
        #reset king pos 
        currentKingPos = list(kingPos)
        while currentKingPos[0] + 1 < 8:
            currentKingPos[0] += 1
            if board[(currentKingPos[0], currentKingPos[1])] == '': 
                continue
            elif board[(currentKingPos[0],  currentKingPos[1])] in [ 'q', 'r']:
                return True
            else:
                return False

def isKingInCheckOnRank(board, kingPos, colour): 
    
    currentKingPos = list(kingPos)

    if colour == 'w':
        #check below
        while currentKingPos[1] - 1 > 0 and currentKingPos[0] - 1 > 0:
            currentKingPos[0] -= 1
            if board[(currentKingPos[0], currentKingPos[1])] == '': 
                continue
            elif board[(currentKingPos[0],  currentKingPos[1])] in [ 'q', 'r']:
                return True
            else:
                return False
        #check above
        #reset king pos 
        currentKingPos = list(kingPos)
        while currentKingPos[0] + 1 <= 8:
            currentKingPos[0] += 1
            if board[(currentKingPos[0], currentKingPos[1])] == '': 
                continue
            elif board[(currentKingPos[0],  currentKingPos[1])] in [ 'q', 'r']:
                return True
            else:
                return False

def isKingInCheckOnDiagonal(board, kingPos, colour): # to fix on a keyboard
 
    currentKingPos = list(kingPos)
    if colour == 'w':
        #check below to the left
        while currentKingPos[0] - 1 > 0 and currentKingPos[1] - 1 > 0:
            currentKingPos[0] -= 1
            currentKingPos[1] -= 1
            if board[(currentKingPos[0], currentKingPos[1])] == '': 
                continue
            elif board[(currentKingPos[0],  currentKingPos[1])] in ['q', 'b']:
                print(str(kingPos) + 'below left')
                return True
            else:
                return False
        #check below to the right
        #reset king pos 
        currentKingPos = list(kingPos)
        while currentKingPos[0] +1  <8 and currentKingPos[1] - 1 >0:
            currentKingPos[0] += 1
            currentKingPos[1] -= 1
            if board[(currentKingPos[0], currentKingPos[1])] == '': 
                continue
            elif board[(currentKingPos[0],  currentKingPos[1])] in ['q', 'b']:
                print(str(currentKingPos) + 'below right')
                return True
            else:
                return False
        #check above to the right
        #reset king pos 
        currentKingPos = list(kingPos)
        possiblePieces = ['q', 'b', 'p']
        while currentKingPos[0] + 1 < 8 and currentKingPos[1] + 1 < 8:
            currentKingPos[0] += 1
            currentKingPos[1] += 1
            if board[(currentKingPos[0], currentKingPos[1])] == '':
                possiblePieces = ['q', 'b']
                continue
            elif board[(currentKingPos[0],  currentKingPos[1])] in possiblePieces:
                print(possiblePieces)
                print(str(currentKingPos)  + 'above and right')
                return True
            else:
                return False
        #check above to the left
        #reset king pos 
        currentKingPos = list(kingPos)
        possiblePieces = ['q', 'b', 'p']
        while currentKingPos[0] - 1 < 0 and currentKingPos[1] + 1 > 8:
            currentKingPos[0] -= 1
            currentKingPos[1] += 1
            if board[(currentKingPos[0], currentKingPos[1])] == '':
                possiblePieces = ['q', 'b']
                continue
            elif board[(currentKingPos[0],  currentKingPos[1])] in possiblePieces:
                print(possiblePieces)
                print(str(currentKingPos)  + 'above and left')
                return True
            else:
                return False

def doesKnightAttackSquare(kingPos):
	 
	 x = kingPos[0]
	 y = kingPos[1]
	 
	 attackedSquares = [ 
	 (x-1, y-2), (x-1, y+2),
	 (x-2, y-1),(x-2, y+1),
	 (x+1, y-2), (x+1, y+2), 
	 (x+2, y+1), (x+2, y-1)
	 ]
	 
	 return attackedSquares

def isKingInCheckFromKnight(board, kingPos, colour): 
	if colour == 'w':
			for square in doesKnightAttackSquare(kingPos):
				try:
					if board[(square)] == 'n':
						return True
				except:
					continue
					
	return False 
				
def printBoard(board):
    for j in range(8 ,0, -1):
        for i in range(1, 9):
            if not board[(i, j)] == '': 
                print("| " + board[(i, j)], end=" |")
            else:
                print("|  ", end=" |")
        print()

def test():
    pieces = generateRandomPieceSet()
    board = generateboard()
    #board = {(1, 1): '', (1, 2): 'p', (1, 3): '', (1, 4): '', (1, 5): 'p', (1, 6): '', (1, 7): 'p', (1, 8): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): 'p', (2, 7): 'p', (2, 8): '', (3, 1): '', (3, 2): 'K', (3, 3): 'p', (3, 4): '', (3, 5): '', (3, 6): '', (3, 7): 'p', (3, 8): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (4, 7): '', (4, 8): '', (5, 1): '', (5, 2): 'p', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (5, 7): '', (5, 8): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): 'p', (6, 7): '', (6, 8): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (7, 7): '', (7, 8): '', (8, 1): '', (8, 2): '', (8, 3): 'k', (8, 4): '', (8, 5): '', (8, 6): 'p', (8, 7): 'p', (8, 8): ''}
    placepieces(board, pieces)
    print(str(board))
    printBoard(board)
    return isWhiteKingInCheck(board)
	
isInCheck = False
while isInCheck == False:
	isInCheck = test()
	print('\n')
