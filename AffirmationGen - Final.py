print("Welcome to your Daily Affirmations (or Insults) Generator!")

print("What's your name?")
name = input()

print("What day of the week is it today?")
day = input()

print("What's one of your favorite things?")
favorite_thing = input()

if day.lower() == "monday":
    print(name.capitalize() + ", it's Monday, the start of a new week! Remember, just like " + favorite_thing.lower() + ", you bring something special to every day!")
elif day.lower() == "tuesday":
    print("Hello " + name.capitalize() + "! It's Tuesday, and you're doing great! Just like your love for " + favorite_thing.lower() + ", your perseverance shines through!")
elif day.lower() == "wednesday":
    print(name.capitalize() + ", it's Wednesday, the middle of the week! Keep pushing, and let " + favorite_thing.lower() + " give you the boost you need!")
elif day.lower() == "thursday":
    print("Hey " + name.capitalize() + ", it's Thursday! You're almost at the weekend. Stay strong, just like your passion for " + favorite_thing.lower() + "!")
elif day.lower() == "friday":
    print(name.capitalize() + ", it's Friday! The week is almost over. Celebrate with a little bit of " + favorite_thing.lower() + " and enjoy!")
elif day.lower() == "saturday":
    print(name.capitalize() + ", it's Saturday, a day to relax! Let " + favorite_thing.lower() + " bring you joy and peace today!")
elif day.lower() == "sunday":
    print("Hi " + name.capitalize() + "! It's Sunday, a day of rest. Reflect on your week and enjoy some time with " + favorite_thing.lower() + "!")
else:
    print("Hmm, " + name.capitalize() + ", I'm not sure what day '" + day + "' is, but every day is a good day for " + favorite_thing.lower() + "!")

print("Have a great day, " + name.capitalize() + "!")
