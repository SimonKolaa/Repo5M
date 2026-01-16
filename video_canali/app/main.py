from flask import Blueprint, render_template, request, redirect, url_for

from .repositories import canale_repository, video_repository

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    """Mostra la lista di tutti i canali"""
    canali = canale_repository.get_all_canali()
    return render_template('index.html', canali=canali)


@bp.route('/canale/<int:id>')
def canale_detail(id):
    """Mostra i video di un canale specifico"""
    canale = canale_repository.get_canale_by_id(id)
    video = video_repository.get_video_by_canale(id)
    return render_template('canale.html', canale=canale, video=video)


@bp.route('/canale/create', methods=['GET', 'POST'])
def create_canale():
    """Crea un nuovo canale"""
    if request.method == 'POST':
        nome = request.form['nome']
        numero_iscritti = request.form['numero_iscritti']
        categoria = request.form['categoria']

        # TODO: validazione

        canale_repository.create_canale(nome, numero_iscritti, categoria)
        return redirect(url_for('main.index'))

    return render_template('create_canale.html')


@bp.route('/video/create/<int:canale_id>', methods=['GET', 'POST'])
def create_video(canale_id):
    """Inserisce un video in un canale"""
    if request.method == 'POST':
        titolo = request.form['titolo']
        durata = request.form['durata']
        immagine = request.form.get('immagine', '')

        # TODO: validazione

        video_repository.create_video(canale_id, titolo, durata, immagine)
        return redirect(url_for('main.canale_detail', id=canale_id))

    canale = canale_repository.get_canale_by_id(canale_id)
    return render_template('create_video.html', canale=canale)
