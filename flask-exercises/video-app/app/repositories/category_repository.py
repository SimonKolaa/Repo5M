from app.db import get_db


def create_category(nome: str):
    """Crea una nuova categoria."""
    db = get_db()
    cursor = db.execute(
        "INSERT INTO categoria (nome) VALUES (?)", (nome,)
    )
    db.commit()
    return cursor.lastrowid


def get_all_categories():
    db = get_db()
    categories = db.execute(
        "SELECT id, nome FROM categoria ORDER BY nome"
    ).fetchall()
    return categories
