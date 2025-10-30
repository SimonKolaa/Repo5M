# 📘 SCHEMA VERIFICA SQL E DIAGRAMMA ER

## 🔹 PARTE 1: SIMBOLI CARDINALITÀ (Mermaid)

### Simboli da ricordare:
```
||    = esattamente 1
|o    = 0 o 1
}|    = 1 o molti (almeno 1)
}o    = 0 o molti
```

### Combinazioni più comuni:
```
||--||   = 1:1 (uno a uno)
||--}o   = 1:N (uno a molti)  ⬅️ LA PIÙ USATA!
}o--}o   = N:N (molti a molti)
```

### 💡 TRUCCO: Leggere la cardinalità dal testo

**Dal testo ai simboli:**
- "Un professore insegna **molti** corsi" → `PROFESSORE ||--}o CORSO`
- "Uno studente può frequentare **molti** corsi" → `STUDENTE }o--}o CORSO`
- "Un cliente fa **molti** ordini" → `CLIENTE ||--}o ORDINE`

---

## 🔹 PARTE 2: DA DIAGRAMMA ER A CREATE TABLE

### ⚠️ REGOLA ORO:
**Relazione 1:N** → La FK va nella tabella **"N"** (quella dei molti)

### Esempio pratico:
```
"Ogni studente può sostenere molti esami"
STUDENTE ||--}o ESAME
```

➡️ La FK va in **ESAME** (è il lato "molti")

```sql
CREATE TABLE Studenti (
    Matricola INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL
);

CREATE TABLE Esami (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Matricola INTEGER NOT NULL,  -- ⬅️ FK qui!
    Corso TEXT NOT NULL,
    Voto INTEGER,
    FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
);
```

### Altro esempio:
```
"Un artista può pubblicare molti album"
ARTISTA ||--}o ALBUM
```

➡️ La FK va in **ALBUM**

```sql
CREATE TABLE Artista (
    ID_Artista INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL
);

CREATE TABLE Album (
    ID_Album INTEGER PRIMARY KEY,
    Titolo TEXT NOT NULL,
    Prezzo FLOAT,
    ID_Artista INTEGER,  -- ⬅️ FK qui!
    FOREIGN KEY (ID_Artista) REFERENCES Artista(ID_Artista)
);
```

### 🎯 DOMANDA VELOCE per decidere dove mettere FK:
**"Chi ha molti di cosa?"**
- Studente ha molti Esami → FK in Esami
- Artista ha molti Album → FK in Album
- Categoria ha molti Prodotti → FK in Prodotti

---

## 🔹 PARTE 3: INSERT DEI DATI

### Sintassi base:
```sql
INSERT INTO Studenti (Matricola, Nome, Cognome) 
VALUES (101, 'Mario', 'Rossi');
```

### Con INSERT OR IGNORE (per evitare errori):
```sql
INSERT OR IGNORE INTO Studenti (Matricola, Nome, Cognome) 
VALUES (101, 'Mario', 'Rossi');
```
💡 Usa "OR IGNORE" se hai paura di inserire dati duplicati

### Inserire più righe insieme:
```sql
INSERT INTO Esami (Matricola, Corso, Voto) VALUES
    (101, 'Matematica', 28),
    (101, 'Informatica', 30),
    (101, 'Fisica', 27);
```

---

## 🔹 PARTE 4: LE 3 QUERY SEMPLICI (tipo verifica)

### 📌 QUERY TIPO 1: Elenco semplice (SELECT base)

**Testo tipico:** "Elenca tutti gli studenti con matricola, nome e cognome"

```sql
SELECT Matricola, Nome, Cognome 
FROM Studenti;
```

**Oppure:** "Elenca tutti gli album con titolo e prezzo"
```sql
SELECT Titolo, Prezzo 
FROM Album;
```

💡 **Quando usarla:** Quando il testo dice "elenca tutti...", "mostra tutti..."

---

### 📌 QUERY TIPO 2: JOIN + WHERE (collegare e filtrare)

