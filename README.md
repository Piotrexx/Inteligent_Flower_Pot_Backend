# Backend oraz kod do raspberry pi dedykowany dla inteligentnej doniczki

## Wstęp oraz biblioteki

Kod do kontroli i wysyłania danych z inteligentnej doniczki zrobionej na konukrs ["Elektronika – by żyło się łatwiej"](https://konkurs.aei.polsl.pl/). Projekt został stworzony za pomocą
języka programowania [Python](https://www.python.org/) wraz z jego następującą bibliotekami: 

 - Do stworzenia web serwera i do napisania API użyliśmy [Django](https://docs.djangoproject.com/en/5.0/) (wraz z jego frameworkiem [djnago-restframework](https://www.django-rest-framework.org/))
 - Do kierowaniem czujnikami w raspberry pi użyliśmy tych bibliotek: [Adafruit_Python_DHT](https://pypi.org/project/Adafruit_Python_DHT/) oraz [gpiozero](https://gpiozero.readthedocs.io/en/stable/), ta druga powinna być domyślnie zainstalowana na raspberry pi, **UWAGA, BIBLIOTEKI DO STEROWANIA RASPBERRY PI NIE DZIAŁAJĄ NA KOMPUTERACH**

 Do pobrania wszystkich bibliotek należy użyć tej komendy:

 ```shell
 pip install -r requirements.txt
 ```

Frontendowa część projektu (aplikacja):
[inteligent-flower-pot-frontend](https://github.com/janekskr/inteligent-flower-pot-frontend)


Części jakich użyliśmy:

 - [raspberry Pi zero W](https://botland.com.pl/moduly-i-zestawy-raspberry-pi-zero/20347-raspberry-pi-zero-2-w-512mb-ram-wifi-bt-42-5904422380700.html)
 - [Pompa wodna 6V](https://botland.com.pl/pompy/14164-pompa-wodna-6v-5904422342401.html)
 - [STEMMA - czujnik wilgotności gleby - Adafuit 4026](https://botland.com.pl/czujniki-wilgotnosci/14431-stemma-czujnik-wilgotnosci-gleby-adafuit-4026-5904422307301.html)
 - [Moduł przekaźnika 1 kanał z optoizolacją - styki 10A/250VAC cewka 5V](https://botland.com.pl/przekazniki-przekazniki-arduino/1997-modul-przekaznika-1-kanal-z-optoizolacja-styki-10a-250vac-cewka-5v-5904422359096.html)
 - [Czujnik poziomu cieczy z pływakiem - kontaktron](https://botland.com.pl/czujniki-poziomu-cieczy/7244-czujnik-poziomu-cieczy-z-plywakiem-kontaktron-5904422310035.html)

## Włączenie serwera na raspberry pi

By włączyć działający serwer należy wpisać poniższe komendy:

 - Dodawanie migracji

```shell
python manage.py makemigrations doniczka_backend_app
```

- Migracja modelu do bazy danych

```shell
python manage.py migrate
```

- Dodanie zadania do crontabu *(dzięki temu raspberry będzie sprawdzał co 2 minuty jaka jest wilgotność gleby oraz będzię ją podlewać jeśli będzie trzeba)*

```shell
python manage.py crontab add
```

- Uruchomienie servera *(dzięki wpisaniu na końcu komendy 0.0.0.0:8000 będzie można kożystać z serwera w sieci lokalnej)*
```shell
python manage.py runserver 0.0.0.0:8000
```



## Dokumentacja routingu (url)

### create_plant
Tworzenie rośliny.

URL:
[http://127.0.0.1:8000/plants/create_plant/](http://127.0.0.1:8000/plants/create_plant/)

Przykład requestu:

```json
{
    "plant_name": "Moja roślinka",
    "plant_specie": "Kaktus"
}

```


### get_info

Otrzymywanie informacji o roślinie oraz automatycznie aktualizuje informację na temat temperatury, wilgoci i ilości wody w doniczce.
Przyjmuje tylko metodę GET


URL:
[http://127.0.0.1:8000/plants/get_info/](http://127.0.0.1:8000/plants/{id}/get_info/)


### edit_plant

Endpoint do edycji rośliny (nazwa, rodzaj).
Przyjmuje tylko metodę PUT.

Przykładowe zapytanie:

```json
{
    "plant_name": "Moja roślinka",
    "plant_specie": "Kaktus"
}
```

Nie trzeba wprowadzać wszystkiego można np. tylko wpisać nazwę rośliny.

URL:
[http://127.0.0.1:8000/plants/edit_plant/](http://127.0.0.1:8000/plants/edit_plant/)

## Opis działania doniczki

### Funkcje doniczki wraz z aplikacją:

 - Automatycznie sprawdzanie wilgotności gleby oraz automatyczne podlewanie gdy zajdzie taka potrzeba
 
 - Monitorowanie temperatury, wilgotności powietrza.

 - Monitorowanie poziomu wody w doniczce oraz informowanie użytkownika o tym gdy trzeba będzie ją uzupełnić

 - Możliwość edytcji/zmiany nazwy oraz gatunku rośliny.
