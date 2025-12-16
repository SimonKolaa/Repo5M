#Esercizio: database studenti
#Crea un database SQLite chiamato "scuola.db".
#Crea due tabelle:
#Studenti: Matricola (INTEGER PRIMARY KEY), Nome (TEXT NOT NULL), Cognome (TEXT NOT NULL).
#Esami: Id (INTEGER PRIMARY KEY AUTOINCREMENT), Matricola (INTEGER NOT NULL), Corso (TEXT NOT NULL), Voto (INTEGER), con FOREIGN KEY su Studenti(Matricola).
#Inserisci i seguenti dati (tutti gli studenti devono avere gli stessi record di esami):
#Studenti:
#Matricola 101, Nome Mario, Cognome Rossi
#Matricola 102, Nome Lucia, Cognome Bianchi
#Esami (da inserire per ogni studente: per Matricola 101 e per Matricola 102):
#Corso "Matematica", Voto 28
#Corso "Informatica", Voto 30
#Corso "Fisica", Voto 27
#Esegui tre query semplici:
#Elenco di tutti gli studenti (Matricola, Nome, Cognome).
#Elenco dei corsi e voti sostenuti da uno studente specifico (usa la matricola 101 come esempio).
#Numero di esami sostenuti per ciascuno studente (GROUP BY Matricola).
#Suggerimento: usa INSERT OR IGNORE per evitare errori su violazioni di vincoli (es. PRIMARY KEY)

import sqlite3

conn = sqlite3.connect('scuola.db')
cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Studenti (
        Matricola INTEGER PRIMARY KEY,
        Nome TEXT NOT NULL,
        Cognome TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Esami (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Matricola INTEGER NOT NULL,
        Corso TEXT NOT NULL,
        Voto INTEGER,
    FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
    )
    """)

    cursor.execute(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        (101, 'Dario', 'Casali')
    )
    cursor.execute(
        "INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)",
        (102, 'Lucia', 'Bianchi')
    )

    cursor.execute (
     "INSERT INTO Esami (id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
     (1, 101, 'Matematica', 28))
    
    cursor.execute (
     "INSERT INTO Esami (id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
     (2, 101, 'Informatica', 30))
    
    cursor.execute (
     "INSERT INTO Esami (id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
     (3, 102, 'Informatica', 30))
    
    cursor.execute (
     "INSERT INTO Esami (id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
     (4, 101, 'Fisica', 27))
    
    cursor.execute (
     "INSERT INTO Esami (id, Matricola, Corso, Voto) VALUES (?, ?, ?, ?)",
     (5, 102, 'Fisica', 27))   
    
    studenti = cursor.execute("SELECT * FROM Studenti").fetchall()
    esami = cursor.execute("SELECT Corso, Voto FROM Esami WHERE Matricola = ?", (101,)).fetchone()
    q = cursor.execute("SELECT Corso, Voto FROM Esami WHERE Matricola = ?", (101,)).fetchone()
    z = cursor.execute("SELECT Matricola, COUNT(*) as NumeroEsami FROM Esami GROUP BY Matricola").fetchall()
    print("Studenti:", studenti)
    print("Esami di Matricola 101:", esami)
    print("Esami di Matricola 101 (variabile q):", q)
    print("Numero di esami per ciascuno studente:", z)


finally:
    conn.commit()
    conn.close()