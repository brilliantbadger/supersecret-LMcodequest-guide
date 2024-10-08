# Problem Explained

>***NOTE:*** *This is just one way to solve this problem. Remeber that there are multiple ways to approach a problem.*

This problem requires us to compare the names of "systems listed in the shipyard database" to the names of "systems reported by the ship's computer." Our task is to print a list of systems that are not "appear in the database, but [is not] reported by the ships's computer". It should also be noted that our program should print the list, "in alphabetical order (case-insensitive), with one system per line."

In the sample I/O given, the first 5 lines after the input containing integers (Cannon, Engine, Helm, Deck, Anchor) are systems listed in the ship database. The next 3 lines (Engine, Helm, Anchor) are systems reported by the ship's computer.

Sample Input:

```
1
5 3
Cannon
Engine
Helm
Deck
Anchor
Engine
Helm
Anchor
```

Our program should print out the systems that are in the database but not in the computer report (Cannon, Deck).

Sample Output:

```
Cannon
Deck
```

# Solution Explained

Hmmm... storing names in groups... sounds familiar... We can use lists here! One to store the names of systems listed and another to store the names reported. We then can compare those two lists and return a new list of names that are included in the database but are not present in the computer's report. Finally, we can sort the list in alphabetical order (case-insensitive) and print the sorted list one line at a time.

Default Initialization [Line 1]:

```py
for _ in range(int(input())):
```

Create empty lists (database, report) to store the input data [Lines 2-3]:

```py
    database = []
    report = []
```

Read input data and add names of systems to their respective lists (Lines 5-10):

```py
    inp = input().split()

    for i in range(int(inp[0])):
        database.append(input())
    for i in range(int(inp[1])):
        report.append(input())
```

Create new list (inspect) that contains elements that are present in the database list but not in the report list [Line 12-14]:

```py
    inspect = database
    for element in list2:
        inspect.remove(element)
```

Sort the new list (inspect) in alphabetical order (case-insensitive) [Line 16]:

```py
    inspect.sort(key=str.lower)
```

Print out the list (inspect) one line at a time [Lines 118-19]:

```py
    for i in inspect:
        print(i)
```

> **Final Thoughts:** The difficulty of solving this problem will most likely come from sorting the list in alphabetical order (case-insensitive). It is important to understand how each method works so you do not fall into various traps you might be presented with.

