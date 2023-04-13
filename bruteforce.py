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


print('Algo force', force_brute(plafond, liste_actions, actions_selectionnees))
