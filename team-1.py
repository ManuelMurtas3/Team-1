import random

# Classe Entità: base per tutti i personaggi. Vedere documentazione (README.md)
class Entita:
    def __init__(self, livello, nome, tipo):
        self.livello = livello
        self.nome = nome
        self.tipo = tipo
        self.attacco = 1 #statistica attacco
        self.difesa = 1 #statistica difesa
        self.punti_vita = 1 #punti vita massimi
        self.punti_esperienza = 50 #punti esperienza massimi
        self.punti_vita_correnti = 1 #punti vita correnti
        self.punti_esperienza_correnti = 0 #punti esperienza correnti
        self.abilita_attivata = False #indica se l'abilità dell'entità è già stata utilizzata nel combattimento corrente
        self.lista_strumenti = []

    def attacca(self):
        #ritorna un numero casuale tra 0 e il valore massimo di attacco durante il combattimento
        return random.randint(0, self.attacco)
    
    def difende(self):
        #ritorna un numero casuale tra 0 e il valore massimo di difesa durante il combattimento
        return random.randint(0, self.difesa)
    
    def prendi_danno(self, punti_vita_sottratti):
        #sottrae la vita in base al danno subito
        self.punti_vita_correnti -= punti_vita_sottratti
        if self.punti_vita_correnti < 0:
            self.punti_vita_correnti = 0

    def sconfitto(self):
        #ritorna se l'entità è stata sconfitta o meno in base ai punti vita rimasti
        return self.punti_vita_correnti <= 0

    def guadagna_xp(self, livello_avversario):
        if self.livello > livello_avversario:
            #se l'avversario è di livello più basso guadagnamo solo 10 xp
            self.punti_esperienza_correnti += 10
        elif self.livello == livello_avversario:
            #se l'avversario è di livello uguale al nostro guadagnamo 25 xp
            self.punti_esperienza_correnti += 25
        else:
            #se l'avversario è di livello più alto guadagnamo ben 50 xp
            self.punti_esperienza_correnti += 50

        if self.punti_esperienza_correnti >= self.punti_esperienza:
            #abbiamo superato la soglia, aumentiamo di livello salvandoci l'eccesso di xp
            self.punti_esperienza_correnti %= self.punti_esperienza
            self.aumenta_livello()

    def aumenta_livello(self):
        #aggiornerà attacco, difesa e punti vita, aumentando di livello
        self.livello += 1
        
    def rigenera_salute(self):
        #alla fine del combattimento rigeneriamo la vita dell'entità
        self.punti_vita_correnti = self.punti_vita

    def stampa_statistiche(self):
        #resoconto delle statistiche correnti del personaggio
        risultato = f"Classe: {self.tipo} | Livello: {self.livello}\n"
        risultato += f"ATK {self.attacco} DEF {self.difesa}\n"
        risultato += f"HP: {self.punti_vita} | XP: {self.punti_esperienza_correnti} su {self.punti_esperienza}\n"
        return risultato

    def stampa_stato(self):
        #resoconto dei punti vita dell'entità durante il combattimento
        return f"{self.nome} | HP {self.punti_vita_correnti} su {self.punti_vita}"
    
    def attiva_abilita(self, nemico):
        #attivazione abilita
        self.abilita_attivata = True
        return "Abilità attivata"
    
    def rigenera_abilita(self):
        #rigenerazione abilita dopo l'eventuale utilizzo
        self.abilita_attivata = False
    
    def aggiungi_strumento(self, strumento):
        #aggiunta strumento alla lista strumenti
        self.lista_strumenti.append(strumento)

    def utilizza_strumento(self, indice_strumento, nemico):
        #utilizzo ed eliminazione di uno strumento
        strumento = self.lista_strumenti[indice_strumento]
        print(strumento.attiva_strumento(self, nemico))
        self.lista_strumenti.pop(indice_strumento)

