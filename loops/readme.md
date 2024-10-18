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