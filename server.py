from flask import Flask, render_template, request, redirect
from flask import url_for
from markupsafe import escape
import csv

# To instantiate a Flask app
app = Flask(__name__)
print(__name__)

# Use a declarator (to give higher level of abstraction)
# Everytime we hit 'slash' or the root, please define a function call
# hello_world() and return the "Hello World!" string
'''
@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    #print(url_for('static', filename='sunny_day.ico'))
    #return "<p>Hello, World! So nice to see you Justin and Ryan and Boris!</p>"
    return render_template('index.html', name=username, post_id=post_id)
'''

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

'''
@app.route("/index.html")
def index_page():
    return render_template('index.html')

@app.route("/works.html")
def works_page():
    return render_template('works.html')

@app.route("/about.html")
def about_page():
    return render_template('about.html')

@app.route("/contact.html")
def contact_page():
    return render_template('contact.html')

@app.route("/components.html")
def components_page():
    return render_template('components.html')
'''

def write_to_file(data):
    email  = data['email']
    subject = data['subject']
    message = data['message']
    with open("database.txt", 'a') as file:
        file.write(f'{email},{subject},{message}\n')

def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open("database2.csv", newline='', mode='a') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #return render_template('login.html', error=error)
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong, try again!'