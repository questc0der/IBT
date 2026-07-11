#Unique cities
cities = ["Addis Ababa", "Adama","Bahir Dar","Mekelle","Hawassa","Addis Ababa","Jimma","Bahir Dar","Dire Dawa","Hawassa"]
unique = {city for city in cities}
count = {city: cities.count(city) for city in unique}
print(count)
print(unique)
