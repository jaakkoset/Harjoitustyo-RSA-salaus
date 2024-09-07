# Määrittelydokumnetti

Opinto-ohjelmani on tietojenkäsittelytieteen kandiohjelma ja projektin kieli on suomi. Käytän 
ohjelmointikielenä Pythonia ja pystyn vertaisarvioimaan sitä ja SQL:ää. 

Teen RSA-salaukseen perustuvan ohjelman, jolla voi salata ja purkaa tekstiä. Harjoitustyön ydin on
siis RSA-algoritmi. Sen voi jakaa neljään osaan. Ensimmäisessä osassa luodaan salausavaimet. Toisessa 
osassa julkinen salausavain jaetaan. Kolmannessa osassa viesti salataan ja neljännessä salaus 
puretaan. 

Salausavaimien luomista varten täytyy löytää suuria alkulukuja ja tässä käytetään Miller-Rabin 
algoritmia. Salausavaimen jakaminen ei nyt ole oleellista, koska ohjelmani toimii vain paikallisesti 
omille viesteilleni. Viestin salauksessa ja purkamisessa tarvitaan modulaarista potenssiin korotusta 
ja yritän toteuttaa tämän itse binääristä potenssiin korotusta käyttämällä ellei se osoittaudu jotenkin 
liian vaikeaksi.

Lähteenä olen käyttänyt Wikipediaa.

Wikipedia, RSA (cryptosystem): https://en.wikipedia.org/wiki/RSA_(cryptosystem)

Wikipedia, Modular exponentiation: https://en.wikipedia.org/wiki/Modular_exponentiation
