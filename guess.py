#guess the number generted
import random



def ask_for_input():
    print ("\nPick a Min and Max")
    minimum = int (input("minimum: " ))
    maximum = int (input("maximum: " ))
    if minimum> maximum:
        print("Min is supposed to be smaller than Max :/")
        ask_for_input()
    else:
         guess_answer(random.randint(minimum, maximum))

def guess_answer(answer):
    answer = answer
    user_guess = input("\nguess the number generated: ")
    user_guess = int(user_guess)

    if user_guess<answer:
        print("\nguess a higher number")
        guess_answer(answer)
    elif(user_guess>answer):
        print("\nguess a lower number")
        guess_answer(answer)
    elif(user_guess == answer):
        print ("Yayy")

ask_for_input()
        




