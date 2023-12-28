# Body Mass Index Calculator

while True:
    try:
        height = int(input("Your Height (IN): "))
        weight = int(input("Your Weight (LBS): "))
    except ValueError:
        print("Please enter a whole number for your height and weight.")
        continue

    if height <= 0 or weight <= 0:
        print("Height and weight must be postive whole numbers.")
        continue
    
    break

BMI = 703 * (weight / (height ** 2))

status = ''

if BMI < 18.5:
    status = 'Underweight'
elif BMI < 25.0:
    status = 'Normal Weight'
elif BMI < 30.0:
    status = 'Overweight'
else:
    status = 'Obese'

print(f'---> Your BMI is {BMI:.1f}.')
print(f'---> Weight Status: {status}')