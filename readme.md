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