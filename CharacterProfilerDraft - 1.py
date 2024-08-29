print("Welcome to the Fantasy World Character Generator!")
print("Answer the following questions to find out which character you are.")

answer1 = input("Do you prefer to work alone or in a team? (alone/team): ").strip().lower()
if answer1 == "alone":
    answer2 = input("Do you rely more on physical strength or intelligence? (strength/intelligence): ").strip().lower()
    if answer2 == "strength":
        print("You are the Lone Warrior! A strong and independent fighter who needs no one.")
    elif answer2 == "intelligence":
        print("You are the Shadow Mage! A cunning and clever user of dark magic.")
    else:
        print("Hmm, you seem a bit mysterious... No character matches your description.")