# Problem Explained

>***NOTE:*** *This is just one way to solve this problem. Remeber that there are multiple ways to approach a problem.*

This problem requires us to "count the amount of sqaures - of any size - in the provided image." The tile layout is inputted into our program one line at a time, "consisting of pipes ['|'], underscores ['_'], and spaces [' ']", and our program should output the amount of squares that can be formed.

Note that "lines will not contain any trailing whitespace, and as such may not all be the same length, even within the test case."

In the sample I/O given, the input gives us 2 test cases. The first tile layout has a height of 5 lines and the second tile layout has a height of 4 lines

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

Our program should print the number of squares that can be formed in the tile layout given. In this case, it is 30 squares for the first tile layout and 21 for the second.

Sample Output:

```
30
21
```

# Solution Explained

>***NOTE:*** *The very first thing we should do when solving a problem that is as complicated as this is to browse the internet for any formulas or algorithms we can use to help us. However, as of writing this guide, I couldn't find anything useful regarding this particular problem* 

The tile layout we are given can be formatted into a nested list so that the information can be worked with more easily. We should think about how we, as humans, would count the total amount of squares in a given layout, and try to replicate that process in our program. We would first start with a reference point within the layout, count how many squares we can make from that point, then repeat this process with all the other reference points (Note that this is just one way to count the squares; there are other methods). We can use a nested for loop to cycle through all the reference points in the nested list containing the tile layout. To check if squares can be formed we can check if all the sides are valid characters (top and bottom should all be '_' and sides should be all '|'). A for loop would also be used to cycle through the different sized squares that we would check. 

To avoid errors, we should also determine the max square size that can be formed from that reference point by checking its distance to the right edge and bottom of the tile layout. By doing this, we don't check for squares that are impossible to form. Additionally, not all the lines inputted are of the same length, so we would have a nested list containing lists of differing sizes. Navigating up and down in this nested list and checking if certain elements exists would most likely result in the “IndexError: list index out of range” error. To prevent this, we can "pad" out the nested list, so that each row is of the same length.

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

Read the input data and store them in a list where each element is a single character. The list, which represents a single row of the tile layout, is then added to the list created earlier (layout) [Lines 6-12]:

```py
    for i in range(int(input())):
        row = []

        for char in input():
            row.append(char)

        layout.append(row)
```

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

Check if the current element is a '_' character [Line 30]:

```py
            if(layout[rowIndex][colIndex] == '_'):
```

Based on the current index of the element, determine the maximum possible size a square can be formed in the layout and store the value in a variable (maxSquareSize) [Lines 31-37]:

```py
                disToRightEdge = (len(row) - colIndex)/2
                disToBot = len(layout) - rowIndex - 1

                if(disToBot > disToRightEdge):
                    maxSquareSize = int(disToRightEdge)
                else:
                    maxSquareSize = int(disToBot)
```

Iterate through the possible number of squares that can be formed [Line 39]:

```py
                for squareSize in range(1, maxSquareSize+1):
```

Check if a square with a size of 'squareSize' can be made in the index of the tile layout [Lines 40-50]:

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
```

If a square with a size of 'squareSize' can be made, increment the variable storing the amount of squares found (numOfSquares) [Lines 52-53]:

```py
                    if(isSquare):
                        numOfSquares += 1
```

Print out the amount of squares found in the tile layout [Line 55]:

```py
    print(numOfSquares)
```

> **Final Thoughts:** This problem truly tests your ability to navigate through a nested list using for loops. Besides the complex logic used to solve this problem, it is also important that you account for any errors you might come across. The most common error that you will face while working with lists is the “IndexError: list index out of range” error. Think through your pseudocode and program to make sure you won't have to deal with errors. It can also be distracting trying to optimize the code. The solution provided can be heavily optimized, but the important thing is that it works. Your main goal is to solve the problem. Although the LMcodequest does measure the runtime of your code, it is rarely used, as it only becomes important in tiebreakers.