from crudoperation import *
from flask import *
app=Flask(__name__)
@app.route('/')
def openhomepage():
    return render_template('Home.html')
@app.route('/studentreg')
def studentreg():
    return render_template('studentreg.html')
@app.route('/savetostudenttable',methods=['POST','GET'])
def savedetails():
    if request.method=='POST':
        a=int(request.form['sid'])
        b = request.form['sname']
        c = request.form['sphone']
        d = request.form['saddress']
        e = request.form['sdob']
        f = request.form['sdoj']
        print(a,b,c,d,e,f)
        try:
            insertstudent(a,b,c,d,e,f)
            msg="Successfully Inserted"
        except:
            msg="Not Successfully Inserted"
        return render_template('result.html',msg=msg)
@app.route('/allstudent')
def openallstudent():
    rows=readallstudent()
    print(rows)
    return render_template('allstudent.html',rows=rows)
@app.route('/<id>/deletestudent')
def deletesinglestudent(id):
    print(id)
    msg=deletestudent(id)
    return render_template('result.html',msg=msg)
@app.route('/<id>/editstudent')
def updatesinglestudent(id):
    print(id)
    rows=readsinglestudent(id)
    print(rows)
    return render_template('editstudent.html',rows=rows)
@app.route('/updatetostudenttable',methods=['POST','GET'])
def updatedetails():
    if request.method=='POST':
        a=int(request.form['sid'])
        b = request.form['sname']
        c = request.form['sphone']
        d = request.form['saddress']
        e = request.form['sdob']
        f = request.form['sdoj']
        print(a,b,c,d,e,f)
        try:
            updatestudent(a,b,c,d,e,f)
            msg="Successfully updated"
        except:
            msg="Not Successfully updated"
        return render_template('result.html',msg=msg)

if __name__=='__main__':
    app.run(port=2022)