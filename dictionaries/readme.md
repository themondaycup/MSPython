# Dictionaries

### Creating a dictionary

"Python dictionaries allow you to work with related sets of data. A dictionary is a collection of key/value pairs. Think of it like a group of variables inside of a container, where the key is the name of the variable, and the value is the value stored inside it."

-   created by using curly braces `{}` and the colon `:`to denote a dictionary. 

```python
planet = {
    'name': 'Earth',
    'moons': 1
}
```

### Reading dictionary values
- The `get` method will allow you to access a value by using its key. 

```python
print(planet.get('name'))
```

- you can also use square bracket notation `[]`. This method uses less code than `get` and most programmers use this syntax indead.

```python
print(planet['name'])
```

**remember**

"Although the behavior of get and the square brackets `([ ])` is generally the same for retrieving items, there's one key difference. If a key isn't available, get returns None, and `[ ]` raises a KeyError."

```python
wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError
```

### Modify dictionary values

Its possible to modify values inside a dictionary by using the `update` method. 

```python
planet.update({'name': 'Makemake'})

# No output: name is now set to Makemake.
```

Its also possible to use the shortcut square brackets `[]` and using the `=` to provide a new value. 

```python
planet['name'] = 'Makemake'

# No output: name is now set to Makemake.
```
Both methods word just using different syntax. "You're free to use whichever syntax you feel is most appropriate. Most developers choose square brackets to update individual values."

### Add and remove keys

To add a new key, you would assign it just as an existing one

```python
planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
```

*Just be mindful*
"Key names, like everything else in Python, are case sensitive. As a result, 'name' and 'Name' are seen as two separate keys in a Python dictionary."

- `.pop` will remove the key from the dictionary

```python
planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }
```

### Complex data types
"Dictionaries are able to store any type of a value, including other dictionaries. This allows you to model complex data as needed. Imagine needing to store the diameter for planet, which could be measured around its equator or poles. You can create another dictionary inside of planet to store this information:"

```python
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }
```

"To retrieve values in a nested dictionary, you chain together square brackets, or calls to `get`"

```python
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
```

### Retrieve all keys and values

- `keys.()` method returns a list object that contains all the keys. You can then iterate through all the items in the dictionary 

```python
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

#output
#october: 3.5cm
#november: 4.2cm
#december: 2.1cm
```

### Determine if a key exists in a dictionary

"When you update a value in a dictionary, Python will either overwrite the existing value or create a new one, if the key doesn't exist. If you wish to add to a value rather than overwriting it, you can check to see if the key exists by using `in`. For example, if you want to add a value to December or create a new one if it doesn't exist, you can use the following:

```python
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
#because december exists, the value will be 3.1
```

### Retrieve all values

"Similar to `keys()`, `values()` returns the list of all values in a dictionary *without* their respective keys. `values()` can be helpful when you're using the key for labeling purposes, such as the preceding example, in which the keys are the name of the month. you can use `values()` to determine the total rainfall amount:

```python
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')

#There was 10.8cm in the last quarter.
```