import json
import random

def quiz(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    questions = data
    random.shuffle(questions) # shuffle the questions
    score = 0
    counter = 0
    incorrect_answers = []  # Store incorrect answers
    for question in questions:
        if counter == 40:
            break
        print(question['question'])
        answer = input('Inserisci la tua risposta (0 o 1): ')
        if int(answer) == question['answer']:
            score += 1
        else:
            incorrect_answers.append(question)  # Add incorrect answer to the list
        counter += 1
    print(f'Hai totalizzato {score} punti su 40')

    # Display incorrect answers
    print("\nRisposte errate:")
    for question in incorrect_answers:
        print(question['question'])
        print(f"Risposta corretta: {question['answer']}")
        print()

quiz('quiz.json')
