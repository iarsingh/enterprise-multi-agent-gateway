from agentx.progression import gateway

def test_gateway_rbac():
    denied = gateway("ada", "acme", "cloud.apply", role="analyst")
    ok = gateway("ada", "acme", "why did revenue drop", role="analyst")
    assert denied["allowed"] is False
    assert ok["agent"] == "sql"
    assert ok["applied"] is False

