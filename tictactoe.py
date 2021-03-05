cells = {
    "1": {
        "A": " ",
        "B": " ",
        "C": " ",
    },
    "2": {
        "A": " ",
        "B": " ",
        "C": " ",
    },
    "3": {
        "A": " ",
        "B": " ",
        "C": " ",
    }
}

# ░█▀▀▀ ░█─░█ ░█▄─░█ ░█▀▀█ ▀▀█▀▀ ▀█▀ ░█▀▀▀█ ░█▄─░█ ░█▀▀▀█
# ░█▀▀▀ ░█─░█ ░█░█░█ ░█─── ─░█── ░█─ ░█──░█ ░█░█░█ ─▀▀▀▄▄
# ░█─── ─▀▄▄▀ ░█──▀█ ░█▄▄█ ─░█── ▄█▄ ░█▄▄▄█ ░█──▀█ ░█▄▄▄█

def checkOrder(cellNumber):
    cellNumber = cellNumber.upper()
    try:
        if cellNumber[1].isdigit() and int(cellNumber[1]) < 4 and len(cellNumber) < 3 and cellNumber[0] in "ABC":
            return True
        else:
            return False
    except:
        return False

def drawBoard():
    print("\n   A   B   C")
    for num in cells:
        print(" +---+---+---+")
        row = num + "|"

        cols = cells.get(num)
        for letter in "ABC":
            row = row + f" {cols.get(letter)} |"
        print(row)
    print(" +---+---+---+\n")

def checkCell(cellNumber):
    cellNumber = cellNumber.upper()
    if checkOrder(cellNumber):
        rowCol = cellNumber[0]
        rowName = cellNumber[1]
        cell = cells.get(rowName).get(rowCol)
        if cell == " ":
            return True
        else:
            return False
    else:
        return False

def setCell(cellNumber, value):
    cellNumber = cellNumber.upper()
    if value in "XO ":
        rowCol = cellNumber[0]
        rowName = cellNumber[1]
        rowValues = cells.get(rowName)
        rowValues[rowCol] = value
    else:
        print("Wrong data type given.\n")

def checkWinner():
    winner = False
    # Horizontal Check
    for row in cells:
        row = cells.get(row)
        xPoints = 0
        oPoints = 0
        for col in row:
            col = row.get(col)
            if col == "X":
                xPoints = xPoints + 1
            elif col == "O":
                oPoints = oPoints + 1
        if xPoints == 3:
            winner = "X"
            break
        elif oPoints == 3:
            winner = "O"
            break

    # Vertical Check
    for col in "ABC":
        xPoints = 0
        oPoints = 0
        for row in cells:
            row = cells.get(row)
            value = row.get(col)
            if value == "X":
                xPoints = xPoints + 1
            elif value == "O":
                oPoints = oPoints + 1
        if xPoints == 3:
            winner = "X"
            break
        elif oPoints == 3:
            winner = "O"
            break

    # Diognal Check
    DiagonalChecks = 0
    DiaognalPattern = "ABC"
    while DiagonalChecks < 2:
        xPoints = 0
        oPoints = 0
        rowNum = 1
        for col in DiaognalPattern:
            row = cells.get(str(rowNum))
            value = row.get(col)
            if value == "X":
                xPoints = xPoints + 1
            elif value == "O":
                oPoints = oPoints + 1
            rowNum = rowNum + 1
        if xPoints == 3:
            winner = "X"
            break
        elif oPoints == 3:
            winner = "O"
            break
        else:
            DiaognalPattern = "CBA"
            DiagonalChecks = DiagonalChecks + 1

    # Tie Check
    busyCells = 0
    for row in cells:
        row = cells.get(row)
        for col in row:
            col = row.get(col)
            if col != " ":
                busyCells += 1
    if busyCells >= 9:
        winner = "tie"

    return winner

def cleanDict():
    for row in cells:
        for col in "ABC":
            cellNumber = str(col + row)
            setCell(cellNumber, " ")

# ░█─░█ ░█▀▀▀█ ░█▀▀▀ ░█▀▀█ 　 ▀█▀ ░█▄─░█ ▀▀█▀▀ ░█▀▀▀ ░█▀▀█ ─█▀▀█ ░█▀▀█ ▀▀█▀▀ ▀█▀ ░█▀▀▀█ ░█▄─░█
# ░█─░█ ─▀▀▀▄▄ ░█▀▀▀ ░█▄▄▀ 　 ░█─ ░█░█░█ ─░█── ░█▀▀▀ ░█▄▄▀ ░█▄▄█ ░█─── ─░█── ░█─ ░█──░█ ░█░█░█
# ─▀▄▄▀ ░█▄▄▄█ ░█▄▄▄ ░█─░█ 　 ▄█▄ ░█──▀█ ─░█── ░█▄▄▄ ░█─░█ ░█─░█ ░█▄▄█ ─░█── ▄█▄ ░█▄▄▄█ ░█──▀█

drawBoard()
stopGame = False
while not stopGame:
    player = "X"
    over = False
    while not over:
        userinput = input(f"Where do you want to place an {player}?: ")
        if checkOrder(userinput):
            if checkCell(userinput):
                setCell(userinput, player)
                if player == "X":
                    player = "O"
                elif player == "O":
                    player = "X"
                winner = checkWinner()
                if winner:
                    if winner != "tie":
                        print(f"\n Player {winner} won the game!\n")
                    else:
                        print("\n It's a tie!")
                    drawBoard()
                    ans = input("Would you like to play again? [Y/N]: ").upper()
                    if ans == "Y":
                        cleanDict()
                        over = True
                    else:
                        over = True
                        stopGame = True
            else:
                print("The cell is unavailable. Try somewhere else\n")
        else:
            print("Wrong data type entered. A correct entry example: A1\n")
        drawBoard()
