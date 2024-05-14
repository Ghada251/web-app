from flask import Flask, render_template, request, redirect 

import mysql.connector

app = Flask(__name__, static_folder='static')

mysql_host = 'database'  # This matches the service name in your Docker Compose configuration
mysql_user = 'root'
mysql_password = '25102004****$'
mysql_database = 'cloud'

def connect_to_mysql():
    return mysql.connector.connect(host=mysql_host, user=mysql_user, password=mysql_password, database=mysql_database)



# Define route to fetch data from MySQL and render HTML template
@app.route('/')
def homepage():
    return render_template("index.html"
                            )

@app.route('/register')
def register():
    return render_template("home.html"
                            )



@app.route("/data")

def data():

    connection = connect_to_mysql()
    cursor = connection.cursor()

        # Execute SELECT query to retrieve data from MySQL student table
    cursor.execute('SELECT * FROM students')

        # Fetch all rows from the result set
    students = cursor.fetchall()

    connection.close()  # Close database connection

    return render_template('index2.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
