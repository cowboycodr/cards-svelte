import uuid
from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.cards

DEFAULT_PFP = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwOAz9F23MraOeH5RtdAj883MB-ywpMIPYSv36fcSVFazd1DQANyabtJ3eKBgRw1_t2PM&usqp=CAU"

def create_user(nickname, username, pfp=DEFAULT_PFP, publish=False):
  user = {
    'id': str(uuid.uuid4()),
    'nick': nickname,
    'name': username,
    'pfp': pfp
  }

  if publish:
    db.users.insert_one(
      user
    )

  return user

def create_card(content, author, publish=False):
  card = {
    'id': str(uuid.uuid4()),
    'author': author,
    'content': content,
    'likes': 0,
    'shares': 0
  }

  if publish:
    db.cards.insert_one(
      card
    )

  return card

def get_user(id):
  user = db.users.find_one({'id': id})

  return user

def get_card(id):
  card = db.users.find_one({'id': id})

  return card

me = get_user('c12073cc-c3c0-468a-9393-f46836b0e607')

cards = 10
for _ in range(cards):
  print(
    create_card(
      content='Cards, the in-progress, open-source, simplistic retake of social media.',
      author=me,
      publish=True
    )['id']
  )