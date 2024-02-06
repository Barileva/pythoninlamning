
#importerting av NumPy-biblioteket
import numpy as np


# Funktionen skapar en egen alfabet baserat på antalet förskjutningar (shift)
def omvandling_till_krypterat_alfabet(shift):
    # skapar NumPy-array med alla engelska bokstäver (små och stora) baserat på intervaller tillhörande ASCII-värden
    alfabet = np.array([chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)])
    # alfabetet skiftas beroende på antalet angivna shift
    forskjutet_alfabet = np.roll(alfabet, -shift)
    # alfabetet inkl. det manipulerade alfabetet sätts samman parvis för att konverteras till dictionary
    krypterat_alfabet = dict(zip(alfabet, forskjutet_alfabet))
    # returnerar krypterat_alfabet
    return krypterat_alfabet


# funktionen krypterar ett meddelande med en angiven förskjutning
def kryptering(meddelande, shift):
    # anropar funktionen omvandling_till_krypterat_alfabet(shift)
    alfabetet = omvandling_till_krypterat_alfabet(shift)
    #
    krypterat_meddelande = "".join([alfabetet.get(i, i) for i in meddelande])
    return krypterat_meddelande

def dekryptering(meddelande, shift):
    alfabetet = omvandling_till_krypterat_alfabet(-shift)
    dekrypterat_meddelande = "".join([alfabetet.get(i, i) for i in meddelande])
    return dekrypterat_meddelande

def get_valid_shift():
    while True:
        try:
            shift = int(input("Ange antal steg för förskjutning i alfabetet (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Ogiltigt antal. Vänligen ange ett tal mellan 1 och 25.")
        except ValueError:
            print("Ogiltig inmatning. Ange ett heltal.")

def get_valid_index(max_val):
    while True:
        try:
            val = int(input("Välj det meddelande du vill dekryptera (ange nummer): ")) - 1
            if 0 <= val < max_val:
                return val
            else:
                print(f"Ogiltigt val. Ange ett nummer mellan 1 och {max_val}.")
        except ValueError:
            print("Ogiltig inmatning. Ange ett heltal.")

def confirm_exit():
    while True:
        svar = input("Är du säker på att du vill avsluta programmet? (ja/nej): ").lower()
        if svar == "ja":
            return True
        elif svar == "nej":
            return False
        else:
            print("Ogiltig inmatning. Vänligen svara med 'ja' eller 'nej'.")

def start_menu():
    krypterade_meddelanden = []  # Ändrat till att lagra tuples av meddelande och shift
    while True:
        svar = input("\nVälj ett av följande alternativ: 1. Kryptera meddelande, 2. Dekryptera meddelande, \n"
                     "3. Se antalet krypterade meddelande, 4. Avsluta programmet. Ange ditt val här: ")

        if svar == "1":
            shift = get_valid_shift()
            meddelande = input("Ange meddelandet du önskar kryptera: ")
            krypterat = kryptering(meddelande, shift)
            krypterade_meddelanden.append((krypterat, shift))  # Sparar både meddelande och shift
            print(f"Ditt angivna meddelande: '{meddelande}', har krypterats till: '{krypterat}' med en förskjutning på {shift}")

        elif svar == "2":
            if not krypterade_meddelanden:
                print("Det finns inga krypterade meddelanden att dekryptera.")
                continue
            print("\nLista över krypterade meddelanden:")
            for idx, (msg, _) in enumerate(krypterade_meddelanden, 1):
                print(f"{idx}. {msg}")
            val = get_valid_index(len(krypterade_meddelanden))
            meddelande, shift = krypterade_meddelanden[val]
            dekrypterat = dekryptering(meddelande, shift)  # Använder sparad shift för dekryptering
            print(f"Dekrypterat meddelande: '{dekrypterat}'")
            krypterade_meddelanden.pop(val)

        elif svar == "3":
            print(f"Antal krypterade meddelanden: {len(krypterade_meddelanden)}")
            for idx, msg in enumerate(krypterade_meddelanden, 1):
                print(f"{idx}. {msg}")

        elif svar == "4":
            if confirm_exit():
                print("Avslutar programmet...")
                break

        else:
            print("Ogiltig inmatning, försök igen.")

start_menu()




# import numpy as np
#
# def omvandling_till_krypterat_alfabet(shift):
#     alfabet = np.array([chr(i) for i in range(97, 123)])
#     forskjutet_alfabet = np.roll(alfabet, -shift)
#     krypterat_alfabet = dict(zip(alfabet, forskjutet_alfabet))
#     return krypterat_alfabet
#
# def kryptering (meddelande, shift):
#     alfabetet = omvandling_till_krypterat_alfabet(shift)
#     krypterat_meddelande = "".join([alfabetet.get(i, i) for i in meddelande])
#     return krypterat_meddelande
#
# def dekryptering(meddelande, shift):
#     alfabetet = omvandling_till_krypterat_alfabet(-shift)
#     dekrypterat_meddelande = "".join([alfabetet.get(i, i) for i in meddelande])
#     return dekrypterat_meddelande
#
#
#
# def start_menu():
#     krypterade_meddelande = []
#     while True:
#         svar = input("\nvälj ett av följande alternativ: 1. kryptera ord/meddelande, 2. dekryptera ord/meddelande, \n"
#         "3. se antalet krypterade ord/meddelande, 4. avsluta programmet, Ange ditt val här: ")
#
#
#
#         if svar in ["1","2"]:
#             shift = int(input("Ange antal steg för förskjutning i alfabetet (1-25): "))
#             if svar == "1":
#                 meddelande = (input("Ange meddelandet du önskar kryptera? ")).lower()
#                 krypterat = kryptering (meddelande, shift)
#                 krypterade_meddelande.append(krypterat)
#                 print(f"ditt angivna meddelande: {meddelande}, har krypterats till: {krypterat}")
#             elif svar == "2":
#                 meddelande = (input("Ange meddelandet du önskar dekryptera? ")).lower()
#                 dekrypterat = dekryptering(meddelande, shift)
#                 antalet_meddelande -= 1
#                 print(f"dekrypterat medelande: {dekrypterat}")
#
#         elif svar == "3":
#             print(f"Antal krypterade meddelande:  {len(krypterade_meddelande)}")
#             for meddelande in krypterade_meddelande:
#                 print(meddelande)
#
#         elif svar == "4":
#             break
#         else:
#             print("Ogiltig inmatning, försök igen")
#
# start_menu()
#

