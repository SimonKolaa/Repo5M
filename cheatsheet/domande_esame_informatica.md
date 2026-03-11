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

Quando dobbiamo sviluppare un'applicazione web moderna, ci servono competenze che vanno dalla programmazione alla gestione dei dati, fino alla pubblicazione online. Partiamo da **Python**, che è un linguaggio di programmazione con una caratteristica particolare: la tipizzazione dinamica. Cosa vuol dire? Semplicemente che non dobbiamo dichiarare esplicitamente il tipo di una variabile - Python lo capisce da solo mentre il programma gira. Per esempio, se scriviamo `numero = 5`, Python capisce automaticamente che è un intero. Però possiamo aggiungere i **Type Hints**, che sono come dei "suggerimenti" che diciamo noi sul tipo che dovrebbe avere una variabile. Anche se Python non ci obbliga a usarli, strumenti come gli IDE possono leggerli e avvisarci se stiamo facendo qualcosa di sbagliato, rendendo il nostro codice più robusto.

Prima ancora di scrivere codice, dobbiamo organizzare bene il nostro ambiente di lavoro. Qui entra in gioco l'**ambiente virtuale venv**, che è come creare una "bolla" separata per ogni progetto. Immaginate di avere due progetti: uno usa la versione 2.0 di una libreria, l'altro la versione 3.0. Senza venv, questi progetti andrebbero in conflitto! Per documentare quali librerie servono, creiamo un file chiamato **requirements.txt** che elenca tutto, così chiunque altro può ricreare lo stesso ambiente. Infine c'è il **.gitignore**, un file che dice a Git quali cose NON deve salvare nel repository - tipo le password, l'ambiente virtuale stesso, o file temporanei. Tutto questo ci permette di avere lo stesso ambiente sia sul nostro computer che sul server di produzione.

Ora arriviamo al cuore dell'applicazione: il database. Prima di buttarci a scrivere codice, facciamo l'**analisi dei requisiti** - cioè ci chiediamo: "Cosa deve fare esattamente questa applicazione?". È come fare il progetto di una casa prima di costruirla. Questo approccio si chiama Design-First. Per visualizzare come organizzeremo i dati usiamo il **modello ER** (Entità-Relazioni), che è praticamente un disegno. In questo disegno mettiamo le **entità**, che sono gli "oggetti" del nostro dominio - per esempio, in una scuola avremmo Studenti e Corsi. Ogni entità ha degli **attributi**, cioè le sue caratteristiche: uno studente ha nome, cognome, data di nascita. Poi ci sono le **relazioni**, che mostrano come le entità sono collegate tra loro - tipo "uno studente frequenta molti corsi". Ogni relazione ha una **cardinalità** che dice quanti elementi possono essere collegati: 1:1 significa uno a uno (come una persona e il suo passaporto), 1:N significa uno a molti (un cliente può fare molti ordini), e N:N significa molti a molti (tanti studenti frequentano tanti corsi).

Una volta fatto il disegno, dobbiamo trasformarlo in tabelle SQL vere e proprie. Qui applichiamo la **Normalizzazione**, che è un processo per organizzare i dati in modo intelligente ed evitare problemi. Quali problemi? Le **anomalie** - cioè situazioni strane che possono succedere quando inseriamo, modifichiamo o cancelliamo dati. La normalizzazione si fa in passi progressivi. La **Prima Forma Normale** dice: "Non mettere più valori nello stesso campo" - tipo non puoi avere un campo "telefoni" con dentro tre numeri separati da virgole. La **Seconda Forma Normale** elimina le dipendenze parziali - significa che ogni campo deve dipendere dalla chiave primaria completa, non solo da una sua parte. La **Terza Forma Normale** elimina le dipendenze transitive - cioè se un campo A dipende da B, e B dipende da C, allora A non può stare nella stessa tabella di C.

Per far funzionare tutto questo abbiamo bisogno di alcuni meccanismi. La **Chiave Primaria** è un campo (o un insieme di campi) che identifica in modo unico ogni riga della tabella - tipo il numero di matricola per gli studenti. La **Chiave Esterna** invece è un campo che "punta" alla chiave primaria di un'altra tabella, creando il collegamento tra i dati. Poi ci sono altri **vincoli di integrità** che sono come "regole" che il database deve far rispettare: **UNIQUE** dice "questo valore non può ripetersi", **NOT NULL** dice "questo campo deve essere compilato", e **CHECK** ci permette di definire condizioni personalizzate tipo "l'età deve essere maggiore di 0".

