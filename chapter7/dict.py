# this is a dictionary, it's main difference from a list is that 
# u can use diffrent data types as indexes, size,color and ram is 
# keys and responings are values

my_mac ={'size': '14','color':'space blue', 'ram': '8gb' }


print(my_mac['size'])
print(my_mac['color'])
print(my_mac['ram'])


your_mac ={'color':'space blue', 'ram': '8gb','size': '14'} 

print(my_mac == your_mac)# order of the items does not matters unlike lists since the dictionary isnt a sequence data type and cant be sliced


