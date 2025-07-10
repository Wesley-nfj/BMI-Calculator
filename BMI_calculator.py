def get_values():
    weight= float(input("Enter your weight in kg: "))
    height= float(input("Enter your height m: "))
    BMI = (weight / height**2)

    print(f" Your Body Mass Index is : {BMI:.2f}")
    if BMI < 18.5:
        print("You are underweighted")
        print("Tip: Eat more calories and try to see a doctor")
    elif 18.5<= BMI <= 24.9:
        print("You have a normal weight!")
        print("Tip: Keep up with the good habits and the balanced diet.")
    elif 24.9 < BMI <= 29.9:
        print("You are Overweighted")
        print("Tip: Do regular workouts and eat healtier meals.")
    elif BMI > 29.9:
        print("You are Obese")
        print("Tip: Consider seeing a doctor and a fitness coach")

print("Body Mass Index Calculator- Lets calculate your BMI")

while True:
 choice= input("Do you want to get started? 'yes' or 'no' : ").lower()
 if choice == 'yes':
    get_values()
 elif choice.lower()== 'no':
    break
 else:
    print("Please enter a valid input!")





