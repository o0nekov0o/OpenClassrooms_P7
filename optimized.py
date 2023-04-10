liste_actions = [('action_1', 20, 5), ('action_2', 30, 10), ('action_3', 50, 15), ('action_4', 70, 20),
                 ('action_5', 60, 17), ('action_6', 80, 25), ('action_7', 22, 7), ('action_8', 26, 11),
                 ('action_9', 48, 13), ('action_10', 34, 27), ('action_11', 42, 17), ('action_12', 110, 9),
                 ('action_13', 38, 23), ('action_14', 14, 1), ('action_15', 18, 3), ('action_16', 8, 8),
                 ('action_17', 4, 12), ('action_18', 10, 14), ('action_29', 24, 21), ('action_20', 114, 18)]
actions_triees = sorted(liste_actions, key=lambda x: x[2])
actions_selectionnees = []
gain_total = 0
cout_total = 0
plafond = 500

while actions_triees:
    action = actions_triees.pop()
    if action[1] + cout_total <= plafond:
        actions_selectionnees.append(action)
        gain_total += action[2]
        cout_total += action[1]
print("Voici la liste des actions sélectionnées : ")
for i in range(len(actions_selectionnees)):
    print(f"{actions_selectionnees[i][0]}, "
          f"Coût : {actions_selectionnees[i][1]}€, "
          f"Bénéfice : {actions_selectionnees[i][2]}%")
benefice_total = gain_total/len(actions_selectionnees)
print(f"Votre bénéfice total a été amélioré à {benefice_total}% pour un coût total de {cout_total}€")
