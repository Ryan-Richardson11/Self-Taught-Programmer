# Chapter 5
favorite_musicians = ["Eminem", "Taylor Swift", "Bob Dylan", "Jay-Z"]
places_visited = [("40.4173° N", "82.9071° W"), ("27.6648° N", "81.5158° W")]
Ryan_dict = {"eyes": "brown",
             "height": "6 foot 4",
             "weight": 225
             }

def ask_about_ryan():
    while True:
        user_question = input("Type eyes, weight, or height to know my attributes: ")
        if user_question == "eyes":
            print(Ryan_dict["eyes"])
        elif user_question == "height":
            print(Ryan_dict["height"])
        elif user_question == "weight":
            print(Ryan_dict["weight"])
        else:
            print("I don't know")
ask_about_ryan()

musicians_dict = {"Eminem": ["Lose Yourself", "Stan"],
                  "Taylor Swift": ["Love Story", "Shake it Off"],
                  "Bob Dylan": ["Like a Rolling Stone", "Blowin' in the Wind"],
                  "Jay-Z": ["Empire State of Mind", "99 Problems"]
                 }