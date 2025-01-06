from functools import reduce
## Exo 1 

prix_euro = [50, 20, 35, 100, 80]

prix_dollars = map(lambda x: x*1.1, prix_euro)

print(list(prix_dollars))

## Exo 2

liste_age = [12, 25, 17, 18, 40, 15, 22]

trie_adulte = filter(lambda x: x>=18, liste_age)

print(list(trie_adulte))

## Exo 3

liste_vente = [120, 50, 30, 20, 90, 100]

total_liste = reduce(lambda x,y: x+y, liste_vente)

print(total_liste)

## Exo 4 

note = [12, 15, 9, 18, 6, 20, 14]

convertion_100 = map(lambda x: x/20*100, note)

note_50 = filter(lambda x: x>=50, convertion_100)

moyenne = reduce(lambda x,y: x+y, note_50) / len(note)

print(moyenne)


## Refaire tp du matin a faire avec map/filter/reduce/...

