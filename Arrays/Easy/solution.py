for _ in range(int(input())):
    inp = input().split()

    database = []
    report = []
    
    for i in range(int(inp[0])):
        database.append(input())
    for i in range(int(inp[1])):
        report.append(input())
    
    inspect = list(set(database) - set(report))
    inspect.sort(key=str.lower)

    for i in inspect:
        print(i)

#trick in this problem is sorting in alphabetical order but case-insensitive
#make sure to add this to main README.md