import random

# ● ┌ ─ ┐ │ └ ┘


dice_body = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),

    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),

    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),

    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),

    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),

    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘")
       
}

dice = []
total = 0
numbers = int(input("Enter number of dices : "))

for i in range(numbers):
    dice.append(random.randint(1,6))

for j in range(numbers):
    for z in dice_body.get(dice[j]):
        print(z)

for k in dice:
    total = total+k

print("Total is : ",total)
