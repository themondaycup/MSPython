#creating while loops

#create the varaile for user input
new_planet = ''
#creat the list to store the values
planets = []

#starting while loop
while new_planet != 'done':
    #check if theres a value in new_planet
    if new_planet:
        #stores the new value in the list
        planets.append(new_planet)
        #prompts for a new value
    new_planet = input('Enter a new planet or done when done: ')

#displays all the items in planets
print(planets)