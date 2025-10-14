import sqlite3



def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Autori (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Libri (
        id INTEGER PRIMARY KEY,
        titolo TEXT NOT NULL,
        autore_id INTEGER,
        anno INTEGER,
        genere TEXT,
        FOREIGN KEY (autore_id) REFERENCES Autori(id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Prestiti (
        id INTEGER PRIMARY KEY,
        libro_id INTEGER,
        utente TEXT NOT NULL,
        data_prestito TEXT,
        data_restituzione TEXT,
        FOREIGN KEY (libro_id) REFERENCES Libri(id)
    )
    """)

def insert_data():
    #Autori
    cursor.execute(
        "INSERT OR IGNORE INTO Autori (id, nome, cognome) VALUES (?, ?, ?)",
        (1, 'Federico', 'Di Luca')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Autori (id, nome, cognome) VALUES (?, ?, ?)",
        (2, 'Giampiero', 'Calma')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Autori (id, nome, cognome) VALUES (?, ?, ?)",
        (3, 'Alessandro', 'Cavour')
    )
    #Libri
    cursor.execute(
        "INSERT OR IGNORE INTO Libri (id, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)",
        (1, 'Il mistero del castello', 1, 2020, 'Giallo')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Libri (id, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)",
        (2, 'Viaggio nel tempo', 1, 2018, 'Fantascienza')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Libri (id, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)",
        (3, 'La cucina italiana', 2, 2019, 'Cucina')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Libri (id, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)",
        (4, 'Storia antica', 3, 2021, 'Storia')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Libri (id, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)",
        (5, 'Romanzo moderno', 3, 2022, 'Narrativa')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Libri (id, titolo, autore_id, anno, genere) VALUES (?, ?, ?, ?, ?)",
        (6, 'Il ritorno del castello', 1, 2023, 'Giallo')
    )
    #Prestiti
    cursor.execute(
        "INSERT OR IGNORE INTO Prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?, ?, ?, ?, ?)",
        (1, 1, 'Federico Di Luca', '2023-01-01', '2023-01-15')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?, ?, ?, ?, ?)",
        (2, 2, 'Giampiero Calma', '2023-02-01', None )
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?, ?, ?, ?, ?)",
        (3, 3, 'Alessandro Cavour', '2023-03-01', '2023-03-10')
    )
    cursor.execute(
        "INSERT OR IGNORE INTO Prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?, ?, ?, ?, ?)",
        (4, 4, 'Federico Di Luca', '2023-04-01', None )
    )




conn = sqlite3.connect('libreria.db')
cursor = conn.cursor()


create_tables()
insert_data()

cursor.execute("SELECT * FROM Autori")
autori = cursor.fetchall()
for autore in autori:
    print(autore)

cursor.execute("SELECT * FROM Libri")
libri = cursor.fetchall()
for libro in libri:
    print(libro)


# query_libri_per_autore(autore_id): Restituisce tutti i libri di un autore specifico (usa JOIN).
def query_libri_per_autore(autore_id):
    cursor.execute("""
                   SELECT Libri.titolo, Autori.nome, Autori.cognome
                   FROM Libri
                   JOIN Autori ON Libri.autore_id = Autori.id
                   WHERE Autori.id = ?""", (autore_id,))
    return cursor.fetchall()

#query_prestiti_per_utente(utente): Restituisce i prestiti di un utente (usa JOIN).
def query_prestiti_per_utente(utente):
    cursor.execute("""
                   SELECT Prestiti.libro_id, Libri.titolo, Prestiti.data_prestito, Prestiti.data_restituzione
                   FROM Prestiti
                   JOIN Libri ON Prestiti.libro_id = Libri.id
                   WHERE Prestiti.utente = ?""", (utente,))
    return cursor.fetchall()


#Restituisce il numero di libri per genere (usa GROUP BY).
cursor.execute("""
            SELECT Libri.genere, COUNT(*) as numero_libri
            FROM Libri 
            GROUP BY Libri.genere 
            """)

libri_per_genere = cursor.fetchall()
for libro in libri_per_genere:
    print(f"{libro}")

# # query_autori_con_piu_libri(): Restituisce gli autori ordinati per numero di libri (usa JOIN, GROUP BY, ORDER BY).
def query_autori_con_piu_libri():
 cursor.execute("""
                SELECT A.nome, A.cognome, COUNT(*) as numero_libri
                FROM Libri L
                JOIN Autori A
                ON L.autore_id = A.id
                GROUP BY A.id
                ORDER BY numero_libri DESC
                """)

# #query_prestiti_non_restituiti(): Restituisce i prestiti non ancora restituiti (data_restituzione IS NULL).
def query_prestiti_non_restituiti():
    cursor.execute("""
                    SELECT data_prestito,id as prestiti_non_restituiti
                    FROM PRESTITI
                    WHERE data_restituzione IS NULL
                     """)
    return cursor.fetchall()

#esercizio 6

#Elenco di tutti i libri con titolo, anno e nome dell'autore (usa JOIN).
cursor.execute("""
               SELECT L.titolo, L.anno, A.nome, A.cognome
               FROM Libri L
               JOIN Autori A
               ON L.autore_id = A.id
               """)
elenco_libri = cursor.fetchall()

#Elenco di tutti i prestiti con titolo del libro, utente e data di prestito (usa JOIN).
cursor.execute("""
               SELECT L.titolo, P.utente, P.data_prestito
               FROM Prestiti P
               JOIN Libri L ON P.libro_id = L.id
               """)
elenco_prestiti = cursor.fetchall()

#Libri pubblicati dopo il 2020. 
cursor.execute("""
               SELECT titolo, anno
               FROM Libri
               WHERE anno > 2020
               """)
