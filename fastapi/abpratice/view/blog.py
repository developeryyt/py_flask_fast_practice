from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.user_mgmt import User
from control.session_mgmt import BlogSession
import datetime

blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        print(request.args.get('user_email'), 'Email Address')
        return redirect(url_for('blog.test_blog'))
    else:
        # print('check type', request.headers)
        # print('set_email', request.form['user_email'])
        # print('blog_check', request.form['blog_id'])
        user = User.create(request.form['user_email'], request.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        return redirect(url_for('blog.blog_fullstack'))

@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.test_blog'))

@blog_abtest.route('/blog_fullstack1')
def blog_fullstack():
    BlogSession.get_blog_page()
    if current_user.is_authenticated:
        return render_template('blog_A.html', user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'], 'anonymous', webpage_name)
        return render_template(webpage_name)
