first_num = input("put the first number:")
second_num = input("put the second number:")

sum_result = int(first_num) + int(second_num)

subtraction_result = int(first_num) - int(second_num)

multiplication_result = int(first_num) * int(second_num)

division_result = int(first_num) / int(second_num) if second_num != 0 else None


print(f"Sum: {sum_result}")
print(f"Subtraction: {subtraction_result}")
print(f"Multiplication: {multiplication_result}")
print(f"Division: {division_result}")