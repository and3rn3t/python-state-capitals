from capitals import states
import random

score = 0
wrong = 0
print("Thanks for playing State Capitals!")
print("Guess the correct state capital, or 'quit' to end the game.")

for i in range(50):
    rand_state = (random.randint(0,49))
    # print(states[rand_state]['name'])
    # print(states[rand_state]['capital'])
    
    answer = input(f"What is the capital of {states[rand_state]['name']}? ('quit' to end game): ")

    if answer == states[rand_state]['capital']:
        print("Correct!")
        score = score + 1
        print(f"You got one! Score: {score} correct and {wrong} incorrect.")
    elif answer == 'quit':
        print(f"Thanks for playing! You finished with {score} correct answers, and {wrong} incorrect. Great job!")
        break
    else:
        wrong = wrong + 1
        print(f"Incorrect! The capital of {states[rand_state]['name']} is {states[rand_state]['capital']}")
        print(f"You currently have {score} correct answers and {wrong} incorrect answers.")
