print("Welcome to the Age Classifier!")

print("Please enter the year you were born:")
birth_year = int(input())

if birth_year >= 1925 and birth_year <= 1946:
    print(
        "🎩 You belong to the Traditionalists generation (1925-1946). A time of great values and strength!"
    )
elif birth_year >= 1947 and birth_year <= 1964:
    print(
        "🎉 You're a Baby Boomer (1947-1964)! You were born in a time of prosperity and cultural change!"
    )
elif birth_year >= 1965 and birth_year <= 1981:
    print(
        "🎸 You're part of Generation X (1965-1981)! The generation that brought us MTV and grunge music!"
    )
elif birth_year >= 1982 and birth_year <= 1995:
    print(
        "💻 You're a Millennial (1982-1995)! The generation that grew up with the internet and social media!"
    )
elif birth_year >= 1996 and birth_year <= 2010:
    print(
        "📱 You're from Generation Z (1996-2015)! A tech-savvy generation born into the digital age!"
    )
elif birth_year >= 2011 and birth_year <= 2024:
    print(
        "💀 You're from Generation Alpha (2011-2024)! Also known as the brainrot generation significantly worse than Gen Z!"
    )
else:
    print(
        "Hmm, it seems like your birth year doesn't fall within our range. You must be from a future generation or an unknown era!"
    )

print("Thanks for using the Age Classifier!")
