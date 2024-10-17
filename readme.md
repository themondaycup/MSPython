Notes from [Microsoft Learning for Python.](https://learn.microsoft.com/en-us/training/paths/beginner-python/)

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