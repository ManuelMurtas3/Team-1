

personaggio = Drago(1, 'nome_scelto')

def switch_gioco():
    flag = True 
    while flag: 
        print (" COSA VUOI FARE? \n")
        print (" Premi [1] per COMBATTERE\n Premi [2] per VISUALIZZARE LE STATISTICHE DEL TUO PERSONAGGIO\n Premi [0] per TORNARE INDIETRO\n")
        scelta = int(input(""))
        
        if scelta == 1 :
            print ("Combatti")
            #genera_nemico
            #gestione dei turni
            #assegnazione degli xp
            
        elif scelta == 2:
            
            print ("STATISTICHE PERSONAGGIO: \n")
            print(personaggio.stampa_statistiche())
            #crea un oggetto per ogni entità
        
        elif scelta == 0:
            print("INDIETRO AL MENU")
            break
        
        else:
            print("ATTENZIONE ")
      

switch_gioco()
    