# Timer

###Potrzebne moduły
* flask
* Flask-SocketIO

###Jak uruchomić?
Należy uruchomić plik `server.py` interpreterem pythona, po czym zalogować się do panelu administratora `/admin` używając wygenerowanego tokenu.

###Struktura
Timer podzielony jest na 2 panele: `/admin` i `/`.
Po przejściu na pierwszy z nich dostaniemy się do panelu administratora.
Drugi odpowiada za to, co widzi użytkownik.

###/admin
Tutaj można ustawiać czas timera, wysyłać wiadomości do użytkowników oraz słuchać muzyki.

###/
Na stronie głównej znajduje się timer, pod którym będą się pojawiały wiadomości w razie ich otrzymania.
