from user import User

users = [
    User(1, 'bob', '123456')
]

username_mapping = { x.username: x for x in users }
userid_mapping   = { x.id: x for x in users }

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)