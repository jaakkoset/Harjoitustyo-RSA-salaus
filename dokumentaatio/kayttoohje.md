## Käyttöohje

Kloonaa repositorio koneellesi. Jos haluat ajaa testit, asenna Poetry. Ohjelma käynnistetään suorittamalla app.py-tiedosto.

Komennolla 1 voi luoda automaattisesti satunnaiset salausavaimet. Ohjelma on säädetty luomaan noin 380 numeroa pitkiä salausavaimia ja sillä voi mennä muutama sekunti niiden luonnissa.

Komennolla 2 voi määrittää oman salausavaimen. Tällöin täytyy antaa kaksi alkulukua. Luvun e voi halutessaan myös määritellä tai voi käyttää oletusarvoa 65537. Luvun e täytyy täyttää tietyt ominaisuudet, jotka voi katsoa englanninkielisestä Wikipediasta artikkelista RSA (cryptosystem) otsikon Key generation alta (https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation). Tämä komento on tarkoitettu lähinnä ohjelman testailuun. Se tarkastaa annettuja lukuja jossain määrin, mutta sitä ei ole testailtu kattavasti bugien varalta.

Komennolla 3 voi tulostaa salausavaimen eri osat. Niistä d on salainen avain ja n sekä e julkisia avaimia. Luvut p, q ja ln liittyvät avainten luontiin ja ovat turhia jälkeenpäin.

Komennolla 4 voi salata noin 128 merkkiä pitkiä viestejä. Viestissä voi käyttää UTF-8 merkkejä.  Kirjoita salattava viesti terminaaliin ja paina enter. Ohjelma tulostaa tämän jälkeen viestin salattuna kokonaislukuna.

Komennolla 5 voi purkaa salatun viestin. Salattu viesti pitää itse kopioida terminaalista viestin luonnin jälkeen ja sitten antaa purettavaksi viestiksi. Tämän jälkeen ohjelma tulostaa alkuperäisen viestin.

Komennolla 6 voi tulostaa annetun viestin sekä sen muunnoksen kokonaisluvuksi ja salatuksi kokonaisluvuksi.

Ohjelmalla ei ole tällä hetkellä mahdollista tallentaa salausavaimia tai viestejä. Tämä tarkoittaa, että jos on kirjoittanut viestin ja tämän jälkeen luot uudet salausavaimet, et enää voi purkaa viestiäsi ellet itse tallenna sitä sekä p:n, q:n ja e:n arvoja ja sitten määrittele niitä salausavaimen arvoiksi.
