#creating a list
running_shoes = ["nike", "hoka", "new balance", "on"]
print("I am currently run in", running_shoes[2])

#access list by index
running_shoes = ["nike", "hoka", "new balance", "on"]
running_shoes[3] = "saucony"
print("My next running shoes will be", running_shoes[3])

#using len function
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

#appending item to list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

#removing items from list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
planets.pop() #Goodby, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

#finding a value
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")