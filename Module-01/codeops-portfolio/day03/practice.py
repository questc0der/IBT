#Unique cities
cities = ["Addis Ababa", "Adama","Bahir Dar","Mekelle","Hawassa","Addis Ababa","Jimma","Bahir Dar","Dire Dawa","Hawassa"]
unique = {city for city in cities}
count = {city: cities.count(city) for city in unique}
print(count)
print(unique)

#Price Report
groceries = {"banana": 25, "Avocado": 30, "Tomato": 45, "Orange": 30, "apple": 150}
for grocery in groceries:
    print(f"{grocery}: {groceries[grocery]}")