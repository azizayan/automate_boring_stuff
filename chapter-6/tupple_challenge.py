info = ("Aziz", 21, "CS Student", True)
print(info[1])
if info[-1] == True: print('TRUE') 
else: print("FALSE")

person = ("Emre", [180, 75], ("Türkiye", "Ankara"))

print(person[2][1])
person[1][0] = 185
print(person[1][0])

coords = (39.9, 32.8)

lat,lon = coords

lat,lon = lon,lat
print(lat)
print(lon)


locations = {
    (39.9, 32.8): "Ankara",
    (41.0, 28.9): "Istanbul"
}

def find_city(lat, lon):
    key = (lat, lon)
    if key in locations:
        return locations[key]
    else:
        return "Unknown location"
    

print(find_city(41.0,28.9))
print(find_city(0.0,12.9))



    


