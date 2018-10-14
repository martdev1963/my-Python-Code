#from flask.ext.sqlalchemy import SQLAlchemy
#from flask_caching.backends.cache import SQLAlchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)

# ------------------------------------DATABASE CODE START---------------------------------------------------------------------------------
#          notice dict key and its value...This is your database connection...
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/height_collector'
db=SQLAlchemy(app) # now the app object will know where the database is...

class Data(db.Model): # SQLAlchemy object now inheriting the Model class...
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True) # variables local to this class only...
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer) # if user enters a decimal number you get error (you would have to use float data type...)

    # initialize the class instance variables...
    def __init__(self, email_, height_):   # self is the object being instantiated...upon calling the class constructor...
        self.email_=email_
        self.height_=height_
# ------------------------------------DATABASE CODE END-------------------------------------------------------------------------------------

@app.route("/")  # GET method is the default method for request object of HTTP class...(implicitly)
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST']) # explicitly specifying POST method...
def success():
    if request.method=='POST': # making sure this is a POST request and not a GET request...
        email=request.form['email_name'] # variables local to this function only... email_name is a key which holds a value (key/value pair...)
        height=request.form['height_name']
        print(email, height)
        print(request.form) # print out the type attribute of the form for the email...
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email,height) # this maps the instance variables to the user input otherwise you get: sqlalchemy.orm.exc.UnmappedInstanceError
            db.session.add(data) # SQLAlchemy object...
            db.session.commit() # commit changes to database...
            # notice this line of code is after the db.session.commit() so it can also grab the last user entry...
            # .scalar() extracts the number out of this variable average_height...which is an SQL statement returned by db.session.query(func.avg(Data.height_))
            average_height=db.session.query(func.avg(Data.height_)).scalar() # grabbing all the height data input from the database including the last user's entry!
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count() # counting the height values in the database table...
            send_email(email, height, average_height, count) # function call, invoking the email code...
            print(average_height)
            return render_template("success.html") # if email isn't already in the database, return success.html
    return render_template('index.html',  # else, return index.html and have user have another go...
     text="Hummm...seems like we got something from that email address already.")

if __name__ == '__main__':
    app.debug=True
    app.run() # default port is port 5000 if left empty app.run(port=5002)...
