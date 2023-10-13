from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height1 = [2.71]
weight1 = [165.3, 38.4]
bmi1 = give_bmi(height1, weight1)
print(bmi1, type(bmi1))
print(apply_limit(bmi1, 26))

height2 = [2.71, 'a']
weight2 = [165.3, 38.4]
bmi2 = give_bmi(height2, weight2)
print(bmi2, type(bmi2))
print(apply_limit(bmi2, 26))
