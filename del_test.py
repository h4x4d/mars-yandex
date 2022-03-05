import requests

print(requests.delete('http://127.0.0.1:5000/api/jobs/delete/5').json())
print(requests.get('http://127.0.0.1:5000/api/jobs').json())

print(requests.delete('http://127.0.0.1:5000/api/jobs/delete/5ad').json())
print(requests.delete('http://127.0.0.1:5000/api/jobs/delete/111').json())