**Testo tipico:** "Mostra i corsi e i voti di uno studente specifico (matricola 101)"

```sql
SELECT Corso, Voto
FROM Esami
WHERE Matricola = 101;
```

**Versione con JOIN (se vuoi anche il nome dello studente):**
```sql
SELECT S.Nome, S.Cognome, E.Corso, E.Voto
FROM Studenti S
JOIN Esami E ON S.Matricola = E.Matricola
WHERE S.Matricola = 101;
```

**Altro esempio:** "Mostra gli album di Vasco Rossi con il prezzo"
```sql
SELECT A.Titolo, A.Prezzo
FROM Album A
JOIN Artista R ON A.ID_Artista = R.ID_Artista
WHERE R.Nome = 'Vasco' AND R.Cognome = 'Rossi';
```

💡 **Quando usarla:** Quando vedi "di uno specifico...", "solo quelli con...", "filtra per..."

**Schema mentale JOIN:**
```
FROM Tabella1 T1
JOIN Tabella2 T2 ON T1.colonna_FK = T2.colonna_PK
WHERE condizione
```

---

### 📌 QUERY TIPO 3: GROUP BY (raggruppare e contare)

**Testo tipico:** "Conta il numero di esami per ogni studente"

```sql
SELECT Matricola, COUNT(*) AS Numero_Esami
FROM Esami
GROUP BY Matricola;
```

**Con nome studente (usando JOIN):**
```sql
SELECT S.Nome, S.Cognome, COUNT(E.Id) AS Numero_Esami
FROM Studenti S
JOIN Esami E ON S.Matricola = E.Matricola
GROUP BY S.Matricola;
```

**Altro esempio:** "Conta gli album per ogni artista"
```sql
SELECT R.Nome, R.Cognome, COUNT(A.ID_Album) AS Numero_Album
FROM Artista R
JOIN Album A ON R.ID_Artista = A.ID_Artista
GROUP BY R.ID_Artista;
```

**Esempio con media:** "Calcola la media voti per ogni studente"
```sql
SELECT S.Nome, S.Cognome, AVG(E.Voto) AS Media_Voti
FROM Studenti S
JOIN Esami E ON S.Matricola = E.Matricola
GROUP BY S.Matricola;
```

💡 **Quando usarla:** Quando leggi "PER OGNI...", "conta...", "numero di...", "media di..."

**Funzioni aggregate più usate:**
- `COUNT(*)` = conta le righe
- `AVG(colonna)` = calcola la media
- `SUM(colonna)` = somma
- `MAX(colonna)` = massimo
- `MIN(colonna)` = minimo

---

## 🔹 PARTE 5: SCHEMA DECISIONALE VELOCE

### Come capire quale query serve:

| Parola chiave nel testo | Query da usare | Esempio |
|--------------------------|----------------|---------|
| "Elenca tutti..." | `SELECT * FROM Tabella` | SELECT * FROM Studenti |
| "Solo...", "Filtra..." | `WHERE` | WHERE Matricola = 101 |
| "Di uno specifico..." | `JOIN + WHERE` | JOIN + WHERE Nome = 'Mario' |
| "**PER OGNI**..." | `GROUP BY` | GROUP BY Matricola |
| "Conta...", "Numero di..." | `COUNT() + GROUP BY` | COUNT(*) GROUP BY ... |
| "Media di..." | `AVG() + GROUP BY` | AVG(Voto) GROUP BY ... |
| "Ordina per..." | `ORDER BY` | ORDER BY Prezzo ASC |

---

## 🔹 PARTE 6: ESEMPI COMPLETI PRONTI

### 📚 ESEMPIO 1: STUDENTI-ESAMI (il modello del prof)

**Diagramma ER:**
```
STUDENTI ||--}o ESAMI : "sostiene"
```

**CREATE TABLE:**
```sql
CREATE TABLE Studenti (
    Matricola INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL
);

CREATE TABLE Esami (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Matricola INTEGER NOT NULL,
    Corso TEXT NOT NULL,
    Voto INTEGER,
    FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
);
```

