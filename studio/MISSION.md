# Missione: le basi dell'analisi HRTEM per costruire l'app di indicizzazione

## Perché
Devo costruire, insieme a Davide, un'applicazione che trasforma un'immagine al microscopio elettronico (HRTEM) in dati cristallografici: dalla FFT dell'immagine alle distanze tra piani, agli angoli, fino all'asse di zona e agli indici hkl. Deve farlo senza dipendere da programmi esterni. Per progettarla devo capire cosa calcola ogni passaggio e perché.

## Quando potrò dire "ci sono"
- Spiego a parole mie cos'è un cristallo e cosa vuol dire che una sostanza cristallizza.
- Dico cosa si vede in un'immagine HRTEM e perché si usa.
- Spiego cosa fa la FFT su un'immagine HRTEM: perché le "macchie" corrispondono ai piani del cristallo.
- Spiego a grandi linee cosa vuol dire "indicizzare": d-spacing, angoli, indici hkl, asse di zona.
- So cosa fanno i programmi che esistono già (per esempio CrysTBox) e dove la nostra app può fare meglio.
- Faccio a Davide le domande giuste per decidere come procedere.

## Cosa mi limita
- Formazione da informatico; chimica solo di base (primi due anni). Nessuna base di cristallografia o microscopia.
- Imparo per costruire un software: mi serve capire l'algoritmo più che la teoria fine a sé stessa.

## Lasciato fuori per ora
- Matematica e formule in dettaglio (diffrazione, trasformata di Fourier "a mano"): prima i concetti. Torneranno quando si scrive il codice dell'app.
- Il codice Python per l'analisi dei dati.
