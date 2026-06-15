import random


def generate_question(category, difficulty):

    generators = {
        "DSA": generate_dsa,
        "Probability": generate_probability,
        "Recursion": generate_recursion,
        "OOPS": generate_oops,
        "Logical Puzzles": generate_logic
    }

    if category == "Mixed Mode":
        category = random.choice(list(generators.keys()))

    return generators[category](difficulty)


# ---------------------------------------------------
# ---------------- DSA ------------------------------
# ---------------------------------------------------

def generate_dsa(difficulty):

    if difficulty == "Hard":
        text = (
            "You are given an array of integers.\n"
            "Find the length of the longest subarray with sum = 0.\n\n"
            "Constraints:\n"
            "- Must be O(n)\n"
            "- Use hashing concept"
        )

        solution = (
            "Use prefix sum + hashmap.\n"
            "If prefix sum repeats → subarray between indices has sum 0.\n"
            "Track max length while iterating."
        )

    else:
        text = "Find the second largest element in an array in one traversal."
        solution = "Keep two variables: first_max and second_max."

    return {"text": text, "solution": solution}


# ---------------------------------------------------
# ---------------- PROBABILITY ----------------------
# ---------------------------------------------------

def generate_probability(difficulty):

    if difficulty == "Hard":
        text = (
            "Two dice are rolled.\n"
            "What is the probability that the sum is divisible by 3\n"
            "given that at least one die shows 4?"
        )

        solution = (
            "Use conditional probability.\n"
            "Total cases where one die is 4 = 11.\n"
            "Favourable cases = calculate sums divisible by 3.\n"
            "Final probability = favourable / 11."
        )

    else:
        text = "If 3 coins are tossed, what is probability of exactly 2 heads?"
        solution = "Favourable = 3, Total = 8 → 3/8."

    return {"text": text, "solution": solution}


# ---------------------------------------------------
# ---------------- RECURSION ------------------------
# ---------------------------------------------------

def generate_recursion(difficulty):

    if difficulty == "Hard":
        text = (
            "Write a recursive function to generate all permutations "
            "of a string without using any library function.\n\n"
            "Also analyze its time complexity."
        )

        solution = (
            "Swap characters recursively.\n"
            "Base case: when index reaches end.\n"
            "Time complexity: O(n!)."
        )

    else:
        text = "Write recursive function to compute GCD."
        solution = "Use Euclid's algorithm recursively."

    return {"text": text, "solution": solution}


# ---------------------------------------------------
# ---------------- OOPS -----------------------------
# ---------------------------------------------------

def generate_oops(difficulty):

    if difficulty == "Hard":
        text = (
            "Design a class structure for an Online Examination System.\n"
            "Include:\n"
            "- Inheritance\n"
            "- Polymorphism\n"
            "- Encapsulation\n"
            "- Abstract class usage\n\n"
            "Draw class relationships."
        )

        solution = (
            "Create abstract User class.\n"
            "Student and Admin inherit from User.\n"
            "Use encapsulation for marks.\n"
            "Polymorphism in submitExam()."
        )

    else:
        text = "Explain difference between abstraction and encapsulation with example."
        solution = "Abstraction hides implementation; Encapsulation binds data + methods."

    return {"text": text, "solution": solution}


# ---------------------------------------------------
# ---------------- LOGICAL PUZZLES ------------------
# ---------------------------------------------------

def generate_logic(difficulty):

    if difficulty == "Hard":
        text = (
            "You have 3 boxes:\n"
            "1 labelled 'Apples'\n"
            "1 labelled 'Oranges'\n"
            "1 labelled 'Mixed'\n"
            "All labels are wrong.\n"
            "You can pick only ONE fruit from ONE box.\n"
            "How will you correctly label all boxes?"
        )

        solution = (
            "Pick from box labelled 'Mixed'.\n"
            "Since all labels are wrong, it must contain single type.\n"
            "Then deduce remaining logically."
        )

    else:
        text = "A bat and ball cost ₹110. Bat costs ₹100 more than ball. Cost of ball?"
        solution = "Let ball = x, bat = x+100 → 2x+100=110 → x=5."

    return {"text": text, "solution": solution}