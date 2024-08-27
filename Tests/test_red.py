import dataclasses

import requests
import  json
import time
headers = {
  'authorization': 'Bearer eyJraWQiOiJqMmpwRmpPXC9aUlVZRWJVN0pZVHpIUUp4STF1UWh5ZHlFcEFcL25mMXdFSEE9IiwiYWxnIjoiUlMyNTYifQ.eyJvcmlnaW5fanRpIjoiY2E4ZmRiMjctMzczMi00NGQzLTlmMmYtOTI2NzM3ODBkNDQwIiwic3ViIjoiYjdmNTcxNDktOGRhOS00ZWRjLWJjMTAtMTUzNzgyNDhmM2EwIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTcyNDMzNTgzNiwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfbWs2YTVwTklMIiwiZXhwIjoxNzI0NTk2ODE0LCJpYXQiOjE3MjQ1OTUwMTQsImp0aSI6IjMxM2NjMjQzLTQyOTQtNDNjYS1iNWNjLWU1ZmEyZWJhMmM5NCIsImNsaWVudF9pZCI6ImFlMTVyM2tyZjQzdDFqbWNxZWJ0Z2Y2MzYiLCJ1c2VybmFtZSI6ImM0OGRkOGNhLTgxYzAtNDVlNi04YWUzLWU0MmEzMWNjYzdkOSJ9.fGspT3YKvCR5lkB_sfcd3b_shY8_V3zghPLt47ZgHdbLAq7MKPs3bYgUIlyYk5jKZ9TvCv8_bN4MtJQwovG8AtCgOV5c-9Bd805gZ_PoIQaRwYPKadZ8CeCs5L4X9MOkNXSh4SDoAV7j1IOYekJky8EyNivs21U2c8MbUzqbsLHr-WTe3FNF3oHo75yEhrAtCuW26T0U_YH4VDA1qrBeWcLVQjnOi5p0aSJPVlAQzZknRC3KM8jofYCPvpi9-tsWLn3KMeq9n6gWWgAJf0KdIIXPN6UURVUcQF4iDHViOBBP88oaUC-aAcx9zl0Iu1cvXR3dDsKv4M642lhB3gNtyg',
}

ENDPOINT ="https://todo.pixegami.io/"

# response = requests.get(ENDPOINT)
# print(response)
# data =response.json()
# print(data)
#
# status_code =response.status_code
# print(status_code)

def test_can_Call_endpoint():
    response = requests.get(ENDPOINT)
    print(response)
    assert response.status_code==200
    pass

def test_can_create_task():
    payload= new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code==200
    data = create_task_response.json()
    print(data)
    task_id = data['task']['task_id']
    get_task_response =  get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data= get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_can_update_task():
    payload= new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code ==200
    task_id = create_task_response.json()["task"]["task_id"]

    new_payload={
            "user_id":payload["user_id"],
            "task_id":task_id,
            "content": "my UODATEDDD test contents ",
            "is_done": True
        }
    update_task_response= update_task(new_payload)
    assert update_task_response.status_code == 200
    get_task_response =get_task(task_id)
    assert get_task_response.status_code ==200
    get_task_data =get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

    pass

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)


def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")


def new_task_payload():
     return {
        "content": "my test contents ",
        "user_id": "test_user",
        "is_done": False
     }
