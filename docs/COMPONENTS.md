# Software Components

HiveCheck estimates the strength of rented honey bee colonies (frames of bees) from hive sensor readings and shows the results on a shared dashboard for Rideau Valley Orchards and its three beekeepers.

## 1. Component Inventory
| Component / Module | Directory / File Path | Primary Responsibility | Key Dependencies |
| :--- | :--- | :--- | :--- |
| Application Entry Point | /app.py | Creates the Flask app, wires the repository into the app config, seeds demo data and starts the web server | Flask, src.data, src.ui |
| Presentation / UI | /src/ui (routes.py, templates/dashboard.html) | Serves the hive dashboard (`/`), the JSON API (`/api/hives`) and the health check (`/health`) | Flask (Blueprint, Jinja2 templates), src.core |
| Core Logic / Service | /src/core/strength.py | Converts weight, temperature and sound readings into an estimated number of frames of bees, checks the 8-frame contract standard and assigns OK / WATCH / ALERT status | Python standard library only |
| Data Access / Storage | /src/data/repository.py | Stores sensor readings, returns the latest reading per hive, and seeds one simulated day of 15-minute readings | SQLite (`sqlite3`) |
| Tests | /tests/test_strength.py | Unit tests for the strength estimate and status bands | `unittest` |
| Container Build | /Dockerfile, /.dockerignore | Packages the application into a Docker image | python:3.12-slim base image |

## 2. External Interfaces & APIs
- Input Interfaces:
  - Sensor readings (hive ID, beekeeper, timestamp, weight in kg, temperature in °C, sound in dB) written through `ReadingRepository.add()`. In the prototype these are simulated by `seed_demo_data()`.
  - Environment variables: `PORT` (default 5000) and `HIVECHECK_DB` (SQLite path, default in-memory).
  - HTTP GET requests to `/`, `/api/hives` and `/health`.
- Output Interfaces:
  - `/` returns an HTML dashboard listing each hive, its beekeeper, last reading time, estimated frames and status.
  - `/api/hives` returns a JSON array of hive summaries (`hive_id`, `beekeeper`, `taken_at`, `frames`, `meets_contract`, `status`).
  - `/health` returns `{"status": "ok"}` for container and uptime checks.
  - SQLite writes to the `readings` table.
