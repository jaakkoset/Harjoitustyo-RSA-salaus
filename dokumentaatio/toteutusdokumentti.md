# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman kaikki koodi sijaitsee src-kansiossa.

`app.py` sisältää luokan Program, jossa on käyttöliittymän tarvitsemat metodit sekä ohjelmasilmukka. Käyttäjän luomat salausavaimet ja viestit tallennetaan luokan Program muuttujiksi.

`create_key.py` sisältää metodit salausavainten luomiseen. Metodi create_key luo satunnaisen salausavaimen ja metodi create_own_key luo salausavaimen käyttäjän määrittämillä arvoilla.

`key.py` sisältää metodeja, joita tarvitaan salausavaimen luonnissa lukuun ottamatta alkulukujen luontia.

`encryption.py` sisältää metodit, joilla viestejä salataan ja salauksia puretaan sekä metodit, joilla merkkijonoja muutetaan kokonaisluvuiksi ja toisin päin.

`prime.py` sisältää metodit, joita tarvitaan alkulukujen luonnissa.

Kansiossa src/tests/ ovat kaikki testit. Kansiossa src/tests/data on testien käyttämiä teksitiedostoja.

## Algoritmien aikavaativuudet

- Miller-Rabin: O(k*log(n)^3). [2]

- Eukleideen algoritmi: O(log(min(a, b)). [13]

  - Pienin yhteinen monikerta lasketaan Eukleideen algoritmia hyödyntäen, joten sillä on sama aikavaativuus O(log(min(a, b)).

  - Myös Eukleideen laajennetulla algoritmilla on sama aikavaativuus. Lisäksi Modulaariaritmetiikan käänteisluku (modular multiplicative inverse) selvitetään Eukleideen laajennetulla algoritmilla, joten silläkin on sama aikavaativuus O(log(min(a, b)).

- Eratostheneen seula: O(n*log(log(n))). [14]

## Työn mahdolliset puutteet ja parannusehdotukset

Kun ohjelma luo salausavamia, se saattaa satunnaisesti luoda luvun ln, joka on jaollinen luvulla e. Tällöin metodi multiplicative_inverse (tiedostossa key.py) tuottaa virheen (ValueError("e and ln are not coprime")) ja ohjelma pysähtyy. Näin voi käydä sekä silloin, kun käyttäjä käyttää ohjelmaa että silloin, kun ajetaan testejä. Tämän todennäköisyys on hyvin pieni.

Jos käyttäjä yrittää salata merkkejä, joiden Unicode-arvo on yli 255, ohjelma tuottaa virheen ja pysähtyy.

Vertaisarvioinnissa testi TestEncryption.test_encryption_1024_big ei mennyt läpi. En tiedä mistä tämä johtui. Vertaisarvioija käytti Windowsia, joten kenties se vaikutti asiaan. Ongelmaa voi yrittää ratkaista poistamalla src/tests/data/text-128.txt -tiedostosta muutaman merkin.

## Laajojen kielimallien käyttö

Kysyin ChatGPT:ltä erilaisia tapoja muuntaa Pythonilla tekstiä kokonaisluvuksi. En lopulta hyödyntänyt mitään tästä työssäni.

## Lähteet

1. Wikipedia: RSA (cryptosystem).  
https://en.wikipedia.org/wiki/RSA_(cryptosystem) (Haettu 25.10.2024)

2. Wikipedia: Miller–Rabin primality test.  
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test (Haettu 27.9.2024)

1. Wikipedia: Sieve of Eratosthenes.  
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes (Haettu 27.9.2024)

1. Wikipedia: Euclidean algorithm.  
https://en.wikipedia.org/wiki/Euclidean_algorithm (Haettu 13.9.2024)

1. Wikipedia: Extended Euclidean algorithm.  
https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm (Haettu 21.9.2024)

1. Wikipedia: Mersenne prime.  
https://en.wikipedia.org/wiki/Mersenne_prime (Haettu 16.10.2024)

1. Wikipedia: RSA numbers.  
https://en.wikipedia.org/wiki/RSA_numbers (Haettu 23.10.2024)

1. PrimePages: First 1000 primes.  
https://prime-numbers.info/list/first-1000-primes (Haettu 8.10.2024)

1. PrimePages: First 100 primes.  
https://prime-numbers.info/list/first-100-primes (Haettu 8.10.2024)

1. PrimePages: List of Primes: 81001 - 82000.  
https://prime-numbers.info/list/primes-page-81 (Haettu 8.10.2024)

1. PrimePages: The first fifty million primes.  
https://t5k.org/lists/small/millions/ (Haettu 16.10.2024)

1. RSA-challenge numbers.  
https://www.ontko.com/pub/rayo/primes/rsa_fact.html (Haettu 23.10.2024)

1. Jitender Punia, 2024: Euclidean Algorithm | Basic and Extended.  
https://www.scaler.com/topics/data-structures/euclidean-algorithm-basic-and-extended/ (Haettu 26.10.2024)

1. GeeksforGeeks, 2023: How is the time complexity of Sieve of Eratosthenes is n*log(log(n))?  
https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/ (Haettu 26.10.2024)

1. dCode: Primality Test.  
https://www.dcode.fr/primality-test (Haettu 28.10.2024)

