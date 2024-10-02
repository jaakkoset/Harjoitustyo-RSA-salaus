# Aineopintojen harjoitustyö: algoritmit ja tekoäly

Repositorio Aineopintojen harjoitustyölle RSA-salauksesta.

## Dokumentaatio

[Määrittelydokumentti](./dokumentaatio/maarittelydokumentti.md)

[Viikkoraportti 1](./dokumentaatio/viikkoraportit/viikkoraportti_1.md)

[Viikkoraportti 2](./dokumentaatio/viikkoraportit/viikkoraportti_2.md)

[Viikkoraportti 3](./dokumentaatio/viikkoraportit/viikkoraportti_3.md)

[Viikkoraportti 4](./dokumentaatio/viikkoraportit/viikkoraportti_4.md)

## Käyttöohje

Ohjelman käyttämiseen tarvitsee vain app.py-tiedoston. Lataa se koneelle ja suorita. 

Komennolla 1 voi luoda automaattisesti satunnaiset salausavaimet. Ohjelma on säädetty luomaan noin 380 numeroa pitkiä salausavaimia ja sillä voi mennä muutama sekunti niiden luonnissa.

Komennolla 2 voi määrittää oman salausavaimen. Tällöin täytyy antaa kaksi alkulukua. Luvun e voi halutessaan myös määritellä tai sen voi luoda automaattisesti. Luvun e täytyy täyttää tietyt ominaisuudet, jotka voi katsoa englanninkielisestä Wikipediasta artikkelista RSA (cryptosystem) otsikon Key generation alta (https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation). Tämä komento on tarkoitettu ohjelman testailuun eikä se tarkista mitenkään annettuja lukuja.

Komennolla 3 voi tulostaa salausavaimen eri osat. Niistä d on salainen avain ja n sekä e julkisia avaimia. p, q ja ln syntyvät avainten luonnin yhteydessä ja ovat turhia jälkeenpäin.

Komennolla 4 voi salata noin 120 merkkiä pitkiä viestejä. Ohjelma tulostaa tämän jälkeen salatun viestin.

Komennolla 5 voi purkaa salatun viestin. Salattu viesti pitää kopioida terminaalista ja sitten liittää itse terminaaliin. 

Komennolla 6 voi tulostaa annetun viestin ja sen muunnoksen kokonaisluvuksi ja salatuksi kokonaisluvuksi.

Ohjelmalla ei ole tällä hetkellä mahdollista tallentaa salausavaimia tai viestejä. Tämä tarkoittaa, että jos on kirjoittanut viestin ja tämän jälkeen luot uudet salausavaimet, et enää voi purkaa viestiäsi ellet itse tallenna sitä sekä p:n, q:n ja e:n arvoja ja sitten määrittele niitä salausavaimen arvoiksi.
