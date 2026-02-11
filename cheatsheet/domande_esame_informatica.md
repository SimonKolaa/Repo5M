**Python, tipizzazione e Type Hinting**

- Python è un linguaggio a "tipizzazione dinamica": cosa significa questo concetto rispetto a linguaggi a tipizzazione statica?
- Cosa sono i "Type Hints" e qual è il loro scopo principale, dato che l'interprete Python non li rende obbligatori per l'esecuzione del codice?

**.gitignore e Ambiente Virtuale**
- A cosa serve l'ambiente virtuale (`venv`) in Python?
- Perché generiamo il file `requirements.txt` per il deployment?
- Qual è lo scopo del file `.gitignore` e quali file critici non dovrebbero mai finire su GitHub?

**Modello ER e Database**
- Quali sono i componenti fondamentali di un diagramma ER?
- Spiega i tipi di cardinalità (1:1, 1:N, N:N) e fornisci un esempio per ciascuno.
- Come si traduce una relazione "Molti a Molti" dal modello ER al codice SQL (Tabella di Raccordo)?
- In cosa consiste la Normalizzazione e quali problemi risolve (anomalie)?
- Qual è la differenza tra Prima, Seconda e Terza Forma Normale?
- Definizione e ruolo della Chiave Primaria e della Chiave Esterna.

**SQL e Interazione con Python**
- Qual è la differenza tra DDL (`CREATE`, `DROP`) e DML (`INSERT`, `SELECT`)?
- A cosa servono le clausole `GROUP BY` e `HAVING`?
- Spiega la differenza tra `JOIN` e `LEFT JOIN`.
- Cos'è la SQL Injection?
- A cosa servono i file `.sqlite` e la cartella `instance` in Flask?

**Architettura Web e Flask**
- A cosa serve il file `__init__.py` all'interno della cartella `app`?
- Cosa sono i **Blueprint** e qual è il loro vantaggio rispetto a un file unico?
- Cos'è il **Repository Pattern** e perché separiamo le query SQL dalle route di Flask?
- Come funziona il motore di template **Jinja2** e il concetto di ereditarietà (`{% extends %}`)?

**HTTP, API e Sicurezza**
- Descrivi il ciclo Request/Response e il ruolo dello Status Code.
- Qual è la differenza tra i metodi HTTP `GET` e `POST`?
- Cosa significa che il protocollo HTTP è "Stateless" e come le **Sessioni** risolvono questo problema?
- Perché è necessario fare l'hashing delle password (`generate_password_hash`) prima di salvarle nel DB?
- Cos'è un server WSGI (es. Gunicorn) e perché è necessario per il deployment (invece di `flask run`)?
- A cosa servono le Variabili d'Ambiente (`.env`) e perché non bisogna committare la `SECRET_KEY`?

**DB e DBMS**
- Qual è la differenza sostanziale tra un Database (i dati) e un DBMS (il software)?
- Quali sono le funzioni principali di un DBMS (es. controllo concorrenza, gestione transazioni)?

**Relazionale vs NoSQL**
- Come sono organizzati i dati in un database relazionale rispetto a uno NoSQL?
- In quali contesti si preferisce un database NoSQL rispetto a uno relazionale?

**ACID**
- Cosa significa l'acronimo ACID nel contesto delle transazioni?
- Spiega brevemente le proprietà di Atomicità e Durabilità.

**Analisi dei Requisiti**
- Qual è l'obiettivo principale dell'analisi dei requisiti nella progettazione "Design-First"?

**Vincoli di Integrità**
- Cosa sono i vincoli di integrità e perché garantiscono la qualità dei dati?
- Oltre alla Chiave Primaria ed Esterna, a cosa servono i vincoli `UNIQUE`, `NOT NULL` e `CHECK`?

**Sicurezza (Autenticazione, Autorizzazione, Audit)**
- Qual è la differenza tecnica tra Autenticazione (chi sei) e Autorizzazione (cosa puoi fare)?
- In cosa consiste l'Audit di un database e perché è utile per la sicurezza?

**API e REST**
- Cos'è un'API e come funziona l'analogia del "Ristorante" (Cliente, Cameriere, Cucina)?
- Quali sono i principi fondamentali dello stile architetturale REST (es. Stateless, Risorse)?

**Endpoint**
- Cos'è un Endpoint e da quali due elementi è composto?
- Fai un esempio di due endpoint diversi che usano lo stesso URL ma metodi HTTP differenti.

**Deployment**
- Qual è la differenza tra l'ambiente di Sviluppo e quello di Produzione?
- Perché in produzione è necessario usare un server WSGI come Gunicorn?
- Perché i dati su piattaforme gratuite come Render (con SQLite) sono considerati "effimeri"?# Domande Esame Orale Maturità - Informatica

