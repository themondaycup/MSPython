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