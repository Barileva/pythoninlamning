
# koden avser uppgift Kryptografi med NumPy

#importerting av NumPy-biblioteket
import numpy as np


# Funktionen skapar ett krypterat alfabet baserat på antalet förskjutningar (shift)
def omvandling_till_krypterat_alfabet(shift):
    # skapar NumPy-array med alla engelska och svenska bokstäver (små och stora) baserat på intervaller tillhörande ASCII-värden
    alfabet = np.array(
        [chr(i) for i in range(97, 123)] + ['å', 'ä', 'ö'] +
        [chr(i) for i in range(65, 91)] + ['Å', 'Ä', 'Ö'])
    # alfabetet förskjuts beroende på antalet angivna shift, ett nytt alfabete skapas baserat på antalet angivna shift
    forskjutet_alfabet = np.roll(alfabet, -shift)
    # "alfabetet" inkl. det manipulerade alfabetet (forskjutet_alfabet) sätts samman parvis för att konverteras till dictionary
    krypterat_alfabet = dict(zip(alfabet, forskjutet_alfabet))
    # returnerar krypterat_alfabet
    return krypterat_alfabet


# funktionen krypterar ett meddelande med en angiven förskjutning
def kryptering(meddelande, shift):
    # skapar ett krypterat alfabet med angivet shift-värde genom att anropar funktionen: omvandling_till_krypterat_alfabet(shift)
    alfabetet = omvandling_till_krypterat_alfabet(shift)
    # list comprehensions, get() anrop till dictionary alfabetet. Get() söker efter värdet för nyckeln "i" i dictionaryn. Om nyckeln "i" finns, returneras värdet som är kopplat till den nyckeln (det krypterade tecknet).
    # Om nyckeln inte finns, returneras "i" (det andra argumentet till .get() metoden), vilket innebär att tecknet inte ändras. .join() sammanfogar till en enda sträng.
    krypterat_meddelande = "".join([alfabetet.get(i, i) for i in meddelande])
    # returnerar krypterat_meddelande
    return krypterat_meddelande

# funktionen återställer ett krypterat meddelande
def dekryptering(meddelande, shift):
    # anropar funktionen: omvandling_till_krypterat_alfabet(-shift), det negativa värdet på shift används för att  skapa ett alfabet där varje bokstav har skiftats tillbaka till sin ursprungliga position.
    alfabetet = omvandling_till_krypterat_alfabet(-shift)
    # list comprehensions, get() anrop till dictionary alfabetet. Get() söker efter värdet för nyckeln "i" i dictionaryn. Om nyckeln "i" finns, returneras värdet som är kopplat till den nyckeln (det krypterade tecknet).
    # Om nyckeln inte finns, returneras "i" (det andra argumentet till .get() metoden), vilket innebär att tecknet inte ändras. .join() sammanfogar till en enda sträng.
    dekrypterat_meddelande = "".join([alfabetet.get(i, i) for i in meddelande])
    # returnerar dekrypterat_meddelande
    return dekrypterat_meddelande

# funktionen säkerställer att användaren anger giltig inmatning (1-28) enligt cesar-kryptering för det engelska alfabetet.
def giltig_inmatning():
    # oändlig loop, körs till ett giltigt värde har erhållits och funktionen returnerar ett värde.
    while True:
        # try-sats för felhantering och undantag. Om fel/undantag uppstår anropas except ValueError.
        try:
            # if-sats med vilkorskontroll
            shift = int(input("Ange antal steg för förskjutning i alfabetet (1-28): "))
            if 1 <= shift <= 28:
                return shift
            else:
                print("Ogiltigt antal. Vänligen ange ett tal mellan 1 och 28.")
        except ValueError:
            print("Ogiltig inmatning. Ange ett heltal.")

# funktionen säkerställer att inmatningen är ett giltigt heltalsindex inom ett visst intervall
def get_valid_index(max_val):
    while True:
        try:
             # "-1" subtrahera från det användaren matar in för att omvandla det till ett index som är lämpligt för användning "
            val = int(input("Välj det meddelande du vill dekryptera (ange nummer): ")) - 1
            # kontrollerar om val ligger inom intervallet [0, max_val-1].
            if 0 <= val < max_val:
                return val
            else:
                # ber användaren att ange ett nummer mellan 1 och det högsta värdet
                print(f"Ogiltigt val. Ange ett nummer mellan 1 och {max_val}.")
        except ValueError:
            print("Ogiltig inmatning. Ange ett heltal.")

# funktionen frågar användaren om den verkligen önskar avsluta programmet med while loop och vilkorssatser. .lower() omvandlar till små bokstäver.
def confirm_exit():
    while True:
        svar = input("Är du säker på att du vill avsluta programmet? (ja/nej): ").lower()
        if svar == "ja":
            return True
        elif svar == "nej":
            return False
        else:
            print("Ogiltig inmatning. Vänligen svara med 'ja' eller 'nej'.")

