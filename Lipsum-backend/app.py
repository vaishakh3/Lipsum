from flask import Flask, request, jsonify, make_response
import jwt
from functools import wraps
from pymongo import MongoClient
import random, string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdiufhsibfjqwe298hiwsfu872gwbJHBGUfy'
client = MongoClient('localhost', 27017)
db = client.flask_db


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing.'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid.'}), 401

        return f(*args, **kwargs)

    return decorated


@app.route('/login', methods='POST')
def login():
    user = request.json.get('user')
    hash = request.json.get('hash')



    if auth and auth.username == 'username' and auth.password == 'password':
        token = jwt.encode({'user': auth.username}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route('/signup', methods='POST')
def signup():
    user = request.json.get('user')
    hash = request.json.get('hash')

    if user and hash:
        db.users.insert_one({'user': user, 'hash': hash})
        return jsonify({'message': 'User created.'})

    return jsonify({'message': 'User not created.'})

@app.route('/create-quiz', methods='POST')
@token_required
def create_quiz():
    user = request.json.get('user')
    quiz = request.json.get('quiz')

    raw = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))

    if quiz:
        db.quizzes.insert_one({'quiz': quiz, 'user': user})
        return jsonify({'message': 'Quiz created.', 'code' : raw})

    return jsonify({'message': 'Quiz not created.'})

@app.route('/<room>/', methods='POST')
def get_quiz(room):
    pass