**Le 3 query:**
```sql
-- 1. Tutti gli studenti
SELECT Matricola, Nome, Cognome FROM Studenti;

-- 2. Corsi e voti di matricola 101
SELECT Corso, Voto 
FROM Esami 
WHERE Matricola = 101;

-- 3. Numero esami per studente
SELECT S.Nome, S.Cognome, COUNT(E.Id) AS Num_Esami
FROM Studenti S
JOIN Esami E ON S.Matricola = E.Matricola
GROUP BY S.Matricola;
```

---

### 🎵 ESEMPIO 2: ARTISTI-ALBUM (come quello del prof)

**Diagramma ER:**
```
ARTISTA ||--}o ALBUM : "pubblica"
```

**CREATE TABLE:**
```sql
CREATE TABLE Artista (
    ID_Artista INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL
);

CREATE TABLE Album (
    ID_Album INTEGER PRIMARY KEY,
    Titolo TEXT NOT NULL,
    Prezzo FLOAT,
    ID_Artista INTEGER,
    FOREIGN KEY (ID_Artista) REFERENCES Artista(ID_Artista)
);
```

**Le 3 query:**
```sql
-- 1. Tutti gli artisti
SELECT Nome, Cognome FROM Artista;

-- 2. Album di Vasco Rossi ordinati per prezzo
SELECT A.Titolo, A.Prezzo
FROM Album A
JOIN Artista R ON A.ID_Artista = R.ID_Artista
WHERE R.Nome = 'Vasco' AND R.Cognome = 'Rossi'
ORDER BY A.Prezzo ASC;

-- 3. Numero album e prezzo medio per artista
SELECT R.Nome, R.Cognome, 
       COUNT(A.ID_Album) AS Num_Album,
       AVG(A.Prezzo) AS Prezzo_Medio
FROM Artista R
JOIN Album A ON R.ID_Artista = A.ID_Artista
GROUP BY R.ID_Artista;
```

---

### 🏪 ESEMPIO 3: CATEGORIA-PRODOTTI

**Diagramma ER:**
```
CATEGORIA ||--}o PRODOTTO : "contiene"
```

**CREATE TABLE:**
```sql
CREATE TABLE Categoria (
    ID_Categoria INTEGER PRIMARY KEY,
    Nome_Categoria TEXT NOT NULL
);

CREATE TABLE Prodotto (
    ID_Prodotto INTEGER PRIMARY KEY,
    Nome_Prodotto TEXT NOT NULL,
    Prezzo FLOAT NOT NULL,
    Quantita INTEGER,
    ID_Categoria INTEGER,
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria)
);
```

**Le 3 query:**
```sql
-- 1. Tutte le categorie
SELECT Nome_Categoria FROM Categoria;

-- 2. Prodotti della categoria 'Elettronica' con prezzo > 50
SELECT P.Nome_Prodotto, P.Prezzo
FROM Prodotto P
JOIN Categoria C ON P.ID_Categoria = C.ID_Categoria
WHERE C.Nome_Categoria = 'Elettronica' AND P.Prezzo > 50;

-- 3. Numero prodotti per categoria
SELECT C.Nome_Categoria, COUNT(P.ID_Prodotto) AS Num_Prodotti
FROM Categoria C
JOIN Prodotto P ON C.ID_Categoria = P.ID_Categoria
GROUP BY C.Nome_Categoria;
```

---

### 📖 ESEMPIO 4: AUTORE-LIBRI

**Diagramma ER:**
```
AUTORE ||--}o LIBRO : "scrive"
```

**CREATE TABLE:**
```sql
CREATE TABLE Autore (
    ID_Autore INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL
);

CREATE TABLE Libro (
    ID_Libro INTEGER PRIMARY KEY,
    Titolo TEXT NOT NULL,
    Anno INTEGER,
    Prezzo FLOAT,
    ID_Autore INTEGER,
    FOREIGN KEY (ID_Autore) REFERENCES Autore(ID_Autore)
);
```

