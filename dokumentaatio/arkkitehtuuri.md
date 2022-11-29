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

CalculatorView lähettää komennot CalculatorServices ja MenubarService kun laskimen näppäimiä painetaan. Sovelluksen sovelluslogiikasta vastaavat luokat CalculatorServices ja MenubarService. CalculatorServices tallentaa laskut Calculation luokkaan


```mermaid
classDiagram
    CalculatorView --|> CalculatorServices
    CalculatorView --|> MenubarService
    CalculatorServices --|> Calculation
```