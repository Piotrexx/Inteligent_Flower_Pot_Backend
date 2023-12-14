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

Części jakich użyliśmy:

 - [raspberry Pi zero W](https://botland.com.pl/moduly-i-zestawy-raspberry-pi-zero/20347-raspberry-pi-zero-2-w-512mb-ram-wifi-bt-42-5904422380700.html)
 - [Pompa wodna 6V](https://botland.com.pl/pompy/14164-pompa-wodna-6v-5904422342401.html)
 - [STEMMA - czujnik wilgotności gleby - Adafuit 4026](https://botland.com.pl/czujniki-wilgotnosci/14431-stemma-czujnik-wilgotnosci-gleby-adafuit-4026-5904422307301.html)
 - [Moduł przekaźnika 1 kanał z optoizolacją - styki 10A/250VAC cewka 5V](https://botland.com.pl/przekazniki-przekazniki-arduino/1997-modul-przekaznika-1-kanal-z-optoizolacja-styki-10a-250vac-cewka-5v-5904422359096.html)
 - [Czujnik poziomu cieczy z pływakiem - kontaktron](https://botland.com.pl/czujniki-poziomu-cieczy/7244-czujnik-poziomu-cieczy-z-plywakiem-kontaktron-5904422310035.html)

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

### update_temp

Endpoint, który automatycznie sie aktualizuje, nie będzie trzeba go używać ale warto o nim wspomnieć.
Przyjmuje tylko metodę **PUT**

URL:
[http://127.0.0.1:8000/plants/update_temp/](http://127.0.0.1:8000/plants/update_temp/)

Przykład requesta:

```json
{
    "temperature":25.0,
    "air_humidity":57
}
```

### get_info

Otrzymywanie informacji o roślinie.
Przyjmuje tylko metodę GET

URL:
[http://127.0.0.1:8000/plants/get_info/](http://127.0.0.1:8000/plants/get_info/)