
import numpy as np

def omvandling_till_krypterat_alfabet(shift):
    alfabet = np.array([chr(i) for i in range(97, 123)])
    forskjutet_alfabet = np.roll(alfabet, -shift)
    krypterat_alfabet = dict(zip(alfabet, forskjutet_alfabet))
    return krypterat_alfabet

def kryptering (meddelande, shift):
    alfabetet = omvandling_till_krypterat_alfabet(shift)
    krypterat_meddelande = "".join([alfabetet.get(i, i) for i in meddelande])
    return krypterat_meddelande

def dekryptering(meddelande, shift):
    alfabetet = omvandling_till_krypterat_alfabet(-shift)
    dekrypterat_meddelande = "".join([alfabetet.get(i, i) for i in meddelande])
    return dekrypterat_meddelande



def start_menu():
    while True:
        svar = input("""
                    \n välj ett av nedan alternativ 
                    \n 1. kryptera  ord/meddelande 
                    \n 2. dekryptera ord/meddelande
                    \n 3. se antalet krypterade ord/meddelande
                    \n 4. avsluta programmet
                    \n Ange ditt val här: """)

        shift = int(input("Ange antal steg för förskjutning i alfabetet (1-25)"))
        meddelande = (input("Ange meddelandet du önskar kryptera?")).lower()
        antalet_meddelande = 0

        if svar == "1":
            krypterat = kryptering (meddelande, shift)
            antalet_meddelande += 1
            print(f"krypterat meddelande: {krypterat}")
        elif svar == "2":
            dekrypterat = dekryptering(meddelande, shift)
            antalet_meddelande -= 1
            print(f"dekrypterat medelande: {dekrypterat}")
        elif svar == "3":
            print(f"Antal krypterade meddelande:  {antalet_meddelande}")
        elif svar == "4":
            break
        else:
            print("Ogiltig inmatning, försök igen")

start_menu()


