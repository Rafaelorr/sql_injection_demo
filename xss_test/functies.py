import sqlite3

def read_comments_from_db(db_path: str) -> list[str]:
    comments = []
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT comment FROM comments")
    rows = cursor.fetchall()
    comments = [row[0] for row in rows]
    cursor.close()
    conn.close()
    return comments

def add_comments_to_db(db_path: str, comments: list[str]) -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for comment in comments:
        cursor.execute("INSERT INTO comments (comment) VALUES (?)", (comment,))
    conn.commit()
    cursor.close()
    conn.close()