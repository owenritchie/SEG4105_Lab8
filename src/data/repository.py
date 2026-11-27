"""Data access: stores hive sensor readings in SQLite."""
import random
import sqlite3
from datetime import datetime, timedelta

SCHEMA = """
CREATE TABLE IF NOT EXISTS readings (
    hive_id   TEXT NOT NULL,
    beekeeper TEXT NOT NULL,
    taken_at  TEXT NOT NULL,
    weight_kg REAL NOT NULL,
    temp_c    REAL NOT NULL,
    sound_db  REAL NOT NULL
);
"""

BEEKEEPERS = ["Beekeeper A", "Beekeeper B", "Beekeeper C"]


class ReadingRepository:
    def __init__(self, path: str = ":memory:"):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    def add(self, hive_id, beekeeper, taken_at, weight_kg, temp_c, sound_db):
        self.conn.execute(
            "INSERT INTO readings VALUES (?, ?, ?, ?, ?, ?)",
            (hive_id, beekeeper, taken_at, weight_kg, temp_c, sound_db),
        )
        self.conn.commit()

    def latest_per_hive(self):
        return self.conn.execute(
            """SELECT r.* FROM readings r
               JOIN (SELECT hive_id, MAX(taken_at) AS t FROM readings GROUP BY hive_id) m
                 ON r.hive_id = m.hive_id AND r.taken_at = m.t
               ORDER BY r.hive_id"""
        ).fetchall()

    def seed_demo_data(self, hives: int = 12, seed: int = 4105):
        """Simulate one day of 15-minute readings for a set of hives."""
        rng = random.Random(seed)
        start = datetime(2027, 5, 1, 0, 0)
        for n in range(1, hives + 1):
            hive_id = f"H{n:03d}"
            keeper = BEEKEEPERS[(n - 1) % len(BEEKEEPERS)]
            base = rng.uniform(23, 30)
            for step in range(96):
                t = start + timedelta(minutes=15 * step)
                self.add(hive_id, keeper, t.isoformat(),
                         round(base + rng.uniform(-0.3, 0.3), 2),
                         round(rng.uniform(31, 36), 1),
                         round(rng.uniform(35, 55), 1))
