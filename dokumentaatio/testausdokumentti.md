# Testausdokumentti

Ei riitä todeta, että testaus on tehty käyttäen automaattisia yksikkötestejä, vaan tarvitaan konkreettista tietoa testeistä, kuten:

 * Testattu, että tekoäly osaa tehdä oikeat siirrot tilanteessa, jossa on varma 4 siirron voitto. Todettu, että siirroille palautuu voittoarvo 100000.
 
 * Testattu 10 kertaan satunnaisesti valituilla lähtö- ja maalipisteillä, että JPS löytää saman pituisen reitin kuin Dijkstran algoritmi.
 
 * Kummallakin algoritmilla on pakattu 8 MB tekstitiedosto, purettu se ja tarkastettu, että tuloksena on täsmälleen alkuperäinen tiedosto.


## Yksikkötestauksen kattavuusraportti.

Name                Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------
src/create_key.py      79      9     28      5    87%   110, 124-125, 127-128, 142-143, 147-151
src/encryption.py      32      0     12      0   100%
src/key.py             46      0     10      0   100%
src/prime.py           65      0     36      0   100%
---------------------------------------------------------------
TOTAL                 222      9     86      5    95%


## Mitä on testattu, miten tämä tehtiin?
## Minkälaisilla syötteillä testaus tehtiin?
## Miten testit voidaan toistaa?
## Ohjelman toiminnan mahdollisen empiirisen testauksen tulosten esittäminen graafisessa muodossa. (Mikäli sopii aiheeseen)


