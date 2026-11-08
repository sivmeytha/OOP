class Rectangle:
    def __init__(self, width, height):
        if width < height:
            raise ValueError("Width cannot be smalle than height.")
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height) 
        return perimeter

    def calculate_area(self):
        area = self.width * self.height
        return area

    def display_results(self):
        print(f"Perimeter: {self.calculate_perimeter()}")
        print(f"Area: {self.calculate_area()}")

try:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    rect = Rectangle(width, height)
    rect.display_results()
except ValueError as e:
    print(f"Error: {e}")