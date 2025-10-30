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

## 🔹 PARTE 5: QUERY PIÙ DIFFICILI (con 2-3 JOIN)

### 🎓 Sistema Università: STUDENTE - ISCRIZIONE - CORSO - PROFESSORE

### Query 1: Studenti con corsi e professori (3 JOIN)
```sql
SELECT S.Nome, S.Cognome, C.Nome_Corso, P.Cognome AS Prof
FROM Studente S
JOIN Iscrizione I ON S.Matricola = I.Matricola
JOIN Corso C ON I.ID_Corso = C.ID_Corso
JOIN Professore P ON C.ID_Professore = P.ID_Professore;
```
💡 Collego 4 tabelle in sequenza

---

### Query 2: Media voti per corso (2 JOIN + GROUP BY)
```sql
SELECT C.Nome_Corso, AVG(I.Voto) AS Media_Voti
FROM Corso C
JOIN Iscrizione I ON C.ID_Corso = I.ID_Corso
WHERE I.Voto >= 18
GROUP BY C.ID_Corso;
```
💡 WHERE prima di GROUP BY = filtro le righe, poi raggruppo

---

### Query 3: Numero corsi per professore con media crediti (JOIN + GROUP BY)
```sql
SELECT P.Nome, P.Cognome,
       COUNT(C.ID_Corso) AS Num_Corsi,
       AVG(C.Crediti) AS Media_Crediti
FROM Professore P
JOIN Corso C ON P.ID_Professore = C.ID_Professore
GROUP BY P.ID_Professore;
```
💡 Raggruppo per professore, conto i corsi e calcolo media crediti

---

### Query 4: Studenti con almeno 3 esami da 30 (WHERE + GROUP BY + HAVING)
```sql
SELECT S.Nome, S.Cognome, COUNT(*) AS Num_Trenta
FROM Studente S
JOIN Iscrizione I ON S.Matricola = I.Matricola
WHERE I.Voto = 30
GROUP BY S.Matricola
HAVING COUNT(*) >= 3;
```

**Spiegazione:**
1. `WHERE I.Voto = 30` → filtro SOLO i voti da 30
2. `GROUP BY S.Matricola` → raggruppo per studente
3. `HAVING COUNT(*) >= 3` → mostro solo chi ha ALMENO 3 trenta

💡 **DIFFERENZA WHERE vs HAVING:**
- `WHERE` = filtra le RIGHE (prima del raggruppamento)
- `HAVING` = filtra i GRUPPI (dopo il raggruppamento)

---

### Query 5: Top 3 studenti per media voti (LIMIT)
```sql
SELECT S.Nome, S.Cognome, AVG(I.Voto) AS Media
FROM Studente S
JOIN Iscrizione I ON S.Matricola = I.Matricola
GROUP BY S.Matricola
ORDER BY Media DESC
LIMIT 3;
```
💡 `LIMIT 3` prende solo i primi 3 risultati

---

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

## 🔹 PARTE 8: MODELLO COMPLETO STUDENTI-ESAMI

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