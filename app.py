from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)                 # Creates a Flask application instance to run the web app

@app.route('/')                       # @app.route('/') → Defines the URL path (here '/' = homepage)
def home():                           # def home(): → Function that runs when the homepage is visited
    return render_template('index.html')             # return "Home it is!" → Sends this text as response to the browser

@app.route('/login')                  
def login():                          
    return render_template('auth/login.html')           

@app.route('/register')                  
def register():                          
    return render_template('auth/register.html')
        
@app.route('/forgot_password')                  
def forgot_password():                          
    return render_template('auth/forgot_password.html') 

@app.route('/dashboard/user')                  
def user():                          
    return render_template('dashboard_user.html')   

@app.route('/dashboard/admin')                  
def admin():                          
    return render_template('dashboard_admin.html')

if __name__ == '__main__':            # if __name__ == '__main__': → Makes sure this file runs only when executed directly
    app.run(debug=True)               # app.run(debug=True) → Starts the Flask development server
                                      # debug=True → Automatically restarts server on code changes & shows error details


    
