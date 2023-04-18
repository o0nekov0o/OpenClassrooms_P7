liste_actions = [('action_1', 20, 5), ('action_2', 30, 10), ('action_3', 50, 15), ('action_4', 70, 20),
                 ('action_5', 60, 17), ('action_6', 80, 25), ('action_7', 22, 7), ('action_8', 26, 11),
                 ('action_9', 48, 13), ('action_10', 34, 27), ('action_11', 42, 17), ('action_12', 110, 9),
                 ('action_13', 38, 23), ('action_14', 14, 1), ('action_15', 18, 3), ('action_16', 8, 8),
                 ('action_17', 4, 12), ('action_18', 10, 14), ('action_29', 24, 21), ('action_20', 114, 18)]
actions_triees = sorted(liste_actions, key=lambda x: x[2])
actions_selectionnees = []
benefice_total = 0
cout_total = 0
plafond = 500


def methode_glouton(plafond, liste_actions, cout_total, benefice_total):
    actions_triees = sorted(liste_actions, key=lambda x: x[2])
    actions_selectionnees = []
    while actions_triees:
        action = actions_triees.pop()
        if action[1] + cout_total <= plafond:
            actions_selectionnees.append(action)
            benefice_total += action[2]
            cout_total += action[1]
    return sum([i[2] for i in actions_selectionnees]), actions_selectionnees


def force_brute(plafond, liste_actions, actions_selectionnees):
    if liste_actions:
        val1, lstVal1 = force_brute(plafond, liste_actions[1:], actions_selectionnees)
        val = liste_actions[0]
        if val[1] <= plafond:
            val2, lstVal2 = force_brute(plafond - val[1], liste_actions[1:], actions_selectionnees + [val])
            if val1 < val2:
                return val2, lstVal2
        return val1, lstVal1
    else:
        return sum([i[2] for i in actions_selectionnees]), actions_selectionnees


def force_brute_v2(plafond, liste_actions):
    matrice = [[0 for x in range(plafond + 1)] for x in range(len(liste_actions) + 1)]
    for i in range(1, len(liste_actions) + 1):
        for w in range(1, plafond + 1):
            if liste_actions[i-1][1] <= w:
                matrice[i][w] = max(liste_actions[i-1][2] + matrice[i-1][w-liste_actions[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]
    # Retrouver les éléments en fonction de la somme
    w = plafond
    n = len(liste_actions)
    elements_selection = []
    while w >= 0 and n >= 0:
        e = liste_actions[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]
        n -= 1
    return matrice[-1][-1], elements_selection


print('Algo glouton', methode_glouton(plafond, liste_actions, cout_total, benefice_total))
print('Algo force', force_brute(plafond, liste_actions, actions_selectionnees))
print('Algo dynamique', force_brute_v2(plafond, liste_actions))
