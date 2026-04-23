def compute_assessed_value(county, market_value):
    if county.lower() == "cook":
        percent = 0.90
    elif county.lower() == "dupage":
        percent = 0.80
    elif county.lower() == "mchenry":
        percent = 0.75
    elif county.lower() == "kane":
        percent = 0.60
    else:
        percent = 0.70

    return market_value * percent


total_market = 0
total_assessed = 0

while True:
    choice = input("Do you want to enter a home? (Yes/No): ").lower()
    
    if choice != "yes":
        break

    county = input("Enter county: ")
    market_value = float(input("Enter market value: "))

    assessed_value = compute_assessed_value(county, market_value)

    print("Assessed Value:", assessed_value)

    total_market += market_value
    total_assessed += assessed_value

print("\nTotal Market Value:", total_market)
print("Total Assessed Value:", total_assessed)