## Risposte Brevi (max 2 righe ciascuna)

### Python, tipizzazione e Type Hinting

**Q: Python è un linguaggio a "tipizzazione dinamica": cosa significa questo concetto rispetto a linguaggi a tipizzazione statica?**

La tipizzazione dinamica significa che il tipo delle variabili viene determinato a runtime durante l'esecuzione, mentre nei linguaggi statici viene verificato in fase di compilazione prima dell'esecuzione.

**Q: Cosa sono i "Type Hints" e qual è il loro scopo principale?**

I Type Hints sono annotazioni opzionali che documentano i tipi attesi e permettono a strumenti esterni (IDE, linter) di effettuare controlli statici, migliorando la leggibilità e la manutenibilità del codice.

### .gitignore e Ambiente Virtuale

**Q: A cosa serve l'ambiente virtuale `venv` in Python?**

L'ambiente virtuale `venv` isola le dipendenze del progetto, evitando conflitti tra librerie di progetti diversi e garantendo versioni specifiche per ogni applicazione.

**Q: Perché generiamo il file `requirements.txt` per il deployment?**

Il file `requirements.txt` elenca tutte le dipendenze necessarie con le relative versioni, permettendo di ricreare l'ambiente identico su altre macchine o in produzione.

**Q: Qual è lo scopo del file `.gitignore`?**

Il `.gitignore` specifica quali file escludere dal version control; non si devono committare file sensibili come `.env`, chiavi segrete, `venv/`, e file temporanei o generati automaticamente.

### Modello ER e Database

**Q: Quali sono i componenti fondamentali di un diagramma ER?**

I componenti fondamentali sono: entità (oggetti del dominio), attributi (proprietà delle entità), relazioni (associazioni tra entità) e chiavi (identificatori univoci).

**Q: Spiega i tipi di cardinalità (1:1, 1:N, N:N) e fornisci un esempio per ciascuno.**

1:1 (persona-passaporto), 1:N (cliente-ordini), N:N (studenti-corsi): indicano quante istanze di un'entità possono associarsi a un'altra.

**Q: Come si traduce una relazione "Molti a Molti" dal modello ER al codice SQL?**

Una relazione N:N si traduce creando una tabella di raccordo che contiene le chiavi esterne di entrambe le entità, trasformandola in due relazioni 1:N.

**Q: In cosa consiste la Normalizzazione e quali problemi risolve?**

La Normalizzazione organizza i dati per eliminare ridondanze e anomalie (inserimento, aggiornamento, cancellazione), migliorando integrità e efficienza del database.

**Q: Qual è la differenza tra Prima, Seconda e Terza Forma Normale?**

1NF elimina valori multipli negli attributi, 2NF rimuove dipendenze parziali dalla chiave, 3NF elimina dipendenze transitive tra attributi non chiave.

**Q: Definizione e ruolo della Chiave Primaria e della Chiave Esterna.**

La Chiave Primaria identifica univocamente ogni record; la Chiave Esterna crea collegamenti tra tabelle referenziando la chiave primaria di un'altra tabella.

### SQL e Interazione con Python

**Q: Qual è la differenza tra DDL e DML?**

DDL (Data Definition Language) definisce la struttura del database, mentre DML (Data Manipulation Language) gestisce i dati contenuti nelle tabelle esistenti.

**Q: A cosa servono le clausole `GROUP BY` e `HAVING`?**

`GROUP BY` raggruppa righe con valori identici per aggregazioni; `HAVING` filtra i gruppi risultanti (mentre `WHERE` filtra singole righe prima del raggruppamento).

**Q: Spiega la differenza tra `JOIN` e `LEFT JOIN`.**

`JOIN` restituisce solo righe con corrispondenze in entrambe le tabelle; `LEFT JOIN` include tutte le righe della tabella sinistra anche senza corrispondenze a destra.

**Q: Cos'è la SQL Injection?**

La SQL Injection è un attacco che inserisce codice SQL malevolo attraverso input utente non sanitizzato, potenzialmente compromettendo o distruggendo il database.

**Q: A cosa servono i file `.sqlite` e la cartella `instance` in Flask?**

I file `.sqlite` contengono il database fisico; la cartella `instance` in Flask è dove vengono salvati file specifici dell'istanza come database e configurazioni locali.

### Architettura Web e Flask

**Q: A cosa serve il file `__init__.py` all'interno della cartella `app`?**

Il file `__init__.py` trasforma la cartella in un package Python e tipicamente contiene la factory function per creare e configurare l'applicazione Flask.

**Q: Cosa sono i Blueprint e qual è il loro vantaggio?**

I Blueprint sono componenti modulari che raggruppano route correlate, permettendo di organizzare applicazioni grandi in sezioni logiche separate e riutilizzabili.

**Q: Cos'è il Repository Pattern?**

