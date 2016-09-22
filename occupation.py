from flask import Flask, render_template
import random
JOBS = {}

app = Flask(__name__)

def opener():
    a = open("occupations.csv", "r")
    b = a.read().split("\n")
    b = b[1:]
    for i in range(len(b) -2):
        if b[i][0] == "\"":
            JOBS[b[i].split("\"")[1]] = float(b[i].split("\"")[2][1:])
        else:    
            JOBS[b[i].split(",")[0]] = float(b[i].split(",")[1])

def chooser():
    choices = []
    jobs = JOBS.keys()
    for i in jobs:
        for j in range(int(JOBS[i] * 10) -1 ):
            choices.append(i)
    a = random.randrange(len(choices))
    return(choices[a])

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

@app.route('/occupations')
def run():
    opener()
    a = chooser()
    return render_template("temp.html", george = JOBS.keys() , mike = JOBS, harry = a)

if __name__ == "__main__":
    app.run()
