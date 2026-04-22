def compute_forecast(month, sales):

    #determine forecast percent
    if month in ["Jan", "Feb", "Mar"]:
        percent = 0.10
    elif month in ["Apr", "May", "Jun"]:
        percent = 0.15
    elif month in ["Jul", "Aug", "Sep"]:
        percent = 0.20
    elif month in ["Oct", "Nov", "Dec"]:
        percent = 0.25
    else:
        percent = 0

    #calculate next month's sales
    next_sales = sales * (1 + percent)

    return next_sales


# input phase + loop
while True:
    user_choice = input("Do you want to run the program? (Yes/No): ")

    if user_choice.lower() != "yes":
        break

    # input phase
    last_name = input("Enter last name: ")
    month = input("Enter month (Jan-Dec): ")
    sales = float(input("Enter sales: "))

    # process phase
    forecast_sales = compute_forecast(month, sales)

    # output phase
    print("----- Forecast Result -----")
    print("Name:", last_name)
    print("Next Month Sales:", format(forecast_sales, ".2f"))
    print()