class Drago(Entita):
    def __init__(self, livello, nome):
        #inizializziamo il drago con attacco max, difesa min e punti_vita medi
        #lo relazioniamo al livello partendo da 9 livelli in più per evitare disomogeneità esagerate
        #nella fase di early game
        super().__init__(livello, nome, "Drago")
        self.attacco = (self.livello + 9) * 11
        self.punti_vita = (self.livello + 9) * 10
        self.difesa = (self.livello + 9) * 9
        self.punti_vita_correnti = self.punti_vita

    def aumenta_livello(self):
        #ricalcola le statistiche a partire dal nuovo livello ottenuto
        super().aumenta_livello()
        self.attacco = (self.livello + 9) * 11
        self.punti_vita = (self.livello + 9) * 10
        self.difesa = (self.livello + 9) * 9
    
    def attiva_abilita(self, nemico):
        #aumenta la sua difesa di un massimo del 20% in relazione ai punti vita rimasti
        if not self.abilita_attivata:
            percentuale_punti_vita = self.punti_vita_correnti * 100 // self.punti_vita
            percentuale_boost_difesa = 20 - int(0.2 * percentuale_punti_vita)
            self.difesa += self.difesa * percentuale_boost_difesa // 100
            if percentuale_boost_difesa == 0:
                return "Abilità non attivabile ora. Hai ancora tutti i punti vita.\n"
            else:
                return super().attiva_abilita(nemico) + f" - La difesa di {self.nome} è aumentata del {percentuale_boost_difesa}%.\n"
        return "Abilità non attivabile. È già stata attivata.\n"

class Elfo(Entita):
    def __init__(self, livello, nome):
        #inizializziamo l'elfo con attacco min, difesa medi e punti_vita max
        #lo relazioniamo al livello partendo da 9 livelli in più per evitare disomogeneità esagerate
        #nella fase di early game
        super().__init__(livello, nome, "Elfo")
        self.attacco = (self.livello + 9) * 9
        self.punti_vita = (self.livello + 9) * 11
        self.difesa = (self.livello + 9) * 10
        self.punti_vita_correnti = self.punti_vita

    def aumenta_livello(self):
        #ricalcola le statistiche a partire dal nuovo livello ottenuto
        super().aumenta_livello()
        self.attacco = (self.livello + 9) * 9
        self.punti_vita = (self.livello + 9) * 11
        self.difesa = (self.livello + 9) * 10
    
    def attiva_abilita(self, nemico):
        #aumenta il suo attacco di un massimo del 20% in relazione ai punti vita rimasti
        if not self.abilita_attivata:
            percentuale_punti_vita = self.punti_vita_correnti * 100 // self.punti_vita
            percentuale_boost_attacco = 20 - int(0.2 * percentuale_punti_vita)
            self.attacco += self.attacco * percentuale_boost_attacco // 100
            if percentuale_boost_attacco == 0:
                return "Abilità non attivabile ora. Hai ancora tutti i punti vita.\n"
            else:
                return super().attiva_abilita(nemico) + f" - L'attacco di {self.nome} è aumentato del {percentuale_boost_attacco}%.\n"
        return "Abilità non attivabile. È già stata attivata.\n"

class Strega(Entita):
    def __init__(self, livello, nome):
        #inizializziamo la strega con attacco medi, difesa max e punti_vita min
        #lo relazioniamo al livello partendo da 9 livelli in più per evitare disomogeneità esagerate
        #nella fase di early game
        super().__init__(livello, nome, "Strega")
        self.attacco = (self.livello + 9) * 10
        self.punti_vita = (self.livello + 9) * 9
        self.difesa = (self.livello + 9) * 11
        self.punti_vita_correnti = self.punti_vita

    def aumenta_livello(self):
        #ricalcola le statistiche a partire dal nuovo livello ottenuto
        super().aumenta_livello()
        self.attacco = (self.livello + 9) * 10
        self.punti_vita = (self.livello + 9) * 9
        self.difesa = (self.livello + 9) * 11
    
    def attiva_abilita(self, nemico):
        #diminuisce di un livello l'avversario
        if not self.abilita_attivata:
            if nemico.livello > 1:
                nemico.livello -= 2
                nemico.aumenta_livello()
                return super().attiva_abilita(nemico) + f" - Il livello di {nemico.nome} è stato ridotto di uno.\n"
            else:
                return f"Abilità non attivata, il livello di {nemico.nome} è troppo basso.\n"
        return "Abilità non attivabile. È già stata attivata.\n"

class Samurai(Entita):
    def __init__(self, livello, nome):
        #inizializziamo il samurai con attacco medi, difesa medi e punti_vita medi
        #lo relazioniamo al livello partendo da 9 livelli in più per evitare disomogeneità esagerate
        #nella fase di early game
        super().__init__(livello, nome, "Samurai")
        self.attacco = (self.livello + 9) * 10
        self.punti_vita = (self.livello + 9) * 10
        self.difesa = (self.livello + 9) * 10
        self.punti_vita_correnti = self.punti_vita

    def aumenta_livello(self):
        #ricalcola le statistiche a partire dal nuovo livello ottenuto
        super().aumenta_livello()
        self.attacco = (self.livello + 9) * 10
        self.punti_vita = (self.livello + 9) * 10
        self.difesa = (self.livello + 9) * 10
    
    def attiva_abilita(self, nemico):
        #abbassa la difesa dell'avversario del 5%
        if not self.abilita_attivata:
            nemico.difesa -= int(nemico.difesa * 0.05)
            return super().attiva_abilita(nemico) + f" - La difesa di {nemico.nome} è stata ridotta del 5%.\n"
        return "Abilità non attivabile. È già stata attivata.\n"

