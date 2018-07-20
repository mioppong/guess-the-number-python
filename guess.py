#guess the number generted
import random



def ask_for_input():
    print "\nPick a number b/w a max and min value and we will say if too high or too low"
    minimum = int (input("minimum: " ))
    maximum = int (input("maximum: " ))
    if minimum> maximum:
        ask_for_input()
    else:
         guess_answer(random.randint(minimum, maximum))

def guess_answer(answer):
    answer = answer
    user_guess = raw_input("\nguess the number generated: ")
    user_guess = int(user_guess)

    if user_guess<answer:
        print("\nguess a higher number")
        guess_answer(answer)
    elif(user_guess>answer):
        print("\nguess a lower number")
        guess_answer(answer)
    elif(user_guess == answer):
        print "Yayy"

ask_for_input()
        




