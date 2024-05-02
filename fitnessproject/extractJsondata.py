import re

data = """
{'text': ' Sure, here is a study plan for learning Python programming language in 10 days:\n```json\n

{\n    "Day 1": "Introduction to Python: Installing and Setting Up",\n    "Day 2": "Variables and Data Types in Python",\n    "Day 3": "Control Flow: If Statements, Loops, and Break Statements",\n    "Day 4": "Functions and Modules in Python",\n    "Day 5": "Lists, Tuples, and Dictionaries in Python",\n    "Day 6": "Object-Oriented Programming in Python: Classes and Methods",\n    "Day 7": "Exception Handling in Python",\n    "Day 8": "Files and Input/Output Operations in Python",\n    "Day 9": "Regular Expressions in Python",\n    "Day 10": "Final Project",\n}

\n```\nThis study plan covers the basic concepts of Python programming, from installation and setting up the development environment to regular expressions and object-oriented programming. The final day is left open for the student to work on a final project of their choice.\n\nLet me know if you have any questions about this study plan or if there\'s anything else I can help you with!</s>}'
"""

# Define regex pattern to extract JSON data between curly braces
pattern = r'\{([^{}]*)\}'

# Find all matches using the pattern
matches = re.findall(pattern, data, re.DOTALL)

# Print the matches
for match in matches:
    print(match.strip())
