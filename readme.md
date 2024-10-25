Notes from [Microsoft Learning for Python.](https://learn.microsoft.com/en-us/training/paths/beginner-python/)
This document will contain all my notes, while each folder will just have the section that is just written from here. 

# Boolean Logic
common logic operators

- equals: a == b
- not equals: a != b
- less than: a < b
- less than or equal to: a <= b
- greater than: a > b
- greater than or equal to: a >= b

The body of an `if` statement must be indented. `if` statements only test expression if it is `true`. Anything outside of it will still run as normal. 

```python
if test_expression:
    #statement(s) to be run
```

### Else & Elif

to test code that is `false`, use an `else` statement.

```python
if test_expression:
    #statement(s) to be run
else:
    #statement(s) to be run
```

syntax of an `if/elif` statement:
```python
if test_expression:
    #statement(s) to be run
elif:
    #statement(s) to be run
```
`elif` will only run when the `if` condition is false

combining `if/elif/else` statements

`if` block can only have one `else` block but it can have multiple `elif` blocks
```python
if test_expression:
    #statement(s) to be run
elif test_expression:
    #statement(s) to be run
elif test_expression:
    #statement(s) to be run
else:
    #statement(s) to be run
```

Nested conditional logic can create more complex programs. to next conditions, indent the inner conditions and everything at the same level of indentation will be run in the same code block:

syntax
```python
if test_expression:
    #statement(s) to be run
    if test_expression:
        #statement(s) to be run
    else:
        #statement(s) to be run
elif test_expression:
    #statement(s) to be run
    if test_expression:
        #statemen(s) to be run
    else:
        #statement(s) to be run
else:
    #statement(s) to be run
```

### And, Or
used to evaluate multiple condition in one statement 

`or` statement can connect two boolean expressions. For the entire expression to evaluate to `True` at least one subexpression must be ture. 

syntax:
```python
sub-expresssion1 or sub-expression2
```

`and` statement can connect two boolean expressions. Both expressions must evalute to `True`, otherwise the case will be `False`. 

syntax:
```python
sub-expression1 and sub-expression2
```

Truth Table for `and`

| Subexpression1  | Operator | Subexpression2 | Result |
| ------------- | ------------- | ------------ | ------------ |
| True  | and  | True | True |
| True  | and  | False | False |
| False  | and  | True | False |
| False  | and  | False | False |


Truth table for `or`

| Subexpression1  | Operator | Subexpression2 | Result |
| ------------- | ------------- | ------------ | ------------ |
| True  | or  | True | True |
| True  | or  | False | True |
| False  | or  | True | True |
| False  | or  | False | False |

# Strings
Be mindful string are case-sensitive, so Moon and moon are considered different words.

### Immutability of Strings

Strings are immutable, meaning they cant be change. To modify a string, you can return it from a new string by assigning it to a new variable.

```python
variable1 = "output"
variable2 = varible1 + "new output"
print(variable2)
```

### Quotation Marks
Strings cant be placed in single, double, or triple quotation marks. Its best to choose one type and stick with it consistently within a project. 

When a string contains a word, number or special character that also uses a qotation mark, you should use a different style. If you dont alternate single and double quotation marks, can cause a syntax error. 

```python
'The "near side" is the part of the Moon that faces the Earth.'

or 

"We only see about 60% of the Moon's surface."
```

### Multiline text
Many different ways to define multiple lines of text in a single varaible. The most commany are
- use a newline character (`\n`)
- use a triple quotation mark(`"""`)

### Methods 
see method.py file for example. 
Common method types to manipulate strings. String methods are part of the `str` type. 

- `.title()` will return the first letter of each word capitalized. 
- `.split()` will separate the string at every space

when using with a newline (`\n`)character can help create single lines for. "This type of splitting becomes handy when you need a loop to process or extract information, or when you're loading data from a text file."

- `in` can be used to find if a word exists in a string
-  `.find()` it will find a the position of a specific word in a string. If it returns `-1` the word isnt found. If a number is returned it represents the place in the string. 
- `.count()` this method will return the total number of times it occures 
- `.lower()` this will convert a string to all lowercase letters
- `.upper()` this will conver every character to uppercase

**Tip**
"When you're searching for and checking content, a more robust approach is to lowercse a string so that casing doesnt prevent  match. For example, if you're counting the number of times the word the apears, the method wouldn't count the times where The appears, even though they're both the same word. You can use the `.lower()` method to change all characters to lowercase."

### Check content 
Able to extract information thats irregular in its presentataion. 

```python
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
```
Anything after the colon (`:`) is trusted is a tempature. Splitting the string at `:` and then using a `-1` on the return list to return the last item in the list. 

You also able to use
- `.isnumeric()` checks to see if the number is numeric

```python
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

#will output: 30
```

- `.isdecimal()` checks to see if the number is a decimal
- `.startswith()` helps with prefixed numbers such as negiatives

example: 
```python
print("-60".startswith('-'))
#will output: True
``` 

- `.endswith()` helps with verifying the last character of a string
```python
if "30 C".endswith("C"):
    print("This temperature is in Celsius)
```

### Transform text
using `.replace()` can find and replace characters or group of characters.

```python
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
```
This will output everything that says Celsius to C

- `.join()` method can put split characters back together. 

```python
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
```
` ' ' ` is used to join the list back together. 

### Format in Python

- `%s and %` - %s is the placeholder for a varaible in a string. % goes at the end of the string. 

syntax:
```python
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
```

multiple `%s` requires to use parentheses so the variables are passed in.

```python
% ("Moon", "Earth", "Moon", "Earth")
```

- `.format()` uses braces `{}` as placeholders within a string.

you can also use numbers in the brackets `{0}`. This will pass the first(index of zero) into the `.format()`. However for readability its best to use a keyword argument as the reference

```python
#number in bracket example
mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

#keyword argument example
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))
```

- F-strings uses the variable names from the code. It doesnt need to be assign a value beforehand

```python
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
```

- `round()` can be used for expression within the braces.

```python
print(round(100/6, 1))

#or 

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")
```

# Mathematical Operations
Most common operators used: addition, subtraction, multiplication, and division.
- `+` used to add numbers together and provide the total
- `-` used to subtract numbers and provide the difference
- `*` multiplication operator and provides the product of the numbers
- `/` used for division and provides the quotient of the numbers.

In order to round down  the "floor division" `//` can be used.  helpful when only wanting to get a whole number when dividing.

- `%` called modulo operator is used to get the remainder of a number
```python
display_seconds = 1042 % 60
print(displayseconds)
```

### Order of Operation
1. Parentheses
2. Exponents
3. Multiplication and Division
4. Addition and Subtraction

```python
result_1 = 1032 + 26 * 2
print(result_1)

#or

result_2 = 1032 + (26 * 2)
print(result_2)
```

### Converting Strings to numbers

Twp types of numbers:
- `int` integers
- `float` floating point

Different between the two is the decimal point. Integers are whole number and floating ppints contain a decimal value.

when converting a string to a number you use the type needed to convert. 
```python
demo_int = int("215")
print(demo_int)

#or

demo_float = float("215.3")
print(demo_float)
```

- `abs` absolute value. This will convert a negative value to an absolutate value (positive number)
```python
print(abs(16 - 39))
#will output 23 not -23
```
- `round` will round up or down to the nearest integer if teh decimal value is greater than .5 or less than .5
```python
print(round(1.4))
print (round(2.6))

#will output 1, 3
```

Python has libraries to provide more advanced operations and calculations. One of the most common is the `math` library"
- `ceil` round number up to the nearest whole number
- `floor` round number down to the nearest whole number

```python
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
```

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

# Loops

### While loop

- "A `while` loop performs an operation *while* a certain condition is true. You could use a `while` loop to:
- check for another line in a file.
- check if a flag has been set
- check if a user has finished entering values
- check if something else has changed to indicate that the code can stop performing the operation."

its important to remember when creating a `while` loop to ensure that condition change. If not then python will continue to run the code until the program crashes.

"A`while` loop has three important parts:
1. the keyword `while`, followed by a space.
2. the condition you test. if the condition is true, the code inside the while loop runs.
3. the code want to run for each iteration, indented while nested whitespace."

```python
#syntax
while <condition>:
    # code here

#example:
user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done')
#the user_input is the condition that is test for the while loop
```
### For loop

- "The `for` loop is a statement with five important parts:
1. the word `for`, followed by a space.
2. the variable name you want to create for each value in teh sequence (`number`). Note multiple variables need to be separated by commas.
3. The word `in`, surrounded by spaces.
4. The name of the list (`countdown`, in the preceding example), or iterable that you want to loop over, followed by a colon (`:`)
5. The code you want to run for each item in the iterable, spearated by nested whitespaces."

```python
from time import sleep

countdown = [4,3,2,1,0]

for number in countdown:
    print(number)
    sleep(1) # wait 1 second
print("blast off! ")
```

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

# Functions

### Functions with no arguments

Funtions use the `def` keyword follow by a name, parentheses, and the body of the function code:

```python
def rocket_parts(): #rocket_parts is the name of the function
    print("payload, propellant, structure")
```
"In python, if a function doesn't explicitly return a value, it implicitly returns `none`. Updating the function to return the string instead of printing it causes the `output` variable to have a different value:

```python
def rocket_parts():
    return "payload, propellant, structure"
output = rocket_parts()
output
```

### Required and optional arguments

A built-in function that requires an argument is `any()`. It takes an iterable(example, a list) and returns `true` if any item is `true` otherwise it returns `false`.

```python
any([True, False, False])
#returns True

any([False, False, False])
#returns False
```

An error message will show that at least one argument is needed when calling `any()` without any argument. 

### Requiring an argument

Required inputs are called *arguments* to a function. An arguments can be a destination to caluclate travel distance.

```python
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
```

### Multiple required arguments

When using multiple arguments, you must separeate them by using a comma. 

```python
def days_to_complete(distance, speed):
    hours = distance / speed
    return hours/24
```

### Functions as arguments

Its possible to use a value and assign it to a varaible.

```python
total_days = days_to_complete(238855, 75)
round(total_days)
```

### Using keyword arguments in Python

