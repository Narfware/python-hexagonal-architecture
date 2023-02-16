from requests import post

# Basic component test, TODO factory boy to create mock data and create/delete data for each test

api_orders_url = "http://localhost/orders"


def test_should_return_201():
    request = post(api_orders_url, json={"product_id": "1234"})
    assert request.status_code == 201
    # TODO: delete data created


def test_should_return_400():
    # TODO: create data for this scenario
    request = post(api_orders_url, json={"product_id": "1234"})
    assert request.status_code == 400
