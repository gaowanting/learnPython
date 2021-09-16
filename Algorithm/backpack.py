items = [(4, 20), (3, 18), (2, 14)]
capacity = 7
'''
sort the items list by the density
'''


def density(i):
    return i[1] / i[0]


items.sort(reverse=True, key=density)
print(items)


def max_calorie0(items, capacity):
    current_capacity = capacity
    current_calorie = 0
    i = 0
    while current_capacity > 0:
        if current_capacity >= items[i][0]:
            current_calorie += items[i][1]
            current_capacity = current_capacity - items[i][0]
        else:
            current_calorie += (current_capacity / items[i][0]) * items[i][1]
            current_capacity = 0
        i += 1
    return int(current_calorie)

print(max_calorie0(items, capacity))
'''
create a density list
'''

items = [(4, 20), (3, 18), (2, 14)]
capacity = 7

def max_calorie1(items, capacity):
    density = [i[1] / i[0] for i in items]
    current_capacity = capacity
    current_calorie = 0
    while current_capacity > 0:
        index = density.index(max(density))
        if current_capacity < items[index][0]:
            current_calorie += (current_capacity / items[index][0]) * items[index][1]
            current_capacity = 0
        else:
            current_capacity = current_capacity - items[index][0]
            current_calorie += items[index][1]
        density[index] = 0
    return int(current_calorie)

print(max_calorie1(items, capacity))
