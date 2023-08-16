from flask import Flask, render_template, Blueprint

app = Flask(__name__)

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'
@app.route('/')
def login_page():
    return render_template("login.html", name="")

@app.route('/index')
def index_page():
    return render_template("index.html", name="")

#@app.route('/<name>')
#def profile_page(name):
#    return render_template("name.html", name=name, image="test.jpg")

@app.route('/search')
def search_page():
    return render_template("search.html")

@app.route('/add')
def add_page():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181)
