import requests

data = {
    'id': 5,
    'team_leader': 1,
    'job': '123',
    'work_size': 17,
    'collaborators': '1, 2, 3, 4'
}

print(requests.post('http://127.0.0.1:5000/api/jobs', json=data).json())
print(requests.get('http://127.0.0.1:5000/api/jobs').json())

data = {
    'id': 5,
    'team_leader': 1,
    'job': '123',
    'work_size': 17,
    'collaborators': '1, 2, 3, 4'
}

print(requests.post('http://127.0.0.1:5000/api/jobs', json=data).json())
# Совпадение id

data = {
    'id': 7,
    'team_leader': '1234asdf',
    'job': '123',
    'work_size': 17,
    'collaborators': '1, 2, 3, 4'
}

print(requests.post('http://127.0.0.1:5000/api/jobs', json=data).json())
# Team_leader не int

data = {
    'id': 6,
    'team_leader': 1,
    'job': '123',
    'work_size': 'asd',
    'collaborators': '1, 2, 3, 4'
}

print(requests.post('http://127.0.0.1:5000/api/jobs', json=data).json())
# Work_size не int