import requests

def test_check_api():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)

    assert response.status_code==200 ,f"Expected response status code 200 but got {response.status_code}"

    assert response.headers["Content-Type"]=="application/json; charset=utf-8" ,f"got content-type {response.headers['Content-Type']}"

    json_response = response.json()

    assert json_response["name"]=="Leanne Graham", f"expected the name to be Leane Graham but got {json_response['name']}"

    assert json_response['company']['bs'] == 'harness real-time e-markets', f"expected company.bs 'harness real-time e-markets' but got {json_response['company']['bs']}"

