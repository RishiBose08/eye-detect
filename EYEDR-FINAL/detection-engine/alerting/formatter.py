import json


def write_alert(alert, file_path):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(json.dumps(alert) + "\n")