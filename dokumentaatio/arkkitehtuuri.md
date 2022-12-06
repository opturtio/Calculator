# Arkkitehtuurikuvaus

## Rakenne

Sovellus koittaa noudattaa referenssisovellukset rakennetta:

```mermaid
graph TD;
    ui-->services;
    services-->entities;
    services-->repositories;
    repositories-->entities;
```

## Sovelluslogiikka

CalculatorView lähettää komennot CalculatorService ja MenubarService kun laskimen näppäimiä painetaan. Sovelluksen sovelluslogiikasta vastaavat luokat CalculatorServices ja MenubarService. CalculatorServices tallentaa laskut Calculation luokkaan. **HUOM!** Lisäsin lisää toiminnallisuuksia. Päivitän tämän tekstin myöhemmin ja teen luokkadiagrammista tarkemma.


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

    CalculatorRepository --|> HistoryView
    CalculatorRepository --|> Calculations
```

## Sekvenssikaavio

**HUOM!** Tämä on alku. Minun piti tehdä tätä koko tiistai mutta koska menetin 6-7 tuntia työaikaa minun piti korjata asioita, jotta saan julkastua toimivan version. Tämä kuvaa nappien toimintaa.

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

    CalculatorView->>CalculatorService: Service of all calculation buttons

    CalculatorView->>MenubarService: self._menubar.create_new()
    CalculatorView->>MenubarService: self._menubar.show_history()
    CalculatorView->>MenubarService: self._menubar.delete_history()
    CalculatorView->>AboutService: self._about_service.initialize_about_view()
```