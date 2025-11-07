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

### 💡 TRUCCO: Dal testo ai simboli
- "Un professore insegna **molti** corsi" → `PROFESSORE ||--}o CORSO`
- "Uno studente frequenta **molti** corsi" → `STUDENTE }o--}o CORSO`
- "Un cliente fa **molti** ordini" → `CLIENTE ||--}o ORDINE`

---

## 🔹 PARTE 2: DA DIAGRAMMA ER A CREATE TABLE

### ⚠️ REGOLA ORO:
**Relazione 1:N** → La FK va nella tabella **"N"** (quella dei molti)
**Relazione N:N** → Crea **tabella intermedia** con 2 FK che diventano PK composta

### Esempio 1:N
```
"Ogni studente può sostenere molti esami"
STUDENTE ||--}o ESAME
```
➡️ FK va in **ESAME**

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

### Esempio N:N
```
"Uno studente frequenta molti corsi, un corso ha molti studenti"
STUDENTE }o--}o CORSO
```
➡️ Tabella intermedia con 2 FK

```sql
CREATE TABLE Studente (
    Matricola INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL
);

CREATE TABLE Corso (
    ID_Corso INTEGER PRIMARY KEY,
    Nome_Corso TEXT NOT NULL
);

-- ⬅️ Tabella intermedia
CREATE TABLE Iscrizione (
    Matricola INTEGER,
    ID_Corso INTEGER,
    Voto INTEGER,
    PRIMARY KEY (Matricola, ID_Corso),  -- PK composta
    FOREIGN KEY (Matricola) REFERENCES Studente(Matricola),
    FOREIGN KEY (ID_Corso) REFERENCES Corso(ID_Corso)
);
```

---

## 🔹 PARTE 3: FUNZIONI AGGREGATE

### Le 5 funzioni principali:

| Funzione | Cosa fa | Esempio |
|----------|---------|---------|
| `COUNT(*)` o `COUNT(colonna)` | Conta le righe | `COUNT(*)` conta tutte le righe |
| `AVG(colonna)` | Calcola la media | `AVG(Voto)` media dei voti |
| `SUM(colonna)` | Somma i valori | `SUM(Prezzo)` totale prezzi |
| `MAX(colonna)` | Trova il massimo | `MAX(Voto)` voto più alto |
| `MIN(colonna)` | Trova il minimo | `MIN(Voto)` voto più basso |

### Esempi pratici:

```sql
-- Conta tutti gli studenti
SELECT COUNT(*) AS Totale_Studenti FROM Studenti;

-- Voto medio di tutti gli esami
SELECT AVG(Voto) AS Media_Voti FROM Esami;

-- Voto massimo e minimo
SELECT MAX(Voto) AS Voto_Max, MIN(Voto) AS Voto_Min FROM Esami;

-- Somma totale dei prezzi
SELECT SUM(Prezzo) AS Totale FROM Album;
```

### ⚠️ IMPORTANTE: Con GROUP BY

Quando usi **GROUP BY**, le funzioni aggregate calcolano **per ogni gruppo**:

```sql
-- Media voti PER OGNI studente
SELECT Matricola, AVG(Voto) AS Media
FROM Esami
GROUP BY Matricola;
```

**Risultato:**
```
Matricola | Media
101       | 28.3
102       | 27.0
103       | 29.5
```

💡 **Regola:** Se nel testo leggi "PER OGNI" → usa `GROUP BY` + funzione aggregata

---

## 🔹 PARTE 4: LE 3 QUERY TIPO VERIFICA

### 📌 QUERY TIPO 1: SELECT con JOIN e filtri

**Testo:** "Mostra gli album di Vasco Rossi ordinati per prezzo"

```sql
SELECT A.Titolo, A.Prezzo
FROM Album A
JOIN Artista R ON A.ID_Artista = R.ID_Artista
WHERE R.Nome = 'Vasco' AND R.Cognome = 'Rossi'
ORDER BY A.Prezzo ASC;
```

