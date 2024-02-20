def get_user_input():
    while True:
        try:
            height = float(input("Enter your height : "))
            weight = float(input("Enter your weight : "))
            return height, weight
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    unit_system = input("Choose unit system (metric/imperial): ").lower()

    height, weight = get_user_input()

    if unit_system == "metric":
        bmi = (weight / (height ** 2))*10000
    else:
        bmi = (weight / (height ** 2)) * 703

    if bmi < 18.5:
        health_category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        health_category = "Normal weight"
    elif 25 <= bmi < 29.9:
        health_category = "Overweight"
    else:
        health_category = "Obesity"
    print(f"Your BMI is: {bmi}")
    print(f"Health category: {health_category}")

    if health_category == "Normal weight":
        print("Health Information:Your BMI is within the normal weight")
    elif health_category == "Underweight":
        print("Health Information:Your BMI is below the normal range.So yo have to take care of your health.Take some healthy fruits and vegetables to maintain the normal weight.")
    elif health_category == "Overweight":
        print("Health Information: Your BMI is above the normal weight.We suggest you to maintain the proper diet for your health improvement.")
    else:
        print("Health Information: Your BMI is above the normal weight.We suggest you to maintain the proper diet for your health improvement.")

if __name__ == "__main__":
    bmi_calculator()
