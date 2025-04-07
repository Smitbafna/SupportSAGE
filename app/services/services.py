import json
from datetime import datetime

def log_feedback(query, response):
    log_data = {
        "timestamp": str(datetime.utcnow()),
        "query": query,
        "response": response
    }
    with open("feedback_logs.json", "a") as f:
        f.write(json.dumps(log_data) + "\n")
