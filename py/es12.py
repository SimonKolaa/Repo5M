import requests

# URL base - CONTROLLA LA PORTA nel messaggio del server!
BASE_URL = "http://localhost:3001"

# --- FUNZIONI GET ---

def get_books_by_author(author_id):
    try:
        response = requests.get(f"{BASE_URL}/books?author_id={author_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore: {e}")
        return None

def get_author(author_id):
    try:
        response = requests.get(f"{BASE_URL}/authors/{author_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore: {e}")
        return None

def get_books_by_genre(genre_id):
    try:
        response = requests.get(f"{BASE_URL}/books?genre_id={genre_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore: {e}")
        return None

def get_genre(genre_id):
    try:
        response = requests.get(f"{BASE_URL}/genres/{genre_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore: {e}")
        return None

# --- MAIN ---

def main():
    # 1. CERCA LIBRI DI UN AUTORE
    author_id = 1
    
    # Prendi info autore
    author = get_author(author_id)
    if author is None:
        return
    
    # Prendi libri dell'autore
    books = get_books_by_author(author_id)
    if books is None:
        return
    
    # Stampa libri
    print(f"Libri di {author['name']}:")
    for book in books:
        print(f"  - {book['title']} ({book['pages']} pagine)")
    
    
    # 2. FILTRA PER DISPONIBILITÀ
    libri_disponibili = []
    for book in books:
        if book['available']:
            libri_disponibili.append(book)
    
    # Stampa disponibili
    print("\nLibri disponibili:")
    for book in libri_disponibili:
        print(f"  - {book['title']}")
    
    
    # 3. CONTA PAGINE TOTALI
    pagine_totali = 0
    for book in libri_disponibili:
        pagine_totali += book['pages']
    
    # Stampa totale
    print(f"\nPagine totali disponibili: {pagine_totali}")
    
    
    # 4. LIBRI PER GENERE
    genre_id = 101
    
    # Prendi info genere
    genre = get_genre(genre_id)
    if genre is None:
        return
    
    # Prendi libri del genere
    books_genre = get_books_by_genre(genre_id)
    if books_genre is None:
        return
    
    # Stampa risultato
    print(f"\nGenere: {genre['name']}")
    print(f"Numero di libri: {len(books_genre)}")

if __name__ == "__main__":
    main()