import random

def getRandomInteger(min, max):
    """
    Generates a random integer between min and max .
    
    Parameters:
    min: The minimum possible value.
    max: The maximum possible value.
    
    Returns:
    int: A randomly generated integer within the specified range.
    """
    return random.randint(min_value, max_value)

def getRandomOperator():
    """
    Randomly selects a mathematical operator from '+', '-', or '*'.
    
    Returns:
    str: A randomly selected operator.
    """
    return random.choice(['+', '-', '*'])

def getMathProblem(num1, num2, operator):
    """
    Generates a math problem and its correct answer based on the operator.
    
    Parameters:
    num1 (int): The first operand.
    num2 (int): The second operand.
    operator (str): The operator ('+', '-', or '*') to use in the problem.
    
    Returns:
    tuple: A tuple containing the problem as a string and the correct answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    
    # Calculate the answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator == '*'
        answer = num1 * num2
    
    return problem, answer

def mathQuiz():
    """
    Starts the math quiz game, presenting a series of questions and calculating the score based on correct answers.
    """
    score = 0  # Initialize score
    totalQuestions = 5  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(totalQuestions):
        # Generate random numbers and an operator
        num1 = getRandomInteger(1, 10)
        num2 = getRandomInteger(1, 5)
        operator = getRandomOperator()

        # Generate the problem and calculate the answer
        problem, correctAnswer = getMathProblem(num1, num2, operator)
        
        print(f"\nQuestion: {problem}")
        
        # Error handling for user input
        try:
            userAnswer = int(input("Your answer: "))
            
            if userAnswer == correctAnswer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correctAnswer}.")
                
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"\nGame over! Your score is: {score}/{totalQuestions}")

if __name__ == "__main__":
    math_quiz()
