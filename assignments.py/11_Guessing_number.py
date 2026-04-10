#Number Guessing Game

import random
correct_number = random.randint(1,20)
count=0
while True:
    try:
        guessed_number = int(input("Guess the number: "))
        count+=1
        print("Attempt: ", count)
        
        if guessed_number == correct_number:
            print(f"You guessed it right! The number is: {correct_number}")
            
            break
        elif guessed_number < correct_number:
         print("Too low!")
         
        elif guessed_number > correct_number:
         print("Too high!")
         
    except ValueError:
           print("Invalid")
           continue