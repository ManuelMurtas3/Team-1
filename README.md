# Team 1
Membri: Manuel Murtas, Madalina Sfirlog, Eleonora Zarrilli, Daniele Cuomo

# Processo di sviluppo
Ogni membro del gruppo scrive le porzioni di codice ad esso assegnate in un branch personale.

Il team leader si occuperà di unire i vari snippet di codice all'interno del branch principale (main).

Nel caso si presentino problemi dopo l'assegnazione di sotto-obiettivi da svolgere ci si ferma per risolvere le difficoltà assieme.

# Commit
Ogni problema verrà suddiviso in sotto-obiettivi.

Ad ogni commit corrisponde un sotto-obiettivo col nome del sotto-obiettivo.

# Commenti
I commenti verrano riportati all'inizio di ogni blocco logico.

# Nomenclatura e standard
Classi: Upper Camel Case (NomeClasse).

Variabili e metodi: snake_case (nome_variabile).

I nomi delle variabili devono essere descrittivi. Evitare abbreviazioni.

Indentazione di default (4 spazi o 1 un tab).

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