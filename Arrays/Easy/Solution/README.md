# Explanation

>***NOTE:*** *This is just one way to solve this problem. Remeber that there are multiple ways to approach a problem.*

This problem wants us to compare the names of "systems listed in the shipyard database" to the names of "systems reported by the ship's computer." Our task is to print a list of systems that are not "appear in the database, but [is not] reported by the ships's computer". It should also be noted that our program should print the list, "in alphabetical order (case-insensitive), with one system per line."

Hmmm... storing names in groups... sounds familiar... We can use lists here! One to store the names of systems listed and another to store the names reported. We then can compare those two lists and return a new list of names that are included in the database but are not present in the computer's report. Finally, we can sort the list in alphabetical order (case-insensitive) and print the sorted list one line at a time.

Default Initialization [Line 1]:

```py
for _ in range(int(input())):
```

Create empty lists (database, report) to store the input data [Lines 1-2]:

```py
    database = []
    report = []
```

Read input data and add said data to their respective lists (Lines 5-10):

```py
    inp = input().split()

    for i in range(int(inp[0])):
        database.append(input())
    for i in range(int(inp[1])):
        report.append(input())
```

Compare the two lists (database, report) and create new list (inspect) that contains elements that are present in the database list but not in the report list [Line 12]:

```py
    inspect = list(set(database) - set(report)):
```

>***NOTE:*** *The problem explicitly stated that "[n]ames are unique within a test case. This means that there will be no duplicates in the test cases. Because of this fact, we can use the code in Line 12. If there were any duplicates we would have to use a for loop and .remove(). More details can be found [here](../../README.md#operations)* 

Sort the new list (inspect) in alphabetical order (case-insensitive) [Line 12]:

```py
    inspect.sort(key=str.lower)
```

Print out the list (inspect) one line at a time [Lines 15-16]:

```py
    for i in inspect:
        print(i)
```

> **Final Thoughts:** The difficulty of solving this problem will probably come from sorting the list in alphabetical order (case-insensitive). It is important to understand how each method works so you do not fall into various trickery and traps you might be presented with.

