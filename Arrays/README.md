# Arrays (Lists)

>***NOTE:*** *Although the LMcodequest has a category called Arrays, it is much easier to use lists as they have different properties and methods that make them more suitable to solve the given problems.*

Lists are a way to store multiple variables in order. There are multiple cases in which a list would greatly aid you in both managing and processing multiple elements. 

**Here is a general guidelines you can use when deciding to use a list:**

1. **Indexing:** In scenarios where the order of the elements are important, lists allow you to retrieve elements based on their position in the list or index (we will go over index later)
2. **Number and Position of elements are dynamic:** When the order and position of elements constantly change or are unknown, lists can make your life considerably easier. Methods (we will go over them later) can actively modify, add, and remove elements in a list.
3. **Iterative Operations:** Lists should be used when you have to use operations that involve iterating through multiple elements (i.e. finding the sum of several numbers, finding the maximum/minimum, etc.)

>***NOTE:*** *As you work through and solve problems on your own, you will get a better sense of when and how to apply the concepts from this document.*

***

### Initializing a List

```py
newList = [0, 1, 2, 3, 4]
```

Lists can also hold different type of variables. Here is an exmaple of a list that contains integers, strings, and a boolean.

```py
newList = [0, 1, 'hello', 'world', True]
```

***

### Retrieving Elements from a List

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
```

***

### Slicing a List

A slice is a new list that contains a range of elements from a sliced list. It is written in this notation:

```py
listName[start:end:step]
# start = index of the first element that is included in the slice   | DEFAULT VALUE = 0
# end   = index where the slice ends; this element is NOT included   | DEFAULT VALUE = 0
# step  = the increment in which the elements are added to the slice | DEFAULT VALUE = 1
```

Remember that the stop index is not included in the sliced list. The default value of the start arguement is 0, so you can but you do not have to write the 0. The same thing applys for the end and step arguements.

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

***

### Modifying Elements

To change an element in a list:

```py
newList = [0, 1, 2, 3, 4, 5]

newList[2] = 'hello'
print(newList)
# Output: [0, 1, 'hello', 3, 4, 5]
```

***

### Adding New Elements

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

***


### Inserting New Elements

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

***

### Removing Elements

```py
listName.remove(index)
```

Example:

```py
newList = [0, 1, 2, 3, 4, 5]

newList.remove(1)
print(newList)
# Output: [0, 2, 3, 4, 5, ]
```

>Explaination: This method removes the element at index 1 (1). The previous element at index 2 (2) now becomes index 1 and the pattern follows for the rest of the elements after index 1. Because of this the list also becomes 1 element smaller.

***

### Finding Index of Elements

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

***

### Finding Length of a List:
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

***
### Finding How Many Times an Element Appears

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

***

### Sorting a List

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

***

### Reversing a List

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

***

### Clearing a List

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

***

### Operations:

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
