for _ in range(int(input())):
    database = []
    report = []

    inp = input().split()

    for i in range(int(inp[0])):
        database.append(input())
    for i in range(int(inp[1])):
        report.append(input())
    
    inspect = list(set(database) - set(report))
    inspect.sort(key=str.lower)

    for i in inspect:
        print(i)