'''
This a terminal simulation
of Connect 4 Game
Via Python
'''

# import required modules
from os import system
from termcolor import colored

# Creating colored circles
greenCircle = colored(u'\u25C9', 'green')
yellowCircle = colored(u'\u25C9', 'yellow')
blueCircle = colored(u'\u25C9', 'blue', attrs=['bold'])

# Players Name
# P1 = input("Please Enter Player 1 name: \n")
# P2 = input("Please Enter Player 2 name: \n")

P1 = "Hossein"
P2 = "Hana"
turn = P1

# initializing gameboard matrix
gameBoardMatrix = []

# Creating 6 X 7 matrix to produce game board
for row in range(6):
    tempRowList = []

    for column in range(7):
        tempRowList.append(blueCircle)

    gameBoardMatrix.append(tempRowList)


# Print playing board to user with the player name
def boardToScreen(list, playerName=True):

    # clear screen
    try:
        system('clear')  # for unix
    except:
        system('cls')  # for windows

    # output a black line
    print()

    for num in range(len(list[0])):
        print(num + 1, end=" ")

    # output a black line
    print()

    for row in list:

        for rowB in row:
            print(rowB, end=" ")

        print("")

    # Print out player name
    if playerName:
        print("\n" + turn + " it\'s your turn, select a column:")


'''
This is the function in which I check
if any of the players have won the game
based on checkWinH, checkWinV and checkWinD
functions. If none of these functions
returns True value the checkWinTotal
function returns False value which
means nobody has won the game yet
'''


# check win Total
def checkWinTotal(list, player):

    if checkWinH(list, player):
        boardToScreen(gameBoardMatrix)
        return True

    if checkWinV(list, player):
        boardToScreen(gameBoardMatrix)
        return True

    if checkWinD(list, player):
        boardToScreen(gameBoardMatrix)
        return True

    return False


# Check win Horizontal
def checkWinH(list, player):
    # initially, there is no winner
    win = False

    # determine player color
    if player == P1:
        boxColor = greenCircle
    else:
        boxColor = yellowCircle

    # find row center
    center = len(list[0]) // 2

    # if the center is free return false
    # because it's not possible to connect
    # four box without filling center box
    for row in range(len(list) - 1, -1, -1):
        if list[row][center] is blueCircle:
            return False

        # count same color as center for this row
        # of course horizontal winner owns
        # the center horizontal box
        centerValue = list[row][center]
        sameAsCenter = 0
        for box in list[row]:
            if box is centerValue:
                sameAsCenter += 1

        # now if there are at least four boxes
        # equal to center value there could be a
        # winner in this row
        if sameAsCenter >= 4:
            # used to determine connected boxes
            connected = 0
            # used to move comparing box
            currentBox = 0

            for i in range(len(list[row])):
                if list[row][currentBox] is list[row][i]:
                    win = True
                    connected += 1

                    # when there are exactly 4 same color box connected together
                    if connected is 4:
                        break

                # if the center box is not the same color
                # as it's contiguous box this row could
                # not have a winner, so let's go to next row
                elif i > center:
                    win = False
                    connected = 1
                    break

                else:
                    currentBox = i
                    # Becuase it does not count itself
                    connected = 1
                    win = False

            if win:
                return True

        # if there are not at least four
        # boxes with same value as center
        # box, so let's check next row
        else:
            continue


# Check win Vertical
def checkWinV(list, player):
    # initially, there is no winner
    win = False

    # determine player color
    if player == P1:
        boxColor = greenCircle
    else:
        boxColor = yellowCircle

    # find row center or center adjacent
    center = len(list) // 2

    # matrix width
    matrixWidth = len(list[0])

    # matrix height
    matrixHeight = len(list)

    # if the center is free go to next column
    # because it's not possible to have four
    # connected boxes without filling the
    # center box
    for column in range(matrixWidth):
        if (list[center][column] is blueCircle
                or list[center][column] != list[center - 1][column]):
            continue

        # count colored boxes for each player
        yellowBox = 0
        greenBox = 0

        for box in range(matrixHeight):
            if list[box][column] is yellowCircle:
                yellowBox += 1
            elif list[box][column] is greenCircle:
                greenBox += 1

        # now if there are at least four boxes
        # with equal colors, this column could
        # have a winner, so let's check if at least
        # four same color boxes are connected together
        if yellowBox >= 4 or greenBox >= 4:
            # return True
            connected = 0
            currentBox = 0
            for i in range(len(list)):
                if list[currentBox][column] is list[i][column]:
                    win = True
                    connected += 1
                    # when there are exactly 4 same color box connected together
                    if connected is 4:
                        break
                elif i >= center:
                    win = False
                    break
                else:
                    currentBox = i
                    # Becuase it does not cout itself
                    connected = 1
                    win = False
            if win:
                return True

        # if there are not at least four same
        # color boxes in this column, let's
        # check next column
        else:
            continue


