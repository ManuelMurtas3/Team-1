# Team 1
Membri: Manuel Murtas, Madalina Sfirlog, Eleonora Zarrilli, Daniele Cuomo

# Processo di sviluppo
Ogni membro del gruppo scrive le porzioni di codice ad esso assegnate in un branch personale.

Il team leader si occuperà di unire i vari snippet di codice all'interno del branch principale (main).

Nel caso si presentino problemi dopo l'assegnazione di sotto-obiettivi da svolgere ci si ferma per risolvere le difficoltà assieme.

# Commit
Ogni problema verrà suddiviso in sotto-obiettivi.

Ad ogni commit corrisponde un sotto-obiettivo.

# Commenti
I commenti verrano riportati all'inizio di ogni blocco logico.

# Nomenclatura e standard
Classi: Upper Camel Case (NomeClasse).

Variabili e metodi: snake_case (nome_variabile).

I nomi delle variabili devono essere descrittivi. Evitare abbreviazioni.

Indentazione di default (4 spazi o 1 un tab).

# Roadmap
Versione 1.0: permettere ai giocatori di creare personaggi, combattere contro nemici, guadagnare punti esperienza e livellare.

Versione 2.0: implementare abilità e strumenti.

Future release: implementazione di boss dopo un numero definito di combattimenti con premio speciale, studio di statistiche per il bilanciamento
delle classi dei personaggi, aggiunta di missioni meglio legate alle nuove feature del gioco, scelta di diversi tipi di attacco (es. normale o speciale)
che possono essere utilizzati un numero limitato di volte, possibilità di fuggire con perdita di punti esperienza, possibilità di riposare il proprio personaggio
per un turno al posto di attaccare per riguadagnare salute, nuovo sistema di esperienza legato anche alla salute del personaggio, sistema di riposo post combattimento opzionale, ottimizzazione del sistema di turni

# Struttura programma
## Classe Entità
Definisce tutti gli attributi delle entità di gioco (personaggio e vari nemici)
Ogni entità apparterrà a una classe mostro e memorizzerà i seguenti...

attributi:
- nome
- tipo
- punti-vita
- punti-vita
- punti-esperienza
- punti-esperienza
- livello
- attacco
- difesa
- abilità-attivata

metodi:
- attacca
- difende
- prendi_danno
- sconfitto
- guadagna_xp
- aumenta_livello
- rigenera_salute
- stampa_statistiche (menù statistiche)
- stampa_stato (durante combattimento)
- rigenera_abilità
- attiva_abilità

Sono state previste quattro classi di personaggi:
- Drago (ATK 110 DEF 90 HP 100) con l'abilità di potenziare la sua difesa in proporzione agli HP persi per un massimo del 20%
- Elfo (ATK 90 DEF 100 HP 110) con l'abilità di potenziare il suo attacco in proporzione agli HP persi per un massimo del 20%
- Strega (ATK 100 DEF 110 HP 90) con l'abilità di ridurre di un livello l'avversario
- Samurai (ATK 100 DEF 100 HP 100) con l'abilità di ridurre del 5% la difesa dell'avversario
