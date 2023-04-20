liste_actions = [('action_1', 20, 5), ('action_2', 30, 10), ('action_3', 50, 15), ('action_4', 70, 20),
                 ('action_5', 60, 17), ('action_6', 80, 25), ('action_7', 22, 7), ('action_8', 26, 11),
                 ('action_9', 48, 13), ('action_10', 34, 27), ('action_11', 42, 17), ('action_12', 110, 9),
                 ('action_13', 38, 23), ('action_14', 14, 1), ('action_15', 18, 3), ('action_16', 8, 8),
                 ('action_17', 4, 12), ('action_18', 10, 14), ('action_29', 24, 21), ('action_20', 114, 18)]
actions_selectionnees = []
benefice_total = 0
cout_total = 0
plafond = 500


def force_brute(plafond, liste_actions, actions_selectionnees):
    if liste_actions:  # s'il reste des éléments à traiter, appel récursif.
        # ignorer élément courant, appel fonction sans 1èr élément, sans rien ajouter.
        val1, lstVal1 = force_brute(plafond, liste_actions[1:], actions_selectionnees)
        val = liste_actions[0]  # selectionner 1er élément.
        if val[1] <= plafond:  # si on l'ajoute, on respecte les limitations.
            # nouvel appel récursif, on réduit le plafond du prix de l'élément ajouté,
            # renvoi liste d'éléments sans 1er, puis on sélectionne 1er élément ajouté.
            val2, lstVal2 = force_brute(plafond - val[1], liste_actions[1:], actions_selectionnees + [val])
            # on compare les 2 solutions, quelle est la plus rentable ?
            if val1 < val2:  # mieux vaut-il ajouter l'élément ou non ?
                return val2, lstVal2  # on ramène la meilleure solution révursivement.
        return val1, lstVal1  # on ramène la meilleure solution révursivement.
    # si plus d'éléments à traiter, on renvoie la liste des éléments,
    else:  # avec la meilleure solution, affichage bénéfice et éléments choisis.
        return sum([i[2] for i in actions_selectionnees]), actions_selectionnees


print('Algo force', force_brute(plafond, liste_actions, actions_selectionnees))