Il Repository Pattern separa la logica di accesso ai dati dal resto dell'applicazione, centralizzando le query SQL e facilitando testing e manutenzione.

**Q: Come funziona il motore di template Jinja2?**

Jinja2 è un template engine che genera HTML dinamico; `{% extends %}` permette l'ereditarietà dei template riutilizzando layout base e sovrascrivendo blocchi specifici.

### HTTP, API e Sicurezza

**Q: Descrivi il ciclo Request/Response e il ruolo dello Status Code.**

Il client invia una Request HTTP al server che elabora e restituisce una Response con uno Status Code (200 successo, 404 non trovato, 500 errore server).

**Q: Qual è la differenza tra i metodi HTTP `GET` e `POST`?**

`GET` recupera dati dal server ed è visibile nell'URL; `POST` invia dati al server nel body della richiesta per creare o modificare risorse.

**Q: Cosa significa che il protocollo HTTP è "Stateless"?**

"Stateless" significa che ogni richiesta è indipendente senza memoria delle precedenti; le Sessioni salvano stato utente lato server identificato da cookie nel browser.

**Q: Perché è necessario fare l'hashing delle password?**

L'hashing trasforma la password in una stringa irreversibile; in caso di data breach gli attaccanti non ottengono password in chiaro ma solo hash inutilizzabili.

**Q: Cos'è un server WSGI e perché è necessario per il deployment?**

Un server WSGI come Gunicorn è un'interfaccia production-ready tra web server e applicazione Python, gestendo concorrenza e performance meglio del server di sviluppo Flask.

**Q: A cosa servono le Variabili d'Ambiente `.env`?**

Le variabili d'ambiente in `.env` separano configurazioni sensibili dal codice; committare `SECRET_KEY` esporrebbe la chiave usata per firmare sessioni e token.

### DB e DBMS

**Q: Qual è la differenza sostanziale tra un Database e un DBMS?**

Il Database è l'insieme organizzato dei dati persistenti; il DBMS (Database Management System) è il software che gestisce, interroga e protegge quei dati.

**Q: Quali sono le funzioni principali di un DBMS?**

Un DBMS gestisce controllo degli accessi concorrenti, garantisce transazioni ACID, ottimizza query, gestisce backup/recovery e mantiene integrità referenziale.

### Relazionale vs NoSQL

**Q: Come sono organizzati i dati in un database relazionale rispetto a uno NoSQL?**

I database relazionali usano tabelle con schema rigido e relazioni; i NoSQL usano strutture flessibili (documenti, chiave-valore, grafi) senza schema fisso predefinito.

**Q: In quali contesti si preferisce un database NoSQL?**

NoSQL è preferibile per dati non strutturati, scalabilità orizzontale massiva, schema evolutivo frequente e quando servono performance elevate su operazioni specifiche.

### ACID

**Q: Cosa significa l'acronimo ACID nel contesto delle transazioni?**

ACID sta per Atomicity, Consistency, Isolation, Durability: proprietà che garantiscono affidabilità delle transazioni nei database relazionali.

**Q: Spiega brevemente le proprietà di Atomicità e Durabilità.**

Atomicità: la transazione è tutto-o-niente, non può completarsi parzialmente; Durabilità: i dati committati sopravvivono anche a crash di sistema.

### Analisi dei Requisiti

**Q: Qual è l'obiettivo principale dell'analisi dei requisiti?**

L'analisi dei requisiti identifica e documenta cosa deve fare il sistema prima di progettarlo, evitando sviluppo di funzionalità sbagliate o incomplete.

### Vincoli di Integrità

**Q: Cosa sono i vincoli di integrità?**

I vincoli di integrità sono regole imposte dal database per garantire validità, coerenza e correttezza dei dati inseriti o modificati.

**Q: A cosa servono i vincoli `UNIQUE`, `NOT NULL` e `CHECK`?**

`UNIQUE` impedisce duplicati, `NOT NULL` richiede un valore obbligatorio, `CHECK` valida condizioni personalizzate sui dati inseriti.

### Sicurezza (Autenticazione, Autorizzazione, Audit)

**Q: Qual è la differenza tecnica tra Autenticazione e Autorizzazione?**

Autenticazione verifica l'identità dell'utente (login con credenziali); Autorizzazione determina quali risorse o azioni quell'utente può accedere o eseguire.

**Q: In cosa consiste l'Audit di un database?**

L'Audit registra cronologicamente tutte le operazioni sul database (chi, cosa, quando) per tracciabilità, conformità normativa e analisi di sicurezza post-incidente.

### API e REST

**Q: Cos'è un'API e come funziona l'analogia del "Ristorante"?**

Un'API è un'interfaccia che permette comunicazione tra applicazioni; nel ristorante il cliente (app) ordina al cameriere (API) che porta richieste alla cucina (server).