**Le 3 query:**
```sql
-- 1. Tutti gli autori
SELECT Nome, Cognome FROM Autore;

-- 2. Libri di Alessandro Manzoni
SELECT L.Titolo, L.Anno, L.Prezzo
FROM Libro L
JOIN Autore A ON L.ID_Autore = A.ID_Autore
WHERE A.Nome = 'Alessandro' AND A.Cognome = 'Manzoni';

-- 3. Numero libri per autore
SELECT A.Nome, A.Cognome, COUNT(L.ID_Libro) AS Num_Libri
FROM Autore A
JOIN Libro L ON A.ID_Autore = L.ID_Autore
GROUP BY A.ID_Autore;
```

---

## 🔹 PARTE 7: ERRORI COMUNI DA EVITARE

### ❌ 1. Dimenticare la condizione ON nel JOIN
```sql
-- SBAGLIATO:
SELECT * FROM Studenti S JOIN Esami E;

-- GIUSTO:
SELECT * FROM Studenti S 
JOIN Esami E ON S.Matricola = E.Matricola;
```

### ❌ 2. Usare GROUP BY senza funzione aggregata
```sql
-- SBAGLIATO:
SELECT Nome FROM Studenti GROUP BY Matricola;

-- GIUSTO:
SELECT Nome, COUNT(*) FROM Studenti 
JOIN Esami ON ... GROUP BY Matricola;
```

### ❌ 3. Dimenticare gli alias quando necessario
```sql
-- SBAGLIATO (se entrambe hanno colonna Nome):
SELECT Nome FROM Studenti JOIN Corsi;

-- GIUSTO:
SELECT S.Nome, C.Nome_Corso 
FROM Studenti S JOIN Corsi C ON ...;
```

### ❌ 4. Mettere la FK nella tabella sbagliata
```
"Un cliente fa molti ordini"
CLIENTE ||--}o ORDINE
```
➡️ FK va in ORDINE (non in Cliente!)

---

## ✅ CHECKLIST FINALE VERIFICA

### Prima di consegnare controlla:

**Diagramma ER:**
- [ ] Entità disegnate (rettangoli)
- [ ] Attributi inseriti (PK sottolineata)
- [ ] Relazioni con verbi
- [ ] Cardinalità corrette (`||--}o`)

**CREATE TABLE:**
- [ ] PRIMARY KEY in ogni tabella
- [ ] FOREIGN KEY nella tabella giusta (lato "N")
- [ ] NOT NULL dove serve
- [ ] Nomi tabelle/colonne corretti

**INSERT:**
- [ ] Valori nell'ordine giusto
- [ ] Testo tra apici singoli `'Mario'`
- [ ] Numeri senza apici `101`

**QUERY:**
- [ ] SELECT con colonne giuste
- [ ] FROM con tabella corretta
- [ ] JOIN se collego tabelle
- [ ] ON con FK = PK
- [ ] WHERE per filtrare
- [ ] GROUP BY se c'è "per ogni"
- [ ] Alias (S, E, A) usati correttamente

---

## 🎯 TRUCCO FINALE: Ordine delle clausole SQL

**Ricorda sempre questo ordine:**
```sql
SELECT colonne
FROM tabella
JOIN altra_tabella ON condizione
WHERE filtro_righe
GROUP BY colonna
ORDER BY colonna
LIMIT numero
```

💡 Non puoi mettere WHERE dopo GROUP BY, o JOIN dopo WHERE!

---

**🍀 IN BOCCA AL LUPO PER DOMANI!**

Stampa questo schema e tienilo vicino. Quando leggi il testo della verifica:
1. Cerchia le entità → Diagramma ER
2. Sottolinea "molti", "uno", "può" → Cardinalità
3. Cerchia "per ogni", "conta", "filtra" → Tipo di query

Vedrai che andrà benissimo! 💪