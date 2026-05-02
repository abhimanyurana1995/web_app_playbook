import os
import sqlite3
from flask import g

DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "playbook.db")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA journal_mode=WAL")
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(app):
    with app.app_context():
        db = get_db()
        db.executescript("""
            CREATE TABLE IF NOT EXISTS progress (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id   TEXT NOT NULL UNIQUE,
                tech_key   TEXT NOT NULL,
                first_seen TEXT NOT NULL DEFAULT (datetime('now')),
                last_seen  TEXT NOT NULL DEFAULT (datetime('now')),
                view_count INTEGER NOT NULL DEFAULT 1
            );

            CREATE TABLE IF NOT EXISTS bookmarks (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id   TEXT NOT NULL UNIQUE,
                tech_key   TEXT NOT NULL,
                topic_name TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS notes (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id   TEXT NOT NULL UNIQUE,
                tech_key   TEXT NOT NULL,
                content    TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS journey_progress (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                step_id      TEXT NOT NULL UNIQUE,
                step_order   INTEGER NOT NULL,
                completed    INTEGER NOT NULL DEFAULT 0,
                completed_at TEXT,
                notes        TEXT
            );
        """)
        db.commit()
