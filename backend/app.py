import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.cards

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  api_calls = {
    'users': '/users',
    'cards': '/cards'
  }

  return jsonify(api_calls)

@app.route('/cards', methods=['POST', 'GET'])
def cards():
  reponse_object = {'status': 200}

  if request.method == 'GET':
    cursor = db.cards.find({})
    result = []

    for document in cursor:
      document['_id'] = str(document['_id'])
      result.append(document)

    reponse_object['cards'] = result
  elif request.method == 'POST':
    pass

  return jsonify(reponse_object)

@app.route('/users')
def users():
  response_object = {'status': 200}

  if request.method == 'GET':
    cursor = db.users.find({})
    result = []

    for document in cursor:
      document['_id'] = str(document['_id'])
      result.append(document)

    response_object['users'] = result

  return jsonify(response_object)

@app.route('/users/<user_id>')
def user(user_id):
  response_object = {'status': 200}

  if request.method == 'GET':
    result = db.users.find_one({'id': user_id})
    result['_id'] = str(result['_id'])

    response_object['user'] = result

  return jsonify(response_object)

if __name__ == '__main__':
  app.run(port=5050)