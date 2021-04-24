from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def index(methods=['GET', 'POST']):
    if request.method == 'GET':
        return render_template('index.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])
    if request.method == 'POST':
        print(request.form['complaint'])
        return redirect(url_for('complaints'))

@app.route("/complaints")
def complaints():
    return render_template('complaints.html', complaintid=49, complaint="People in musichouse can't flush the toilet for shit.", upvotes=29)

if __name__ == '__main__':
    app.run(debug=True)