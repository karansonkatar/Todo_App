from flask import Blueprint, render_template, session, request, redirect, url_for, flash


auth_bp = Blueprint('auth', __name__)

USER_CREDENTIAL={"username":"karan","password":"123"}


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method =="POST":
       username = request.form.get('username')
       password = request.form.get('password')

       if username == USER_CREDENTIAL['username'] and password == USER_CREDENTIAL['password']:
          session['user'] = username
          flash("login successful",'success')
          return redirect(url_for('tasks.view_tasks'))
       else:
            flash('invalid username and password','danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash('Logged out successfully', 'info')
    return redirect(url_for('auth.login')) 