#Classe strumento: base per tutti i strumenti
class Strumento:
    def __init__(self, nome, descrizione):
        self.nome = nome #nome dello strumento
        self.descrizione = descrizione #breve descrizione dello strumento
    
    def attiva_strumento(self, personaggio, nemico):
        #attivazione dello strumento
        return f"Strumento {self.nome} attivato"
    
    def to_string(self):
        #resoconto dello strumento
        return f"Strumento {self.nome}: {self.descrizione}"

class PozioneCura(Strumento):
    def __init__(self):
        super().__init__("Pozione cura", "Permette di recuperare 10 punti vita.")
    
    def attiva_strumento(self, personaggio, nemico):
        #incrementa la vita del personaggio di 10 punti vita
        personaggio.punti_vita_correnti = min(personaggio.punti_vita_correnti + 10, personaggio.punti_vita)
        return super().attiva_strumento(personaggio, nemico)

class PozioneDanno(Strumento):
    def __init__(self):
        super().__init__("Pozione danno", "Permette di infliggere un danno di 10 punti vita.")
    
    def attiva_strumento(self, personaggio, nemico):
        #decrementa la vita dell'avversario di 10 punti vita
        nemico.prendi_danno(10)
        return super().attiva_strumento(personaggio, nemico)

#programma

def switch():
    #switch per la gestione dell'accesso al gioco
    accensione = True #booleana che gestisce il loop del programma

    while accensione: 
        print("Benvenuto nel gioco. \nScegliere l'opzione desiderata")
        print("1. Entra")
        print("0. Esci")
        
        scelta = input("Inserisci la tua scelta: ")
        print()

        if scelta == "0": 
            #l'utente vuole uscire dal programma, chiediamo conferma
            print("Sei sicuro di voler uscire dal gioco?")
            print("1. Conferma l'uscita dal gioco")
            print("2. Ritorna nel gioco")

            scelta = input("Inserisci la tua scelta: ")
            print()
            
            if scelta == "1": 
                #conferma l'uscita
                accensione = False 
                print("Sei uscito dal gioco\n")
            
            elif scelta == "2": 
                #rimanere nel gioco
                print("Sei rimasto nel gioco, buon divertimento!\n")

            else:
                print("L'opzione da te inserita non è corretta, riprova.\n")

        elif scelta == "1":
            #entra nel gioco
            print("Sei entrato nel gioco, buon divertimento!\n")

            #creazione personaggio
            personaggio = crea_personaggio()

            #ingresso in menu di gioco
            print (f"\nBENVENUTO {personaggio.nome}\n")
            switch_gioco(personaggio)

        else:
            #errore, opzione inesistente
            print("L'opzione da te inserita non è corretta, riprova.\n")

def crea_personaggio():
    #creazione personaggio
    #inserimento nome personaggio
    print("Benvenuto, crea il tuo personaggio.")
    nome_scelto = input('Insersci il nome del tuo personaggio: ')
    print()

    #stampa di tutte le statistiche delle varie classi per scelta
    print('Queste sono le statistiche di tutti i mostri:\n')

    drago = Drago(1, nome_scelto)
    print(drago.stampa_statistiche())
    print()

    elfo = Elfo(1, nome_scelto)
    print(elfo.stampa_statistiche())
    print()

    strega = Strega(1, nome_scelto)
    print(strega.stampa_statistiche())
    print()

    samurai = Samurai(1, nome_scelto)
    print(samurai.stampa_statistiche())
    print()

    check = 1 #variabile che gestisce il loop di inserimento della classe desiderata
    while check == 1:
        print('premi D per scegliere il drago, E per elfo, St per strega e S per samurai')
        tipo_scelto = input("Inserisci la tua scelta: ")
        print()
        
        check = 0 #se scelta è valida, uscire dal ciclo

        if tipo_scelto == 'D':
            #selezione drago
            personaggio_scelto = drago

        elif tipo_scelto == 'E':
            #selezione elfo
            personaggio_scelto = elfo

        elif tipo_scelto == 'St':
            #selezione strega
            personaggio_scelto = strega

        elif tipo_scelto == 'S':
            #selezione samurai
            personaggio_scelto = samurai
        else:
            #scelta non valida, ripetere il ciclo
            print("L'opzione da te inserita non è corretta, riprova.\n")
            check = 1

    return personaggio_scelto

