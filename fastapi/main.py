from flask import Flask


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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