**Quando usarla:** "Mostra...", "Elenca...", "Filtra per..."

---

### 📌 QUERY TIPO 2: JOIN con 2-3 tabelle

**Testo:** "Mostra studenti con i loro corsi e il professore che li insegna"

```sql
SELECT S.Nome AS Studente, C.Nome_Corso, P.Cognome AS Professore
FROM Studente S
JOIN Iscrizione I ON S.Matricola = I.Matricola
JOIN Corso C ON I.ID_Corso = C.ID_Corso
JOIN Professore P ON C.ID_Professore = P.ID_Professore;
```

**Spiegazione passo-passo:**
1. Parto da `Studente` (tabella principale)
2. Mi collego a `Iscrizione` (tabella intermedia N:N)
3. Da `Iscrizione` vado a `Corso`
4. Da `Corso` vado a `Professore`
5. Ogni JOIN ha la sua condizione `ON` con FK = PK

**Quando usarla:** Quando i dati sono sparsi in 3+ tabelle collegate

---

### 📌 QUERY TIPO 3: GROUP BY con funzioni aggregate

**Testo:** "Conta il numero di album per ogni artista e calcola il prezzo medio"

```sql
SELECT R.Nome, R.Cognome, 
       COUNT(A.ID_Album) AS Num_Album,
       AVG(A.Prezzo) AS Prezzo_Medio
FROM Artista R
JOIN Album A ON R.ID_Artista = A.ID_Artista
GROUP BY R.ID_Artista;
```

**Spiegazione:**
1. Collego Artista e Album con JOIN
2. `GROUP BY R.ID_Artista` → raggruppa per artista
3. `COUNT(A.ID_Album)` → conta gli album di OGNI artista
4. `AVG(A.Prezzo)` → calcola prezzo medio di OGNI artista

**Risultato:**
```
Nome  | Cognome  | Num_Album | Prezzo_Medio
Vasco | Rossi    | 4         | 13.63
Lucio | Battisti | 3         | 13.67
```

**Quando usarla:** "PER OGNI...", "conta...", "media di..."

---

## 🔹 PARTE 5: QUERY PIÙ DIFFICILI

Query 1: Mostrare il numero totale di album pubblicati da ogni artista

(JOIN + GROUP BY + COUNT)

SELECT R.nome, R.cognome, COUNT(A.id) AS Numero_Album
FROM Artista R
JOIN Album A ON R.id = A.artista_id
GROUP BY R.id;


💡 Indica quanti album ha prodotto ciascun artista.

Query 2: Trovare gli album che hanno venduto più di 10 copie

(GROUP BY + HAVING)

SELECT A.titolo, SUM(V.quantità) AS Copie_Vendute
FROM Album A
JOIN Vendita V ON A.id = V.album_id
GROUP BY A.titolo
HAVING SUM(V.quantità) > 10;


💡 Mostra solo gli album che hanno venduto oltre 10 copie in totale.

Query 3: Elencare tutti gli album venduti in un negozio specifico

(JOIN + WHERE)

SELECT A.titolo, A.prezzo, N.nome AS Negozio
FROM Album A
JOIN Vendita V ON A.id = V.album_id
JOIN Negozio N ON V.negozio_id = N.id
WHERE N.nome = 'Music Planet';


💡 Visualizza gli album acquistati nel negozio “Music Planet”, con titolo e prezzo.

Query 4: Calcolare il totale incassato da ciascun artista

(JOIN + GROUP BY + SUM)

SELECT R.nome, R.cognome, SUM(A.prezzo * V.quantità) AS Totale_Incasso
FROM Artista R
JOIN Album A ON R.id = A.artista_id
JOIN Vendita V ON A.id = V.album_id
GROUP BY R.id;


💡 Mostra quanto ha guadagnato ogni artista dalle vendite complessive.

