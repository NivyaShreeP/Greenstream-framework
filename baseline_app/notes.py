from database import get_connection

def create_note(title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (title, content)
    )
    conn.commit()
    conn.close()
    return {"message": "Note created"}

def get_all_notes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()
    return notes

def update_note(note_id, title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE notes SET title=?, content=? WHERE id=?",
        (title, content, note_id)
    )
    conn.commit()
    conn.close()
    return {"message": "Note updated"}

def delete_note(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
    return {"message": "Note deleted"}
