for _ in range(int(input())):
    layout = []
    maxRowLen = 0
    numOfSquares = 0

    for i in range(int(input())):
        row = []

        for char in input():
            row.append(char)

        layout.append(row)

        if len(row) > maxRowLen:
                maxRowLen = len(row)
   
    for index, row in enumerate(layout):
        padding = []

        if len(row) < maxRowLen:
            diff = maxRowLen - len(row)

            for i in range(diff):
                padding.append(' ')
            
            layout[index] = row + padding

    for rowIndex, row in enumerate(layout[:-1]):
        for colIndex in range(1, len(row), 2):

            disToRightEdge = (len(row) - colIndex)/2
            disToBot = len(layout) - rowIndex - 1
            if(disToBot > disToRightEdge):
                maxSquareSize = int(disToRightEdge)
            else:
                maxSquareSize = int(disToBot)

            for squareSize in range(1, maxSquareSize+1):
                isSquare = True
                for j in range(0, squareSize*2, 2):
                    if(layout[rowIndex][colIndex+j] != '_'):
                        isSquare = False
                    if(layout[rowIndex+squareSize][colIndex+j] != '_'):
                        isSquare = False   
                for j in range(1,squareSize+1):
                    if(layout[rowIndex+j][colIndex-1] != '|'):
                        isSquare = False
                    if(layout[rowIndex+j][colIndex+(squareSize*2)-1] != '|'):
                        isSquare = False
                if(isSquare):
                    numOfSquares += 1
    
    print(numOfSquares)
