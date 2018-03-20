from flask import Flask, render_template, request,jsonify
import requests
from  sqlalchemy import  create_engine, MetaData, Column, Table
import json
#import database as dbb
app = Flask(__name__,static_folder='/home/varun/PycharmProjects/untitled1/templates/static')
database_url="sqlite:////home/varun/PycharmProjects/untitled1/university.db"

def notnull(var):
    if(var ==''):
        return True
    return False
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/form2', methods=['GET', 'POST'])
def page2():
    unilisr=[]
    countrylist=[]
    deadlinelist=[]
    db = create_engine(database_url)
    con = db.connect()
    metadata = MetaData(db)
    uni = Table('universe', metadata, autoload=True, autoload_with=db)

    select = "SELECT name from universe"
    select2="SELECT DISTINCT country from universe"
    select3="SELECT DISTINCT deadline from universe"
    dele = "DELETE from universe where  name='Massachusetts Institute of Technology'"
    con.execute(dele)
    #on.execute("INSERT into universe values('Massachusetts Institute of Technology','USA',164,160,95,7,'AWA 5.0','15 December 2017')")
    name_list = []
    coun = []
    greq = []
    grev = []
    toefl = []
    ielts = []
    spec = []
    deadline = []
    selectcustom="SELECT * from universe"
    stringstate=""
    for i in con.execute(select3):
        deadlinelist.append(i[0])
    for i in con.execute(select):
        unilisr.append(i[0])
    for i in con.execute(select2):
        countrylist.append(i[0])
    if request.method=='POST':
        requni=request.form['univname']
        reqcoun=request.form['count']
        reqquant=request.form['quant']
        reqverbal=request.form['verbal']
        reqtoefl=request.form['toefl']
        reqielts=request.form['ielts']
        reqdead=request.form['deadselect']

        if requni != "":
            if len(stringstate)>0:
                stringstate = stringstate + " AND name= '" + requni + "'"
            else:
                stringstate=stringstate + " name= '"+requni +"'"
        if reqcoun !="":
            if len(stringstate) > 0:
                stringstate=stringstate+ " AND country='"+reqcoun +"'"
            else:
                stringstate = stringstate + " country='" + reqcoun + "'"
        if reqquant != "":
            if len(stringstate)>0:
                stringstate=stringstate+" AND greq<='"+reqquant+"'"
            else:
                stringstate = stringstate + " greq<='" + reqquant + "'"
        if reqverbal != "":
            if len(stringstate):
                stringstate = stringstate + " AND grev<='" + reqverbal + "'"
            else:
                stringstate=stringstate+ " grev<='"+reqverbal+"'"
        if reqtoefl !="":
            if len(stringstate):
                stringstate = stringstate + " AND toefl<='" + reqtoefl + "'"
            else:
                stringstate=stringstate+ " toefl<='"+reqtoefl+"'"
        if reqielts !="":
            if len(stringstate)>0:
                stringstate = stringstate + " AND ielts<='" + reqielts + "'"
            else:
                stringstate=stringstate+" ielts<='"+reqielts+"'"
        if reqdead !="" and reqdead!= "All":
            if len(stringstate)>0:
                stringstate=stringstate+ " AND deadline='"+reqdead+"'"
            else:
                stringstate = stringstate + " deadline='" + reqdead + "'"
        if stringstate!="":
            selectcustom=selectcustom+" where"+stringstate

        result = con.execute(selectcustom)
        for i in result:
            name_list.append(i[0])
            coun.append(i[1])
            greq.append(i[2])
            grev.append(i[3])
            toefl.append(i[4])
            ielts.append(i[5])
            spec.append(i[6])
            deadline.append(i[7])
        if len(name_list)==0:
            error="Enter the right credentials."
            return render_template("Page2.html",pagelist=unilisr,country=countrylist,dead=deadlinelist,error=error)
        resdic = {"uname": name_list, "ucountry": coun, "greq": greq, "grev": grev, "toefl": toefl,
                  "ielts": ielts, "uspec": spec, "deadline": deadline}
        return render_template("table.html",resdic=resdic)

    return render_template("Page2.html",pagelist=unilisr,country=countrylist,dead=deadlinelist)

if __name__ == '__main__':
    app.run(debug=True)

