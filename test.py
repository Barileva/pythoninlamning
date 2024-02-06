
import numpy as np

x = 3
print(x)

def start_menu():
    while True:
        svar = input("""
                    välj ett av nedan alternativ 
                    \n 1. kryptera  ord/meddelande 
                    \n 2. dekryptera ord/meddelande
                    \n 3. se antalet krypterade ord/meddelande
                    \n 4. avsluta programmet
                    """)
        print(svar)
start_menu()