**Q: Quali sono i principi fondamentali dello stile architetturale REST?**

REST è uno stile architetturale basato su risorse identificate da URL, operazioni HTTP standard, comunicazione stateless e rappresentazioni dati (tipicamente JSON).

### Endpoint

**Q: Cos'è un Endpoint e da quali due elementi è composto?**

Un Endpoint è l'URL specifico che espone una funzionalità dell'API, composto da percorso (path) e metodo HTTP utilizzato.

**Q: Fai un esempio di due endpoint diversi che usano lo stesso URL.**

Esempio: `GET /api/users` recupera la lista utenti; `POST /api/users` crea un nuovo utente sullo stesso URL.

### Deployment

**Q: Qual è la differenza tra l'ambiente di Sviluppo e quello di Produzione?**

Sviluppo è l'ambiente locale dove si programma e testa; Produzione è l'ambiente pubblico dove l'applicazione serve utenti reali con requisiti di stabilità e performance.

**Q: Perché in produzione è necessario usare un server WSGI come Gunicorn?**

In produzione Gunicorn gestisce richieste multiple concorrentemente con worker processes, mentre il server Flask di sviluppo è single-threaded e non sicuro.

**Q: Perché i dati su piattaforme gratuite come Render sono considerati "effimeri"?**

Su piattaforme gratuite il filesystem viene resettato periodicamente, quindi database SQLite locali perdono dati; servono database persistenti esterni o piani a pagamento.

---

## Discorso Collegato

Lo sviluppo di un'applicazione web moderna richiede competenze integrate che spaziano dalla programmazione alla gestione dei dati, fino al deployment. **Python** rappresenta il punto di partenza ideale grazie alla sua tipizzazione dinamica che offre flessibilità durante lo sviluppo, migliorata dall'utilizzo di Type Hints per aumentare robustezza e manutenibilità del codice.

La gestione del progetto richiede strumenti fondamentali come **venv** per isolare le dipendenze, **requirements.txt** per documentarle, e **.gitignore** per proteggere file sensibili ed escludere componenti non necessari dal version control. Questa organizzazione è cruciale per garantire riproducibilità dell'ambiente sia in sviluppo che in produzione.

Il cuore dell'applicazione risiede nella **progettazione del database**, partendo dall'analisi dei requisiti in approccio Design-First. Il **modello ER** permette di visualizzare entità, relazioni e cardinalità, che vengono poi tradotti in tabelle SQL rispettando i principi di **Normalizzazione** per eliminare anomalie e ridondanze. Chiavi primarie ed esterne garantiscono integrità referenziale, mentre vincoli aggiuntivi (UNIQUE, NOT NULL, CHECK) assicurano qualità dei dati.

La distinzione tra **Database e DBMS** chiarisce che i dati necessitano di un software gestionale che implementi transazioni **ACID** (Atomicità, Consistenza, Isolamento, Durabilità) e controlli di concorrenza. La scelta tra database **relazionali** e **NoSQL** dipende dalla natura dei dati e dai requisiti di scalabilità.

L'interazione con il database avviene tramite **SQL**, distinguendo tra comandi DDL per definire strutture e DML per manipolare dati. Clausole come GROUP BY, HAVING e diversi tipi di JOIN permettono query complesse. La protezione da **SQL Injection** diventa imperativa quando si integra SQL con applicazioni web.

**Flask** fornisce l'architettura per sviluppare l'applicazione web, utilizzando **Blueprint** per modularità e il **Repository Pattern** per separare logica di business da accesso dati. Il template engine **Jinja2** genera viste dinamiche con ereditarietà. La struttura include file critici come `__init__.py` per configurazione e la cartella `instance` per dati specifici dell'istanza.

La comunicazione web si basa sul protocollo **HTTP**, un sistema request/response stateless dove metodi come GET e POST definiscono operazioni diverse. Le **Sessioni** superano la natura stateless mantenendo stato utente. La **sicurezza** richiede particolare attenzione: password vanno hashate prima dello storage, variabili sensibili isolate in `.env`, e implementati sistemi di **Autenticazione** (chi sei) e **Autorizzazione** (cosa puoi fare), completati da **Audit** per tracciabilità.

Le **API REST** espongono funzionalità tramite **Endpoint** (URL + metodo HTTP) seguendo principi di design stateless e orientati alle risorse, facilitando integrazione tra sistemi diversi.

Infine, il **deployment** richiede transizione dall'ambiente di sviluppo a quello di produzione, utilizzando server **WSGI** come Gunicorn per gestire carico e concorrenza. La consapevolezza che filesystem su piattaforme gratuite sia effimero guida verso soluzioni database persistenti appropriate. Questa pipeline completa - da progettazione a deployment - rappresenta il ciclo di vita professionale di un'applicazione web moderna.
