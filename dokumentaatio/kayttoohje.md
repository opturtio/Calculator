# Käyttöohje

Lataa projektin viimeisin release lähdekoodi valitsemalla Assests-osion alta _Source code_.

## Konfigurointi

Tallennukseen käytettävien tiedostojen nimiä voi halutessaan konfiguroida käynnistyshakemistossa _.env_-tiedostossa. Tiedostot luodaan automaattisesti _data_-hakemistoon, jos niitä ei siellä vielä ole. Tiedoston muoto on seuraava:

```
DATABASE_FILENAME=database.sqlite
```

&nbsp;

## Ohjelman käynnistäminen

Ennen kuin käynnistät ohjelman, sinun tulee asentaa riippuvuudet komennolla:

```bash
poetry install
```

Tämän jälkeen alusta tietokanta komennolla:

```bash
poetry run invoke build
```

Lopuksi käynnistää sovellus komennolla:

```
poetry run invoke start
```

&nbsp;

## Laskimen perusnäkymä

Laskimen käyttöliittymä on englanniksi.

![](./images/calculator2.png)

Voit suorittaa perus-laskutoimituksia näppäilemällä nappeja. Jos teet väärän laskutoimituksen ohjelma ilmoittaa siitä.

Esimerkki virheilmoituksesta:

![](./images/error_example.png)

## Uuden laskimen luonti ja poistuminen laskimesta

![](./images/file.png)

## Historia näkymään siirtyminen ja historian poistaminen

![](./images/history.png)

## Help näkymä

![](./images/help.png)

## Historia näkymä

![](./images/history_view.png)

## About näkymä

![](./images/about_view.png)