a_list = [1,2,3,4,5,6,7,8,9]#list is comma delimited
print(a_list)


b_list = [['cat','bat'],[1,2,3,4,5,6,7]]
print(b_list[0][1])
print(b_list[1][3])

c_list = ['e','m','r','e','a','z','i','z']
print(c_list[-1],c_list[-2],c_list[-3],c_list[-4])

a_small_list = a_list[0:-2]
print(a_small_list)

d_list = a_list * 2
del d_list[6]
print(d_list)


laptop = ['8gb','m2','512gb']
ram,cpu,ssd = laptop
print(ram)
print(cpu)
print(ssd)


for index, option in enumerate(laptop):
    print('Option ' + str(index)+ ' in laptop is: ' + option)


laptop.insert(1,'14 inch')
print(laptop)


a_list.sort(reverse=True)
print(a_list)


e_list = ['A','e','B','b','c','D','a']
e_list.sort(key=str.lower)
print(e_list)
e_list.reverse()
print(e_list)