def switch_gioco(personaggio):
    flag = True #gestisce il loop del menu di gioco

    while flag: 
        print ("Premi [1] per COMBATTERE\nPremi [2] per VISUALIZZARE LE STATISTICHE DEL TUO PERSONAGGIO\nPremi [0] per TORNARE INDIETRO")
        scelta = input("Inserisci la tua scelta: ")
        print()
        
        if scelta == "1":
            print ("Combatti\n")
            #combattimento

            #generazione nemico
            nemico = genera_nemico(personaggio.livello)

            #gestione del combattimento
            switch_combattimento(personaggio, nemico)
                   
        elif scelta == "2":
            #stampa delle statistiche correnti del personaggio
            print ("STATISTICHE PERSONAGGIO: \n")
            print(personaggio.stampa_statistiche())
        
        elif scelta == "0":
            #uscita dal gioco
            print("Sei sicuro di voler uscire dal gioco?")
            print("1. Conferma l'uscita dal gioco")
            print("2. Ritorna nel gioco")

            scelta = input("Inserisci la tua scelta: ")
            print()
            
            if scelta == "1": 
                #conferma l'uscita
                flag = False 
                print("INDIETRO AL MENU\n")
                break
            
            elif scelta == "2": 
                #rimanere nel gioco
                print("Sei rimasto nel gioco, buon divertimento!\n") 
            else:
                #opzione inesistente
                print("L'opzione da te inserita non è corretta, riprova.\n")
        else:
            #opzione inesistente
            print("L'opzione da te inserita non è corretta, riprova.\n")

def genera_nemico(livello):
    numero_nemico = random.randint(1, 4)
    if numero_nemico == 1:
        #drago
        return Drago(random.randint(max(livello - 1, 1), livello + 1), "Drago")
    elif numero_nemico == 2:
        #elfo
        return Elfo(random.randint(max(livello - 1, 1), livello + 1), "Elfo")
    elif numero_nemico == 3:
        #strega
        return Strega(random.randint(max(livello - 1, 1), livello + 1), "Strega")
    else:
        #samurai
        return Samurai(random.randint(max(livello - 1, 1), livello + 1), "Samurai")

def genera_strumento():
    #generazione di uno strumento (50% di probabilità)
    numero_strumento = random.randint(1, 4)
    if numero_strumento == 1:
        #pozione cura (25%)
        return PozioneCura()
    elif numero_strumento == 2:
        #pozione danno (25%)
        return PozioneDanno()
    else:
        #nessuno strumento (50%)
        return None

