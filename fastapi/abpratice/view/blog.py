from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for


blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        print(request.args.get('user_email'), 'Email Address')
        return redirect('/blog/test_blog')
    else:
        print('check type', request.headers)
        print('set_email', request.form)
        # return redirect('/blog/test_blog')
        return redirect(url_for('blog.test'))
@blog_abtest.route('/test_blog')
def test():
    return render_template('blog_A.html')
