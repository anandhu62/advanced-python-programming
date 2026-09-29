#An online examination system wants to randomly select a question.

import random

questions = [
    "What is Python?",
    "What is recursion?",
    "What is a module?",
    "What is a package?"
]

question = random.choice(questions)

print("Your Question:")
print(question)