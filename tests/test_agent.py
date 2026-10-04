from fastapi.testclient import TestClient
from agentx.main import app
client = TestClient(app)

def test_run_and_refuse():
    payload = client.post("/agent/run", json={"goal": 'why did revenue fall', "payload": {'tenant': 'north'}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["route"]["agent"] == "sql" and payload["route"]["tenant"] == "north"
    refused = client.post("/agent/run", json={"goal": 'drop tenant data now'}).json()
    assert refused["refused"] is True
