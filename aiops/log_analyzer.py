import os
from datetime import datetime

LOG_FILE = "../logs/app/app.log"


def read_logs():
    if not os.path.exists(LOG_FILE):
        print("Log file not found")
        return []

    with open(LOG_FILE, "r") as f:
        return f.readlines()[-50:]


def analyze_logs(logs):
    errors = []
    warnings = []

    for line in logs:
        if "ERROR" in line:
            errors.append(line)
        elif "WARNING" in line:
            warnings.append(line)

    print("\n===== AI LOG ANALYSIS REPORT =====")
    print(f"Timestamp: {datetime.utcnow()}")
    print(f"Total logs analyzed: {len(logs)}")
    print(f"Errors detected: {len(errors)}")
    print(f"Warnings detected: {len(warnings)}")

    if errors:
        print("\n⚠️ Potential Incident Detected:")
        for err in errors[-5:]:
            print(err.strip())
    else:
        print("\n✅ System operating normally")


if __name__ == "__main__":
    logs = read_logs()
    analyze_logs(logs)
