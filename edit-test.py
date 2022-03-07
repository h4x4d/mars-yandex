import requests


data = {
    'team_leader': 1,
    'job': '123',
    'work_size': 456,
    'collaborators': '3, 4'
}

print(requests.post('http://127.0.0.1:5000/api/jobs/edit/5', json=data).json())
print(requests.get('http://127.0.0.1:5000/api/jobs').json())