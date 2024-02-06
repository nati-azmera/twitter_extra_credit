# Extra Credit

This project looks at tweets sent in 2020 which were related to the murder of George Floyd and the subsequent #blm movement. In particular, we will look at from where these tweets were being sent from, what language and how people were using different variations of the hashtag.

# Results

First graph:

```
$ python3 ./src/visualize.py --input_path=reduced.country --key='#blm'
```

Resulting graph:

![#blm by country](blm_country.png)

Second graph:

```
$ python3 ./src/visualize.py --input_path=reduced.lang --key='#blm'
```

Resulting graph:

![#blm by lang](blm_lang.png)

Third graph:

```
$ python3 ./src/alternative_reduce.py --keys '#police_brutality' '#blm' '#george_floyd' '#black_lives_matter' '#DefundPolice'
```

Resulting graph:

![#blm vs #policebrutatlity vs #georgefloyd vs #blacklivesmatter vs #defundpolice](police_brutality_blm_george_floyd_black_lives_matter_DefundPolice.png)
