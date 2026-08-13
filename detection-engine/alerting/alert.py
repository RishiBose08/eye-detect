from datetime import datetime, timezone


def create_alert(event, rule):
    return {
        "alert_id": f"ALERT-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}",
        "rule_id": rule["id"],
        "title": rule["title"],
        "severity": rule["severity"],
        "timestamp": event.get("timestamp"),
        "host": event.get("host"),
        "category": event.get("category"),
        "evidence": {
            "image": event.get("image"),
            "command_line": event.get("command_line"),
            "parent_image": event.get("parent_image"),
            "pid": event.get("pid"),
            "process_guid": event.get("process_guid")
        },
        "mitre": rule.get("mitre", {})
    }