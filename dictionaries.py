# Dictionaries

Walnuts_list = [['carb', 3.7], ['fat', 69.1], ['protein', 15.5]]
Cereal_list = [['fat', 1.8], ['carb', 70], ['protein', 11]]

Walnuts = {'carb': 3.7, 'fat': 69.1, 'protein': 15.5}
Cereal = {'fat': 1.8, 'carb': 70, 'protein': 11}

Compare = {'fat': [], 'carb': [], 'protein': []}

for x in Walnuts.keys():
    if Walnuts[x] > Cereal[x]:
        Compare[x] = 'more'
    else:
        Compare[x] = 'less'

print('Walnuts have {} carb than cereal'.format(Compare['carb']))
print('Walnuts have {} fat than cereal'.format(Compare['fat']))
print('Walnuts have {} protein than cereal'.format(Compare['protein']))
