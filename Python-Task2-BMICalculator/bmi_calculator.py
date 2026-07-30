#BMI CALCULATOR 

def get_positive_number(prompt):
    while True:
        value = input(prompt)
        try:
            number = float(value)
            if number <= 0:
                print("Error: Please enter a positive number.")
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid number (not text).")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = get_positive_number("Enter your weight in kg: ")
height = get_positive_number("Enter your height in m: ")

bmi = weight / (height ** 2)
category = classify_bmi(bmi)

print(f"\nYour BMI is: {round(bmi, 2)}")
print(f"Category: {category}")
