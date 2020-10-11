import random
# creates general scope for these variables
board = [' ' for pos in range(10)]
move = 0

def printBoard(board):
        print(' ', board[1], ' | ', board[2], ' | ', board[3], ' ')
        print('------------------')
        print(' ', board[4], ' | ', board[5], ' | ', board[6], ' ')
        print('------------------')
        print(' ', board[7], ' | ', board[8], ' | ', board[9], ' ')

# handles chosen moves by user and comp
def inputLetter(letter, move):
    board[move] = letter

# returns bool whether space if free, move-1 as I need to ignore index 0
def isBoxFree(board, move):
    return board[int(move)] == ' '

# return bool whether num of free spaces is greater than 1, index 0 will always stay empty
def boardNotFull(board):
    return board.count(' ') > 1

# chaining bool values for all winning combinations; not possible to cut up lines after 'or' or with '\n'
def isWinner(board, char):
    return (board[1] == char and board[2] == char and board[3] == char) \
           or (board[4] == char and board[5] == char and board[6] == char) \
           or (board[7] == char and board[8] == char and board[9] == char) \
           or (board[1] == char and board[4] == char and board[7] == char) \
           or (board[2] == char and board[5] == char and board[8] == char) \
           or (board[3] == char and board[6] == char and board[9] == char) \
           or (board[1] == char and board[5] == char and board[9] == char) \
           or (board[7] == char and board[5] == char and board[3] == char)


def userMove(board):
    # and maybe while here is nonsense, as the comp and user must take turns! but no time to rething the code now.
    validMove = False
    while not validMove:
        move = input("Choose a number 1-9 to place your 'X': ")
        try:
            if 0 < int(move) < 10:
                if isBoxFree(board,move):
                    inputLetter('X', int(move))
                else:
                    print("The box is taken. Choose again.")
            else:
                print("You must type a NUMBER between 1-9!")
        except ValueError:
            print('You must type a NUMBER!')
        finally:
            printBoard(board)


def compMove(board):
    move = 0
    # generates all possible moves that comp can take
    possibleMoves = []
    for x, letter in enumerate(board):
        if board[x] == ' ' and x != 0:
            possibleMoves.append(x)

    # creates board copy to loop through and check if comp can take winning move
    testBoard = board[:]

    # series of elif statements in order of priority from top to bottom; where comp needs to move next
    for x in possibleMoves:
        if isWinner(testBoard, 'O'):
            # return inputLetter('O', move)
            return move
        elif 5 in possibleMoves:
            # return inputLetter('O', move)
            return move
        elif x in [1,3,7,9]:
            possibleCorners = []
            possibleCorners.append(x)
            if len(possibleCorners) > 0:
                move = random.choice(possibleCorners)
            # return inputLetter('O', move)
            return move
        elif x in [2,4,6,8]:
            possibleEdges = []
            if len(possibleEdges) > 0:
                move = random.choice(possibleEdges)
            # return inputLetter('O', move)
            return move
    return inputLetter('O', move)
# one elif statement missing - how comp can block the user from winning on next move.

# prepracoval jsem while cyklus pro stridani user- a compMove.
# nadefinoval jsem nove funcki pro vepisovani zvoleneho pole. tam jsem se musel insirovat na webu.
# kazdopadne program se chova nahodile - nekdy comp policko obsadi, casto vubec ne. nemuzu prijit na to proc.
def program():
    print('Ready to play TicTacToe? Let\'s start.')
    printBoard(board)
    while boardNotFull(board):
        if not isWinner(board, 'O'):
           userMove(board)
           inputLetter('X', move)
           if isWinner(board, 'X'):
                print("You beat the computer.")
                break

        if not isWinner(board, 'X'):
            compMove(board)
            inputLetter('O', move)
            if isWinner(board, 'O'):
                print("The computer beat you. Better luck next time.")
                break

    else:
        print("It's a tie game. Nobody wins.")


program()


# inactive part of code for now - replay feature
# playAgain = True
#
# while playAgain:
#     play_again = input("Play again? (Y / N): ")
#     print(play_again)
#     if play_again == 'Y':
#         program()
#     else:
#         print("Thank you for playing. Good bye!")

