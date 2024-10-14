#simple string
fact = "The moon has no atmospher."
print(fact)

#immutability of string
fact = "The moon has no atmosphere."
two_facts = fact + " No sound can be heard on the Moon."
print(two_facts)

#Quotation marks
moon_radius = "The Moon has a radius of 1,080 miles."
fact2 = moon_radius + ' The "near side" is the part of the Moon that faces the Earth.'
fact3 = fact2 + " We only see about 60% of the Moon's surface."
print(fact3)

#Mutiline text
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline = """Facts about the Moon:
 There is no atmosphere. 
 There is no sound."""
print(multiline)