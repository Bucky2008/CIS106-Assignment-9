# function to compute square footage
def compute_square_footage(length, width, height):
    area = (2 * length * width) + (2 * length * height) + (2 * width * height)
    return area

# main program loop
while True:
    choice = input("Do you want to calculate paint needed? (Yes/No): ")

    if choice.lower() != "yes":
        print("Program ended.")
        break

    # input phase
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    # process phase
    square_feet = compute_square_footage(length, width, height)
    gallons_needed = square_feet / 50

    # output phase
    print("Total square footage:", square_feet)
    print("Gallons of paint needed:", gallons_needed)
    print("-----------------------------")