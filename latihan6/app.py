from flask import Flask, render_template
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flaskmysql"
)

cursor = db.cursor()

app = Flask(__name__, template_folder="templates")

@app.route("/")
def main():
    query = 'select * from users;'
    cursor.execute(query)
    table = cursor.fetchall()
    cursor.close()
    return render_template('home.html', tables=table)

if __name__=='__main__':
    app.run(debug=True)