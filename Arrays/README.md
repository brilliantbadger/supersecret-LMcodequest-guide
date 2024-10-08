# Lists

>***NOTE:*** *Although the category in the LMcodequest is called Arrays, it is much easier to use lists in python as they have different properties and methods that make them more suitable to solve the given problems.*

Lists are a way to store multiple variables in order. There are multiple cases in which a list would greatly aid you in both managing and processing multiple elements. 

**Here is a general guidelines you can use when deciding to use a list:**

1. **Indexing:** In scenarios where the order of the elements are important, lists allow you to retrieve elements based on their position in the list or index (we will go over index later)
2. **Number and Position of elements are dynamic:** When the order and position of elements constantly change or are unknown, lists can make your life considerably easier. Methods (we will go over them later) can actively modify, add, and remove elements in a list.
3. **Iterative Operations:** Lists should be used when you have to use operations that involve iterating through multiple elements (i.e. finding the sum of several numbers, finding the maximum/minimum, etc.)

>***NOTE:*** *As you work through and solve problems on your own, you will get a better sense of when and how to apply the concepts from this document.*

## Table of Contents

- **Basic Usage** 
  - [Initializing a List](#initializing-a-list)
  - [Retrieving Elements from a List](#retrieving-elements-from-a-list)
  - [Modifying Elements in a List](#modifying-elements-in-a-list)
  - [Slicing a List](#slicing-a-list)
  - [Operations](#operations)
- **Useful Methods**
  - [Adding New Elements](#adding-new-elements)
  - [Inserting New Elements](#inserting-new-elements)
  - Removing Elements
    - [Removing Elements (By Element)](#removing-elements-by-element)
    - [Removing Elements (By Index)](#removing-elements-by-index)
    - [Removing Elements (By Index + Return Element)](#removing-elements-by-index--return-element)
  - [Finding Index of an Element](#finding-index-of-an-element)
  - [Finding Length of a List](#finding-length-of-a-list)
  - [Finding How Many Times an Element Appears](#finding-how-many-times-an-element-appears)
  - Sorting a List
    - [Sorting a List](#sorting-a-list)
    - [Sorting a List (Case-Insensitive)](#sorting-a-list-case-insensitive)
    - [Sorting a List (Reversed)](#sorting-a-list-reversed)
  - [Reversing a List](#reversing-a-list)
  - [Clearing a List](#clearing-a-list)
- **[Nested Lists](#nested-lists)**
  - [Initializing a Nested List](#inititalizing-a-nested-list)
  - [Retrieving Elements from a Nested List](#retrieving-elements-from-a-list)
  - [Modifying Elements in a Nested List](#modifying-elements-in-a-nested-list)
  - [Slicing a Nested List](#slicing-a-nested-list)
- **[Dictionaries](#dictionaries)**
- **Useful Code**
  - Iterating over a List
    - [Using a for loop](#using-a-for-loop)
    - [Using a for loop and enumerate()](#using-a-for-loop-and-enumerate)
    - [Using a for loop and range()](#using-a-for-loop-and-range)
  - Iterating over a Nested List
  - Iterating over a Dictionary
  - [Converting ALL String Elements to Integers](#converting-all-string-elements-to-integers)
  - [Converting ALL Integer Elements to Strings](#converting-all-integer-elements-to-strings)
  - Adding Padding
    - [Left Side](#left-side)
    - [Right Side](#right-side)
  - [Subtracting Lists](#subtracting-lists)
- **Sample Problems and Solutions**
  - [Easy](Easy)
  - [Medium](Medium)
  - [Hard](hard)
- [Final Thoughts](#final-thoughts)


## Initializing a List

```py
newList = [0, 1, 2, 3, 4]
```

Lists can also hold different type of variables. Here is an exmaple of a list that contains integers, strings, and a boolean.

```py
newList = [0, 1, 'hello', 'world', True]
```

## Retrieving Elements from a List

To retrive elements from a list, an index operator is used. It is written in this notation:

```py
listName[index]
```

>***NOTE:*** *Indexes are zero-based numbering. This means that the initial number starts with 0 instead of 1.*

```py
newList = [0, 1, 'hello', 'world', True]

print(newList[0]) 
# Output: 0

print(newList[2]) 
# Output: 'hello'
```

You can also use negative indexes! Just remember that the index starts from the end.

```py
newList = [0, 1, 'hello', 'world', True]

print(newList[-1]) 
# Output: True 

print(newList[-3]) 
# Output: 'hello'
```

If you try to retrieve an element with an index number that is bigger than the length of the list (zero-based numbering) you will be hit with a “IndexError: list index out of range” error. Make sure that the index that you are trying to retrieve inside the bounds of the list.

```py
newList = [0, 1, 'hello', 'world', True]

print(newList[5]) 
# Output: IndexError: list index out of range

print(newList[-6]) 
# Output: IndexError: list index out of range
```

## Modifying Elements in a List

To change an element in a list:

```py
newList = [0, 1, 2, 3, 4, 5]

newList[2] = 'hello'
print(newList)
# Output: [0, 1, 'hello', 3, 4, 5]

newList[-1] = 'hello'
print(newList)
# Output: [0, 1, 'hello', 3, 4, 'hello']
```

## Slicing a List

A slice is a new list that contains a range of elements from a sliced list. It is written in this notation:

```py
listName[start:end:step]
# start = index of the first element that is included in the slice   | DEFAULT VALUE = 0
# end   = index where the slice ends; this element is NOT included   | DEFAULT VALUE = 0
# step  = the increment in which the elements are added to the slice | DEFAULT VALUE = 1
```

Remember that the stop index is not included in the sliced list. The default value of the start arguement is 0, so you can but you do not have to write the 0. The same thing applies for the end and step arguements.

```py
newList = [0, 1, 'hello', 'world', True]

print(newList[:2]) 
# Output: [0, 1]

print(newList[2:]) 
# Output: ['hello', 'world', True]
```

This code passes a value through the step parameter. It prints a new list with every 2 elements starting from index 0 in newList.

```py
newList = [0, 1, 2, 3, 4, 5]
print(newList[::2])
# Output: [0, 2, 4]
```

You can pass negative numbers through the parameters.

```py
newList = [0, 1, 2, 3, 4, 5]
print(newList[-2:])
# Output: [4, 5]

print(newList[:-2])
# Output: [0, 1, 3]

print(newList[::-1])
# Output: [5, 4, 3, 2, 1, 0]
```

## Operations

You can add lists together!

```py
list1 = [0, 1, 2]
list2 = [3, 4, 5]

newList= list1 + list2
print(newList)
# Output: [0, 1, 2, 3, 4, 5]
```

Multiplication... woah!

```py
list1 = [0, 1, 2]

newList = list1 * 3
print(newList)
# Output: [0, 1, 2, 0, 1, 2, 0, 1, 2]
```

>***NOTE:*** *Where's subtraction? More information can be found [here](#subtracting-lists)*

# Useful Methods for Lists

## Adding New Elements

```py
listName.append(newElement)
```

Example:

```py
newList = [0, 1, 2, 3, 4, 5]

newList.append(6)
print(NewList)
# Output: [0, 1, 2, 3, 4, 5, 6]
```

>Explaination: This method add a new element (6) to the end of a list (NewList). The list becomes 1 element bigger as a result.

## Inserting New Elements

```py
listName.insert(index, newElement)
```

Example:

```py
newList = [0, 1, 2, 3, 4, 5]

newList.insert(1, “hello”)
print(newList)
# Output: [0, 1, 2, 3, 4, 5, 6]
```

>Explaination: This method inserts a new element (“hello”) to a list (NewList). The previous element at index 1 (1) now becomes index 2 and the pattern follows for the rest of the elements after index 1. Because of this the list also becomes 1 element bigger.

## Removing Elements (By Element)

```py
listName.remove(element)
```

Example:

```py
newList = [0, 'hello', 2, 3, 4, 5]

newList.remove('hello')
print(newList)
# Output: [0, 2, 3, 4, 5]
```

>Explaination: This method removes an element ('hello'). The element at index 2 now becomes index 1 and the pattern follows for the rest of the elements after. Because of this the list becomes 1 element smaller.

## Removing Elements (By Index)

```py
del listName[index]
```

Example:

```py
newList = [0, 'hello', 2, 3, 4, 5]

del newList[1]
print(newList)
# Output: [0, 2, 3, 4, 5]
```

>Explaination: This method removes the element at index 1 ('hello'). The element at index 2 now becomes index 1 and the pattern follows for the rest of the elements after. Because of this the list becomes 1 element smaller.

## Removing Elements (By Index + Return Element)

```py
listName.pop(index)
```

Example:

```py
newList = [0, 'hello', 2, 3, 4, 5]

removedElement = newList.pop(1)
print(newList)
# Output: [0, 2, 3, 4, 5]
print(removedElement)
# Output: 'hello'
```

>Explaination: This method removes the element at index 1 ('hello') and returns the removed element ('hello'). The returned element can then be stored in a variable (removedElement). The element at index 2 now becomes index 1 and the pattern follows for the rest of the elements after. Because of this the list becomes 1 element smaller.

## Finding Index of an Element

```py
listName.index(element, start, stop)
```

Example:

```py
newList = [0, 1, 2, 3, 2, 5]

print(newList.index(2))
# Output: 2
# the first item whose value is equal to 2 in NewList is index 2

print(newList.index(2, 3, 5))
# Output: 4
# the first item whose value equals to 2 starting from index 3 ending index 5 is index 4

print(newList.index(7))
# Output: ValueEror: 7 is not in the list
```

>Explaination: This method returns the index of the first element whose value equals to the value passed through the element parameter. The start and stop arguments are optional; they give parameters to search and works similar to the parameters in slicing. If start and stop arguments are passed the method would return the index of the first element that equals to the value passed through the element parameter starting from index start and ending index stop (exclusive). If no elements are found then a “ValueError” error is returned.

## Finding Length of a List
```py
len(listName)
```

Example:

```py
newList = [0, 1, 2, 3, 4, 5]

print(len(newList))
# Output: 6
```

>Explaination: This method returns the length of a list (newList). It should be noted that this method does not use zero-based numbering to count the length of a list.

## Finding How Many Times an Element Appears

```py
listName.count(element)
```

Example:

```py
newList = [0, 1, 2, 3, 2, 5]

print(newList.count(2))
# Output: 2
```

>Explaination: This method returns how many times an element (2) appears in a list (NewList).

## Sorting a List

```py
listName.sort()
```

Example:

```py
newList =  [0, 3, 2, 1, 5, 4]
newList2 =  [0, 3, 2, 1, 5, 'hello']

newList.sort()
print(newList)
# Output: [0, 1, 2, 3, 4, 5]

newList2.sort()
# Output: TypeError: '<' not supported between isntances of 'str' and 'int'
```

>Explaination: This method modifies a list (NewList) so that every element inside the list is in order. You cannot compare different types of varaibles in python, so you cannot sort a list that holds different types of variables. If you attempt to do so, you will be met with a "TypeError" Error. 

## Sorting a List (Case-Insensitive)

```py
listName.sort(key=str.lower)
```

Example:

```py
newList =  ['a', 'C', 'b']

newList.sort()
print(newList)
# Output: ['C', 'a', 'b']

newList.sort(key=str.lower)
# Output: ['a', 'b', 'C']
```

>Explaination: When comparing strings using ".sort()", uppercased characters will be less than lowercased characters; it is case-sensitive. Passing the "key=str.lower" arguement through the ".sort()" parameter allows string comparison that is case-insensitive.

## Sorting a List (Reversed)

```py
listName.sort(reverse=True)
```

Example:

```py
newList =  [0, 3, 2, 1, 5, 4]

newList.sort(reverse=True)
print(newList)
# Output: [5, 4, 3, 2, 1]
```

>Explaination: This method sorts a list in reverse order. Alternatively, you can use the ."sort()" method normally and reverse it using ".reverse()".

## Reversing a List

```py
listName.reverse()
```

Example:

```py
newList =  [0, 1, 2, 3, 4]

newList.reverse()
print(newList)
# Output: [4, 3, 2, 1, 0] 
```

>Explaination: This method reverses the order of the elements in a list (NewList).

## Clearing a List

```py
listName.clear()
```

Example:

```py
newList =  [0, 1, 2, 3, 4]

newList.clear())
print(newList)
# Output: [] 
```

>Explaination: This method removes everything in a list.


# Nested Lists

You can put lists inside of lists! This can help you when the data given is more organized and manageable in a grid-like layout.

>***NOTE:*** *All the methods used in lists can be applied to nested lists. Useful methods for lists are found [here](#useful-methods-for-lists)*

## Inititalizing a Nested List

To initialize a Nested List:

```py
newList = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

# or alternatively

newList = [[0, 1, 2, 3],
	       [4, 5, 6, 7],
           [8, 9, 10, 11]]
```

## Retrieving Elements from a Nested List

To retrive elements from a list, an index operator is used. It is written in this notation:

```py
listName[rowIndex][colIndex]
```

You can also just retrieve a list from a nested list:

```py
listName[rowIndex]
```

>***NOTE:*** *Indexes are zero-based numbering. This means that the initial number starts with 0 instead of 1.*

```py
newList = [[0, 1, 2, 3],
	       [4, 5, 6, 7],
           [8, 9, 10, 11]]

print(newList[0][0]) 
# Output: 0

print(newList[2][3]) 
# Output: 7

print(newList[1]) 
# Output: [4, 5, 6, 7]
```

You can also use negative indexes! Just remember that the index starts from the end.

```py
newList = [[0, 1, 2, 3],
	       [4, 5, 6, 7],
           [8, 9, 10, 11]]

print(newList[-1][0]) 
# Output: 8

print(newList[-2][-2]) 
# Output: 6

print(newList[-2]) 
# Output: [4, 5, 6, 7]
```

If you try to retrieve an element with an index number that is bigger than the length of the list (zero-based numbering) you will be hit with a “IndexError: list index out of range” error. Make sure that the index that you are trying to retrieve inside the bounds of the list.

```py
newList = [[0, 1, 2, 3],
	       [4, 5, 6, 7],
           [8, 9, 10, 11]]

print(newList[3]) 
# Output: IndexError: list index out of range

print(newList[-4]) 
# Output: IndexError: list index out of range

print(newList[0][4]) 
# Output: IndexError: list index out of range

print(newList[0][-5]) 
# Output: IndexError: list index out of range
```

## Modifying Elements in a Nested List

To change an element or a list in a nested list:

```py
newList = [[0, 1, 2, 3],
	       [4, 5, 6, 7],
           [8, 9, 10, 11]]

newList[1] = ['hello', 'world']
print(newList)
# Output: [[0, 1, 2, 3], ['hello', 'world'], [8, 9, 10, 11]]

newList[2][-2] = 'BOO!'
print(newList)
# Output: [[0, 1, 2, 3], ['hello', 'world'], [8, 9, 'BOO!', 11]]
```

## Slicing a Nested List

You can choose to slice the nested list itself or the lists inside it:

```py
newList = [[0, 1, 2, 3],
	       [4, 5, 6, 7],
           [8, 9, 10, 11]]

print(newList[:2]) 
# Output: [[0, 1, 2, 3], [4, 5, 6, 7]]

print(newList[1:]) 
# Output: [[4, 5, 6, 7], [8, 9, 10, 11]]

print(newList[1][1:3]) 
# Output: [5, 6]
```

>***NOTE:*** *Slicing works the exact same for a nested list as it does for a regular list. The parameters and functions of the parameters are exactly the same. More information about list slicing, can be found [here](#slicing-a-list)!*

# Dictionaries

## Useful Methods for Dictionaries

# Useful Code

## Iterating over a List

### Using a *for loop*

```py
newList = ['1', '2', '3', '4', '5']

for element in newList:
  print(element)

# Output: '1'
#         '2'
#         '3'
#         '4'
#         '5'
```

### Using a *for loop* and *enumerate()*

```py
newList = ['1', '2', '3', '4', '5']

for index, element in enumerate(newList):
  print(index + ' ' + element)

# Output: 0 '1'
#         1 '2'
#         2 '3'
#         3 '4'
#         4 '5'
```

You can also change the starting index for enumeration!

```py
newList = ['1', '2', '3', '4', '5']

for index, element in enumerate(newList, start=2):
  # starts iterating from index 2
  print(index + ' ' + element)

# Output: 0 '1'
#         1 '2'
#         2 '3'
#         3 '4'
#         4 '5'
```

### Using a *for loop* and *range()*

```py
newList = ['1', '2', '3', '4', '5']

for index in range(len(newList)):
  print(element)

# Output: '1'
#         '2'
#         '3'
#         '4'
#         '5'
```

Using the range() function provides more flexibility and allows for complexity. For example, you can choose what index in the list to start iterating from and/or add incrementation:

```py
newList = ['1', '2', '3', '4', '5', '6']

for index in range(1, len(newList), 2):
  # starts iterating from index 1
  # stops at index len(newList) (EXCLUSIVE)
  # increments by 2 
  print(newList[index])

# Output: '2'
#         '4'
#         '6'
```

>***NOTE:*** *For more information on the range() function can be found [here] (placeholder)*

## Iterating over a Nested List

## Iterating over a Dictionary

## Converting ALL String Elements to Integers

```py
newList = ['1', '2', '3', '4', '5']

convertedList = list(map(int, newList))
print(convertedList)

# Output: [1, 2, 3, 4, 5]
```

Alternatively, you can utilize for loops and typecasting:

```py
newList = ['1', '2', '3', '4', '5']
convertedList = []

for element in newList:
  convertedList.appened(int(element))
print(convertedList)

# Output: [1, 2, 3, 4, 5]
```

>***NOTE:*** *Make sure all the elements in the list you are converting to integers CAN be converted to integers. If you try to convert a non-integer value to an integer, you will be met with a "ValueError" error.*

## Converting ALL Integer Elements to Strings

```py
newList = [1, 2, 3, 4, 5]

convertedList = list(map(str, newList))
print(convertedList)

# Output: ['1', '2', '3', '4', '5']
```

Alternatively, you can utilize for loops and typecasting:

```py
newList = [1, 2, 3, 4, 5]
convertedList = []

for element in newList:
  convertedList.appened(str(element))
print(convertedList)

# Output: ['1', '2', '3', '4', '5']
```

## Adding Padding

### Left Side

```py
nestedList = [[1], [1, 2, 3, 4]]
maxRowLen = 0

for row in nestedList:
  if len(row) > maxRowLen:
            maxRowLen = len(row)

for index, row in enumerate(nestedList):
  if len(row) < maxRowLen:
    diff = maxRowLen - len(row)

    for i in range(diff):
        nestedList[index].insert(0, ' ')

# Output: [['1', ' ', ' ', ' '], ['1', '2', '3', '4']]    
```

### Right Side

```py
nestedList = [[1], [1, 2, 3, 4]]
maxRowLen = 0

for row in nestedList:
  if len(row) > maxRowLen:
            maxRowLen = len(row)

for index, row in enumerate(nestedList):
  if len(row) < maxRowLen:
    diff = maxRowLen - len(row)

    for i in range(diff):
        nestedList[index].append(' ')

# Output: [[' ', ' ', ' ', '1'], ['1', '2', '3', '4']]    
```

## Subtracting Lists

```py
list1 = [0, 1, 2, 3, 4, 5]
list2 = [3, 4, 5]

for element in list2:
  list1.remove(element)
print(list1)

# Output: [0, 1, 2]
```

>***NOTE:*** *If you need the contents of the two lists involved in the subtraction to be intact, you can duplicate the list you are subtracting from beforehand!* 

# Final Thoughts