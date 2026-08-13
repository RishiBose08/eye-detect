

import sys
import os

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
from ingestion.event_reader import read_events
from rules.loader import load_rule
from evaluator.engine import evaluate_rule
from alerting.alert import create_alert
from alerting.formatter import write_alert


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TELEMETRY_FILE = os.path.join(
    BASE_DIR,
    "sample",
    "telemetry.ndjson"
)

RULE_FILE = os.path.join(
    BASE_DIR,
    "rules",
    "process",
    "encoded_powershell.yml"
)

ALERT_FILE = os.path.join(
    BASE_DIR,
    "sample",
    "alerts.ndjson"
)


def main():

    print("=" * 60)
    print("EyeDR Detection Engine")
    print("=" * 60)

    # Read telemetry
    events = read_events(TELEMETRY_FILE)

    print(f"\n[+] Events loaded: {len(events)}")

    # Load detection rule
    rule = load_rule(RULE_FILE)

    print(f"[+] Rule loaded: {rule['id']} - {rule['title']}")

    detections = 0

    # Evaluate every event
    for event in events:

        matched = evaluate_rule(event, rule)

        if matched:

            print("\n[!] DETECTION TRIGGERED")

            alert = create_alert(event, rule)

            write_alert(alert, ALERT_FILE)

            detections += 1

            print(f"    Rule     : {rule['id']}")
            print(f"    Title    : {rule['title']}")
            print(f"    Severity : {rule['severity']}")
            print(f"    Host     : {event.get('host')}")
            print(f"    Process  : {event.get('image')}")

        else:

            print(
                f"\n[-] No detection: "
                f"{event.get('image')}"
            )

    print("\n" + "=" * 60)
    print(f"Detection complete. Alerts generated: {detections}")
    print("=" * 60)


if __name__ == "__main__":
    main()