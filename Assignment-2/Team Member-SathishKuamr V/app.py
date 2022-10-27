
from flask import Flask,render_template, flash,redirect, url_for,request
import sqlalchemy
import ibm_db






app = Flask(__name__)
app.secret_key="hello"

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")



@app.route("/about")                                      
def about():
	return render_template("about.html")


@app.route("/list")
def list():
   return render_template("list.html")


@app.route('/signin',methods=["post","get"])
def signin():
  return render_template('signin.html')


@app.route('/signup',methods=["post","get"])
def signup():
  return render_template('signup.html')




        # with sql.connect("users.db") as connection:
        #     cursor = connection.cursor()
        #     cursor.execute(
        #         "SELECT email,password FROM STUDENTS WHERE email=?", (email,))
        #     student = cursor.fetchone()
        #     print(student)
            # if student:
            #     if password == student[1]:
            #         error = "Logged in"
            #         return render_template("home.html", error=error)
            #     else:
            #         error = "User Invalid Password"
            #     return render_template("signin.html", error=error)
            # else:
            #     error = "invalid credentials"
            #     return render_template("signin.html", error=error)

@app.route("/item")
def addItem():
    with sql.connect("students.db") as connection:
        connection.row_factory = sql.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        users = cursor.fetchall()
        # print(users)

    return render_template("item.html", user=users)


@app.route("/edit/<key>", methods=["GET", "POST"])
def editItem(key):
    if request.method == "GET":
        with sql.connect("students.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students WHERE name==? ", (key,))
            user = cursor.fetchone()
            print(user)
            return render_template("addpage.html", item=user)
    else:
        uname = request.form['username']
        contact = request.form['contact']
        with sql.connect("students.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE students SET name=?,contact=? WHERE name=?", (uname, contact, key,))
            connection.commit()
            return redirect("/item")


@app.route("/delete/<name>")
def deletePage(name):
    with sql.connect("students.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE name=?", (name,))
        return redirect("/item")  



 
                   
  
  



  
  
  
  
  
  

  
