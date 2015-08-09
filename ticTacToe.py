theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
            }


def printBoard():
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('-+-+-')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-+-+-')
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])

def isWin():
    if theBoard['top-L']==theBoard['top-M']==theBoard['top-R']!=' ' or \
    theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R']!=' ' or \
    theBoard['top-L']==theBoard['top-M']==theBoard['top-R']!=' ' or \
    theBoard['top-L']==theBoard['mid-L']==theBoard['low-L']!=' ' or \
    theBoard['top-M']==theBoard['mid-M']==theBoard['low-M']!=' ' or \
    theBoard['top-R']==theBoard['mid-R']==theBoard['low-R']!=' ' or \
    theBoard['top-L']==theBoard['mid-M']==theBoard['low-R']!=' ' or \
    theBoard['top-R']==theBoard['mid-M']==theBoard['low-L']!=' ':
        return True
    else:
        return False


def checkInput(move):
    if move in theBoard.keys():
        return True
    else:
        return False

turn = 'X'

while ' ' in theBoard.values():
    print('Turn for ' + turn + '. Move on which space?')
    move = input()

    while checkInput(move) == False:
        print('Something is wrong with your input. Please try again:')
        move = input()
    
    if theBoard[move] == ' ':
        theBoard[move] = turn
        if isWin() == True:
            printBoard()
            print(turn + ' is the winner!')
            break;
        else:
            if turn == 'X':
                turn = '0'
            else:
                turn = 'X'
        printBoard()
    else:
        print('This space is already take. Please choose a different space:')
