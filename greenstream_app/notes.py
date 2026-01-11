from database import get_connection

def create_note(title, content):
    if not title or not content:
        return {"error": "Invalid input"}   # Fail-fast rule

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (title, content)
    )
    conn.commit()
    return {"message": "Note created"}

def get_all_notes():
    conn = get_connection()
    cursor = conn.cursor()

    # Data minimization: only required fields
    cursor.execute("SELECT id, title FROM notes")
    return cursor.fetchall()

def update_note(note_id, title, content):
    if not title or not content:
        return {"error": "Invalid input"}

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE notes SET title=?, content=? WHERE id=?",
        (title, content, note_id)
    )
    conn.commit()
    return {"message": "Note updated"}

def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    return {"message": "Note deleted"}
