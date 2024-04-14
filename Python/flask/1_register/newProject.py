from flask import Flask,render_template,request
app = Flask(__name__)

database = []

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/register')
def register():
   return render_template("register.html")

@app.route('/register_form_data' , methods=['POST'])
def register_form_data():
   email = request.form['email']
   pwd = request.form['password']
   print("This is Email : ",email);
   print("This is Password : ",pwd);
   database.append([email,pwd]);
   print(database);
   return "Register Successfully"


@app.route('/login')
def login():
   return render_template("login.html")

@app.route('/login-form-data',methods=['POST'])
def login_form_data():
   email = request.form['email']
   pwd = request.form['password']

   if [email,pwd] in database:
      return "Login Successfullly"
   return "Invalid Credentials"

print(database)

if __name__ == '__main__':
   app.run()