def switch_combattimento(personaggio, nemico):
    #menu di combattimento
    print("Hai incontrato un nemico!\n")
    print(nemico.stampa_statistiche() + "\n") #mostra le statistiche del nemico

    turno = 0

    while not personaggio.sconfitto() and not nemico.sconfitto():
        turno += 1
        print(f"Turno {turno}\n")

        print("Benvenuto nel menu Combattimento. \nScegliere l'opzione desiderata")
        print("1. Combatti")
        print("2. Usa abilita")
        print("3. Usa strumento")
        print("4. Fuggi")
       
        scelta = input("Inserisci la tua scelta: ")
        print()

        if scelta == "1":
            #l'utente vuole combattere
            print("1. Combatti")
            print("2. Torna al menu")
           
            scelta = input("Inserisci la tua scelta: ")
            print()
           
            if scelta == "2":
                #conferma il ritorno al Menù Combattimento
                print("Sei tornato al menù combattimento\n")
           
            elif scelta == "1":
                #esecuzione di un doppio turno di combattimentos
                combattimento(personaggio, nemico, turno)
                turno += 1
                
            else:
                #opzione inesistente
                print("L'opzione da te inserita non è corretta, riprova.\n")

        elif scelta == "2":
            # richiesta uso abilita
            print("Hai scelto di utilizzare la tua abilità")
            print("1. Utilizza la tua abilità ")
            print("2. Torna al menu")

            scelta = input("Inserisci la tua scelta: ")
            print()

            #richiamo funzione abilità
            if scelta == "1":
                #gestione abilita
                print(personaggio.attiva_abilita(nemico))

            elif scelta == "2":
               #torna al menu combattimento
               print("Sei tornato al menù combattimento\n")

            else:
                #opzione inesistente
                print("L'opzione da te inserita non è corretta, riprova.\n")


        elif scelta == "3":
            print("Hai scelto di utilizzare il tuo strumento")
            print("1. Utilizza uno strumento")
            print("2. Torna al menu")
       
            scelta = input("Inserisci la tua scelta: ")
            print()

            if scelta == "1":
                #utilizza strumento
                if personaggio.lista_strumenti == []:
                    print("Non possiedi alcuno strumento\n")
                else:
                    opzione = 1
                    for strumento in personaggio.lista_strumenti:
                        print(f"{opzione}. {strumento.nome}")
                        opzione += 1
                    print(f"0. Nessuno strumento")
                    
                    indice_strumento = int(input("Scegli lo strumento da utilizzare: "))
                    if indice_strumento > 0 and indice_strumento <= len(personaggio.lista_strumenti):
                        personaggio.utilizza_strumento(indice_strumento - 1, nemico)
                        print(personaggio.stampa_stato())
                        print(nemico.stampa_stato())
                    else:
                        print("L'opzione da te inserita non è corretta, riprova.\n")

            elif scelta == "2":
               print("Sei tornato al menù combattimento\n")

            else:
                #opzione inesistente
                print("L'opzione da te inserita non è corretta, riprova.\n")

       
        elif scelta == "4":
            #menu fuga
            print("Hai scelto di fuggire")
            print("1. Conferma fuga")
            print("2. Torna al menu")

            scelta = input("Inserisci la tua scelta: ")
            print()

            if scelta == "1":
                #fuga confermata
                print("Hai scelto di fuggire, fuggi!\n")
                break
           
            elif scelta == "2":
               #fuga annullata
               print("Sei tornato al menù combattimento\n")

            else:
                #opzione inesistente
                print("L'opzione da te inserita non è corretta, riprova.\n")

        else:
            #errore, opzione inesistente
            print("L'opzione da te inserita non è corretta, riprova.\n")
    
    if personaggio.sconfitto():
        #personaggio sconfitto
        print("Mi dispiace, sei stato sconfitto\n")
    elif nemico.sconfitto():
        #personaggio vittorioso
        print("Congratulazioni, hai sconfitto il nemico\n")
        personaggio.guadagna_xp(nemico.livello) #aggiunta xp della battaglia
        strumento = genera_strumento() #viene generato un eventuale strumento come drop del nemico
        if strumento != None:
            #aggiunta dello strumento alla nostra lista di strumenti
            personaggio.aggiungi_strumento(strumento)
            print("Hai guadagnato uno strumento!")
            print(strumento.to_string())
        print()

    personaggio.rigenera_salute() #il personaggio rigenera salute alla fine di ogni combattimento
    personaggio.rigenera_abilita() #rigeneriamo la possibilità di utilizzare l'abilità al prossimo combattimento

def combattimento(personaggio, nemico, turno):

        #calcolo di attacco personaggio, difesa nemico e della loro differenza
        attacco = personaggio.attacca()
        difesa = nemico.difende()
        print(f"{personaggio.nome}: ATK -> {attacco}")
        print(f"Nemico: DEF -> {difesa}")
        combattimento = attacco - difesa 

        if combattimento > 0:
            #attacco efficace, sottraggo la vita al nemico
            print(f"{personaggio.nome}: datto inflitto -> {combattimento}")
            nemico.prendi_danno(combattimento)
        else:
            #attacco non efficace
            print(f"{personaggio.nome}: l'attacco era troppo debole")

        print(f"\nTurno {turno + 1}\n")

        attacco = nemico.attacca()
        difesa = personaggio.difende()
        print(f"Nemico: ATK -> {attacco}")
        print(f"{personaggio.nome}: DEF -> {difesa}")
        combattimento = attacco - difesa 

        if combattimento > 0:
            #attacco efficace, sottraggo vita al personaggio
            print(f"Nemico: datto inflitto -> {combattimento}")
            personaggio.prendi_danno(combattimento)
        else:
            #attacco non efficace
            print("Nemico: l'attacco era troppo debole\n")

        #recap stato corrente di personaggio e nemico
        print(personaggio.stampa_stato())
        print(nemico.stampa_stato())
        print()

    #termine battaglia

switch() #ingresso nel programma
