import copy

list_1 = [1,2,3,4,5,6,7,8,9,'a','b','c']

list_2 = [1,2,3,4,['a','b','c','d'],5,6,7]

list_1_copy = copy.copy(list_1)
list_2_copy = copy.copy(list_2)
list_2_copy_2 = copy.deepcopy(list_2)


list_2[4][0] = 'E'

print(list_2)
print(list_2_copy)
print(list_2_copy_2)