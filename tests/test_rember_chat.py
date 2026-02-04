from fastapi.testclient import TestClient

def test_chat_remembers_previous_message(client):

    response_1 = client.post(

        "/chat/message",
        json={
            "message": "Quiero agendar una cita",
            "user_id": "123"
        }
    )

    assert response_1.status_code == 200
    assert "fecha" in response_1.json()["reply"].lower()

    response_2 = client.post(
        "/chat/message",
        json={
            "message": "Mañana",
            "user_id": "123"
        }
    )

    assert response_2.status_code == 200

    assert "hora" in response_2.json()["reply"].lower()