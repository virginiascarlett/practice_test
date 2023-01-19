"""
An extremely useful help message.
"""

correct_answers = ['Y', 'y', 'yes', 'Yes']

while True:
    answer = input('Are dogs the best?\n')
    if answer not in correct_answers:
        print("Incorrect. Try again.")
        continue
    else:
        break

print("Correct.")