# Check Diagonal win
def checkWinD(list, player):

    # finding row center
    rowCenter = len(list) // 2
    # finding column center
    columnCenter = len(list[0]) // 2

    # determine player color
    if player == P1:
        playerColor = greenCircle
    else:
        playerColor = yellowCircle
    '''
    These 4 for loops try to check all
    possible diagonal lines which could
    potentially have at least four
    same color boxes and at the same time
    check if at least four of these same color
    boxes are connected.
    '''
    for i in range(rowCenter):
        connected = 1

        for j in range(len(list)):
            tempRow = i + j
            tempColumn = j

            if (tempColumn >= len(list[0]) - 1 or tempRow >= len(list) - 1):
                break

            if (list[tempRow][tempColumn] is playerColor
                    and list[tempRow + 1][tempColumn + 1] is playerColor):
                connected += 1

                # Player won
                if connected is 4:
                    return True

            # restart counter
            else:
                connected = 1

    for i in range(columnCenter + 1):
        connected = 1

        for j in range(len(list)):
            tempRow = j
            tempColumn = j + i

            if (tempColumn >= len(list[0]) - 1 or tempRow >= len(list) - 1):
                break

            if (list[tempRow][tempColumn] is playerColor
                    and list[tempRow + 1][tempColumn + 1] is playerColor):
                connected += 1

                # Player won
                if connected is 4:
                    return True

            else:
                connected = 1

    for i in range(len(list) - 1, rowCenter - 1, -1):
        connected = 1

        for j in range(len(list)):
            tempRow = i - j
            tempColumn = j

            if tempRow is 0:
                continue

            if (list[tempRow][tempColumn] is playerColor
                    and list[tempRow - 1][tempColumn + 1] is playerColor):
                connected += 1

                # Player won
                if connected is 4:
                    return True

            else:
                connected = 1

    for i in range(1, len(list[0])):
        connected = 1

        for j in range(len(list)):
            tempRow = len(list) - 1 - j
            tempColumn = i + j

            if (tempRow is 0 or tempColumn >= len(list[0]) - 1):
                continue

            if (list[tempRow][tempColumn] is playerColor
                    and list[tempRow - 1][tempColumn + 1] is playerColor):
                connected += 1

                # Player won
                if connected is 4:
                    return True

            else:
                connected = 1


# Display Gmae Board to players
# and clear the screen
boardToScreen(gameBoardMatrix)


'''
change variable determines if the player should change
or not. in these cases the player should change:
- if choose a full column
- if choose a column which is out of range
- if enter a string instead of an integer
'''
change = True

# check range possible errors
rangeError = False

'''
intError variable is defined to
check if there is any error in the
converting string to integer process 
'''
intError = False

# to determine if anybody has won the game
winGame = False

'''
The game starts and continues in
this loop until a player wins the game
'''
while True:

    if winGame:
        boardToScreen(gameBoardMatrix, False)
        winnerStr = colored(turn, 'green', attrs=['bold'])
        winnerStr += ", you are the "
        winnerStr += colored("Winner!!!", 'red', attrs=['bold', 'blink'])
        print("\n" + winnerStr + "\n")
        break

    if change:
        boardToScreen(gameBoardMatrix)
        change = False

    # let the player now the entered number
    # in out of the range
    elif rangeError:
        print(turn + "," + " please enter a number between from 1 to",
              len(gameBoardMatrix[0]))
        rangeError = False

    # if it's not possible to convert
    # entered value to integer ask player
    # to enter a valid input
    elif intError:
        print(turn + "," + " please inter a valid number:")
        intError = False

    # if the column is full player should choose another one
    else:
        print(turn + "," + " this column is full please choose anther one!")

    # try to convert user input to an integer
    try:
        decision = int(input())

        # if the entered number is out of the range
        if decision > len(gameBoardMatrix[0]) or decision < 1:
            rangeError = True
            continue
    # if it's not possible to convert
    # entered value to integer
    except ValueError:
        intError = True
        continue

    if turn == P1:
        # filling game board from the last row
        for row in range(len(gameBoardMatrix) - 1, -1, -1):
            if gameBoardMatrix[row][decision - 1] == blueCircle:
                gameBoardMatrix[row][decision - 1] = greenCircle
                # check if this player has won the game
                # stop this for loop and change the
                # winGame value to True, so the while
                # loops also will exit and the shows the
                # winner palyer
                if checkWinTotal(gameBoardMatrix, P1):
                    winGame = True
                    break
                # if not change the player
                else:
                    change = True
                    turn = P2
                    break

    else:
        # filling game board from the last row
        for row in range(len(gameBoardMatrix) - 1, -1, -1):
            if gameBoardMatrix[row][decision - 1] == blueCircle:
                gameBoardMatrix[row][decision - 1] = yellowCircle
                # check if this player has won the game
                # stop this for loop and change the
                # winGame value to True, so the while
                # loops also will exit and the shows the
                # winner palyer
                if checkWinTotal(gameBoardMatrix, P2):
                    winGame = True
                    break
                # if not change the player
                else:
                    change = True
                    turn = P1
                    break
