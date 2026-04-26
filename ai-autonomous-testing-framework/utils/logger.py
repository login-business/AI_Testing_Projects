import json

def log_failure(test_name, error, ai_reason):

    data = {
        "test": test_name,
        "error": error,
        "ai_analysis": ai_reason
    }

    with open("reports/ai_report.json", "a") as f:
        f.write(json.dumps(data) + "\n")