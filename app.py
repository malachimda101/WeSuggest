from flask import Flask, render_template, request, redirect, url_for
from databases import DatabaseStorage
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/suggest-here", methods=['GET', 'POST'])
def suggest_here():
    if request.method == 'GET':
        return render_template('suggest-here.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])
    if request.method == 'POST':
        database = DatabaseStorage()
        database.submit("homie", "mchomieface", "homie@wesleyan.edu", request.form['complaint'])

        return redirect(url_for('complaints'))

@app.route("/complaints")
def complaints():
    seenComplaints = request.cookies.get('seenComplaints')
    if(seenComplaints == None):
        seenComplaints = ""
    seenComplaints = seenComplaints.split()
    database = DatabaseStorage()
    allComplaints = database.query();
    print(allComplaints)
    complaint = "No more complaints!"
    upvotes = 0
    for x in allComplaints:
        complaint = allComplaints[x][0]
        upvotes = allComplaints[x][1]

    
    return render_template('complaints.html', complaintid=49, complaint=complaint, upvotes=upvotes)

@app.route("/agree/<complaint>")
def agree(complaint):
    print(complaint + "agreed with")
    return redirect(url_for('complaints'))

if __name__ == '__main__':
    app.run(debug=True)