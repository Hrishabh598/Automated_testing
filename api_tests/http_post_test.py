import requests

def test_http_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    headers = {"Content-Type":"application/json"}

    payload = {
        "userId": 1,
        "title": "Test Blog title",
        "body": "This is the text of my latest blog post."
    }

    response = requests.post(url,json=payload,headers=headers)

    assert response.status_code==201, f"expected the response status code to be 201 but got {response.status_code}"

    response_json = response.json()

    assert "id" in response_json, f"response does not contain id"

    assert isinstance(response_json['id'],int), f"expected type of id to be int but got {type(response_json['id'])}"