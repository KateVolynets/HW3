group_name = ['Elena', 'Matvei', 'Alexander', 'Bogdan', 'Inna', 'Bogdan', 'Elena', 'Inna', 'Elena']
result_group_name = []
print('All name in group: ')
print(group_name)
for i in group_name:
    if i not in result_group_name:
        result_group_name.append(i)

print('Unique name in group: ')
print(result_group_name)
