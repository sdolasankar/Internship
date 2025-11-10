# Write and Run “Hello World”#
print("Hello World")
print("Hello, World! Welcome to Python 🐍")

# Variables Practice #
name = "Dolasankar"
age = 20
city = "Kolkata"

print(name)
print(age)
print(city)

#combine 
print("My name is", name, "and I am", age, "years old. I live in", city + ".")

#Operations
a = 10
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Strings – Working with Text
greeting = "Hello"
person = "Python Learner"

message = greeting + ", " + person + "!"
print(message)
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Number of letters:", len(message))

#Lists – Storing Multiple Items
favorite_foods = ["Pizza", "Biryani", "Pasta", "Ice Cream"]

print("My favorite foods are:", favorite_foods)
print("First item:", favorite_foods[0])
print("Last item:", favorite_foods[-1])

favorite_foods.append("Burger")
print("Updated list:", favorite_foods)
