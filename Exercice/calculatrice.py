def print_welcome_message(): # Function to print a welcome message
    """Prints a welcome message for the calculator."""
    print("Bienvenue sur la mini-calculatrice !")
    
def input_two_number(): # Function to input two numbers from the user
    """Prompts the user to input two numbers."""
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    return num1, num2

def print_menu_and_get_choice(): # Function to print the menu and get the user's choice
    """Prints the menu and returns the user's choice."""
    print("=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    user_choice = input("Entrez votre choix (1-4) : ")

    while user_choice not in ["1", "2", "3", "4"]:

        user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")

    return user_choice

def sum(a, b):# Function to calculate the sum of two numbers
    """Calculates the sum of two numbers."""
    return a + b

def substraction(a, b):# Function to calculate the subtraction of two numbers
    """Calculates the subtraction of two numbers."""
    return a - b

def multiplication(a, b):# Function to calculate the multiplication of two numbers
    """Calculates the multiplication of two numbers."""
    return a * b

def division(a, b):# Function to calculate the division of two numbers
    """Calculates the division of two numbers."""
    if b != 0:
        return a / b
    else:
        print("Erreur : division par zéro")

def run_calculation(user_choice):# Function to run the calculation based on user's choice
    num1, num2 = input_two_number()
    match user_choice:
        case '1':
            result = sum(num1, num2)
        case '2':
            result = substraction(num1, num2)
        case '3':
            result = multiplication(num1, num2)
        case '4':
            result = division(num1, num2)
        case _:
            print("Choix invalide.")
    return result

if __name__ == '__main__':
    print_welcome_message()
    user_choice = print_menu_and_get_choice()
    result = run_calculation(user_choice)
    print(result)