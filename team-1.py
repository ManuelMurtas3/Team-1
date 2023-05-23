# Classe Entità: base per tutti i personaggi. Vedere documentazione (README.md)
import random

class Entita:
    def __init__(self, livello, nome, tipo):
        self.livello = livello
        self.nome = nome
        self.tipo = tipo
        self.attacco = 1
        self.difesa = 1
        self.punti_vita = 1
        self.punti_esperienza = 50
        self.punti_vita_correnti = 1
        self.punti_esperienza_correnti = 0

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
        risultato += f"ATK {self.attacco} | DEF {self.difesa}\n"
        risultato += f"HP: {self.punti_vita} | XP: {self.punti_esperienza_correnti} su {self.punti_esperienza}\n"
        return risultato

    def stampa_stato(self):
        #resoconto dei punti vita dell'entità durante il combattimento
        return f"{self.nome} | HP {self.punti_vita_correnti} su {self.punti_vita}"

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
        self.punti_vita_correnti = self.punti_vita

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
        self.punti_vita_correnti = self.punti_vita

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
        self.punti_vita_correnti = self.punti_vita

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
        self.punti_vita_correnti = self.punti_vita

#programma

def genera_nemico(livello):
    numero_nemico = random.randint(1, 4)
    if numero_nemico == 1:
        #drago
        return Drago(random.randint(livello - 1, livello + 1), "Drago")
    elif numero_nemico == 2:
        #elfo
        return Elfo(random.randint(livello - 1, livello + 1), "Elfo")
    elif numero_nemico == 3:
        #strega
        return Strega(random.randint(livello - 1, livello + 1), "Strega")
    else:
        #samurai
        return Samurai(random.randint(livello - 1, livello + 1), "Samurai")

personaggio = Drago(10, "Me")
nemico = genera_nemico(personaggio.livello)
turno_personaggio = True

print("Hai incontrato un nemico!\n")
print(nemico.stampa_statistiche() + "\n")

while not personaggio.sconfitto() and not nemico.sconfitto():
    if turno_personaggio:
        attacco = personaggio.attacca()
        difesa = nemico.difende()
        print(f"{personaggio.nome}: ATK -> {attacco}")
        print(f"Nemico: DEF -> {difesa}")
        combattimento = attacco - difesa 

        if combattimento > 0:
            print(f"{personaggio.nome}: datto inflitto -> {combattimento}")
            nemico.prendi_danno(combattimento)
        else:
            print(f"{personaggio.nome}: l'attacco era troppo debole")
        turno_personaggio = False
    else:
        attacco = nemico.attacca()
        difesa = personaggio.difende()
        print(f"Nemico: ATK -> {attacco}")
        print(f"{personaggio.nome}: DEF -> {difesa}")
        combattimento = attacco - difesa 

        if combattimento > 0:
            print(f"Nemico: datto inflitto -> {combattimento}")
            personaggio.prendi_danno(combattimento)
        else:
            print("Nemico: l'attacco era troppo debole")
        turno_personaggio = True
    print(personaggio.stampa_stato())
    print(nemico.stampa_stato())
    print()

if personaggio.sconfitto():
    print("Mi dispiace, sei stato sconfitto")
else:
    print("Congratulazioni, hai sconfitto il nemico")
    personaggio.guadagna_xp(nemico.livello)
