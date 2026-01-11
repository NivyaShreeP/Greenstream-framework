from flask import Flask, request, jsonify
from database import init_db
import notes

app = Flask(__name__)
init_db()

@app.route("/notes", methods=["POST"])
def create():
    data = request.json
    result = notes.create_note(data["title"], data["content"])
    return jsonify(result)

@app.route("/notes", methods=["GET"])
def read():
    data = notes.get_all_notes()
    return jsonify(data)

@app.route("/notes/<int:note_id>", methods=["PUT"])
def update(note_id):
    data = request.json
    result = notes.update_note(note_id, data["title"], data["content"])
    return jsonify(result)

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete(note_id):
    result = notes.delete_note(note_id)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
