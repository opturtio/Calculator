# Arkkitehtuurikuvaus

## Rakenne

Sovellus pyrkii noudattamaan referenssisovelluksen rakennetta:

```mermaid
graph TD;
    ui-->services;
    services-->entities;
    services-->repositories;
    repositories-->entities;
```


## Sovelluslogiikka

CalculatorView lähettää komennot CalculatorService MenubarService ja AboutService luokille kun laskimen näppäimiä painetaan. Sovelluksen sovelluslogiikasta vastaavat luokat CalculatorServices, MenubarService, AboutService sekä HistoryService. CalculatorServices tallentaa laskut CalculationManager luokkaan.


```mermaid
classDiagram
    CalculatorView --|> CalculatorService
    CalculatorView --|> MenubarService
    CalculatorView --|> AboutService

    CalculatorService --|> CalculationManager
    CalculatorService --|> CalculatorRepository

    AboutService --|> AboutView

    MenubarService --|> HistoryView
    MenubarService --|> CalculatorRepository
    MenubarService --|> CalculatorService
    MenubarService --|> CalculationManager

    CalculatorRepository --|> Calculations

    Calculations --|> HistoryView

    HistoryView --|> HistoryService
    HistoryService --|> CalculatorRepository
```


## Päätoiminnallisuudet

### Tämä kaavio kuvaa menubarin ja nappien alustamista ja toiminnallisuutta.


```mermaid
sequenceDiagram
    participant UI
    participant CalculatorView
    participant CalculatorService
    participant MenubarService
    participant CalculatorRepository
    participant AboutService

    UI->>CalculatorView: CalculatorView(root).pack()

    CalculatorView->>CalculatorService: CalculatorService(entry)
    CalculatorView->>MenubarService: MenubarService(entry)

    Note over CalculatorView: self._initialize_buttons()
    Note over CalculatorView: self._initialize_menu()

    CalculatorView->>CalculatorService: Service of all calculation buttons[1]

    CalculatorView->>MenubarService: self._menubar.create_new()
    CalculatorView->>MenubarService: self._menubar.show_history()
    CalculatorView->>MenubarService: self._menubar.delete_history()
    CalculatorView->>AboutService: self._about_service.initialize_about_view()
```

[1] _Service of all calculation buttons_ käsittää kaikki laskimen napit.


## Tietojen pysyväistallennus

Pakkauksen _repositories_ luokka `CalculatorRepository` hoitaa laskutoimitusten tallentamisen. Laskutoimitukset tallennetaan SQLite3-tietokantaan. Luokka noudattaa repository-suunnittelumallia.

Sovelluksen juuressa oleva [.env](../.env) -konfiguraatiotiedosto määrittelee tiedostojen nimet.

Tietokannassa on taulu `Calculations`, johon tallennetaan aikaleima ja laskutoimitus, kun käyttäjä painaa '='-merkkiä.

Tietokanta alustetaan tiedostossa [initialize_database.py](../src/initialize_database.py)


## Ohjelman rakenteeseen jääneet heikkoudet


### CalculatorService-luokka

[CalculatorServices](../src/services/calculator_service.py) -luokka pitää sisällään nappien toiminnallisuuden ja virheiden käsittelyn. Tarkoitukseni oli jakaa tämä luokka kahteen osaan, jossa virheiden käsittely eriytetään omaksi luokaksi. Luokka on mielestäni liian suuri.

### Luokkien koot

Sovellusta kehittäessä taitoni myös kehittyivät. Kävin samaan aikaan ohjelmistotuotanto-kurssia ja lisäsin siellä oppimaani ohjelmaan. Aloin eriyttämään toiminnallisuuksia omiksi luokikseen. Jälkikäteen tämä oli haastavaa riippuvuuksien takia. Kurssin alussa olin toteuttanut CalculatorService-luokan ilman entryn injektoimista, mutta lisäsin sen luokan riippuvuudeksi myöhemmin. Tämä tuotti paljon ongelmia myöhemmässä vaihteessa sovellusta. Koitin rakentaa luokkia:
 - **ErrorHandler**, joka huolehtii virheistä
 - **EntryHandler**, joka hoitaa laskimen näytölle tulevasta tulosteesta
 - **CalculationChecker**, joka huolehtii ettei laskuun lisätä väärää tietoa esim. kahta pistettä numerosarjaan

Mutta riippuvuudet tekivät luokkien tekemisestä todella hankalaa ja tajusin, ettei aikani riitä saamaan ohjelmaa loppuun jos panostan niihin enemmän aikaa. Sen takia osa luokista sisältää enemmän metodeita kuin toiset.

### **Eval**-komennon käyttäminen

Evalin käyttäminen laskutoimitusten ratkaisemiseen ei ole hyvä käytänne. Olisin halunnut rakentaa, jonkinlaisen algoritmin ratkaisemaan laskut, mutta ongelman tuotti sulkeet. En keksinyt siihen vastausta, enkä halunnut käyttää siihen liikaa aikaa, joten jätin sen viimeiseksi asiaksi tehtävälistalla.