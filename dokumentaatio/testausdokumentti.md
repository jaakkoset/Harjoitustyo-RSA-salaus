# Testausdokumentti

## Yksikkötestauksen kattavuusraportti.

<pre>
Name                Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------
src/create_key.py      79      9     28      5    87%   110, 124-125, 127-128, 142-143, 147-151
src/encryption.py      32      0     12      0   100%
src/key.py             46      0     10      0   100%
src/prime.py           65      0     36      0   100%
---------------------------------------------------------------
TOTAL                 222      9     86      5    95%
</pre>


## Testaus

Kaikkia ohjelman metodeja on testattu jotenkin, paitsi käyttöliittymää eli app.py tiedostoa, jota ei ole testattu mitenkään. Miller-Rabin algoritmia on testattu eniten. Muita on testattu ainakin muutamalla arvolla ja aina on pyritty saamaan mukaan joku sen kokoinen arvo, jonka algoritmi kohtaisi ohjelman käytössä. Ainoat osat, joiden testikattavuus ei ole 100 % liittyvät create_own_key metodiin, jolla voi luoda salausavaimia omilla arvoilla. Se tarkastaa saamansa syötteet monin tavoin ja kaikkia näitä tarkastuksia ei testata, koska metodi ei ole työn kannalta tärkeä.

### Moduuli prime.py

Monet testeistä käyttävät alkulukulistoja, jotka ovat kansiossa src/tests/data.

Miller-Rabin algoritmilla on seitsemän testiä miller-rabin_test-py tiedostossa. Testeillä testataan Miller-Rabinin kykyä tunnistaa sekä alkuluvut että yhdistetyt luvut oikein. Kaksi testiä testaa algoritmia luvuilla 4 - 541 ja luvuilla 961 748 941 - 961 766 053 (800 alkulukua ja noin 17 112 muuta lukua). Kolmas testi testaa algoritmia yhdeksällä 60 - 2203 bittiä pitkillä Mersennen alkuluvulla. Neljäs testi kertoo kaikki yhdeksän Mersennen alkulukua parittain ja varmistaa, että algoritmi tunnistaa ne yhdistetyiksi luvuiksi. Viides testi testaa algoritmia 45:llä 100 - 617 numeroa pitkällä yhdistetyllä luvulla (tiedostossa rsa-challenge.txt). Nämä luvut ovat otettu RSA securityn järjestämästä RSA Factoring Challenge -kilpailusta, jossa luvut muodostettiin kertomalla kaksi alkulukua keskenään. Kuudes testi testaa algoritmia 46:lla 50 - 125 numeroa pitkällä alkuluvulla. Nämä luvut ovat RSA Factoring Challenge -kilpailun tunnetut ratkaisut. Seitsemäs testi kokeilee, että algoritmi tunnistaa kaksi peräkkäistä 512 bittistä alkulukua ja niiden välissä olevat 396 yhdistettyä lukua oikein. Käytin peräkkäisten alkulukujen arpomiseen omaa Miller-Rabin algoritmiani ja tarkistin netistä löytyvällä työkalulla ([dCode](https://www.dcode.fr/primality-test)), että ne ovat alkulukuja. Tämän testin huono puoli on, että niiden välissä olevia yhdistettyjä lukuja ei ole testattu.

Metodi factor_twos palauttaa jokaisen luonnollisen luvun muodossa n = 2^s * d. Sitä testataan kahdella pienellä ja kahdella suurella luvulla, jotka on itse keksitty ja joista puolet on parittomia. 

Metodi trial_division selvittää pienillä luvuilla onko kyseessä alkuluku. Sitä testataan arvoilla 2-541 ja 1034233 - 1048129. Tätä metodia käytetään vain metodin random_prime testaamiseen.

Metodi random_prime palauttaa satunnaisen alkuluvun käyttämällä Miller-Rabin algoritmia. Sitä testataan 30 bittiä pitkillä luvuilla, jotka todennetaan alkuluvuiksi metodilla trial_division. Lisäksi luodaan yksi 512 bittinen luku, joka varmistetaan Miller-Rabinilla.

Metodia eratosthenes_sieve testataan ensimmäisellä tuhannella alkuluvulla. 

### Moduuli create_key.py

Metodi create_key luo salausavaimet. Sitä testataan luomalla yksi satunnainen 1024 bittinen salausavain ja tarkistamalla, että kaikki salausavaimen osat toteuttavat halutut ominaisuudet.

Metodia create_own_key kokeillaan yhdellä pienellä ja yhdellä satunnaisella isolla syötteellä. Lisäksi testataan joitain tapauksia, joissa metodi ei hyväksy väärän muotoista syötettä.

### Moduuli encryption.py

Metodit text_to_integer ja integer_to_text muuttavat tekstiä kokonaisluvuiksi ja toisin päin. Niitä testataan kaikilla ascii-merkeillä sekä ääkkösillä ja eri mittaisilla syötteillä. Lisäksi testataan, että ne tuottavat virheen kielletyillä merkeillä. On myös merkkejä, jotka metodit hyväksyvät, mutta joita ei testata.

Metodit encrypt ja decrypt tekevät vain modulaarista potenssiin korotusta, mutta niitäkin testataan yhdellä pienellä esimerkillä.

### Moduuli key.py

Metodia least_common_multiple testataan kuudella pienellä ja yhdellä suurella arvolla, jotka on käsin tarkistettu.

Metodia euclidean_algorithm testataan kuudella pienellä käsin lasketulla syötteellä. Lisäksi kolmen käsin arvotun noin 512 bittisen syötteen tuloksia verrataan metodiin extended_euclidean_algorithm.

Metodia extended_euclidean_algorithm testataan kahdella pienellä käsin lasketulla syötteellä. Lisäksi neljällä suurella syötteellä kokeillaan, että vastaus toteuttaa halutun yhtälön. Käytetään vain metodin euclidean_algorithm testaamiseen.

Metodille multiplicative_inverse annetaan oikean muotoisia pieniä ja suuria syötteitä ja todennetaan, että vastauksella on halutut ominaisuudet. Lisäksi sille annetaan pieniä ja suuria syötteitä, jotka ovat väärän muotoisia ja tarkistetaan, että metodi tuottaa virheen. 

### Salauksen testaaminen

Tiedostossa encrypt_derypt_test.py varmistetaan, että ohjelman metodeilla voi salata tekstiä ja purkaa salauksen siten, että lopputulos on sama kuin alkuperäinen teksti. 1024 bittisillä avaimilla testataan yhden, 50 ja 128 merkin pituisia tekstejä. 2048 bittisellä avaimella testataan 256 merkkistä tekstiä.

## Testien toistaminen

Testit on tehty Poetryllä. Ohjelman juurikansiossa annetaan komento

`poetry install`

Virtuaaliympäristöön siirrytään komennolla 

`poetry shell`

ja testit voi nyt ajaa komennolla

`pytest src`
