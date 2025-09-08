import shelve
shelf_file = shelve.open('mydata')

shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon'] 


print(type(shelf_file))
print(shelf_file['cats'])

shelf_file.close()

shelf_file = shelve.open('mydata')

print(list(shelf_file.keys()))
print(list(shelf_file.values()))

shelf_file.close()


