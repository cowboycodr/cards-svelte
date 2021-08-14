import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

USERS = [
  {
    'id': 'fd96f338-ba68-4f6b-88d9-b272ca61ea33',
    'name': 'cowboycodr',
    'nick': 'Kian',
    'pfp': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwOAz9F23MraOeH5RtdAj883MB-ywpMIPYSv36fcSVFazd1DQANyabtJ3eKBgRw1_t2PM&usqp=CAU'
  }
]

CARDS = [
  {
    'user_id': USERS[0]['id'],
    'id': str(uuid.uuid4()),
    'content': 'Cards, the in-progress, open-source, simplistic retake of social media',
    'likes': 0,
    'shares': 0
  }
]

@app.route('/', methods=['GET'])
def index():
  api_urls = {
    'users': '/users',
    'cards': '/cards',
  }

  return jsonify(api_urls)

@app.route('/cards', methods=['GET'])
def cards():
  response_object = {'status': 200}

  if request.method == 'GET':
    response_object['cards'] = CARDS

  return jsonify(response_object)

@app.route('/cards/<card_id>', methods=['GET'])
def card(card_id):
  response_object = {'status': 200}

  if request.method == 'GET':
    for card in CARDS:
      if card['id'] == card_id:
        response_object['card'] = card
        break

    response_object['status'] = 400

  return jsonify(response_object)

@app.route('/users', methods=['GET'])
def users():
  reponse_object = {'status': 200}

  if request.method == 'GET':
    reponse_object['users'] = USERS

  return jsonify(reponse_object)

@app.route('/users/<user_id>', methods=['GET'])
def user(user_id):
  response_object = {'status': 200}

  if request.method == 'GET':
    for user in USERS: 
      if user['id'] == user_id:
        response_object['user'] = user
    response_object['status'] = 400

  return jsonify(response_object)

if __name__ == '__main__':
  app.run(port=5050)