import requests # type: ignore

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2IiwiZXhwIjoxNzUzMTMxMzMwfQ.AEzO76WZvekmO-GeiM0DbBa0dI8i7ykwuk9fWpF4N-o"
}

requisisao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisisao)
print(requisisao.json())