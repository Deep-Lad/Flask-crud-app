from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['sampledatabase']

#display
@app.route('/')
def index():
    tasks = db.tasks.find()
    return render_template('index.html', tasks=tasks)

#create
@app.route('/create')
def create():
    return render_template('create.html')    


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    db.tasks.insert_one({'task': task})
    return redirect(url_for('create'))

#update
@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/updateaction', methods=['POST'])
def updateaction():
    task = request.form['task']
    new_task = request.form['new_task']
    db.tasks.update_one({'task': task}, {'$set': {'task': new_task}})
    return redirect(url_for('update'))

#delete
@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/deleteaction', methods=['POST'])
def deleteaction():
    task = request.form['task']
    db.tasks.delete_one({'task': task})
    return redirect(url_for('delete'))

if __name__ == '__main__':
    app.run(debug=True)
