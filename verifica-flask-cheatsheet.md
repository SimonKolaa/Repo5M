# 📚 CHEATSHEET COMPLETA - Verifica Flask

## 🎯 INDICE
1. [Verifica Tipo 1: Dettaglio + Ricerca + Commenti](#verifica-tipo-1)
2. [Verifica Tipo 2: Profilo + Archivio + Preferiti](#verifica-tipo-2)
3. [Pattern Comuni](#pattern-comuni)
4. [Checklist Universale](#checklist)
5. [Domande del Prof](#domande-prof)

---

## 🎯 VERIFICA TIPO 1: Dettaglio Post + Ricerca + Commenti {#verifica-tipo-1}

### 📋 ESERCIZIO 1: DETTAGLIO POST

#### FILE: `app/repositories/post_repository.py`

```python
def get_post_by_id(post_id):
    """Recupera un singolo post per ID."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE p.id = ?
    """
    post = db.execute(query, (post_id,)).fetchone()
    if post:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        return post_dict
    return post
```

#### FILE: `app/main.py`

```python
from werkzeug.exceptions import abort

@bp.route('/post/<int:id>')
def post_detail(id):
    """Pagina dettaglio post."""
    post = post_repository.get_post_by_id(id)
    
    if post is None:
        abort(404, f"Post id {id} non esiste.")
    
    return render_template('blog/detail.html', post=post)
```

#### FILE: `app/templates/blog/detail.html`

```html
{% extends 'base.html' %}

{% block title %}{{ post['title'] }}{% endblock %}

{% block content %}
    <article>
        <h1>{{ post['title'] }}</h1>
        <small>Scritto da <strong>{{ post['username'] }}</strong> 
               il {{ post['created'].strftime('%Y-%m-%d') }}</small>
        
        <p>{{ post['body'] }}</p>
    </article>
    
    <a href="{{ url_for('main.index') }}">← Torna alla home</a>
{% endblock %}
```

---

### 📋 ESERCIZIO 2: RICERCA POST

#### FILE: `app/repositories/post_repository.py`

```python
def search_posts_by_title(search_term):
    """Cerca post per titolo (case-insensitive)."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE p.title LIKE ?
        ORDER BY p.created DESC
    """
    search_pattern = f"%{search_term}%"
    posts = db.execute(query, (search_pattern,)).fetchall()
    
    result = []
    for post in posts:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        result.append(post_dict)
    return result
```

#### FILE: `app/main.py`

```python
@bp.route('/search', methods=('GET', 'POST'))
def search():
    """Ricerca post per titolo."""
    results = []
    search_term = None
    
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = post_repository.search_posts_by_title(search_term)
    
    return render_template('search_results.html', 
                         results=results,
                         search_term=search_term)
```

#### FILE: `app/templates/search_results.html`

```html
{% extends 'base.html' %}

{% block title %}Ricerca Post{% endblock %}

{% block content %}
    <h1>Ricerca Post</h1>
    
    <form method="post">
        <input type="text" name="search_term" placeholder="Cerca per titolo..." 
               value="{{ search_term or '' }}" required>
        <button type="submit">Cerca</button>
    </form>
    
    <hr>
    
    {% if search_term %}
        <h3>Risultati per "{{ search_term }}":</h3>
        {% if results %}
            <ul>
            {% for post in results %}
                <li>
                    <strong>{{ post['title'] }}</strong> - 
                    di {{ post['username'] }}
                    <a href="{{ url_for('main.post_detail', id=post['id']) }}">[Leggi]</a>
                </li>
            {% endfor %}
            </ul>
        {% else %}
            <p>Nessun risultato trovato.</p>
        {% endif %}
    {% endif %}
{% endblock %}
```

---

### 📋 ESERCIZIO 3: COMMENTI

#### FILE: `app/schema.sql`

```sql
DROP TABLE IF EXISTS comment;

CREATE TABLE comment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  post_id INTEGER NOT NULL,
  author_id INTEGER NOT NULL,
  body TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (post_id) REFERENCES post (id),
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```

#### FILE: `app/repositories/comment_repository.py` (NUOVO)

```python
from app.db import get_db
from datetime import datetime

def get_comments_by_post(post_id):
    """Lista commenti di un post con autore."""
    db = get_db()
    query = """
        SELECT c.id, c.body, c.created, c.author_id, u.username
        FROM comment c
        JOIN user u ON c.author_id = u.id
        WHERE c.post_id = ?
        ORDER BY c.created ASC
    """
    comments = db.execute(query, (post_id,)).fetchall()
    
    result = []
    for comment in comments:
        comment_dict = dict(comment)
        comment_dict['created'] = datetime.fromisoformat(comment_dict['created'])
        result.append(comment_dict)
    return result

def create_comment(post_id, author_id, body):
    """Inserisce nuovo commento."""
    db = get_db()
    db.execute(
        'INSERT INTO comment (post_id, author_id, body) VALUES (?, ?, ?)',
        (post_id, author_id, body)
    )
    db.commit()
```

#### FILE: `app/main.py`

```python
from app.repositories import comment_repository

@bp.route('/post/<int:id>')
def post_detail(id):
    """Pagina dettaglio post con commenti."""
    post = post_repository.get_post_by_id(id)
    
    if post is None:
        abort(404, f"Post id {id} non esiste.")
    
    comments = comment_repository.get_comments_by_post(id)
    
    return render_template('blog/detail.html', 
                         post=post,
                         comments=comments)

@bp.route('/post/<int:id>/comment', methods=('POST',))
def add_comment(id):
    """Aggiunge commento a un post."""
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    body = request.form['body']
    comment_repository.create_comment(id, g.user['id'], body)
    
    return redirect(url_for('main.post_detail', id=id))
```

#### FILE: `app/templates/blog/detail.html` (AGGIORNA)

```html
{% extends 'base.html' %}

{% block title %}{{ post['title'] }}{% endblock %}

{% block content %}
    <article>
        <h1>{{ post['title'] }}</h1>
        <small>Scritto da <strong>{{ post['username'] }}</strong> 
               il {{ post['created'].strftime('%Y-%m-%d') }}</small>
        <p>{{ post['body'] }}</p>
    </article>
    
    <hr>
    
    <h3>Commenti ({{ comments|length }})</h3>
    
    {% if g.user %}
        <form method="post" action="{{ url_for('main.add_comment', id=post['id']) }}">
            <textarea name="body" placeholder="Scrivi un commento..." 
                      rows="3" required></textarea>
            <button type="submit">Invia Commento</button>
        </form>
    {% else %}
        <p><a href="{{ url_for('auth.login') }}">Accedi</a> per commentare</p>
    {% endif %}
    
    <hr>
    
    {% if comments %}
        {% for comment in comments %}
        <div style="border-left: 2px solid #ccc; padding-left: 10px; margin: 10px 0;">
            <small><strong>{{ comment['username'] }}</strong> - 
                   {{ comment['created'].strftime('%Y-%m-%d %H:%M') }}</small>
            <p>{{ comment['body'] }}</p>
        </div>
        {% endfor %}
    {% else %}
        <p>Nessun commento ancora.</p>
    {% endif %}
    
    <a href="{{ url_for('main.index') }}">← Torna alla home</a>
{% endblock %}
```

---

## 🎯 VERIFICA TIPO 2: Profilo + Archivio + Preferiti {#verifica-tipo-2}

### 📋 ESERCIZIO 1: PROFILO UTENTE

#### FILE: `app/repositories/post_repository.py`

```python
def get_posts_by_author(author_id):
    """Recupera tutti i post di un autore specifico."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE p.author_id = ?
        ORDER BY p.created DESC
    """
    posts = db.execute(query, (author_id,)).fetchall()
    
    result = []
    for post in posts:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        result.append(post_dict)
    return result
```

#### FILE: `app/repositories/user_repository.py`

```python
def get_user_by_id(user_id):
    """Cerca un utente per ID."""
    db = get_db()
    user = db.execute(
        "SELECT * FROM user WHERE id = ?", (user_id,)
    ).fetchone()
    return user
```

#### FILE: `app/main.py`

```python
@bp.route('/user/<int:id>')
def user_profile(id):
    """Profilo utente con lista post."""
    user = user_repository.get_user_by_id(id)
    
    if user is None:
        abort(404, f"Utente id {id} non esiste.")
    
    posts = post_repository.get_posts_by_author(id)
    post_count = len(posts)
    
    return render_template('user_profile.html', 
                         user=user, 
                         posts=posts,
                         post_count=post_count)
```

#### FILE: `app/templates/user_profile.html`

```html
{% extends 'base.html' %}

{% block title %}Profilo - {{ user['username'] }}{% endblock %}

{% block content %}
    <h1>Profilo di {{ user['username'] }}</h1>
    <p>Numero totale di post: <strong>{{ post_count }}</strong></p>
    
    <h3>Post scritti:</h3>
    {% if posts %}
        <ul>
        {% for post in posts %}
            <li>
                <strong>{{ post['title'] }}</strong> - 
                {{ post['created'].strftime('%Y-%m-%d') }}
                <a href="{{ url_for('main.post_detail', id=post['id']) }}">[Leggi]</a>
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>Nessun post scritto.</p>
    {% endif %}
{% endblock %}
```

---

### 📋 ESERCIZIO 2: ARCHIVIO PER DATA

#### FILE: `app/repositories/post_repository.py`

```python
def get_posts_by_month(year, month):
    """Filtra post per anno e mese."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM post p
        JOIN user u ON p.author_id = u.id
        WHERE strftime('%Y', p.created) = ? AND strftime('%m', p.created) = ?
        ORDER BY p.created DESC
    """
    month_str = f"{month:02d}"
    posts = db.execute(query, (str(year), month_str)).fetchall()
    
    result = []
    for post in posts:
        post_dict = dict(post)
        post_dict['created'] = datetime.fromisoformat(post_dict['created'])
        result.append(post_dict)
    return result
```

#### FILE: `app/main.py`

```python
@bp.route('/archive', methods=('GET', 'POST'))
def archive():
    """Archivio post per data."""
    posts = []
    year = None
    month = None
    
    if request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        posts = post_repository.get_posts_by_month(int(year), int(month))
    
    return render_template('archive.html', 
                         posts=posts,
                         year=year,
                         month=month)
```

#### FILE: `app/templates/archive.html`

```html
{% extends 'base.html' %}

{% block title %}Archivio Post{% endblock %}

{% block content %}
    <h1>Archivio Post per Data</h1>
    
    <form method="post">
        <label>Anno:
            <input type="number" name="year" min="2020" max="2030" 
                   value="{{ year or 2026 }}" required>
        </label>
        
        <label>Mese:
            <select name="month" required>
                {% for m in range(1, 13) %}
                <option value="{{ m }}" {% if month and month|int == m %}selected{% endif %}>
                    {{ m }}
                </option>
                {% endfor %}
            </select>
        </label>
        
        <button type="submit">Cerca</button>
    </form>
    
    <hr>
    
    {% if year and month %}
        <h3>Risultati per {{ month }}/{{ year }}:</h3>
        {% if posts %}
            <ul>
            {% for post in posts %}
                <li>
                    <strong>{{ post['title'] }}</strong> - 
                    di {{ post['username'] }} - 
                    {{ post['created'].strftime('%Y-%m-%d') }}
                </li>
            {% endfor %}
            </ul>
        {% else %}
            <p>Nessun post trovato per questo periodo.</p>
        {% endif %}
    {% endif %}
{% endblock %}
```

---

### 📋 ESERCIZIO 3: SISTEMA PREFERITI

#### FILE: `app/schema.sql`

```sql
DROP TABLE IF EXISTS bookmark;

CREATE TABLE bookmark (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (post_id) REFERENCES post (id),
  UNIQUE (user_id, post_id)
);
```

#### FILE: `app/repositories/bookmark_repository.py` (NUOVO)

```python
from app.db import get_db
from datetime import datetime

def add_bookmark(user_id, post_id):
    """Aggiunge un preferito."""
    db = get_db()
    try:
        db.execute(
            'INSERT INTO bookmark (user_id, post_id) VALUES (?, ?)',
            (user_id, post_id)
        )
        db.commit()
        return True
    except db.IntegrityError:
        return False

def remove_bookmark(user_id, post_id):
    """Rimuove un preferito."""
    db = get_db()
    db.execute(
        'DELETE FROM bookmark WHERE user_id = ? AND post_id = ?',
        (user_id, post_id)
    )
    db.commit()

def get_user_bookmarks(user_id):
    """Lista post salvati dall'utente."""
    db = get_db()
    query = """
        SELECT p.id, p.title, p.body, p.created, p.author_id, u.username
        FROM bookmark b
        JOIN post p ON b.post_id = p.id
        JOIN user u ON p.author_id = u.id
        WHERE b.user_id = ?
        ORDER BY b.created DESC
    """
    bookmarks = db.execute(query, (user_id,)).fetchall()
    
    result = []
    for bm in bookmarks:
        bm_dict = dict(bm)
        bm_dict['created'] = datetime.fromisoformat(bm_dict['created'])
        result.append(bm_dict)
    return result

def is_bookmarked(user_id, post_id):
    """Controlla se post è già salvato."""
    db = get_db()
    result = db.execute(
        'SELECT id FROM bookmark WHERE user_id = ? AND post_id = ?',
        (user_id, post_id)
    ).fetchone()
    return result is not None
```

#### FILE: `app/main.py`

```python
from app.repositories import bookmark_repository

@bp.route('/post/<int:id>/bookmark', methods=('POST',))
def toggle_bookmark(id):
    """Toggle preferito."""
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    if bookmark_repository.is_bookmarked(g.user['id'], id):
        bookmark_repository.remove_bookmark(g.user['id'], id)
    else:
        bookmark_repository.add_bookmark(g.user['id'], id)
    
    return redirect(url_for('main.index'))

@bp.route('/bookmarks')
def bookmarks():
    """Pagina preferiti."""
    if g.user is None:
        return redirect(url_for('auth.login'))
    
    bookmarks = bookmark_repository.get_user_bookmarks(g.user['id'])
    return render_template('bookmarks.html', bookmarks=bookmarks)

# MODIFICA index per passare is_bookmarked
@bp.route('/')
def index():
    posts = post_repository.get_all_posts()
    return render_template('index.html', 
                         posts=posts,
                         is_bookmarked=bookmark_repository.is_bookmarked)
```

#### FILE: `app/templates/bookmarks.html`

```html
{% extends 'base.html' %}

{% block title %}I Miei Preferiti{% endblock %}

{% block content %}
    <h1>I Miei Preferiti</h1>
    
    {% if bookmarks %}
        <ul>
        {% for bm in bookmarks %}
            <li>
                <strong>{{ bm['title'] }}</strong> - 
                di {{ bm['username'] }}
                <form method="post" action="{{ url_for('main.toggle_bookmark', id=bm['id']) }}" 
                      style="display:inline;">
                    <button type="submit">[Rimuovi]</button>
                </form>
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>Nessun preferito salvato.</p>
    {% endif %}
{% endblock %}
```

#### FILE: `app/templates/index.html` (MODIFICA)

```html
{% for post in posts %}
<article>
    <header>
        <h2>{{ post['title'] }}</h2>
        <small>{{ post['username'] }} - {{ post['created'].strftime('%Y-%m-%d') }}</small>
    </header>
    <p>{{ post['body'] }}</p>
    
    {% if g.user %}
        <form method="post" action="{{ url_for('main.toggle_bookmark', id=post['id']) }}" 
              style="display:inline;">
            {% if is_bookmarked(g.user['id'], post['id']) %}
                <button type="submit">⭐ Salvato</button>
            {% else %}
                <button type="submit">☆ Salva</button>
            {% endif %}
        </form>
    {% endif %}
</article>
{% endfor %}
```

---

## 📝 PATTERN COMUNI {#pattern-comuni}

### A) Mostrare lista filtrata

```python
# Repository
def get_X_by_Y(y_id):
    query = "SELECT ... WHERE y_id = ?"
    return db.execute(query, (y_id,)).fetchall()

# Route
@bp.route('/X/<int:id>')
def show_X(id):
    items = repository.get_X_by_Y(id)
    return render_template('X.html', items=items)
```

### B) Form di ricerca/filtro

```python
@bp.route('/search', methods=('GET', 'POST'))
def search():
    results = []
    if request.method == 'POST':
        term = request.form['term']
        results = repository.search(term)
    return render_template('search.html', results=results)
```

### C) Relazione Many-to-Many

```sql
CREATE TABLE A_B (
  a_id INTEGER,
  b_id INTEGER,
  FOREIGN KEY (a_id) REFERENCES A(id),
  FOREIGN KEY (b_id) REFERENCES B(id),
  UNIQUE (a_id, b_id)
);
```

### D) Statistiche con GROUP BY

```python
def get_stats():
    query = """
        SELECT author_id, COUNT(*) as count
        FROM post
        GROUP BY author_id
        ORDER BY count DESC
    """
    return db.execute(query).fetchall()
```

---

## ✅ CHECKLIST UNIVERSALE {#checklist}

- [ ] Repository Pattern: ZERO query SQL in `main.py`
- [ ] JOIN quando serve info da più tabelle
- [ ] `abort(404)` se risorsa non esiste
- [ ] `if g.user is None` per proteggere route
- [ ] `db.commit()` dopo INSERT/UPDATE/DELETE
- [ ] `{% extends 'base.html' %}` in tutti i template
- [ ] `datetime.fromisoformat()` per conversione date
- [ ] GET per visualizzare, POST per modificare
- [ ] POST → redirect a GET (pattern PRG)
- [ ] `flash()` per messaggi conferma/errore

---

## 💡 DOMANDE DEL PROF {#domande-prof}

**Q: "Spiegami questa query"**
```sql
SELECT p.*, u.username
FROM post p
JOIN user u ON p.author_id = u.id
```
**A:** "Faccio un JOIN tra post e user sulla chiave esterna author_id per prendere anche lo username dell'autore"

**Q: "Perché usi abort(404)?"**
**A:** "Per restituire errore HTTP 404 quando la risorsa non esiste, così l'utente sa che l'ID non è valido"

**Q: "Cos'è fetchone() vs fetchall()?"**
**A:** "fetchone() restituisce UNA riga, fetchall() una LISTA. Uso fetchone() per cercare elemento specifico per ID"

**Q: "Perché converti created?"**
**A:** "SQLite salva timestamp come stringhe. Li converto in datetime per usare metodi come strftime() nei template"

---

## 🧪 SINTASSI RAPIDE

### SQL
```sql
WHERE ... = ?              -- Filtro
WHERE ... LIKE ?           -- Ricerca testo  
ORDER BY ... DESC          -- Ordinamento
GROUP BY ...               -- Aggregazione
LEFT JOIN ... ON ...       -- Join con NULL
strftime('%Y-%m', date)    -- Formato data
```

### Form HTML
```html
<form method="post">
    <input type="text" name="campo" required>
    <textarea name="testo" rows="5"></textarea>
    <select name="scelta">
        <option value="1">Opzione</option>
    </select>
    <button type="submit">Invia</button>
</form>
```

### Jinja Template
```jinja
{% extends 'base.html' %}
{% block title %}...{% endblock %}
{% block content %}
    {% if condition %}...{% endif %}
    {% for item in items %}...{% endfor %}
    {{ variable }}
    {{ url_for('main.index') }}
{% endblock %}
```

---

**Studia questa cheatsheet e sarai pronto per qualsiasi verifica! 🚀**