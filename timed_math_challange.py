import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 12
try:
    total_problems = int(input("Amount of problems you want to solve: "))
except ValueError:
    raise ValueError("Total amount of problems must be a whole number")


def generated_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong_answers = 0
input("Press Enter to start!")
print("----------------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generated_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        else:
            wrong_answers += 1
            break


end_time = time.time()
total_time = end_time - start_time
percentage_correct_answers = (1-(wrong_answers/total_problems)) * 100

print("-----------------------")
print(f"Well done! You finished in {total_time:.2f} seconds, with {percentage_correct_answers:.2f}% correct answers.")