Ora facciamo una distinzione importante: cosa è un **Database** e cosa è un **DBMS**? Il Database sono i dati veri e propri - le nostre tabelle con dentro le informazioni. Il DBMS (Database Management System) invece è il software che gestisce questi dati - tipo MySQL, PostgreSQL o SQLite. Il DBMS fa un sacco di cose: controlla che più utenti non modifichino gli stessi dati creando casini, implementa le transazioni **ACID** che garantiscono affidabilità, ottimizza le query per renderle veloci, e gestisce backup. ACID è un acronimo di quattro proprietà: **Atomicità** significa che un'operazione è tutto-o-niente (o va tutta a buon fine o non succede nulla), **Consistenza** significa che i dati rimangono sempre validi, **Isolamento** significa che le operazioni non si disturbano a vicenda, e **Durabilità** significa che una volta salvati, i dati sopravvivono anche se il server si spegne.

Quando dobbiamo scegliere che tipo di database usare, abbiamo due grandi famiglie. I **database relazionali** organizzano tutto in tabelle con righe e colonne, con uno schema ben definito che va rispettato. Sono perfetti quando i nostri dati sono strutturati e abbiamo bisogno di relazioni complesse. I **database NoSQL** invece sono più flessibili - possono salvare documenti JSON, coppie chiave-valore, grafi. Li usiamo quando i dati non hanno una struttura fissa, quando dobbiamo scalare su tantissime macchine, o quando lo schema cambia spesso.

Per parlare con un database relazionale usiamo **SQL**, che sta per Structured Query Language. SQL si divide in due grandi categorie. Il **DDL** (Data Definition Language) serve per definire la struttura - con comandi come CREATE per creare tabelle e DROP per eliminarle. Il **DML** (Data Manipulation Language) serve per lavorare coi dati - con comandi come INSERT per inserire e SELECT per leggere. SQL ci dà anche strumenti potenti per query complesse: **GROUP BY** raggruppa righe che hanno lo stesso valore per calcolare aggregazioni tipo "quanti ordini per ogni cliente", **HAVING** filtra questi gruppi (mentre WHERE filtra le singole righe prima ancora di raggrupparle), e i **JOIN** ci permettono di unire dati da più tabelle. Il **JOIN** normale restituisce solo le righe che hanno corrispondenze in entrambe le tabelle, mentre il **LEFT JOIN** include anche le righe della tabella di sinistra che non hanno corrispondenze.

Un pericolo grosso quando usiamo SQL è la **SQL Injection**, che è un attacco dove qualcuno inserisce codice SQL malevolo attraverso un campo di input. Immaginate un form di login: se non stiamo attenti, un attaccante potrebbe scrivere nel campo username qualcosa tipo `admin' OR '1'='1` e bypassare la password! Per evitarlo dobbiamo usare query parametrizzate, non concatenare mai le stringhe direttamente.

Per costruire l'applicazione web usiamo **Flask**, che è un framework Python leggero e flessibile. Flask ci permette di organizzare il codice in **Blueprint**, che sono come "moduli" dove raggruppiamo route correlate - per esempio tutte le route per gestire gli utenti in un blueprint, quelle per i prodotti in un altro. Dentro il progetto Flask ci sono alcuni file importanti: **__init__.py** trasforma una cartella in un package Python e contiene la "fabbrica" che crea l'applicazione, mentre la cartella **instance** è dove Flask salva cose specifiche di quella installazione - tipo il file **.sqlite** che contiene il nostro database SQLite.

Per tenere il codice ordinato usiamo il **Repository Pattern**, che è un pattern architetturale dove isoliamo tutte le operazioni sul database in funzioni dedicate. Invece di scrivere query SQL sparse per tutto il codice, le mettiamo tutte in un posto solo. Così se domani cambiamo database, dobbiamo modificare solo il repository. Per generare le pagine HTML usiamo **Jinja2**, che è un template engine - cioè un sistema che ci permette di scrivere HTML con dentro pezzi di codice Python. La cosa figa è `{% extends %}` che ci permette di fare ereditarietà: creiamo un template base con header e footer, e poi i template specifici "ereditano" da quello e cambiano solo la parte centrale.

