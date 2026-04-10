# Ask the user to enter a model accuracy score (0–100). Print a rating based on the score:



score = int(input("Enter a model accuracy score (0–100)"))
if 90 <= score <=100:
    print("Excellent! Production-ready.")
elif 75 <= score <= 89:
    print("Good. Needs minor tuning.")
elif 60 <= score <= 74:
    print("Fair. More training data needed.")
elif score <= 60:
    print("Poor. Re-evaluate your approach.")
print("Rating based on product score is",score)

