from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFATION'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    completed = db.Column(db.Boolean) 
    
db.create_all()

@app.route("/")
def get_all_items():
    todoList = Todo.query.all()
    return render_template('base.html', todoList = todoList)   

@app.route("/add", methods = ["POST"])
def add_item():
    desc = request.form.get("desc")
    todo = Todo(title = desc, completed = False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for("get_all_items"))

@app.route("/update/<int:todo_id>")
def update_item(todo_id):
    todo = Todo.query.filter_by(id = todo_id).first()
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("get_all_items"))

@app.route("/delete/<int:todo_id>")
def delete_item(todo_id):
    todo = Todo.query.filter_by(id = todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("get_all_items"))





    
        

    
