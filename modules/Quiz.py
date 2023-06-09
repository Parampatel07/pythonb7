import random

print('''WELCOME TO THE QUIZ!!
The qiuz has 5 questons
You need to get at least a score of 3 to pass the quiz....''')

questions = [{"question": 'Who is considered the "father" of the Python programming language?',
"options": ['1. James Gosling', '2. Larry Page', '3. Guido van Rossum', '4. Dennis Ritchie'],
"correct_answer": 3},
{"question": "Which of the following is not a core data type in Python?",
"options": ['1. Float', '2. Boolean', '3. String', '4. Integer'],
"correct_answer": 2},
{"question": "In which year was Python first released?",
"options": ['1. 1991', '2. 1981', '3. 2000', '4. 1995'],
"correct_answer": 1},
{"question": "From which of the following options was the name of python derived?",
"options": ['1. Python Hunters', "2. Monty Python's Personal Best", '3. SnakeBytesTV', "4. Monty Python's Flying Circus"],
"correct_answer": 4},
{"question": "Which was the first programming language in the world?",
"options": ['1. Python', '2. Whitespace', '3. Fortran', '4. Malbolge'],
"correct_answer": 3}]

score = 0

while True:
    score = 0
    random.shuffle(questions)
    
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        user_input = int(input("Enter the number of the correct option: "))
        
        if user_input == question["correct_answer"]:
            score += 1
    
    print("Your score:", score)
    if score >= 2:
        print('Y O U   W O N!!')
        break
    else:
        print("You lost the quiz.")

print('Goodbye')



