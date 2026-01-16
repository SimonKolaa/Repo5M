from app.db import get_db


def get_all_canali():
    """Ottiene tutti i canali"""
    db = get_db()
    canali = db.execute(
        'SELECT * FROM canali ORDER BY nome'
    ).fetchall()
    return canali


def get_canale_by_id(canale_id):
    """Ottiene un canale specifico"""
    db = get_db()
    canale = db.execute(
        'SELECT * FROM canali WHERE id = ?',
        (canale_id,)
    ).fetchone()
    return canale


def create_canale(nome, numero_iscritti, categoria):
    """Crea un nuovo canale"""
    db = get_db()
    db.execute(
        'INSERT INTO canali (nome, numero_iscritti, categoria) VALUES (?, ?, ?)',
        (nome, numero_iscritti, categoria)
    )
    db.commit()


# TODO: altre funzioni se necessarie
