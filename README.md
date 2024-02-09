


Applikationen använder logik för att kryptera och dekryptera meddelanden. 
Koden börjar med att importera NumPy, ett bibliotek för vetenskapliga beräkningar. 

Funktionen "omvandling_till_krypterat_alfabet(shift)"skapar ett krypterat alfabet med hjälp av antalet shift som användaren matar in.
En array skapas med hjälp av ACSII-värden för engelska bokstäver där små och stora bokstäver ingår. Svenska bokstäver är tillagda.   
Np-roll skapar ett förskjutet alfabet baserat med antalet shift.
Slutligen skapas ett dictionary där varje originalbokstav zippas mot sin krypterade motsvarighet.

Funktionen "kryptering(meddelande, shift)" tar ett meddelande och en förskjutning som argument och använder det krypterade alfabetet från första funktionen.
Varje bokstav kan nu bytas ut mot dess krypterade motsvarighet. Ett krypterat meddelande kan nu skapas.


Funktionen "dekryptering(meddelande, shift)" fungerar på motsvarande sätt som funktionen ovan("kryptering(meddelande, shift)").
Den tar emot ett meddelande och förskjuitningen som användes vid kryptering, för att återställer varje bokstav till sin ursprungliga position.

Funktionen "giltig_inmatning()" säkerställer så användaren matar in rätt heltalsindex mellan (1-28). Detta för att förhindra error.
En loop körs tills användaren har matat in rätt heltalsindex. 

Funktionen "get_valid_index(max_val)" säkerställer att användaren väljer ett giltigt index för ett krypterat meddelande som finns i en lista, för att sedan dekryptera det.

Funktionen "confirm_exit" frågar användaren om de verkligen vill avsluta programmet och hanterar svaret.


Funktionen "start_menu()" är själva huvudmenyn för applikationen och låter användaren välja mellan att kryptera ett meddelande, dekryptera ett befintligt meddelande, se antalet krypterade meddelanden inkl. antalet shift, eller avsluta programmet. 
Funktionen använder en loop för att upprepa menyn tills användaren väljer att avsluta.

För detaljerade beskrivningar, se kommentarer i koden. 

