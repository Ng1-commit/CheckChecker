import random

def generateRandomPieceSet():
    whitepieces = ['R', 'N', 'B', 'Q', 'B', 'N', 'R', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    blackpieces = [item.lower() for item in whitepieces]

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
    
    kingPos = list(kingPos)
    if colour == 'w':
        #check to left
        while kingPos[0] - 1 > 0:
            kingPos[0] -= 1
            if board[(kingPos[0], kingPos[1])] == '': 
                continue
            elif board[(kingPos[0],  kingPos[1])] in [ 'q', 'r']:
                return True
            else:
                return False
        #check to right
        while kingPos[0] + 1 < 8:
            kingPos[0] += 1
            if board[(kingPos[0], kingPos[1])] == '': 
                continue
            elif board[(kingPos[0],  kingPos[1])] in [ 'q', 'r']:
                return True
            else:
                return False

def isKingInCheckOnRank(board, kingPos, colour): 
    
    kingPos = list(kingPos)
    if colour == 'w':
        #check below
        while kingPos[1] - 1 > 0 and kingPos[0] - 1 > 0:
            kingPos[0] -= 1
            if board[(kingPos[0], kingPos[1])] == '': 
                continue
            elif board[(kingPos[0],  kingPos[1])] in [ 'q', 'r']:
                return True
            else:
                return False
        #check above
        while kingPos[0] + 1 <= 8:
            kingPos[0] += 1
            if board[(kingPos[0], kingPos[1])] == '': 
                continue
            elif board[(kingPos[0],  kingPos[1])] in [ 'q', 'r']:
                return True
            else:
                return False

def isKingInCheckOnDiagonal(board, kingPos, colour): # to fix on a keyboard
 
    kingPos = list(kingPos)
    if colour == 'w':
        #check below to the left
        while kingPos[0] - 1 > 0 and kingPos[1] - 1 > 0:
            kingPos[0] -= 1
            kingPos[1] -= 1
            if board[(kingPos[0], kingPos[1])] == '': 
                continue
            elif board[(kingPos[0],  kingPos[1])] in [ 'q', 'b']:
                return True
            else:
                return False
        #check below to the right
        while kingPos[0] - 1 > 0 and kingPos[1] + 1 < 8:
            kingPos[0] -= 1
            kingPos[1] += 1
            if board[(kingPos[0], kingPos[1])] == '': 
                continue
            elif board[(kingPos[0],  kingPos[1])] in [ 'q', 'b']:
                return True
            else:
                return False
        #check above to the right
        while kingPos[0] + 1 < 8 and kingPos[1] + 1 < 8:
            kingPos[0] += 1
            kingPos[1] += 1
            possiblePieces = ['q', 'b', 'p']
            if board[(kingPos[0], kingPos[1])] == '':
                possiblePieces = ['q', 'b']
                continue
            elif board[(kingPos[0],  kingPos[1])] in possiblePieces:
                return True
            else:
                break
        #check above to the left
        while kingPos[0] + 1 < 8 and kingPos[1] - 1 > 0:
            kingPos[0] += 1
            kingPos[1] -= 1
            possiblePieces = ['q', 'b', 'p']
            if board[(kingPos[0], kingPos[1])] == '':
                possiblePieces = ['q', 'b']
                continue
            elif board[(kingPos[0],  kingPos[1])] in possiblePieces:
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
	placepieces(board, pieces)
	printBoard(board)
	return isWhiteKingInCheck(board)
	
isInCheck = False
while isInCheck == False:
	isInCheck = test()
	print('\n')