# funktionen är huvudmenyn för applikationen där användaren ges möjlighet att välja mellan olika alternativ för kryptering och dekryptera av meddelanden, visa antalet krypterade meddelande, eller avsluta programmet.
def start_menu():
    # initierar en lista med tuples (lagrade element) där varje tuples innehåller ett krypterat meddelande och den shift-värde som användes för att kryptera det.
    krypterade_meddelanden = []
    # while-loop, presentation av val, svaret sparas i "svar"
    while True:
        svar = input("\nVälj ett av följande alternativ: 1. Kryptera meddelande, 2. Dekryptera meddelande, \n"
                     "3. Se antalet krypterade meddelande, 4. Avsluta programmet. Ange ditt val här: ")
        # if-sats, kontrollerar om användaren valt alternativ 1, vilket är att kryptera ett meddelande
        if svar == "1":
            # anropar funktionen "giltig inmatning()" för att få ett giltigt shift-värde från användaren
            shift = giltig_inmatning()
            # ber användaren ange det meddelande som ska krypteras
            meddelande = input("Ange meddelandet du önskar kryptera: ")
            # anropar funktionen kryptering med användarens meddelande och shift-värde, och sparar det krypterade meddelandet i variabeln krypterat
            krypterat = kryptering(meddelande, shift)
            # lägger till en tuple bestående av det krypterade meddelandet och shift-värdet i listan "krypterade_meddelanden"
            krypterade_meddelanden.append((krypterat, shift))
            # skriver ut det ursprungliga meddelandet, det krypterade meddelandet, och det använda shift-värdet till användaren
            print(f"Ditt angivna meddelande: '{meddelande}', har krypterats till: '{krypterat}' med en förskjutning på {shift}")


        # Kontrollerar om användaren valt alternativ 2, vilket är att dekryptera ett meddelande
        elif svar == "2":
            # kontrollerar om listan krypterade_meddelanden är tom. Om den är tom, informeras användaren om detta och loopen startas om med nästa iteration
            if not krypterade_meddelanden:
                print("Det finns inga krypterade meddelanden att dekryptera.")
                continue
            # skriver ut en lista över alla krypterade meddelanden som är lagrade, med ett indexnummer före varje meddelande
            print("\nLista över krypterade meddelanden:")
            # for-loop tillsammans med funktionerna enumerate och unpackning. Enumerate tar listan "krypterade_meddelanden" och returnerar en annan lista.
            # Den nya listan består av tuples, där varje tuple innehåller ett index och värdet från den ursprungliga listan.
            # indexeringen börjar på 1 istället för 0, för bättre användarvänlighet.
            #  (msg, _) används för att packa upp varje element (som är en tuple) som enumerate ger oss. msg fångar det första värdet i tuple (som är det krypterade meddelandet),
            #  och _ används som en platsinnehållare för att ignorera det andra värdet. (ignoreras ine vanligtvis, i denna applikation ignoreras det)
            for idx, (msg, _) in enumerate(krypterade_meddelanden, 1):
                # skriver ut med f-strings, skriver ut variablernas värden i strängen
                print(f"{idx}. {msg}")
            # anropar funktionen get_valid_index med längden på listan "krypterade_meddelanden" som argument för att få ett giltigt index från användaren
            val = get_valid_index(len(krypterade_meddelanden))
            # hämtar det valda krypterade meddelandet och dess shift-värde baserat på användarens val
            meddelande, shift = krypterade_meddelanden[val]
            # anropar funktionen dekryptering med det valda krypterade meddelandet och dess shift-värde, och sparar det dekrypterade meddelandet i variabeln dekrypterat
            dekrypterat = dekryptering(meddelande, shift)
            # skriver ut det dekrypterade meddelandet till användaren
            print(f"Dekrypterat meddelande: '{dekrypterat}'")
            # tar bort det valda meddelandet från listan krypterade_meddelanden efter att det har dekrypterats
            krypterade_meddelanden.pop(val)

        # kontrollerar om användaren valt alternativ 3, vilket är att se antalet krypterade meddelanden
        elif svar == "3":
            # skriver ut det totala antalet krypterade meddelanden och listar dem med hjälp av funktionen "len()" som returnerar storleken på listan
            print(f"Antal krypterade meddelanden: {len(krypterade_meddelanden)}")
            # samma som ovan (elif svar == "2")
            for idx, msg in enumerate(krypterade_meddelanden, 1):
                print(f"{idx}. {msg}")

        # Kontrollerar om användaren valt alternativ 4, vilket är att avsluta programmet.
        elif svar == "4":
            # anropar funktionen confirm_exit() för att be användaren bekräfta avslutningen. Om användaren bekräftar, skrivs ett meddelande ut och loopen (och därmed programmet) avslutas
            if confirm_exit():
                print("Avslutar programmet...")
                break
        # för alla andra inmatningar än de definierade alternativen (1-4), informeras användaren om att inmatningen var ogiltig och ombeds försöka igen
        else:
            print("Ogiltig inmatning, försök igen.")

# anropar funktionen start_menu() för att starta programmet
start_menu()





