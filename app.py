import json
from flask import Flask, render_template, request, jsonify, Response, g
from database import get_db, close_db, init_db
from content import TECH, JOURNEY_STEPS, get_topic_by_id
import ollama_client

app = Flask(__name__)
app.teardown_appcontext(close_db)
init_db(app)

# ── Helpers ────────────────────────────────────────────────────────────────

def _topic_names():
    """Flat dict of topic_id → topic name for all topics."""
    result = {}
    for tech_key, tech in TECH.items():
        for topic in tech["topics"]:
            result[topic["id"]] = topic["name"]
    return result

TOPIC_NAMES = _topic_names()
TOTAL_TOPICS = sum(len(tech["topics"]) for tech in TECH.values())

# ── Page Routes ────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", TECH=TECH, total=TOTAL_TOPICS)


@app.route("/journey")
def journey():
    db = get_db()
    rows = db.execute("SELECT step_id FROM journey_progress WHERE completed = 1").fetchall()
    completed_ids = {r["step_id"] for r in rows}
    return render_template(
        "journey.html",
        steps=JOURNEY_STEPS,
        completed_ids=completed_ids,
        topic_names=TOPIC_NAMES,
    )


# ── Progress API ────────────────────────────────────────────────────────────

@app.route("/api/progress", methods=["POST"])
def mark_progress():
    data     = request.json or {}
    topic_id = data.get("topic_id", "").strip()
    tech_key = data.get("tech_key", "").strip()
    if not topic_id:
        return jsonify({"error": "topic_id required"}), 400
    db = get_db()
    db.execute("""
        INSERT INTO progress (topic_id, tech_key, view_count)
        VALUES (?, ?, 1)
        ON CONFLICT(topic_id) DO UPDATE SET
            last_seen  = datetime('now'),
            view_count = view_count + 1
    """, (topic_id, tech_key))
    db.commit()
    row = db.execute("SELECT view_count, first_seen FROM progress WHERE topic_id = ?", (topic_id,)).fetchone()
    return jsonify({"view_count": row["view_count"], "first_seen": row["first_seen"]}), 200


@app.route("/api/progress", methods=["GET"])
def get_progress():
    db   = get_db()
    rows = db.execute("SELECT topic_id, tech_key, view_count, first_seen, last_seen FROM progress").fetchall()
    return jsonify({"progress": [dict(r) for r in rows]})


# ── Bookmarks API ───────────────────────────────────────────────────────────

@app.route("/api/bookmarks", methods=["GET"])
def list_bookmarks():
    db   = get_db()
    rows = db.execute("SELECT topic_id, tech_key, topic_name, created_at FROM bookmarks ORDER BY created_at DESC").fetchall()
    return jsonify({"bookmarks": [dict(r) for r in rows]})


@app.route("/api/bookmarks", methods=["POST"])
def add_bookmark():
    data       = request.json or {}
    topic_id   = data.get("topic_id", "").strip()
    tech_key   = data.get("tech_key", "").strip()
    topic_name = data.get("topic_name", topic_id).strip()
    if not topic_id:
        return jsonify({"error": "topic_id required"}), 400
    db = get_db()
    db.execute("""
        INSERT OR REPLACE INTO bookmarks (topic_id, tech_key, topic_name)
        VALUES (?, ?, ?)
    """, (topic_id, tech_key, topic_name))
    db.commit()
    return jsonify({"bookmarked": True}), 201


@app.route("/api/bookmarks/<topic_id>", methods=["DELETE"])
def remove_bookmark(topic_id):
    db = get_db()
    db.execute("DELETE FROM bookmarks WHERE topic_id = ?", (topic_id,))
    db.commit()
    return jsonify({"removed": True})


# ── Notes API ───────────────────────────────────────────────────────────────

@app.route("/api/notes/<topic_id>", methods=["GET"])
def get_note(topic_id):
    db  = get_db()
    row = db.execute("SELECT content, updated_at FROM notes WHERE topic_id = ?", (topic_id,)).fetchone()
    return jsonify({"note": dict(row) if row else None})


@app.route("/api/notes", methods=["POST"])
def upsert_note():
    data     = request.json or {}
    topic_id = data.get("topic_id", "").strip()
    tech_key = data.get("tech_key", "").strip()
    content  = data.get("content", "").strip()
    if not topic_id:
        return jsonify({"error": "topic_id required"}), 400
    db = get_db()
    if content:
        db.execute("""
            INSERT INTO notes (topic_id, tech_key, content)
            VALUES (?, ?, ?)
            ON CONFLICT(topic_id) DO UPDATE SET
                content    = excluded.content,
                updated_at = datetime('now')
        """, (topic_id, tech_key, content))
    else:
        db.execute("DELETE FROM notes WHERE topic_id = ?", (topic_id,))
    db.commit()
    row = db.execute("SELECT updated_at FROM notes WHERE topic_id = ?", (topic_id,)).fetchone()
    return jsonify({"saved": True, "updated_at": row["updated_at"] if row else None})


@app.route("/api/notes/<topic_id>", methods=["DELETE"])
def delete_note(topic_id):
    db = get_db()
    db.execute("DELETE FROM notes WHERE topic_id = ?", (topic_id,))
    db.commit()
    return jsonify({"deleted": True})


# ── Journey API ─────────────────────────────────────────────────────────────

@app.route("/api/journey", methods=["GET"])
def get_journey():
    db   = get_db()
    rows = db.execute("SELECT step_id, step_order, completed, completed_at, notes FROM journey_progress").fetchall()
    by_id = {r["step_id"]: dict(r) for r in rows}
    result = []
    for step in JOURNEY_STEPS:
        sid = step["step_id"]
        result.append({**step, **(by_id.get(sid, {"completed": 0, "completed_at": None, "notes": None}))})
    return jsonify({"steps": result})


@app.route("/api/journey/<step_id>", methods=["POST"])
def toggle_journey_step(step_id):
    data      = request.json or {}
    completed = 1 if data.get("completed") else 0
    step_note = data.get("notes")
    # find order from content
    order = next((s["order"] for s in JOURNEY_STEPS if s["step_id"] == step_id), 0)
    db = get_db()
    db.execute("""
        INSERT INTO journey_progress (step_id, step_order, completed, completed_at, notes)
        VALUES (?, ?, ?, CASE WHEN ? = 1 THEN datetime('now') ELSE NULL END, ?)
        ON CONFLICT(step_id) DO UPDATE SET
            completed    = excluded.completed,
            completed_at = excluded.completed_at,
            notes        = COALESCE(excluded.notes, journey_progress.notes)
    """, (step_id, order, completed, completed, step_note))
    db.commit()
    row = db.execute("SELECT * FROM journey_progress WHERE step_id = ?", (step_id,)).fetchone()
    return jsonify(dict(row))


# ── Chat API (SSE streaming) ─────────────────────────────────────────────────

@app.route("/api/chat/stream")
def chat_stream():
    message  = request.args.get("message", "").strip()
    topic_id = request.args.get("topic_id", "").strip() or None
    if not message:
        return jsonify({"error": "message required"}), 400

    def generate():
        for chunk in ollama_client.chat_stream(message, topic_id):
            yield f"data: {json.dumps({'token': chunk})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
