# Chapter 5 ***********
# favorite_musicians = ["Eminem", "Taylor Swift", "Bob Dylan", "Jay-Z"]
# places_visited = [("40.4173° N", "82.9071° W"), ("27.6648° N", "81.5158° W")]
# Ryan_dict = {"eyes": "brown",
#              "height": "6 foot 4",
#              "weight": 225
#              }

# def ask_about_ryan():
#     while True:
#         user_question = input("Type eyes, weight, or height to know my attributes: ")
#         if user_question == "eyes":
#             print(Ryan_dict["eyes"])
#         elif user_question == "height":
#             print(Ryan_dict["height"])
#         elif user_question == "weight":
#             print(Ryan_dict["weight"])
#         else:
#             print("I don't know")
# ask_about_ryan()

# musicians_dict = {"Eminem": ["Lose Yourself", "Stan"],
#                   "Taylor Swift": ["Love Story", "Shake it Off"],
#                   "Bob Dylan": ["Like a Rolling Stone", "Blowin' in the Wind"],
#                   "Jay-Z": ["Empire State of Mind", "99 Problems"]
#                  }

# Chapter 6 ***********
# string = "Camus"
# for i in string:
#     print(i)

# user_input_one = input("What did you write yesterday?: ")
# user_input_two = input("Who did you send it to?: ")
# print(f"Yesterday I wrote a {user_input_one}. I sent it to {user_input_two}!")

# new_string = "aldos Hoxley was born in 1894"
# print(new_string.capitalize())

# string = "Where now?, When now?, Who now?"
# print(string.split(","))

# string = ["The", "fox", "jumped", "over", "the", "fence", "."]
# print(" ".join(string))

# string = "A screaming comes across the sky"
# print(string.replace("s","$"))

# dialogue = "It's really just \"—he rubbed his hand over his stubble—\" the most frustrating thing I can think of."
# print(dialogue)

# con_add = "three " + "three " + "three "
# con_multiply = "three " * 3
# print(con_add)
# print(con_multiply)

# string = "It was a bright cold day in April, and the clocks were striking thirteen."
# print(string[:33])

# Chapter 7 ***********
# shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
# for i in shows:
#     print(i)

# for i in range(25, 51):
#     print(i)

# guess_list = [8, 19 , 148, 4]
# while True:
#     ask = int(input("Guess numbers in the list in type q to quit: "))
#     if ask == "q":
#         break
#     elif ask in guess_list:
#         print("The number is in the list!")
#     else:
#         print("The number is not in the list.")

# list_one = [8, 19 , 148, 4]
# list_two = [9, 1 , 33, 83]
# new_list = []
# for i in list_one:
#     for j in list_one:
#         new_list.append(i * j)
# print(new_list)

# Chapter 8 ***********
# import statistics
# my_list = [5, 6, 2, 6, 7, 2, 7, 7, 8, 3, 5, 6]
# print(statistics.mean(my_list))

# def cubed(n):
#     return n**3

# Chapter 9 ***********
# with open("ImportPractice.py", "r") as my_file:
#     print(my_file.read())

# ans = input("What is your answer to the question?: ")
# with open("saved_answers.py", "w") as my_file:
#     print(my_file.write(ans))

# import csv
# shows = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
# with open("shows.csv", "w") as my_file:
#     w = csv.writer(my_file, delimiter= ",")
#     for i in shows:
#         w.writerow(i)

# Chapter 10 ***********
# ST_Hangman.py

# Chapter 11 ***********
# class Apple:
#     def __init__(self, color, ripeness, size, type):
#         self.color = color
#         self.ripeness = ripeness
#         self.size = size
#         self.type = type

# import math
# class Circle:
#     def __init__(self, r):
#         self.radius = r

#     def area(self):
#         return (math.pi * self.radius **2)
    
# C1 = Circle(4)
# print(C1.area())

# class Triangle:
#     def __init__(self, b, h):
#         self.base = b
#         self.height = h

#     def area(self):
#         return (self.base * self.height) / 2
    
# T1 = Triangle(4, 6)
# print(T1.area())

# class Hexagon:
#     def __init__(self, s, ):
#         self.side = s

#     def calculate_perimeter(self):
#         return (6 * self.side)
    
# H1 = Hexagon(6)
# print(H1.calculate_perimeter())
