# Lists

List are created by values and separated by comma's. Each list is surrounded by brackets `[]`
```python
running_shoes = ["nike", "hoka", "new balance", "on"]
```

To accesss any item in the list you would call upon it from an index in the bracket. Such as `running_shoe[0]`. Indexes start from 0. You can also use negative numbers `-1` to return the last time in a list or `-2` to return the second to last item etc. 

```python
running_shoes = ["nike", "hoka", "new balance", "on"]
print("I currently run in", runnings_shoe[2])
```

To modify a value in a list you will assign a it by using an index
```python
running_shoes[3] = "saucony"
```

### Len
- `len()` the length built-in function can be used to see how long a list is
```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
```

### Adding values to lists
Lists are dynamic, you can add or remote after creating using `.append(value)`

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
```

### Removing values from lists
- `.pop()` method on a list can remove the last item. 

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
planets.pop() #Goodby, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")
```

### Find a value in a list
"To determine where in a list a value is stored, you use the lists `index` method. This method searches for a the value and returns the index of that items in the list. If it doesnt find a match it returns `-1`

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
```

"Because indexing starts with 0, you need to add 1 to display the proper number."

### Store numbers in lists
Same way to create a list you can do it with numbers as well. Creating it with a bracket, in this example numbers with a decimal places will be stored

```python
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
```

We can then multiply two of the values from the list
```python
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weigh = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")
```

### Min() and Max()
- `min()` will return the smallest number in the list
- `max()` will return the largest number in the list

In this case for the gravity on the planets it will be used as such:

```python
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weigh = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")
```

### Slice

- In order to retrieve a portion of a list a *slice* is needed. It has a starting and ending indexes but the start is the starting inded while the end, ends before (and does not include) the ending index. 

```python
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Nepture"]
planets_before_earth = planets[0:2] # this is the slice
print(planets_before_earth)

#output: Mercury, Venus
```

To get everything in the list without putting the last value you can just put the starting value. Pythin will assume that you want to go to the end of the list

```python
planets_after_earth = planets[3:8]
print(planets_after_earth)

#or 

planets_after_earth = planets[3:]
print(planets_after_earth)
```

### Join list

Joining two list to return a new list you use the `+` operator. This can join two list together and make a new list

```python
amalthea_group = ["metis", "adrastra", "amalthea", "thebe"]
galilean_moons = ["io", "europa", "ganymede", "callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of jupiter are", regular_satellite_moons)
```

### Sort list

- `.sort()`this method will sort a list of string in alphabetical order and a list of number in numeric order
- to sort in reverse order use `.sort(reverse=True)` on the list. 

```python
amalthea_group = ["metis", "adrastra", "amalthea", "thebe"]
galilean_moons = ["io", "europa", "ganymede", "callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort() # here is where the list will be sorted
print("The regular satellite moons of jupiter are", regular_satellite_moons)
```