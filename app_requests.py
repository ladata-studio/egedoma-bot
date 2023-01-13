import requests
from hashlib import sha256
import os
import json

hash_noise = os.getenv('HASH_NOISE')


def save_hash(phrase, user):
    code = f'{hash_noise}{user.id}{phrase}'
    hash = sha256(bytes(code, 'utf-8')).hexdigest()
    payload = {'hash': hash}
    print(json.dumps(payload))
    res = requests.post('http://127.0.0.1:80/auth_hash/', data=payload)
    print(res.text)


def save_user(user, photo):
    user = dict(user)
    user['telegram_id'] = user.pop('id')
    user['telegram_username'] = user.pop('username')
    payload = dict(user)
    payload['photo'] = photo
    print(json.dumps(payload))
    res = requests.post('http://127.0.0.1:80/student/', data=payload)
    print(res.text)
