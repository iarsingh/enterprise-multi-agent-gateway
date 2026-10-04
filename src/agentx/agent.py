TOOLS = ["gateway", "supervisor", "rag", "sql", "research", "cloud", "sre"]
WRITES = ("drop tenant", "disable sso",)

def run(goal, payload):
    if not goal or not str(goal).strip():
        raise ValueError("goal is empty")
    low = goal.lower()
    if any(w in low for w in WRITES):
        return {"refused": True, "reason": "destructive action requires a human", "applied": False, "tools": []}
    tenant = payload.get("tenant"); result = {"tenant": tenant, "agent": "sql" if "revenue" in goal.lower() else "sre" if "latency" in goal.lower() else "rag"}
    return {"refused": False, "tools": TOOLS, "route": result, "applied": False, "needs_approval": False}
