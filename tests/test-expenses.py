def test_create_expense(test_client):
    # Assuming user is already created and authenticated
    response = test_client.post(
        "/expenses/",
        json={
            "title": "Dinner",
            "total_amount": 3000,
            "split_method": "equal",
            "participants": [{"user_id": 1}, {"user_id": 2}, {"user_id": 3}],
        },
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Dinner"