La comunicazione tra browser e server funziona tramite il protocollo **HTTP**. È un sistema request/response: il browser manda una richiesta, il server risponde con i dati e uno **Status Code** - un numero che dice com'è andata. 200 significa "tutto ok", 404 significa "non trovato", 500 significa "errore del server". I **metodi HTTP** definiscono che tipo di operazione vogliamo fare: **GET** serve per leggere dati ed è visibile nell'URL, **POST** serve per inviare dati al server (tipo quando compili un form) e i dati viaggiano nel corpo della richiesta, non nell'URL.

HTTP ha una caratteristica importante: è **stateless**, cioè senza stato. Ogni richiesta è completamente indipendente, il server non si ricorda di te tra una richiesta e l'altra. Ma allora come fa un sito a ricordarsi che hai fatto login? Usa le **Sessioni**: il server salva i tuoi dati (tipo "utente loggato") e ti dà un cookie - un piccolo file - che il browser rimanda a ogni richiesta. Così il server ti riconosce.

La sicurezza è fondamentale. Le password non vanno mai salvate in chiaro! Usiamo l'**hashing**, che è un processo matematico irreversibile: trasforma la password in una stringa incomprensibile. Se rubano il database, gli attaccanti vedono solo questi hash che non possono "decifrare". Le configurazioni sensibili come chiavi di cifratura le mettiamo nelle **variabili d'ambiente**, salvate in un file **.env** che non pubblichiamo mai su GitHub. La **SECRET_KEY** per esempio è quella che Flask usa per firmare le sessioni - se qualcuno la scopre può falsificare sessioni!

Il sistema di sicurezza ha tre pilastri. L'**Autenticazione** risponde alla domanda "chi sei?" - verifichi l'identità con username e password. L'**Autorizzazione** risponde a "cosa puoi fare?" - decidi quali risorse quell'utente può accedere. L'**Audit** registra tutto quello che succede: chi ha fatto cosa e quando. Serve per la sicurezza ma anche per la conformità legale.

Per far comunicare sistemi diversi usiamo le **API** (Application Programming Interface), che sono come "interfacce" che espongono funzionalità. Un'**API REST** è uno stile architetturale con regole precise: le risorse (tipo utenti, prodotti) sono identificate da URL, usiamo i metodi HTTP standard, la comunicazione è stateless, e i dati viaggiano solitamente in JSON. Le funzionalità si espongono tramite **Endpoint**, che sono URL combinati con un metodo HTTP. Per esempio `GET /api/users` recupera gli utenti, `POST /api/users` ne crea uno nuovo - stesso URL, metodo diverso.

L'ultimo passo è il **deployment**, cioè pubblicare l'applicazione online. Abbiamo due ambienti: **sviluppo** è il nostro computer dove programmiamo e testiamo, **produzione** è il server pubblico dove gli utenti veri usano l'app. In produzione non possiamo usare il server di sviluppo di Flask perché gestisce una richiesta alla volta ed è lento. Serve un server **WSGI** come **Gunicorn**, che è un'interfaccia seria che gestisce tante richieste contemporaneamente usando più "worker".

Attenzione però: su molte piattaforme gratuite il filesystem è **effimero** - significa che viene resettato ogni tanto. Se salviamo il database SQLite lì, perdiamo tutti i dati! Dobbiamo usare database esterni persistenti come PostgreSQL, oppure pagare per avere storage permanente. 

In sintesi, abbiamo visto tutto il percorso: partiamo dall'analisi dei requisiti disegnando il modello ER con entità e relazioni, progettiamo il database applicando la normalizzazione per evitare anomalie, implementiamo l'applicazione con Flask usando pattern come Repository e Blueprint, proteggiamo tutto con autenticazione e hashing delle password evitando SQL Injection, esponiamo funzionalità tramite API REST, e infine pubblichiamo su server di produzione con Gunicorn e database persistenti. Questo è il ciclo di vita completo di un'applicazione web professionale
