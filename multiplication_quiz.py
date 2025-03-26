import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
num_of_tries = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    response = input()
    if response.isnumeric():
        ans = num1 * num2
        if int(response) == ans:
            correctAnswers += 1
            print("Correct!")
