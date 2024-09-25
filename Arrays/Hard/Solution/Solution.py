# def checkSquares(nestedList, rowIndex, colIndex):
#     total = 0
#     maxSquareLen = 0
#     maxSqureWid = 0

#     currentElement = nestedList[rowIndex][colIndex]

#     if currentElement == 'o':
#         total -= 1

#     for x in nestedList[rowIndex][colIndex:]:
#         if x != currentElement:
#             break
#         maxSquareWid += 1

#     for row in nestedList:
#         if row[colIndex] != currentElement:
#             break
#         maxSquareLen += 1
    
#     maxSquareSize = min(maxSquareLen, maxSquareWid)

     


                
                    




# for _ in range(int(input())):
#     layout = []
#     maxRowLen = 0

#     for i in range(int(input())):
#         inp = input()
#         row = []

#         if i != 0:
#             for index in range(1, len(inp), 2):
#                 group = inp[index-1:index+2]
#                 if group == '|_|':
#                     row.append('x')
#                 else:
#                     row.append('o')

#             if len(row) > maxRowLen:
#                 maxRowLen = len(row)

#             layout.append(row)
   
#     for index, row in enumerate(layout):
#         padding = []

#         if len(row) < maxRowLen:
#             diff = maxRowLen - len(row)

#             for i in range(diff):
#                 padding.append('o')
            
#             layout[index] = row + padding
    

 
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

            if(layout[rowIndex][colIndex] == '_' and layout[rowIndex+1][colIndex+1] == '|' and layout[rowIndex+1][colIndex-1] == '|' and layout[rowIndex+1][colIndex] == '_'):
                numOfSquares += 1

            disToRightEdge = (len(row) - colIndex)/2
            disToBot = len(layout) - rowIndex - 1
            if(disToBot > disToRightEdge):
                maxSquareSize = int(disToRightEdge)
            else:
                maxSquareSize = int(disToBot)

            for squareSize in range(2, maxSquareSize+1):
                isSquare = True
                for j in range(0, squareSize*2, 2):
                    if(layout[rowIndex][colIndex+j] == ' '):
                        isSquare = False
                    if(layout[rowIndex+squareSize][colIndex+j] == ' '):
                        isSquare = False   
                for j in range(1,squareSize+1):
                    if(layout[rowIndex+j][colIndex-1] == ' '):
                        isSquare = False
                    if(layout[rowIndex+j][colIndex+(squareSize*2)-1] == ' '):
                        isSquare = False
                if(isSquare):
                    numOfSquares += 1
    
    print(numOfSquares)
