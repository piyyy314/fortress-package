# fortress-package

A lightweight Python security monitoring package designed to detect, alert on, and tarpitch suspicious system activity in real time.

## Features

- **Process Sentinel** — Monitors running processes for anomalous behaviour
- **Tarpit** — Slows down and traps malicious actors
- **Alerts** — Real-time alerting system for security events
- **Logging** — Structured event logging via `fortress.log`

## Requirements

- Python 3.8+

## Installation

```bash
git clone https://github.com/piyyy314/fortress-package.git
cd fortress-package
pip install -r requirements.txt
```

## Usage

```bash
python fortress_main.py
```

## Modules

| Module | Description |
|--------|-------------|
| `fortress_main.py` | Entry point — orchestrates all security modules |
| `process_sentinel.py` | Process monitoring and anomaly detection |
| `tarpit.py` | Connection tarpitting to slow attackers |
| `alerts.py` | Alert dispatch system |

## License

MIT — see [LICENSE](LICENSE) for details.
