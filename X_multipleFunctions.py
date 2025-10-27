class multipleFunctions():
    def OddEven():
        num = int(input("Enter the number: "))
        if ((num % 2) == 1):
            print("Odd Number")
            message = "Odd Number"
        else:
            print("Even Number")
            message = "Even Number"
        return message

    def BMI():
        BMI = int(input("Enter the BMI Index: "))
        if (BMI < 18.5):
            print("Underweight")
            message = "Under Weight"
        elif (BMI < 24.9):
            print("Normal")
            message = "Normal"
        elif (BMI < 29.9):
            print("Over Weight")
            message = "Overweight"
        else: 
            print("Very Over Weight")
            message = "Overweight"
        return message