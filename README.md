# Calculator

Tämä on harjoitustyöni Helsingin yliopiston tietojenkäsittelytieteen ohjelmistotekniikka-kurssille.

Calculator on yksinkertainen laskin. Voit laskea sillä peruslaskutoimituksia.

## Dokumentaatio
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testausdokumentti.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

Riippuvuuksien asennus:

```bash
poetry install
```

Käynnistä virtuaaliympäristö:

```bash
poetry shell
```

Alusta tietokanta:

```bash
poetry run invoke build
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
