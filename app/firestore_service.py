import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


project_id = 'platzi-flask-293100'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {'projectId': project_id})

db = firestore.client()


def get_users():
    # Return all the users
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()


def get_todos(user_id):
    # Return the entire collection of a specific user by passing user's ID.
    return db.collection('users').document(user_id).collection('todos').get()
