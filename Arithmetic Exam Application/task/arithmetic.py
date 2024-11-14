import random

# Display prompt for user to select level
print("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9 \n2 - integral squares of 11-29")

# Validate user input for level selection
while True:
    try:
        user_input_level = int(input())
        if user_input_level == 1 or user_input_level == 2:
            break
        else:
            print("Invalid input. Choose 1 or 2.")
    except ValueError:
        print("Invalid input. Choose 1 or 2.")

# Set the level and initialize the correct answer count
level = user_input_level
correctas = 0
level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"

# Level 1: Simple operations with numbers 2-9
if level == 1:
    for i in range(5):  # Repeat 5 times
        var_x = random.randint(2, 9)
        var_y = random.randint(2, 9)
        operador = random.choice(["+", "-", "*"])

        # Create the expression in the format "number operator number"
        expresion = f"{var_x} {operador} {var_y}"

        # Calculate the correct answer
        if operador == "+":
            respuesta_correcta = var_x + var_y
        elif operador == "-":
            respuesta_correcta = var_x - var_y
        elif operador == "*":
            respuesta_correcta = var_x * var_y

        # Display the expression to the user
        print(expresion)

        # Get and validate user input
        while True:
            try:
                av = int(input())  # Get user's answer as an integer
                if av == respuesta_correcta:
                    print("Right!")
                    correctas += 1  # Increment correct count if answer is correct
                    break
                else:
                    print("Wrong!")
                    break
            except ValueError:
                print("Incorrect format.")  # Ask again if input is not a valid integer

# Level 2: Integral squares of numbers between 11 and 29
elif level == 2:
    for i in range(5):  # Repeat 5 times
        numero = random.randint(11, 29)
        correct_answer = numero ** 2

        # Display the number and prompt for the square
        print(f"{numero}")

        # Get and validate user input
        while True:
            try:
                av = int(input())
                if av == correct_answer:
                    print("Right!")
                    correctas += 1  # Increment correct count if answer is correct
                    break
                else:
                    print("Wrong!")
                    break
            except ValueError:
                print("Incorrect format.")  # Ask again if input is not a valid integer

# Display the final score and ask if user wants to save it
print(f"Your mark is {correctas}/5. Would you like to save your result to the file? Enter yes or no.")
save_result = input().strip().lower()

if save_result in ["yes", "y"]:
    print("What is your name?")
    username = input().strip()

    # Open the file in append mode and write the result
    with open("results.txt", "a") as file:
        file.write(f"{username}: {correctas}/5 in level {level} ({level_description})\n")

    # Confirm that the result is saved
    print('The results are saved in "results.txt".')







