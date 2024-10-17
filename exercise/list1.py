#exercise to display information about planets, my code is below

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
planets.append("Pluto")
total_number = len(planets)
print("There are", total_number, "planets and the last planet is", planets[-1])

#MS code
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
planets.append("Pluto")
print("Actually, there are", len(planets), "planets")
print(planets[-1], "is the last planet")
