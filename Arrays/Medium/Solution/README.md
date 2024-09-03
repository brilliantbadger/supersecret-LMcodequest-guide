# Problem Explained

>***NOTE:*** *This is just one way to solve this problem. Remeber that there are multiple ways to approach a problem.*

This problem requires us to assign "six positive integers" to "each of the six ability score abbreviations (STR, DEX, CON, INT, WIS, CHA), listed in order from the highest priority to the lowest priority for the identified class." This means that the highest priority item should be assigned the highest integer, second highest priority item should be assigned the second highest integer, and so on. Our program also has to print out the stored information in a certain format specified by the problem.

In the sample I/O given, the first 3 lines after the input containing integers are the abilities listed in order from the highest priority to the lowest priority for the identified class. For example, the "WARRIOR" class's abilities, listed from highest to lowest priority, are STR, CON, DEX, CHA, WIS, and INT. The next 3 lines are generated characters, each containing the name of a class and six positive integers.

Sample Input:

```
1
3 3
WARRIOR STR CON DEX CHA WIS INT
ROGUE DEX CHA INT WIS STR CON
WIZARD INT DEX WIS CON CHA STR
WARRIOR 5 7 9 11 13 15
ROGUE 8 8 10 11 12 13
WIZARD 10 10 13 13 15 15
```

Our program should assign each number to the identified class's abilities; higher numbers are assigned to higher priority abilties. For the WARRIOR character that was generated, the highest number (15) should be assigned to the highest priority ability (STR), the second highest number (13) should be assigned to the second highest priority ability (CON), and so on. The program should then print the generated character with the stats in the specified format. 

Sample Output:

```
WARRIOR
STR: 15
DEX: 11
CON: 13
INT: 5
WIS: 7
CHA: 9
ROGUE
STR: 8
DEX: 13
CON: 8
INT: 11
WIS: 10
CHA: 12
WIZARD
STR: 10
DEX: 15
CON: 13
INT: 15
WIS: 13
CHA: 10
```

# Solution Explained

We need to store the character name and the order of abilites so that we can access them later. We can use a nested list to achieve this! Each element in the nested list is a list that contains the class name and the abilities from highest priority to lowest priority. We then have to assign the integers to each abilities based on the class. Assigning the inputed intgers (values) to abilities (keys)... We can use a dictionary! Finally, we print out the generated character with the stats in the specified format. As an added bonus, using a dictionary to store the information should also make it easier to print out in the specified format!

Default Initialization [Line 1]:

```py
for _ in range(int(input())):
```

Create empty list (database) to store the class name and abilties [Line 2]:

```py
    database = []
```

Read input data [Line 4]:

```py
    inp = input().split()
```

Store the class name and abilities as a list (info) and add it to the empty list that was created earlier (database) [Lines 6-8]:

```py
    for i in range(int(inp[0])):
        info = input().split()
        database.append(info)
```

Store the class name and integers as a list (info) [Lines 10-11]:

```py
    for i in range(int(inp[1])):
        info = input().split()
```

Remove the first element of the list (info) and store it as a variable (name) [Line 13]:

```py
        name = info.pop(0)
```

>***NOTE:*** *We removed the first element (which contains letters) in order to convert the rest of the elements (which contains integers) from strings to integers. However, we still need the element, hence why we used .pop()* 

Convert the remaining elements in the list (info) from strings to integers and put the converted elements in a new list (stat) [Line 14]:

```py
        stat = list(map(int, info))
```

Sort the list (stat) in reverse order [Line 15]:

```py
        stat.sort(reverse=True)
```

Create a dictionary (character) with the six ability score abbreviation (STR, DEX, CON, INT, WIS, CHA) as keys and empty values [Lines 17-24]:

```py
        character = {
            'STR': '',
            'DEX': '',
            'CON': '',
            'INT': '',
            'WIS': '',
            'CHA': ''
        }
```

Assign the integer values from the list (stat) to the respective key in the dictionary (character) based on the order of abilities in the list (data) from the nested list (database) [Lines 26-29]:

```py
        for data in database:
            if name == data[0]:
                for index in range(len(stat)):
                    character[data[index+1]] = stat[index]
```          

>***NOTE:*** *The reason why we pull the value of data[index+1] is because the first element in the list is taken up by the class name. The elements following that contain the ability names from highest to lowest priority. The first element in the stat list, which was the class name, was removed earlier, so the first element is now the highest integer.* 

Print the name of the class stored in the variable (name) and values in the dictionary (character) so that it looks like the specified format [Lines 31-33]:

```py
        print(name)
        for key,value in character.items():
            print(f"{key}: {value}")
```

> **Final Thoughts:** This problem is a great at testing your ability to keep track of the lists you created and what each element represents in said lists. A dictionary is a nice way to store data but it is not necessary to solve this problem, though it does make it a little bit easier. It should also be noted that the problem did not state that the integers would be ordered from smallest to biggest, even though the sample input is formatted that way. You could have been tricked into thinking this way if you did not fully read the problem.