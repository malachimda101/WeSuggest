from flask import Flask, render_template, request, redirect, url_for, make_response
from databases import DatabaseStorage
app = Flask(__name__)
database = DatabaseStorage()

@app.route("/")
def index():
    return render_template('index.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/suggest-here", methods=['GET', 'POST'])
def suggest_here():
    if request.method == 'GET':
        return render_template('suggest-here.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])
    if request.method == 'POST':
        database = DatabaseStorage()
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        typeof = request.form['typeof']
        complaint = request.form['complaint']
        database.submit(firstname, lastname, email, complaint, typeof)

        return redirect(url_for('complaints'))

@app.route("/complaints")
def complaints():
    seenComplaints = request.cookies.get('seenComplaints')
    if(seenComplaints == None):
        seenComplaints = ""
    seenComplaints = seenComplaints.split()
    allComplaints = database.query();
    complaintId = 0
    complaint = "There are no more suggestions, why not make another one!"
    upvotes = 0
    nomorecomplaints = True

    for x in allComplaints:
        if(request.cookies.get(str(x)) != 'set'):
            nomorecomplaints = False
            complaintId = x
            complaint = allComplaints[x][0]
            upvotes = allComplaints[x][1]
            break

    resp = make_response(render_template('complaints.html', complaintid=complaintId, complaint=complaint, upvotes=upvotes, nomorecomplaints=nomorecomplaints))
    resp.set_cookie(str(complaintId), 'set')
    return resp


@app.route("/agree/<complaintid>")
def agree(complaintid):
    print(complaintid + "agreed with")
    database.add_vote(complaintid)
    return redirect(url_for('complaints'))

@app.route("/topcomplaints")
def topcomplaints():
    topcomplaints = []
    allComplaints = database.query();
    #allComplaints = sorted(allComplaints, )
    #allComplaints.sort(key=lambda x: x[1], reverse=True)
    #for w in sorted(allComplaints, key=(lambda x: allComplaints.get(x)[1]), reverse=True):
    #    print(w, allComplaints[w])
    complaintValues = allComplaints.values()
    complaintValueList = []
    for x in complaintValues:
        
        if(x[1] ==''):
            complaintValueList.append((x[0], 0))
        else:
            complaintValueList.append(x)
    complaintValueList = sorted(complaintValueList, key=lambda x:x[1], reverse=True)

    resp = make_response(render_template('topcomplaints.html', topcomplaints=complaintValueList))
    return resp

if __name__ == '__main__':
    app.run(debug=True)