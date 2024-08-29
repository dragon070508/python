print("Welcome to your Daily Affirmations (or Insults, jk) Generator!")

print("What's your name?")
name = input()

print("What day of the week is it today?")
day = input()

print("What's one of your favorite things?")
favorite_thing = input()

if day.lower() == "monday":
  print(name.capitalize() +
        ", it's Monday, the start of a new week! Remember, just like " +
        favorite_thing.lower() + ", you bring something special to every day!")
elif day.lower() == "tuesday":
  print("Hello " + name.capitalize() +
        "! It's Tuesday, and you're doing great! Just like your love for " +
        favorite_thing.lower() + ", your perseverance shines through!")
elif day.lower() == "wednesday":
  print(name.capitalize() +
        ", it's Wednesday, the middle of the week! Keep pushing, and let " +
        favorite_thing.lower() + " give you the boost you need!")
