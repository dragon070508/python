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
elif answer1 == "team":
    answer3 = input("Do you take charge or follow the lead? (leader/follower): ").strip().lower()
    if answer3 == "leader":
        answer4 = input("Do you solve problems through diplomacy or combat? (diplomacy/combat): ").strip().lower()
        if answer4 == "diplomacy":
            print("You are the Wise King! A ruler who leads with wisdom and fairness.")
        elif answer4 == "combat":
            print("You are the Battle Commander! A fierce and brave leader on the battlefield.")
        else:
            print("Your leadership style is unconventional... No character matches your description.")
    elif answer3 == "follower":
        answer5 = input("Are you more drawn to the arts or sciences? (arts/sciences): ").strip().lower()
        if answer5 == "arts":
            print("You are the Artistic Bard! A creative soul who brings joy through music and poetry.")
        elif answer5 == "sciences":
            print("You are the Inventor's Apprentice! A curious mind eager to learn and create.")
        else:
            print("Your interests are unique... No character matches your description.")
    else:
        print("You seem undecided on your role in the team... No character matches your description.")
else:
    print("It seems you don’t fit into any category we have... No character matches your description.")

print("Thanks for playing!")