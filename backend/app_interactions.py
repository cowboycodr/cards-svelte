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
    content: content
  }

  if publish:
    db.cards.insert_one(
      card
    )

  return card

print(
  create_user(
    nickname='Kian',
    username='cowboycodr',
    publish=True
  )
)