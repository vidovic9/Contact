from flask import Flask, render_template, request, redirect, url_for
from mysql import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    contacts = db.get_all_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        db.add_contact(name, phone)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:contact_id>')
def delete(contact_id):
    db.delete_contact(contact_id)
    return redirect(url_for('index'))

@app.teardown_appcontext
def close_db(exception=None):
    db.close()

if __name__ == '__main__':
    app.run(debug=True)
