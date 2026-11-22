student_name = "Eliza"
student_age = 20
student_gpa = 3.5
is_passed = True

print("\n========== A. Primitive/Built-in Data Types ==========")
print("\nStudent Name: ", student_name, type(student_name))
print("Student Age: ", student_age, type(student_age))
print("Student Gpa: ", student_gpa, type(student_gpa))
print("Student is passed: ", is_passed, type(is_passed))

student_names = ["Lacima", "Jady", "GMengz", "Mann Doss"]
student_ages = (19, 20, 21, 18)
student_gpas = {3.5, 2.0, 2.5, 4.0}
student_record = {
    "name": "Lacima",
    "age": 19,
    "gpa": 3.5
}

print("\n========== B. Collection and Reference Types ==========")
print("\nStudent Names: ", student_names, type(student_names))
print("Student Ages: ", student_ages, type(student_ages))
print("Student Gpas: ", student_gpas, type(student_gpas))
print("Student Record: ", student_record, type(student_record))

class Student:
    def __init__(self, name, age, gpa):
        self.name = name 
        self.age = age
        self.gpa = gpa

student_object = Student("Lacima", 19, 3.5)

print("\n***** Object Output *****")
print("\nObject Type: ", student_object, type(student_object))
print("Object Name attribute: ", student_object.name, type(student_object.name))
print("Object Age attribute: ", student_object.age, type(student_object.age))
print("Object Gpa attribute: ", student_object.gpa, type(student_object.gpa))

num_literal = 19
num_float_literal = 3.5
str_literal = "Lacima" 
bool_literal = True
none_literal = None

list_literal = ["Lacima", "Jady"]
tuple_literal = (19, 20)
set_literal = {3.5, 2.0}
dict_literal = {"name": "Lacima", "age": 19}

print("\n========== C. Literals in Python ==========")
print("\nNumeric Integer Literal: ", num_literal, type(num_literal))
print("Numeric Float Literal: ", num_float_literal, type(num_float_literal))
print("String Literal: ", str_literal, type(str_literal))
print("Boolean Literal: ", bool_literal, type(bool_literal))
print("None Literal: ", none_literal, type(none_literal))
print("Collection Literal (List): ", list_literal, type(list_literal))
print("Collection Literal (Tuple): ", tuple_literal, type(tuple_literal))
print("Collection Literal (Set): ", set_literal, type(set_literal))
print("Collection Literal (Dict): ", dict_literal, type(dict_literal))
print("\n")