Query 5: Prezzo medio di tutti gli album in catalogo

(Funzione aggregata semplice)

SELECT AVG(prezzo) AS Prezzo_Medio
FROM Album;


💡 Calcola il prezzo medio di tutti gli album disponibili.

Query 6: Media delle copie vendute per ogni negozio

(JOIN + GROUP BY + AVG)

SELECT N.nome AS Negozio, AVG(V.quantità) AS Media_Copie
FROM Negozio N
JOIN Vendita V ON N.id = V.negozio_id
GROUP BY N.nome;


💡 Mostra la quantità media di copie vendute da ciascun negozio musicale.

Query 7: Tutti gli album, anche quelli senza vendite

(LEFT JOIN + GROUP BY)

SELECT A.titolo, SUM(V.quantità) AS Copie_Vendute
FROM Album A
LEFT JOIN Vendita V ON A.id = V.album_id
GROUP BY A.titolo;


💡 Visualizza tutti gli album, anche quelli mai venduti (quantità = NULL).

Query 8: Quantità totale venduta per ogni album

(JOIN + GROUP BY + SUM)

SELECT A.titolo, SUM(V.quantità) AS Copie_Totali
FROM Album A
JOIN Vendita V ON A.id = V.album_id
GROUP BY A.titolo;


💡 Somma le copie vendute per ogni album nel sistema.

## 🔹 PARTE 6: SCHEMA DECISIONALE RAPIDO

| Parola chiave nel testo | Comando SQL | Note |
|--------------------------|-------------|------|
| "Elenca tutti..." | `SELECT * FROM Tabella` | |
| "Filtra per...", "Solo..." | `WHERE` | |
| "Ordina per..." | `ORDER BY colonna ASC/DESC` | |
| "**PER OGNI**..." | `GROUP BY` | Quasi sempre! |
| "Conta...", "Numero di..." | `COUNT() + GROUP BY` | |
| "Media di..." | `AVG() + GROUP BY` | |
| "Totale di..." | `SUM() + GROUP BY` | |
| "Almeno / più di..." | `HAVING` | Dopo GROUP BY |
| Dati in 2+ tabelle | `JOIN` | |

---

## 🔹 PARTE 8: MODELLI COMPLETI CON ESEMPI

### 📚 MODELLO 1: STUDENTI-ESAMI (base)

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

**INSERT:**
```sql
INSERT OR IGNORE INTO Studenti (Matricola, Nome, Cognome) VALUES
    (101, 'Mario', 'Rossi'),
    (102, 'Lucia', 'Bianchi');

INSERT INTO Esami (Matricola, Corso, Voto) VALUES
    (101, 'Matematica', 28),
    (101, 'Informatica', 30),
    (101, 'Fisica', 27),
    (102, 'Matematica', 28),
    (102, 'Informatica', 30),
    (102, 'Fisica', 27);
```

**Le 3 query tipo verifica:**

```sql
-- 1. Tutti gli studenti
SELECT Matricola, Nome, Cognome FROM Studenti;

-- 2. Corsi e voti di matricola 101
SELECT Corso, Voto FROM Esami WHERE Matricola = 101;

-- 3. Numero esami per studente
SELECT S.Nome, S.Cognome, COUNT(E.Id) AS Num_Esami
FROM Studenti S
JOIN Esami E ON S.Matricola = E.Matricola
GROUP BY S.Matricola;
```

---

### 🎵 MODELLO 2: NEGOZIO MUSICA (più complesso)

**Diagramma ER:**
```
ARTISTI ||--}o ALBUMVIRTUALE : "pubblica"
NEGOZI ||--}o DIPENDENTI : "impiega"
NEGOZI ||--}o SCONTRINO : "genera"
SCONTRINO ||--}o RIGHESCONTRINO : "contiene"
ALBUMVIRTUALE ||--}o RIGHESCONTRINO : "venduto_in"
```

