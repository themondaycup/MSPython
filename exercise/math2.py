#Convert strings to numbers and use absolute value

#input number from distance from the sun to planets
first_planet_input = input("Enter the distance from the sun for the first planet in km: ")
second_planet_input = input("Enter the distance from the sun for the second planet in km: ")

#convert input numbers to integers
first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

#calculate and convert to absolute value
distance_km = second_planet - first_planet
print(abs(distance_km))