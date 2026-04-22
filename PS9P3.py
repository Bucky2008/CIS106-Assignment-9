# function to compute out-the-door price
def compute_price(msrp, make, model, electric):
    
    # determine discount
    if make.lower() == "honda" and model.lower() == "accord":
        discount_rate = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        discount_rate = 0.15
    elif electric.lower() == "y":
        discount_rate = 0.30
    else:
        discount_rate = 0.05

    discount = msrp * discount_rate
    new_price = msrp - discount
    total_price = new_price * 1.07  # add 7% tax

    return total_price


# main program
total_msrp = 0
total_sales = 0

while True:
    choice = input("Do you want to enter a car? (Yes/No): ")

    if choice.lower() != "yes":
        break

    # input
    make = input("Enter make: ")
    model = input("Enter model: ")
    electric = input("Is it electric? (Y/N): ")
    msrp = float(input("Enter MSRP: "))

    # process
    final_price = compute_price(msrp, make, model, electric)

    # accumulate totals
    total_msrp += msrp
    total_sales += final_price

    # output
    print("Final price:", round(final_price, 2))
    print("-----------------------")

# final totals
print("Total MSRP:", round(total_msrp, 2))
print("Total Sales Price:", round(total_sales, 2))