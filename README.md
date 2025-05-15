# Årsoppgave

## Brukerveiledning

Velkommen til spillet! Følg denne veiledningen for å komme i gang:

### Installasjon
1. Last ned spillet fra GitHub-repositoriet.
2. Pakk ut filene til en ønsket mappe på datamaskinen din.
3. Sørg for at du har python 3.12.5 og pygame-ce installert. Vet ikke hvordan? Scroll ned til "Installasjon av python og pygame"

### Oppstart
1. Åpne mappen der spillet er installert.
2. Kjør hovedfilen for spillet `main.py`.
3. Følg instruksjonene som vises på skjermen.

### Spilleregler
- Målet med spillet er å overleve og ødelegge så mange meteorer så mulig.
- Bruk piltastene til navigere og mellomrom tasten til å skyte lasere.
- Unngå meteorene og overlev så lenge så mulig for å oppnå høy poengsum.


Lykke til og ha det gøy!



#### Installasjon av Python og Pygame

1. **Last ned og installer Python**  
    - Gå til den offisielle Python-nettsiden: [https://www.python.org/downloads/](https://www.python.org/downloads/).
    - Velg versjon 3.12.5 og last den ned for ditt operativsystem.
    - Under installasjonen, sørg for å krysse av for "Add Python to PATH".

2. **Installer Pygame**  
    - Åpne en terminal eller kommandolinje.
    - Skriv inn følgende kommando for å installere Pygame:  
      ```bash
      pip install pygame-ce
      ```
    - Vent til installasjonen er fullført.

3. **Bekreft installasjonen**  
    - Skriv inn følgende kommandoer for å sjekke at både Python og Pygame er riktig installert:  
      ```bash
      python --version
      pip show pygame-ce
      ```
    - Du skal se Python-versjonen og informasjon om Pygame hvis alt er korrekt installert.

Nå er du klar til å kjøre spillet!


### FAQ

#### 1. Hva gjør jeg hvis spillet ikke starter?
- Sjekk at du har installert riktig versjon av Python (3.12.5) og Pygame-CE.
- Sørg for at alle spillfilene er pakket ut og at du kjører `main.py` fra riktig mappe.
- Åpne en terminal og kjør `python main.py` for å se eventuelle feilmeldinger.

#### 2. Kan jeg spille spillet på Mac eller Linux?
- Ja, spillet er kompatibelt med både Mac og Linux, så lenge du har Python og Pygame-CE installert.

#### 3. Hvordan oppdaterer jeg spillet?
- Last ned den nyeste versjonen fra GitHub-repositoriet.
- Erstatt de gamle filene med de nye, men behold eventuelle lagringsfiler hvis spillet støtter det.

#### 4. Hva gjør jeg hvis jeg får en feilmelding under installasjonen av Pygame?
- Sørg for at du har en fungerende internettforbindelse.
- Prøv å oppdatere pip ved å kjøre:
    ```bash
    python -m pip install --upgrade pip
    ```
- Deretter, prøv å installere Pygame-CE på nytt.

#### 5. Kan jeg endre kontrollene i spillet?
- For øyeblikket er kontrollene faste (piltaster for navigasjon og mellomrom for å skyte). Fremtidige oppdateringer kan inkludere muligheten til å tilpasse kontrollene.

#### 6. Hvordan rapporterer jeg feil eller foreslår forbedringer?
- Gå til GitHub-repositoriet og opprett en "Issue" med en detaljert beskrivelse av problemet eller forslaget ditt.



