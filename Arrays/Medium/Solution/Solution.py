for _ in range(int(input())):
    database = []

    inp = input().split()

    for i in range(int(inp[0])):
        info = input().split()
        database.append(info)

    for i in range(int(inp[1])):
        info = input().split()

        name = info.pop(0)
        stat = list(map(int, info))
        stat.sort(reverse=True)

        character = {
            'STR': '',
            'DEX': '',
            'CON': '',
            'INT': '',
            'WIS': '',
            'CHA': ''
        }
        
        for data in database:
            if name == data[0]:
                for index in range(len(stat)):
                    character[data[index+1]] = stat[index]
                     
        print(name)
        for key,value in character.items():
            print(f"{key}: {value}")