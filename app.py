from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/complaints")
def complaints():

    return render_template('complaints.html', complaint="People in musichouse can't flush the toilet for shit.", upvotes=29)

if __name__ == '__main__':
    app.run(debug=True)