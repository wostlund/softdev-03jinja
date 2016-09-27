import random
JOBS = {}

def opener():
    a = open("data/occupations.csv", "r")
    b = a.read().split("\n")
    b = b[1:]
    for i in range(len(b) -2):
        if b[i][0] == "\"":
            JOBS[b[i].split("\"")[1]] = float(b[i].split("\"")[2][1:])
        else:    
            JOBS[b[i].split(",")[0]] = float(b[i].split(",")[1])

opener()

def chooser():
    choices = []
    jobs = JOBS.keys()
    for i in jobs:
        for j in range(int(JOBS[i] * 10) -1 ):
            choices.append(i)
    a = random.randrange(len(choices))
    return(choices[a])

print(chooser())

def trial():
    i = 0
    results = {}
    while i < 1000:
        x = chooser()
        if x in results.keys():
            results[x] = (results[x] + 1)
        else:
            results[x] = 1
        i = i + 1
    print(results)


