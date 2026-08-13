import json


def read_events(file_path):
    events = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                event = json.loads(line)
                events.append(event)
            except json.JSONDecodeError as e:
                print(f"[ERROR] Invalid JSON at line {line_number}: {e}")

    return events