**CREATE TABLE:**
```sql
CREATE TABLE Artisti (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cognome TEXT NOT NULL
);

CREATE TABLE AlbumVirtuale (
    codice INTEGER PRIMARY KEY,
    titolo TEXT NOT NULL,
    prezzo REAL NOT NULL,
    artista_id INTEGER,
    FOREIGN KEY (artista_id) REFERENCES Artisti(id)
);

CREATE TABLE Negozi (
    codice INTEGER PRIMARY KEY,
    indirizzo TEXT NOT NULL,
    citta TEXT NOT NULL
);

CREATE TABLE Scontrino (
    id INTEGER PRIMARY KEY,
    data DATE NOT NULL,
    negozio_id INTEGER,
    importo_totale REAL NOT NULL,
    FOREIGN KEY (negozio_id) REFERENCES Negozi(codice)
);

CREATE TABLE RigheScontrino (
    id INTEGER PRIMARY KEY,
    scontrino_id INTEGER,
    album_id INTEGER,
    quantita INTEGER NOT NULL,
    FOREIGN KEY (scontrino_id) REFERENCES Scontrino(id),
    FOREIGN KEY (album_id) REFERENCES AlbumVirtuale(codice)
);
```

**Query esempio (come quelle del prof):**

```sql
-- 1. Album di Vasco Rossi ordinati per prezzo
SELECT A.titolo, A.prezzo, R.nome, R.cognome
FROM AlbumVirtuale A
JOIN Artisti R ON R.id = A.artista_id 
WHERE R.nome = 'Vasco' AND R.cognome = 'Rossi'
ORDER BY A.prezzo ASC;

-- 2. Tutti gli album con nome artista
SELECT A.titolo, R.nome, R.cognome
FROM AlbumVirtuale A
JOIN Artisti R ON R.id = A.artista_id;

-- 3. Numero album per artista e prezzo medio
SELECT R.nome, R.cognome, 
       COUNT(*) AS num_album, 
       AVG(A.prezzo) AS prezzo_medio
FROM AlbumVirtuale A
JOIN Artisti R ON R.id = A.artista_id
GROUP BY R.nome, R.cognome;

-- 4. Totale vendite per artista (con 2 JOIN)
SELECT A.artista_id, COUNT(*) AS num_vendite
FROM AlbumVirtuale A
JOIN RigheScontrino RS ON A.codice = RS.album_id
GROUP BY A.artista_id;

-- 5. Album con 'a' nel titolo (LIKE)
SELECT * FROM AlbumVirtuale
WHERE titolo LIKE '%a%';
```

💡 **Nota:** Questo modello ha più tabelle collegate, utile per query con 2-3 JOIN

---

## ✅ CHECKLIST FINALE

### Diagramma ER:
- [ ] Entità con attributi
- [ ] PK sottolineata
- [ ] Relazioni con verbi
- [ ] Cardinalità (`||--}o`)

### CREATE TABLE:
- [ ] PRIMARY KEY in ogni tabella
- [ ] FOREIGN KEY nel lato "N" per 1:N
- [ ] Tabella intermedia per N:N con PK composta
- [ ] NOT NULL dove necessario

### Query:
- [ ] Alias usati (S, E, C, P)
- [ ] JOIN con ON corretto (FK = PK)
- [ ] WHERE per filtrare righe
- [ ] GROUP BY quando c'è "per ogni"
- [ ] HAVING per filtrare gruppi
- [ ] ORDER BY se richiesto

---

## 🎯 ORDINE CLAUSOLE SQL (DA RICORDARE!)

```sql
SELECT colonne
FROM tabella
JOIN altra_tabella ON condizione
WHERE filtro_righe
GROUP BY colonna
HAVING filtro_gruppi
ORDER BY colonna
LIMIT numero
```

⚠️ **Non puoi cambiare l'ordine!** WHERE va prima di GROUP BY, HAVING dopo, ecc.

---

**🍀 BUONA FORTUNA!**
