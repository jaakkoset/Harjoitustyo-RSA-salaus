# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman kaikki koodi sijaitsee src-kansiossa.

`app.py` sisältää luokan Program, jossa on käyttöliittymän tarvitsemat metodit sekä ohjelmasilmukka. Käyttäjän luomat salausavaimet ja viestit tallennetaan luokan Program muuttujiksi.

`create_key.py` sisältää metodit salausavainten luomiseen. Metodi create_key luo satunnaisen salausavaimen ja metodi create_own_key luo salausavaimen käyttäjän määrittämillä arvoilla.

`key.py` sisältää metodeja, joita tarvitaan salausavaimen luonnissa. Se sisältää kuitenkin myös metodin extended_euclidian_algorithm, jota käytetään vain muiden metodien testaamiseen.

`encryption.py` sisältää metodit, joilla viestejä salataan ja salauksia puretaan sekä metodit, joilla merkkijonoja muutetaan kokonaisluvuiksi ja toisin päin.

`prime.py` sisältää metodit, joilla luodaan alkulukuja. 

## Algoritmien aikavaativuudet



## Työn mahdolliset puutteet ja parannusehdotukset

Kun ohjelma luo salausavamia, se saattaa satunnaisesti luoda luvun ln, joka on jaollinen luvulla e. Tällöin metodi multiplicative_inverse (tiedostossa key.py) nostaa virheen (ValueError("e and ln are not coprime")) ja ohjelma pysähtyy. Näin voi käydä sekä silloin, kun käyttäjä käyttää ohjelmaa että silloin, kun ajetaan testejä. Ongelma on erittäin harvinainen.

Jos käyttäjä yrittää salata merkkejä, joiden Unicode-arvo on yli 255, ohjelma nostaa virheen ja pysähtyy.

Vertaisarvioinnissa testi TestMessage.test_encryption_1024_big ei mennyt läpi. En tiedä mistä tämä johtui. Vertaisarvioija käytti Windowsia, joten kenties se vaikutti asiaan. Ongelmaa voi yrittää ratkaista poistamalla src/tests/data/text-128.txt -tiedostosta muutaman merkin.

## Laajojen kielimallien käyttö

Kysyin ChatGPT:ltä erilaisia tapoja muuntaa Pythonilla tekstiä kokonaisluvuksi. En lopulta hyödyntänyt mitään tästä työssäni.

## Lähteet

Wikipedia: RSA (cryptosystem).  
https://en.wikipedia.org/wiki/RSA_(cryptosystem) (Haettu 25.10.2024)

Wikipedia: Miller–Rabin primality test.  
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test (Haettu 27.9.2024)

Wikipedia: Sieve of Eratosthenes.  
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes (Haettu 27.9.2024)

Wikipedia: Euclidean algorithm.  
https://en.wikipedia.org/wiki/Euclidean_algorithm (Haettu 13.9.2024)

Wikipedia: Extended Euclidean algorithm.  
https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm (Haettu 21.9.2024)

Wikipedia: Mersenne prime.  
https://en.wikipedia.org/wiki/Mersenne_prime (Haettu 16.10.2024)

Wikipedia: RSA numbers.  
https://en.wikipedia.org/wiki/RSA_numbers (Haettu 23.10.2024)

PrimePages: First 1000 primes.  
https://prime-numbers.info/list/first-1000-primes (Haettu 8.10.2024)

PrimePages: First 100 primes.  
https://prime-numbers.info/list/first-100-primes (Haettu 8.10.2024)

PrimePages: List of Primes: 81001 - 82000.  
https://prime-numbers.info/list/primes-page-81 (Haettu 8.10.2024)

PrimePages: The first fifty million primes.  
https://t5k.org/lists/small/millions/ (Haettu 16.10.2024)

RSA-challenge numbers.  
https://www.ontko.com/pub/rayo/primes/rsa_fact.html (Haettu 23.10.2024)

João Pedro Schmitt 2018: Cryptography algorithm RSA — Rivest-Shamir-Adleman.  
https://joaoschmitt.wordpress.com/2018/09/17/cryptography-algorithm-rsa/ (Haettu 26.10.2024)

