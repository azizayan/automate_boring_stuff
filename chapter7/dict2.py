appareances = {'color':'green', 'item':'book'}

for v in appareances.values():
    print(v)

print()
for k in appareances.keys():
    print(k)

print()
for i in appareances.items():
    print(i)

print()
print(appareances.keys())


print('The book is ' + str(appareances.get('pages',0)) + ' pages.')
# if u try to get the value without get method, program will give error
# if there is no item in real.


appareances.setdefault('pages','412')
print(appareances)

appareances.setdefault('pages','345')#412 stays same since app. has an page value already
print(appareances)




