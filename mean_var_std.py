def calculate(numbers):
    # Check if the input list has exactly 9 numbers
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
