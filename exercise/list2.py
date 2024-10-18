#Exercise goes over working with list data

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Netune"]
prompt = input("What planet will you like to see, (use a captial letter to start): ")
planet_index = planets.index(prompt)
print("Planets closer than " + prompt)
print(planets[0:planet_index])
print("Planets further than " + prompt)
print(planets[planet_index + 1:])

