from flask import Flask, render_template
from utils import occ

app = Flask(__name__)

@app.route('/occupations')
def run():
    occ.opener()
    a = occ.chooser()
    return render_template("temp.html", george = occ.JOBS.keys() , mike = occ.JOBS, harry = a)

if __name__ == "__main__":
    app.run()
