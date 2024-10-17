#title
print("temperatures and facts about the moon".title())

#split
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)

#in
print("Moon" in "This text will describe facts and chellenges with space travel")

print("Moon" in "This text will describe facts about the Moon")

#find
temperatures = """Saturn has a daytim temperature of -170 degress Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

temperatures = """Saturn has a daytim temperature of -170 degress Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

#count
temperatures = """Saturn has a daytim temperature of -170 degress Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Moon"))
print(temperatures.count("Mars"))

#lower
print("Run Fast. Eat Slow".lower())

#upper
print("Run Fast. Eat Slow".upper())