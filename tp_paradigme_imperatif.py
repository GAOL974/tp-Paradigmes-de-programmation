taille = 0
notes = [] 
eleves = [] 
reussite = [] 
echec = [] 
bestnote = 0


def main() :
    print("Combien de note voulez vous saisir ?")
    taille = int(input("Notes :"))

    for i in range (taille) : 
        eleves.append(input(f"Nom de l'étudiant {i+1} :"))
        notes.append(int(input(f"Note de {eleves[i]} :")))

    calculer_moyenne()
    afficher_repartition()
    ##meilleure_note()


def calculer_moyenne() :
    somme = sum(notes)
    moyenne = somme / len(notes)
    print(f"\nLa moyenne de la classe est de {moyenne}")



def afficher_repartition() :

    print("\nÉtudiants ayant réussi :")
    for i in range(len(notes)):
        if notes[i] >= 10 :
            print(- eleves[i])

    print("Étudiants en échec :")
    for i in range(len(notes)):
        if notes[i] < 10 :
            print(- eleves[i])



def meilleure_note() :
    for i in range(taille):
        if notes[i] > bestnote : 
            bestnote = i

    print(f"\nL’étudiant ayant la meilleure note est {eleves[bestnote]} avec {notes[bestnote]}")
        


if __name__ == "__main__":
    main()