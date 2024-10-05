## Käyttöohje

Ohjelman käyttämiseen tarvitsee vain app.py-tiedoston. Lataa se koneelle ja suorita. 

Komennolla 1 voi luoda automaattisesti satunnaiset salausavaimet. Ohjelma on säädetty luomaan noin 380 numeroa pitkiä salausavaimia ja sillä voi mennä muutama sekunti niiden luonnissa.

Komennolla 2 voi määrittää oman salausavaimen. Tällöin täytyy antaa kaksi alkulukua. Luvun e voi halutessaan myös määritellä tai voi käyttää oletusarvoa 65537. Luvun e täytyy täyttää tietyt ominaisuudet, jotka voi katsoa englanninkielisestä Wikipediasta artikkelista RSA (cryptosystem) otsikon Key generation alta (https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation). Tämä komento on tarkoitettu lähinnä ohjelman testailuun eikä se tarkista mitenkään annettuja lukuja.

Komennolla 3 voi tulostaa salausavaimen eri osat. Niistä d on salainen avain ja n sekä e julkisia avaimia. Luvut p, q ja ln liittyvät avainten luontiin ja ovat turhia jälkeenpäin.

Komennolla 4 voi salata noin 120 merkkiä pitkiä viestejä. Ohjelma tulostaa tämän jälkeen viestin salattuna.

Komennolla 5 voi purkaa salatun viestin. Salattu viesti pitää itse kopioida terminaalista viestin luonnin jälkeen ja sitten antaa purettavaksi viestiksi.

Komennolla 6 voi tulostaa annetun viestin ja sen muunnoksen kokonaisluvuksi ja salatuksi kokonaisluvuksi.

Ohjelmalla ei ole tällä hetkellä mahdollista tallentaa salausavaimia tai viestejä. Tämä tarkoittaa, että jos on kirjoittanut viestin ja tämän jälkeen luot uudet salausavaimet, et enää voi purkaa viestiäsi ellet itse tallenna sitä sekä p:n, q:n ja e:n arvoja ja sitten määrittele niitä salausavaimen arvoiksi.
