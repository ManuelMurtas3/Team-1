#programma

def switch(): 

    accensione = True 

    while accensione: 

        print("Benvenuto nel gioco. \nScegliere l'opzione desiderata")
        print("1.Entra")
        print("2.Esci")
        
        scelta = input("Inserisci la tua scelta: ")

        if scelta == "2": 
            
            print("Sei sicuro di voler uscire dal gioco?")
            print("Digita 1 per confermare l'uscita dal gioco")
            print("Digita 2 per ritornare nel gioco ")

            scelta = input("Inserisci la tua scelta")
            
            if scelta == "1": 
                accensione = False 
                print("Sei uscito dal gioco")
            
            elif scelta == "2": 
                #rimanere nel gioco
                print("Sei rimasto nel gioco, buon divertimento!")

        elif scelta == "1":
            print( "Sei entrato nel gioco, buon divertimento!")

        else: 
            print("L'opzione da te inserita non è corretta, riprova.")

switch()       



