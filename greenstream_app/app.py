from flask import Flask, request, jsonify
from database import init_db
import notes

app = Flask(__name__)
init_db()

@app.route("/notes", methods=["POST"])
def create():
    data = request.json
    return jsonify(notes.create_note(
        data.get("title"),
        data.get("content")
    ))

@app.route("/notes", methods=["GET"])
def read():
    return jsonify(notes.get_all_notes())

@app.route("/notes/<int:note_id>", methods=["PUT"])
def update(note_id):
    data = request.json
    return jsonify(notes.update_note(
        note_id,
        data.get("title"),
        data.get("content")
    ))

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete(note_id):
    return jsonify(notes.delete_note(note_id))

if __name__ == "__main__":
    app.run(debug=True)
