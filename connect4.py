'''
This a terminal simulation
of Connect 4 Game
Via Python
'''
'''
Here I defined a function to check if any player won the game
but in the horizontal sense. Acctually, checkWinH stands for
Check Win Horizontal

First of all I check horizontal rows,
if the central box of a horizontal row is not full yet
that row can not have four same color box. so the function
returns False. If not, there are step by step controls as
you can see in function.

'''

# import required modules
import sys
from os import system
from termcolor import colored, cprint

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
def boardToScreen(list, screenClear=True):

    # clear screen
    if screenClear is True:
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
    # print()
    print("\n" + turn + " it\'s your turn, select column:")


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
    win = False
    if player == P1:
        boxColor = greenCircle
    else:
        boxColor = yellowCircle

    # find row center
    center = len(list[0]) // 2

    # if the center free return false
    for row in range(len(list) - 1, -1, -1):
        if list[row][center] is blueCircle:
            return False

        # count same color as center for this row
        centerValue = list[row][center]
        sameAsCenter = 0
        for box in list[row]:
            if box is centerValue:
                sameAsCenter += 1

        # print("same as center:", sameAsCenter)

        # now if there at least four box equal to center
        if sameAsCenter >= 4:
            connected = 0
            currentBox = 0
            for i in range(len(list[row])):
                if list[row][currentBox] is list[row][i]:
                    win = True
                    connected += 1
                    # when there are exactly 4 same color box connected together
                    if connected is 4:
                        break
                elif i > center:
                    win = False
                    connected = 1
                    break
                else:
                    currentBox = i
                    # Becuase it does not count itself
                    connected = 1
                    win = False

            # print("connected:", connected)
            # print("row:", row)
            # print(win)

            if win:
                return True

        else:
            continue


# Check win Vertical
def checkWinV(list, player):
    win = False
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

    # if the center if free go to next column
    for column in range(matrixWidth):
        if (list[center][column] is blueCircle
                or list[center][column] != list[center - 1][column]):
            continue

        # count same color as center for current column
        yellowBox = 0
        greenBox = 0

        for box in range(matrixHeight):
            if list[box][column] is yellowCircle:
                yellowBox += 1
            elif list[box][column] is greenCircle:
                greenBox += 1

        # now if there are at leaset four box equal to center
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

        else:
            continue


# Check Diagonal win
def checkWinD(list, player):
    rowCenter = len(list) // 2
    columnCenter = len(list[0]) // 2

    # determine player color
    if player == P1:
        playerColor = greenCircle
    else:
        playerColor = yellowCircle

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

                print("row", tempRow)
                print("column", tempColumn)
                print("connected", connected)
                # Player won
                if connected is 4:
                    return True

            else:
                connected = 1

            # if list[tempRow][tempColumn] is yellowCircle:
            #     yellowBox += 1
            # elif list[tempRow][tempColumn] is greenCircle:
            #     greenBox += 1

            #     if (yellowBox >= 4 or greenBox >= 4):
            #         return True
            #     else:
            #         continue

    # if column >= row:
    #     row = 0
    #     column = column - row

    #     for i in range(maxRow):
    #         if list[row][column] is boxColor:
    #             connected += 1

    #             if connected is 4:
    #                 return True

    # if row > column:
    #     print("row: ", row)


# Display Board before any choise
boardToScreen(gameBoardMatrix)

change = True
intError = False
winGame = False
while True:

    if winGame:
        print(turn, "Won")
        break

    if change:
        boardToScreen(gameBoardMatrix)
        change = False
    elif intError:
        print(turn + "," + " please enter a number between from 1 to",
              len(gameBoardMatrix[0]))
        intError = False
    else:
        print(turn + "," + " this column is full please choose anther one!")

    try:
        decision = int(input())

        if decision > len(gameBoardMatrix[0]) or decision < 1:
            intError = True
            continue
    except ValueError:
        intError = True
        # print("Please Enter a number!")
        continue

    if turn == P1:
        for row in range(len(gameBoardMatrix) - 1, -1, -1):
            if gameBoardMatrix[row][decision - 1] == blueCircle:
                gameBoardMatrix[row][decision - 1] = greenCircle
                if checkWinTotal(gameBoardMatrix, P1):
                    winGame = True
                    break
                else:
                    change = True
                    turn = P2
                    break

    else:
        for row in range(len(gameBoardMatrix) - 1, -1, -1):
            if gameBoardMatrix[row][decision - 1] == blueCircle:
                gameBoardMatrix[row][decision - 1] = yellowCircle
                if checkWinTotal(gameBoardMatrix, P2):
                    winGame = True
                    break
                else:
                    change = True
                    turn = P1
                    break
