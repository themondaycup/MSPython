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