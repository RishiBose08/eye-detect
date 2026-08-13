# eye-detect — Detection Engine

The detection engine component of the **EyeDR** EDR system. It ingests
endpoint telemetry produced by the collection agent, applies detection
logic and correlation, and generates alerts.

## Role in the EDR pipeline

Collection Agent → Telemetry → **Detection Engine (this repo)** → Alerts
