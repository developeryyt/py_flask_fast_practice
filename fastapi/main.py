from flask import Flask, jsonify, request, render_template
import requests


app = Flask(__name__)



@app.route('/')
def main():
    return '<h1>메인 페이지</h1>'

@app.route('/hello')
def test():
    return 'Hello World!'


@app.route("/first")
def hello_first():
    return "<h3>Hello First</h3>"

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile: ' + username

@app.route('/message/<int:message_id>')
def get_message(message_id):
    print(type(message_id), message_id)
    return "message id: %d " % message_id

@app.route('/myinfo')
def get_myinfo():
    data = { 'name': 'patrick', "age": 30 }
    return jsonify(data)

@app.route('/login')
def login():
    username = request.args.get('user_name')
    pw = request.args.get('pw')
    email = request.args.get('email_address')

    print(username, 'username', email, pw)
    if username == 'patrick':
        return_data = { 'auth' : "success" }
    else:
        return_data = { 'auth' : "fail" }
    return jsonify(return_data)

@app.route('/hello/<user>')
def hello_user(user):
    return render_template('variable.html', name1=user, name2='kim')

@app.route('/loop')
def loop_test():
    info_list = ['list1', 'list2', 'list3']
    return render_template('loop.html', values=info_list)


@app.route("/google")
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

