import csv

import csv

def load_questions(filename):
    """
    Load questions from a CSV file.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the questions.
    """
    questions = []
    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            questions.append(row)
    return questions

def ask_question(question):
    """
    Asks a question and prompts the user to enter their answer.

    Args:
        question (dict): A dictionary containing the question, options, and answer.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    print("\n" + question['Question'])
    options = [question['Option 1'], question['Option 2'], question['Option 3'], question['Option 4']]
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    return options[int(user_answer) - 1] == question['Answer']

def run_quiz():
    questions = load_questions('quiz_questions.csv')
    score = 0
    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print("Wrong. The correct answer was " + question['Answer'])
    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()