# Problem Explained

>***NOTE:*** *This is just one way to solve this problem. Remeber that there are multiple ways to approach a problem.*

This problem requires

Sample Input:

```
2
5
 _ _ _ _
|_|_|_|_|
|_|_|_|_|
|_|_|_|_|
|_|_|_|_|
4
 _ _ _ _
|_|_|_|_|_ _ _
  |_|_|_|_|_|_|
    |_|_|_|_|_|
```

Sample Output:

```
30
21
```

# Solution Explained

Default Initialization [Line 1]:

```py
for _ in range(int(input())):
```

Create empty list (layout) to store the given tile layouts, a variable to store the max length of a single row for padding (maxRowLen), and a variable to store the total amount of squares found in the tile layout (numOfSquares)[Lines 2-4]:

```py
    layout = []
    maxRowLen = 0
    numOfSquares = 0
```

Read the input data and store them in a list where each element is a single character (either ' ', '|', or '_'). The list, which represents a single row of the tile layout, is then added to the list created earlier (layout) [Lines 6-12]:

```py
    for i in range(int(input())):
        row = []

        for char in input():
            row.append(char)

        layout.append(row)
```

>***NOTE:*** *At this point, the given tile layout is interpreted into a nested list in which each element is a single character. However, the lengths of each row can differ. This can result in “IndexError: list index out of range” errors later, hence why we "pad" the nested list so that each row is of the same length.* 

Find the maximum length of a list (row) by comparing it to the previous maximum row length and store the greater value in a variable (maxRowLen) [Lines 14-15]:

```py
        if len(row) > maxRowLen:
                maxRowLen = len(row)
```

Using the stored value of the maximum row length, add blank elements (' ') to the end of each row so the length becomes uniform with the greatest size [Lines 17-26]:

```py
    for index, row in enumerate(layout):
        padding = []

        if len(row) < maxRowLen:
            diff = maxRowLen - len(row)

            for i in range(diff):
                padding.append(' ')
            
            layout[index] = row + padding
```

Use a nested for loop that iterates through every index where the '_' element could appear [Lines 28-29]:

```py
    for rowIndex, row in enumerate(layout[:-1]):
        for colIndex in range(1, len(row), 2):
```

```py
            if(layout[rowIndex][colIndex] == '_'):
```

```py
                disToRightEdge = (len(row) - colIndex)/2
                disToBot = len(layout) - rowIndex - 1

                if(disToBot > disToRightEdge):
                    maxSquareSize = int(disToRightEdge)
                else:
                    maxSquareSize = int(disToBot)
```

```py
                for squareSize in range(1, maxSquareSize+1):
```

```py
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
```

```py1
    print(numOfSquares)
```

> **Final Thoughts:** This problem truly tests your ability to 