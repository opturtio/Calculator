# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Laskimen sovelluslogiikasta vastaavaa `CalculatorService`-luokkaa testataan [TestCalculatorService](src/tests/../../../src/tests/services/calculator_services_test.py)-testiluokassa. Testiluokassa testataan pääsääntöisesti virheilmoitukset, mutta testit testaavat samalla itse luokan toimivuutta. Laskimen laskutoimituksista vastaavaa `CalculationManager`-luokkaa testataan [TestCalculationManager](src/../../src/tests/entities/calculation_manager_test.py)-testiluokassa. Nämä kaksi testiluokkaa testaavat samalla molempia luokkia ei pelkästään luokkaa itsessään.

### Repositorio-luokat

Repostorio-luokkaa `CalcultorRepository` testataan [TestCalculatorRepository](src/../../src/tests/repository/calculator_repository_test.py)-testiluokassa. Tiedostojen nimet on konfiguroitu _.env.test_-tiedostoon. Testattavana on myös `Calculations`-luokka, joka on yhteydessä `CalculatorRepository`-luokkaan. Luokan olio muodostetaan, joka kerta, kun tietokannasta haetaan tietoa. Sitä testaan [TestCalculatios](src/../../src/tests/entities/calculations_test.py)-testiluokassa.

### Testauskattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 96%

![](/dokumentaatio/images/coverage96.png)
Testaamatta jäivät _build.py_- ja _initialize\_database.py_-tiedostojen suorittaminen komentoriviltä. Nämä olisi myös voinut jättää testikattavuuden ulkopuolelle.
Testien ulkopuolelle jäivät myös luokat AboutService, HistoryService ja MenubarService. Nämä luokat olivat sidoksissa käyttöliittymän käynnistämiseen ja sisälsivät käyttöliittymän komponentteja. Kuitenkin haarautumiskattavuus oli silti 85% näiden luokkien ollessa mukana.

![](/dokumentaatio/images/coverage85.png)


![](/dokumentaatio/images/)

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](kayttoohje.md) kuvaamalla tavalla Linux-ympäristössä sekä vastuuopettajan macOS-käyttöjärjestelmässä.


### Toiminnallisuudet

Kaikki [vaatimusmäärittelyn](vaatimusmaarittely.md) ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi.

## Sovellukseen jääneet laatuongelmat

- Sovellusta ei ole tarkoitus käyttää muuten kuin käyttöliittymän näppäimiä käyttämällä. Sovellus ei lisää näppäimistöltä annettuja syötteitä laskutoimitukseen. Niiden lisäämistä ei ole kuitenkaan estetty. Tästä olisi ollut hyvä tehdä virheilmoitukset. Niiden lisääminen ei kuitenkaan kaada sovellusta tai aiheutta vääristymiä laskutoimituksissa, koska lasku palautuu normaaliin tilaan, kun jotain nappia painaa.

- Laskimesta luultavasti löytyy vielä joitain bugeja. On todella vaikea käydä yksin läpi kaikki skennaariot mitkä voisivat aiheuttaa virhetilanteen. Virheitä varten olisin halunnut luoda ErrorHandler-luokan.

- Testaus saattaa tuottaa virheen: FAILED src/tests/repository/calculator_repository_test.py::TestCalculatorRepository::test_deleting_by_timestamp - TypeError: unsupported operand type(s) for -: 'str' and 'str'. Tämä virhe johtuu siitä ettei testi ehditse luoda aikaleimaa tarpeeksi nopeasti. Aja testi uudestaan. Sen pitäisi seuraavalla kerralla mennä läpi. Testauksen aikana tämä virhe ilmestyi vain kerran.

