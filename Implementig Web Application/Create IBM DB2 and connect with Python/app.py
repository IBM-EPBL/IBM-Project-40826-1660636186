from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import ibm_db
connection=ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=plq76207;PWD=ZmeqbSx0vyVOuxoG","","")



app = Flask(__name__)
app.secret_key = 'HIII'


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/Signup')
def new_student():
  return render_template('Signup.html')

@app.route('/aa',methods = ['POST', 'GET'])
def aa():
  if request.method == 'POST':

    name = request.form['name']
    address = request.form['address']
    city = request.form['city']
    phonenumber= request.form['phonenumber'] 
  
    sql = "INSERT INTO CUSTOMERS VALUES(?,?,?,?)"
    stm=ibm_db.prepare(connection,sql)
    ibm_db.bind_param(stm,1,name)
    ibm_db.bind_param(stm,2,address)
    ibm_db.bind_param(stm,3,city)
    ibm_db.bind_param(stm,4,phonenumber)
    ibm_db.execute(stm)
  return render_template('result.html')
