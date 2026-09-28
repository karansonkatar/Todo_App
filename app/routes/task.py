from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task

tasks_bp = Blueprint ('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    tasks = Task.query.all()
    return render_template('task.html', tasks=tasks)

@tasks_bp.route('/add', methods = ["POST"])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        new_tasks= Task (title=title, status = "pending")
        db.session.add(new_tasks)
        db.session.commit()
        flash('task added successfully', 'success')
    
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods = ["POST"])
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == "pending":
           task.status = "working"
        elif task.status == "working":
           task.status = "Done"
        else:
            task.status = "pending"
        
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear', methods = ["POST"])
def clear_task():
    Task.query.delete()
    db.session.commit()
    flash("All Task Cleared", 'info')
    return redirect(url_for('tasks.view_tasks'))