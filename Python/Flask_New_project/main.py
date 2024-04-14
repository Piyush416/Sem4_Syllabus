from flask import Flask,render_template,request

import mysql.connector

sql = mysql.connector

connection = sql.connect(
    host='localhost',
    user='root',
    password='',
    database='first_database'
)

my_cursor = connection.cursor();


app = Flask(__name__)

database = []

@app.route('/')
def home():
    return render_template('homepage.html')

# Register
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')
@app.route('/register-form-data', methods=['POST'])
def register_form_data():
    phn = request.form['phn']
    pwd = request.form['pwd']
    query = '''insert into user_data(phn,pwd) values(%s,%s);'''
    values = (phn,pwd)
    my_cursor.execute(query,values)
    connection.commit()
    database.append([phn,pwd])
    return "Register SuccessFully <br><a href='login'>GO TO LOGIN</a>"

# Login
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
@app.route('/login-form-data', methods=['POST'])
def login_form_data():
    phn1 = int(request.form['phn'])
    pwd1 = request.form['pwd']
    query1 = '''select * from user_data'''
    my_cursor.execute(query1)
    mydata = my_cursor.fetchall()
    print(mydata)
    if (phn1,pwd1) in mydata:
        return "Login SuccessFully"
    return "Invalid Login"

app.run(debug=True)
