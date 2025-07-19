spam = [0,1,2,3]
eggs = spam 
eggs[1] = 'helllo'
print(spam)
spam[2] = 'by'
print(eggs)


#this reference operation works different for lists from other variables(int,string etc)


a = 42
b = a
a = 123
print(b)
b = 89
print(a)


c = "asdads"
d = c
c = "bgggg"
print(d)
d = "klklklk"
print(c)