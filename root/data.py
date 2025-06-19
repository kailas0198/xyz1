from flask import Flask,render_template,request
import mysql.connector


app2 = Flask(__name__)

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "kailas@4225",
    database = "student_raw"
)
data1=conn.cursor()
@app2.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        action = request.form.get("action")

        if action=="insert":

            check_email = "SELECT*FROM student_raw WHERE email=%s"
            data1.execute(check_email,(email,))
            result = data1.fetchone()
            if result:
                return f"already taken"
            sql = "INSERT INTO student_raw(name,email) VALUES(%s,%s)"
            val = (name,email)
            data1.execute(sql,val)
            conn.commit()
            return f"data saved"

        elif action=="update":
                sql = "UPDATE student_raw SET email=%s WHERE name=%s"
                val = (email,name)
                data1.execute(sql, val)
                conn.commit()
                return f"Update successfully"




    return render_template("form.html")

if __name__=="__main__":
    app2.run(debug=True)

