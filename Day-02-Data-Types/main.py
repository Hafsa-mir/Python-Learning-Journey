# Project: Python Data Type Analyzer

student_name = input("Enter Your Name: ")
student_age = int(input("Enter Your Age: "))
student_cgpa = float(input("Enter Your CGPA: "))
is_graduated = input("Are you graduated? (True/False): ") == "True"

print("\n========== STUDENT INFORMATION ==========")
print(f"Name       : {student_name}")
print(f"Age        : {student_age}")
print(f"CGPA       : {student_cgpa}")
print(f"Graduated  : {is_graduated}")

print("\n========== DATA TYPES ==========")
print(f"student_name -> {type(student_name)}")
print(f"student_age -> {type(student_age)}")
print(f"student_cgpa -> {type(student_cgpa)}")
print(f"is_graduated -> {type(is_graduated)}")
