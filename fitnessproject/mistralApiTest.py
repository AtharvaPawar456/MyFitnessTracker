import requests

# URL of the Flask API endpoint
url = 'https://358d-34-147-76-124.ngrok-free.app/api/text'

# Text data to send in the POST request
text_data = "Act as a personal programming teacher, create a study plan for learning python programming language in 10 days, also give the study plan in json format strictly key will be day and the value will me the learning topic"

# Make the POST request
response = requests.post(url, data=text_data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message
    print("Error:", response.status_code)

'''

{'text': ' Sure, here is a study plan for learning Python programming language in 10 days:\n```json\n{\n    "Day 1": "Introduction to Python: Installing and Setting Up",\n    "Day 2": "Variables and Data Types in Python",\n    "Day 3": "Control Flow: If Statements, Loops, and Break Statements",\n    "Day 4": "Functions and Modules in Python",\n    "Day 5": "Lists, Tuples, and Dictionaries in Python",\n    "Day 6": "Object-Oriented Programming in Python: Classes and Methods",\n    "Day 7": "Exception Handling in Python",\n    "Day 8": "Files and Input/Output Operations in Python",\n    "Day 9": "Regular Expressions in Python",\n    "Day 10": "Final Project",\n}\n```\nThis study plan covers the basic concepts of Python programming, from installation and setting up the development environment to regular expressions and object-oriented programming. The final day is left open for the student to work on a final project of their choice.\n\nLet me know if you have any questions about this study plan or if there\'s anything else I can help you with!</s>'}
'''