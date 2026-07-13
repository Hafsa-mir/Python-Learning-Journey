# ==========================================
# Project: Screen Time Calculator
# Topic: Python Operators Mini Project
# ==========================================

mobile_hours = float(input("Enter Mobile Screen Time (hours): "))
laptop_hours = float(input("Enter Laptop Screen Time (hours): "))
tv_hours = float(input("Enter TV Screen Time (hours): "))

# Arithmetic Operators
total_screen_time = mobile_hours + laptop_hours + tv_hours
average_screen_time = total_screen_time / 3
remaining_time = 8 - total_screen_time

# Comparison Operators
more_than_8_hours = total_screen_time > 8
mobile_more_than_laptop = mobile_hours > laptop_hours
laptop_equal_tv = laptop_hours == tv_hours

# Logical Operators
healthy_usage = total_screen_time <= 8 and mobile_hours <= 5
high_usage = total_screen_time > 8 or mobile_hours > 5

