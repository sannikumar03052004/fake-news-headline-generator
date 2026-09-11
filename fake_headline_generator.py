# 1- import the random module
import random

# 2 - create subjects
subjects = [
    "shahrukh khan",
    "virat kohli",
    "nirmala sitaraman",
    "A mumbai cat",
    "A group of monkeys",
    "prime minister modi",
    "Auto rickshaw driver from delhi"
]

actions = [
    "lunches",
    "cancels",
    "dances with",
    "orders",
    "celebrates"
]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "during ipl match",
    "at india gate"
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no) ").strip().lower()
    if user_input == "no":
        break

# print goodbye message
print("\nThanks for using the fake news headlines generator. Have a fun day")