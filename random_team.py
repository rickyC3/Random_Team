import random

def Random_Team_Func(N:int, teams:int, names:list):
    l = N
    emptyList = []
    last_teams = [ list(emptyList) for i in range(teams)]
    t = 0
    for i in range(N):
        n = random.randint(0, 1000) % l
        print("pls", names[n] ,"go to", t, "team.")
        last_teams[t].append(names[n])
        names.pop(n)
        l -= 1
        t = (t+1)%teams
        if (l == 1):
            last_teams[(t)%teams].append(names[0])
            print("pls", names[0], "go to", (t)%teams,"team.")
            break

    return last_teams
"""

    while 1:
        N = input("people number: ")
        if (N.isnumeric() and int(N) != 0):
            N = int(N)
            break
        else:
            print("input wrong type. Pls input again.")

    while 1:
        teams = input("teams number: ")
        if (teams.isnumeric() and int(teams) != 0):
            teams = int(teams)
            break
        else:
            print("input wrong type. Pls input again.")

    print("input people name or number ")

    for i in range(N):
        print(i+1, end = " ")
        name = input("th: ")
        names.append(name)
"""
    
    









