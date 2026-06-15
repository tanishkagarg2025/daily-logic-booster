import random
from datetime import datetime
from math import factorial

class AIQuestionGenerator:

    def __init__(self):
        # Use today's date as seed (same question whole day)
        today = datetime.now().strftime("%Y-%m-%d")
        random.seed(today)

    def generate_question(self):
        question_type = random.choice([
            "array_sum",
            "probability",
            "factorial",
            "missing_number"
        ])

        if question_type == "array_sum":
            return self.array_sum_question()
        elif question_type == "probability":
            return self.probability_question()
        elif question_type == "factorial":
            return self.factorial_question()
        else:
            return self.missing_number_question()

    # --------------------------

    def array_sum_question(self):
        arr = random.sample(range(1, 30), 5)
        target = arr[0] + arr[1]

        question = f"Given array {arr}, find two numbers whose sum is {target}."
        solution = f"The two numbers are {arr[0]} and {arr[1]}."

        return {"text": question, "solution": solution}

    # --------------------------

    def probability_question(self):
        coins = random.randint(2, 4)
        total = 2 ** coins
        favorable = factorial(coins) // (factorial(2) * factorial(coins - 2))

        question = f"If {coins} coins are tossed, what is the probability of getting exactly 2 heads?"
        solution = f"Total outcomes = {total}. Favorable = {favorable}. Probability = {favorable}/{total}."

        return {"text": question, "solution": solution}

    # --------------------------

    def factorial_question(self):
        n = random.randint(4, 7)
        result = factorial(n)

        question = f"What is the factorial of {n}? (Use recursion logic)"
        solution = f"{n}! = {result}"

        return {"text": question, "solution": solution}

    # --------------------------

    def missing_number_question(self):
        numbers = list(range(1, 8))
        missing = random.choice(numbers)
        numbers.remove(missing)
        random.shuffle(numbers)

        question = f"Find the missing number in the array {numbers}."
        solution = f"The missing number is {missing}."

        return {"text": question, "solution": solution}