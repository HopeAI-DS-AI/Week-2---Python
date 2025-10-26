class MultipleFuncs():
    def Subfields():
        a = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print("The Subfields are:")
        for i in a:
            print(i)
    def OddEven():
        num = int(input("Enter the number: "))
        if ((num % 2) == 0):
            print(num, " is Even Number")
        else:
            print(num, " is Odd Number")
    def eligibility():
        gender = str(input("Your Gender: "))
        age = int(input("Your Age: "))
        if (gender == "Female") and (age > 18):
            print("Eligible")
        elif (gender == "Male") and (age > 21):
            print("Eligible")
        else:
            print("Not Eligible")
    def percentage():
        Subject1 = int(input("Subject1 = "))
        Subject2 = int(input("Subject2 = "))
        Subject3 = int(input("Subject3 = "))
        Subject4 = int(input("Subject4 = "))
        Subject5 = int(input("Subject5 = "))
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        Percentage = Total/5
        print("Total: ", Total)
        print("Percentage: ", Percentage) 
    def triangle():
        height = int(input("Height: "))
        breadth = int(input("Breadth: "))
        area = (height * breadth)/2
        print("area formula = (Height * Breadth) / 2")
        print("Area of Triangle: ", area)
        height1 = int(input("Height1: "))
        height2 = int(input("Height2: "))
        breadth = int(input("Breadth: "))
        print("Perimeter formula = Height1 + Height2 + Breadth")
        perimeter = height1 + height2 + breadth
        print("Perimeter of Triangle: ", perimeter)
