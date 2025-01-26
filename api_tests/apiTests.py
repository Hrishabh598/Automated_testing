import requests
import pytest

@pytest.mark.parametrize("userid,status_code,header,name,bs_element",[(1,200,"application/json; charset=utf-8","Leanne Graham","harness real-time e-markets"),(2,200,"application/json; charset=utf-8","Ervin Howell","synergize scalable supply-chains"),(3,200,"application/json; charset=utf-8","Clementine Bauch","e-enable strategic applications")])
def test_check_api(userid,status_code,header,name,bs_element):
    url = f"https://jsonplaceholder.typicode.com/users/{userid}"
    response = requests.get(url)

    assert response.status_code==status_code ,f"Expected response status code 200 but got {response.status_code}"

    assert response.headers["Content-Type"]==header ,f"got content-type {response.headers['Content-Type']}"

    json_response = response.json()

    assert json_response["name"]==name, f"expected the name to be {name} but got {json_response['name']}"

    assert json_response['company']['bs'] == bs_element, f"expected company.bs '{bs_element}' but got {json_response['company']['bs']}"

