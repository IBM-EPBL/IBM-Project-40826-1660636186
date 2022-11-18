from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import sqlite3 as sql

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
         phonenumber = request.form['phonenumber']
         con = sql.connect("customer.db")
         cur=con.cursor()
         cur.execute("INSERT INTO customer(name,address,city,phonenumber) VALUES (?,?,?,?)",(name,address,city,phonenumber))
         con.commit()
  return render_template("result.html")

@app.route('/list')
def list():
   con = sql.connect("customer.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from customer")
   
   customer  = cur.fetchall()
   return render_template("list.html", customer  = customer )
