# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman kaikki koodi sijaitsee src-kansiossa.

`app.py` sisältää luokan Program, jossa on käyttöliittymän tarvitsemat metodit sekä ohjelmasilmukka. Käyttäjän luomat salausavaimet ja viestit tallennetaan luokan Program muuttujiksi.

`generator.py` sisältää kaksi metodia salausavainten luomiseen. Metodi create_key luo satunnaisen 1024 bittisen salausavaimen ja metodi create_own_key luo salausavaimen käyttäjän määrittämillä arvoilla.

`key.py` sisältää metodeja, joita tarvitaan salausavaimen luonnissa. Se sisältää kuitenkin myös metodin extended_euclidian_algorithm, jota käytetään vain muiden metodien testaamiseen.

`message.py` sisältää metodit, joilla viestejä salataan ja salauksia puretaan sekä metodit, joilla merkkijonoja muutetaan kokonaisluvuiksi ja toisin päin.

`prime.py` sisältää metodit, joilla luodaan alkulukuja. 

## Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)
## Suorituskyky- ja O-analyysivertailu (mikäli sopii työn aiheeseen)

## Työn mahdolliset puutteet ja parannusehdotukset

Kun ohjelma luo salausavamia, se saattaa satunnaisesti luoda luvun ln, joka on jaollinen luvulla e. Tällöin metodi multiplicative_inverse (tiedostossa key.py) nostaa virheen (ValueError("e and ln are not coprime")) ja ohjelma pysähtyy. Näin voi käydä sekä silloin, kun käyttäjä käyttää ohjelmaa että silloin, kun ajetaan testejä. Ongelma on erittäin harvinainen.

Jos käyttäjä yrittää salata merkkejä, joiden Unicode-arvo on yli 255, ohjelma nostaa virheen ja pysähtyy.

Vertaisarvioinnissa testi TestMessage.test_encryption_1024_big ei mennyt läpi. En tiedä mistä tämä johtui. Vertaisarvioija käytti Windowsia, joten kenties se vaikutti asiaan. Ongelmaa voi yrittää ratkaista poistamalla src/tests/data/text-128.txt -tiedostosta muutaman merkin.

## Laajojen kielimallien käyttö

Kysyin ChatGPT:ltä erilaisia tapoja muuntaa Pythonilla tekstiä kokonaisluvuksi. En lopulta hyödyntänyt mitään tästä työssäni.

## Lähteet

Wikipedia, RSA (cryptosystem).
https://en.wikipedia.org/wiki/RSA_(cryptosystem)

Wikipedia, Miller–Rabin primality test.
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

Wikipedia, Sieve of Eratosthenes.
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Wikipedia, Extended Euclidean algorithm.
https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

Wikipedia, Mersenne prime.
https://en.wikipedia.org/wiki/Mersenne_prime

Wikipedia, RSA numbers.
https://en.wikipedia.org/wiki/RSA_numbers

PrimePages, First 1000 primes.
https://prime-numbers.info/list/first-1000-primes

PrimePages, First 100 primes.
https://prime-numbers.info/list/first-100-primes

PrimePages, List of Primes: 81001 - 82000.
https://prime-numbers.info/list/primes-page-81

PrimePages, The first fifty million primes.
https://t5k.org/lists/small/millions/

RSA-challenge numbers.
https://www.ontko.com/pub/rayo/primes/rsa_fact.html
