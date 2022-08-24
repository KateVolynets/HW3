vip_zona = ('Elena', 'Matvei', 'Irina', 'Alexander', 'Bogdan', 'Inna')
common_room = ('Serjoscha', 'Vanya', 'Bogdan', 'Elena')

print('Number of people in the VIP room: ')
print(len(vip_zona))
print('Number of people in the common room: ')
print(len(common_room))

# vip_zona[6] = 'Oksana'

iteam_common_room = list(common_room)
iteam_common_room.append('Kristina')
tuple(iteam_common_room)

print('New number of people in the VIP room: ')
print(len(vip_zona))
print('New number of people in the common room: ')
print(len(iteam_common_room))
