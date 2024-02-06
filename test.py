
# import numpy as np

def start_menu():
    while True:
        svar = input("""
                    \n välj ett av nedan alternativ 
                    \n 1. kryptera  ord/meddelande 
                    \n 2. dekryptera ord/meddelande
                    \n 3. se antalet krypterade ord/meddelande
                    \n 4. avsluta programmet
                    """)

        if svar == "1":
            shift = int(input("Ange antal steg för förskjutning i alfabetet"))

            print("kryptera")
        elif svar == "2":
            print("dekryptera")
        elif svar == "3":
            print("antalet meddelande")
        elif svar == "4":
            break
        else:
            print("Ogiltig inmatning, försök igen")

start_menu()


