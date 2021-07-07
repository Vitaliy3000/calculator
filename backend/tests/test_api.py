def test_calc(client):
    # success case 1
    response = client.post("/calc", json={"number1": 10, "number2": 20})
    assert response.status_code == 200
    assert response.json() == {"result": 30}

    # success case 2
    response = client.post("/calc", json={"number1": 1, "number2": 0})
    assert response.status_code == 200
    assert response.json() == {"result": 1}

    # failure case: number1 not positive
    response = client.post("/calc", json={"number1": 0, "number2": 20})
    assert response.status_code == 422

    # failure case: number2 negative
    response = client.post("/calc", json={"number1": 1, "number2": -1})
    assert response.status_code == 422
