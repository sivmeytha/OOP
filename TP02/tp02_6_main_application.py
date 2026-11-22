from tp02_1_greeting import Greeting
from tp02_2_rectangle import Rectangle
from tp02_3_equation import EquationCalculator
from tp02_4_hundreds_counter import HundredsCounter
from tp02_5_lucky_number import CheaterGame

def main():
    while True:
        print("\n=========== TP02 Python OOP ==========")  
        print("1. Greeting")
        print("2. Rectangle")
        print("3. Equation Calculator")
        print("4. Hundreds Counter")
        print("5. Cheater Game")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            name = input("Enter your name: ")
            g = Greeting(name)
            print(g.get_greeting())
            
        elif choice == '2':
            try:
                width = float(input("Enter the width: "))
                height = float(input("Enter the height: "))
                if width < 0 or height < 0:
                    print("Error: Dimensions cannot be negative.")
                    continue
                rect = Rectangle(width, height)
                print(f"Perimeter: {rect.calculate_perimeter()}")
                print(f"Area: {rect.calculate_area()}")
            except ValueError:
                print("Invalid input! Please enter valid numeric values.")
                
        elif choice == '3':
            try:
                y = float(input("Enter y: "))
                z = float(input("Enter z: "))
                eq = EquationCalculator(y, z)
                print(f"Calculated x: {eq.calculate_x()}")
            except ValueError:
                print("Invalid input! Please enter valid numeric values for y and z.")
                
        elif choice == '4':
            try:
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Error: Number must be non-negative.")
                    continue
                counter = HundredsCounter(num)
                print(f"Complete hundreds: {counter.get_complete_hundreds()}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '5':
            try:
                num = int(input("Enter an integer: "))
                game = CheaterGame(num)
                print(f"Result (number plus one): {game.get_next_number()}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
        elif choice == '0':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid option! Please select a valid number from the menu (0-5).")

if __name__ == "__main__":
    main()