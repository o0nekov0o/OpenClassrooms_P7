liste_actions = [('action_1', 20, 5), ('action_2', 30, 10), ('action_3', 50, 15), ('action_4', 70, 20),
                 ('action_5', 60, 17), ('action_6', 80, 25), ('action_7', 22, 7), ('action_8', 26, 11),
                 ('action_9', 48, 13), ('action_10', 34, 27), ('action_11', 42, 17), ('action_12', 110, 9),
                 ('action_13', 38, 23), ('action_14', 14, 1), ('action_15', 18, 3), ('action_16', 8, 8),
                 ('action_17', 4, 12), ('action_18', 10, 14), ('action_19', 24, 21), ('action_20', 114, 18)]
actions_triees = sorted(liste_actions, key=lambda x: x[2])
actions_selectionnees = []
benefice_total = 0
cout_total = 0
plafond = 500


def methode_glouton(plafond, liste_actions, cout_total, benefice_total):
    # tri des elements selon leur valeur, avec la fonction lambda, donc pour chaque valeur x, on associe la valeur 2.
    actions_triees = sorted(liste_actions, key=lambda x: x[2])  # on associe donc le bénéfice dans ce cas.
    actions_selectionnees = []  # éléments qui seront séléctionnés pour maximiser les bénéfices.
    while actions_triees:  # tant qu'il reste des éléments à trier dans la liste.
        action = actions_triees.pop()  # je prends le dernier élément de la liste, avec la plus grande valeur.
        if action[1] + cout_total <= plafond:  # si cout dernier élément + cout de tous les élements <= limites.
            actions_selectionnees.append(action)  # alors on ajoute aux éléments qu'on sélectionne.
            benefice_total += action[2]  # on met à jour le benefice_total, en ajoutant le benefice de l'élement ajouté.
            cout_total += action[1]  # on met à jour le cout_total, en ajoutant le cout de l'élement ajouté.
    # on retourne la solution obtenue, avec bénéfice et éléments sélectionnés.
    return sum([i[2] for i in actions_selectionnees]), actions_selectionnees


print('Algo glouton', methode_glouton(plafond, liste_actions, cout_total, benefice_total))
