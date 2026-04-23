# function to compute ticket price
def get_price(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5

total = 0

while True:
    choice = input("Do you want to continue? (Yes/No): ")

    if choice.lower() != "yes":
        break

    last_name = input("Enter last name: ")
    miles = int(input("Enter miles from downtown Chicago: "))

    price = get_price(miles)
    total += price

    print(f"{last_name} ticket price: ${price}")

print(f"Total price of all tickets: ${total}")