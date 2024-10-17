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