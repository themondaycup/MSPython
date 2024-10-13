#else
a = 27
b = 93
if a > b:
    print(a)
else:
    print(b)
#output will be 93

#elif
a = 27
b = 93
if a <= b:
    print("a is less than or equal to b")
elif a == b:
    print("a is equal to b")
#output will be a is less than or equal to be

#if elif else
a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")
#output will be a is than b

#nested conditional logic
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print("a is greater than b and b is greater than c")
    else:
        print("a is greater than b and less than c")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")
#output will be a is less than b