## Käyttöohje

Kloonaa repositorio koneellesi. Jos haluat ajaa testit, asenna Poetry. Ohjelma käynnistetään suorittamalla app.py-tiedosto.

Komento 1 luo automaattisesti satunnaisen salausavaimen. Ohjelma on säädetty luomaan 1024 bittiä pitkiä salausavaimia. Ohjelma tulostaa samalla kuinka montaa paritonta kokonaislukua piti kokeilla yhden alkuluvun löytämiseksi. Ohjelma luo enemmän kuin kaksi alkulukua silloin, kun niiden tulo ei ole halutut 1024 bittiä. Lisäksi ohjelma tulostaa, kuinka monta sekuntia eri vaiheet veivät (lukuun ottamatta vaihetta 4). 

Komennolla 2 voi määrittää oman salausavaimen. Tällöin täytyy antaa kaksi alkulukua. Luvun e voi halutessaan myös määritellä tai voi käyttää oletusarvoa 65537. Luvun e täytyy täyttää tietyt ominaisuudet, jotka voi katsoa Wikipediasta artikkelista RSA (cryptosystem) (https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation). Tämä komento on tarkoitettu lähinnä ohjelman testailuun. Se tarkastaa annettuja lukuja jossain määrin, mutta sitä ei ole testailtu kattavasti bugien varalta.

Komento 3 tulostaa salausavaimen eri osat. Niistä d on salainen avain ja n sekä e julkisia avaimia. Luvut p, q ja ln liittyvät avainten luontiin ja ovat turhia jälkeenpäin (eikä niitä saa julkistaa).

Komennolla 4 voi salata 128 merkkiä pitkiä viestejä. Viestissä voi käyttää ASCII-merkkejä, ääkkösiä ja joitain muita erikoisempia merkkejä. Kirjoita salattava viesti terminaaliin ja paina enter. Ohjelma tulostaa tämän jälkeen viestin salattuna kokonaislukuna.

Komento 5 purkaa salatun viestin. Salattu viesti pitää itse kopioida terminaalista ja sitten antaa purettavaksi viestiksi. Tämän jälkeen ohjelma tulostaa viestin purettuna.

Komento 6 tulostaa annetun viestin ja sen muunnoksen kokonaisluvuksi sekä salatuksi kokonaisluvuksi.

Komento q pysäyttää ohjelma.

Ohjelmalla ei ole tällä hetkellä mahdollista tallentaa salausavaimia tai viestejä. Tämä tarkoittaa, että jos on kirjoittanut viestin ja tämän jälkeen luot uudet salausavaimet, et enää voi purkaa viestiäsi ellet itse tallenna sitä sekä p:n, q:n ja e:n arvoja ja sitten määrittele niitä salausavaimen arvoiksi.
