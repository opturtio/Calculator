# Calculator

HUOM! Sovellus toimi vielä tiistaina 22.11 mutta tällä hetkellä on ongelmia tietokannan kanssa. 

Tämä on harjoitustyöni Helsingin yliopiston tietojenkäsittelytieteen ohjelmistotekniikka-kurssille.

Calculator on yksinkertainen laskin. Voit laskea sillä peruslaskutoimituksia. Ohjelma laajenee kurssin myötä.

## Dokumentaatio
- [Työaikakirjanpito](https://github.com/opturtio/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

Riippuvuuksien asennus:

```bash
poetry install
```

## Komentorivitoiminnot

#### Ohjelman suorittaminen
Suorittaa ohjelman komennolla:

```bash
poetry run invoke start
```

#### Ohjelman testaus
Suorittaa testit komennolla:

```bash
poetry run invoke test
```

#### Ohjelman testikattavuusraportti
Luo testikattavuus raportin:

```bash
poetry run invoke coverage-report
```

#### Pylint - koodin laatu
Tarkistaa koodin laadun:

```bash
poetry run invoke lint
```

#### Autopep8 - koodin formatointi
Koodin automaattinen formatointi:

```bash
poetry run invoke format
```