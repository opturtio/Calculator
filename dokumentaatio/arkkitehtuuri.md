# Arkkitehtuurikuvaus

## Rakenne

Sovellus noudattaa referenssisovelluksen rakennetta:

```mermaid
graph TD;
    ui-->services;
    services-->entities;
    services-->repositories;
    repositories-->entities;
```

# Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

- Laskimen perusnäkymä
- Historia näkymä
- Laskimen tiedot-näkymä

Jokainen näkymä toteutettu omana luokkanaan. Laskimen perusnäkymä pysyy aina näkyvissä. Historia ja laskimen tiedot avautuvat uuteen ikkunaan. Näiden ikkunoiden sulkeminen ei vaikuta laskimen perusnäkymään. Sulkemalla laskimen perusnäkymän sulkeutuu kaikki ikkunat. Käyttöliittymä on pyritty eriyttämään sovelluslogiikasta.

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

## Sovelluslogiikka

#### Seuraaviin kaavioihin on kuvattu pääpiirtein luokkien väliset toiminnot

CalculatorView lähettää komennot CalculatorService MenubarService ja AboutService luokille, kun laskimen näppäimiä painetaan. Sovelluksen sovelluslogiikasta vastaavat luokat CalculatorService, MenubarService, AboutService sekä HistoryService. CalculatorService tallentaa laskut CalculationManager luokkaan. Laskutoimitukset tallennetaan pysyvästi CalculatorServicestä CalculatorRepositoryyn, jossa ne lisätään tietokantaan. CalculatorRepositoryssa muodostetaan olio Calculations, jossa on kaikki laskutoimitukset. Nämä laskutoimutukset tulostetaan HistoryViewissä. Jos HistoryViewissä laskutoimituksia muokataan nämä muokkaukset tapahtuvat HistoryServicessä ja tallentuvat sieltä CalculatorRepositoryyn. AboutService alustaa AboutViewin näkymän.


```mermaid
classDiagram
    CalculatorView --|> CalculatorService
    CalculatorView --|> MenubarService
    CalculatorView --|> AboutService

    CalculatorService <|--|> CalculationManager
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

### CalculatorService

Tämä kaavio kuvaa CalculatorServicen, CalculationManagerin ja CalculatorRepositoryn välistä toimintaa. CalculatorService vastaa laskimen sovelluslogiikasta. Se lähettää käskyt CalculationManagerille, joka hoitaa laskutoimitusten käsittelyn. CalculatorService kutsuu CalculationManageria, joka palauttaa laskutoimituksen, joka tulostetaan laskimen käyttöliittymään. Painamalla '='-nappia CalculatorService ratkaisee laskutoimituksen ja lähettää sen CalculatorRepositorylle, joka tallentaa laskutoimituksen ja vastauksen tietokantaan.

```mermaid
sequenceDiagram
    participant CalculatorService
    participant CalculationManager
    participant CalculatorRepository

    Note over CalculatorService, CalculationManager: Adding number
    CalculatorService->>CalculationManager: self._calculation.add_sign(str(number))
    CalculationManager->>CalculatorService: self._calculation.return_input()

    Note over CalculatorService, CalculationManager: Adding signs: + - * / . ( )
    CalculatorService->>CalculationManager: self._calculation.add_sign("sign")
    CalculationManager->>CalculatorService: self._calculation.return_input()

    Note over CalculatorService, CalculationManager: Deleting calculation
    CalculatorService->>CalculationManager: self._calculation.delete()

    Note over CalculatorService, CalculationManager: Deleting last
    CalculatorService->>CalculationManager: self._calculation.delete_last()

    Note over CalculatorService, CalculationManager: Creating answer
    CalculationManager->>CalculatorService: self._calculation.return_input()
    Note over CalculatorService: result = eval(self._calculation.return_input())
    CalculatorService->>CalculatorRepository: self._calculator_repository.add_calculation(f"{self._calculation.return_input()}={result}")
    CalculatorService->>CalculationManager: self._calculation.reset_points()
```

### MenubarService

Tämä kaavio kuvaa Menubarin toimintaa ja sitä miten se on liitoksissa muihin luokkiin.


```mermaid
sequenceDiagram
    participant MenubarService
    participant CalculatorService
    participant CalculatorRepository
    participant CalculationManager
    participant HistoryView
    participant Calculations

    rect rgb(191, 223, 0)
    Note over MenubarService: Create new
    MenubarService->>CalculatorRepository: self._calculator_repository.delete_calculations()
    MenubarService->>CalculatorService: self._calculator_service.reset()
    MenubarService->>CalculationManager: self._calculation.delete()
    end

    rect rgb(255, 255, 160)
    Note over MenubarService: Delete history
    MenubarService->>CalculatorRepository: self._calculator_repository.delete_calculations()
    end

    rect rgb(0, 223, 160)
    rect rgb(10, 150, 160)
    Note over MenubarService: Show history
    MenubarService->>HistoryView: self._history_view.open_history_window()
    MenubarService->>HistoryView: self._history_view.create_scrollbar()
    MenubarService->>HistoryView: self._history_view.create_history_list()
    HistoryView->>CalculatorRepository: self._calculation_repository.list_calculations()
    CalculatorRepository->>Calculations: return [Calculations(row["calculation"], row["timestamp"]) for row in rows]
    Calculations-->>HistoryView: choises created
    end

    rect rgb(110, 100, 160)
    MenubarService->>HistoryView: self._history_view.config_scrollbar()
    HistoryView->>HistoryService: self._history_service.replace_current_calculation_with_selected(self._listbox)
    HistoryService->>CalculationManager: self._calculation_manager.insert_calculation(selected)
    end

    rect rgb(110, 100, 250)
    MenubarService->>HistoryView: self._history_view.create_buttons()
    HistoryView->>HistoryService: self._history_service.delete_calculation_from_history_view(self._listbox)
    HistoryService->>CalculatorRepository: self._calculation_repository.delete_by_timestamp(selected)
    end
    end
```


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