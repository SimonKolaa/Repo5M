from app.db import get_db


def get_video_by_canale(canale_id):
    """Ottiene tutti i video di un canale"""
    db = get_db()
    video = db.execute(
        'SELECT * FROM video WHERE canale_id = ?',
        (canale_id,)
    ).fetchall()
    return video


def create_video(canale_id, titolo, durata, immagine):
    """Inserisce un nuovo video"""
    db = get_db()
    db.execute(
        'INSERT INTO video (canale_id, titolo, durata, immagine) VALUES (?, ?, ?, ?)',
        (canale_id, titolo, durata, immagine)
    )
    db.commit()


# TODO: get_video_by_id se serve
