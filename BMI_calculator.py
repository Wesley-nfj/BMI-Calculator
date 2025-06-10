def get_values():
    weight= float(input("Enter your weight in kg: "))
    height= float(input("Enter your height m: "))
    BMI = (weight / height**2)

    print(f" Your Body Mass Index is : {BMI:.2f}")
    if BMI < 18.5:
        print("You are underweighted")
    elif BMI > 18.5 and BMI < 24.9:
        print("You have a normal weight!")
    elif BMI > 25 and BMI < 29.9:
        print("You are Overweighted")
    elif BMI > 30:
        print("You are Obese")

print("Body Mass Index Calculator- Lets calculate your BMI")

while True:
 choice= input("Do you want to get started? 'yes' or 'no' : ").lower()
 if choice == 'yes':
    get_values()
 elif choice.lower()== 'no':
    break
 else:
    print("Please enter a valid input!")





