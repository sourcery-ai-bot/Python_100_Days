print("Welcome to the Tip Calculator")
bill = int(input("What was the total bill ? "))
tip_percent = int(input("What percentage tip would you like to give ? 10, 12 ,or 15 ?"))

total_bill = bill * (1 + (tip_percent/100))
            # bill * (1 + 0.12) => bill * 1.12
no_of_people = int(input("How many people to split the bill ?"))
each_pay = round(total_bill/no_of_people,2)

print(f"Each Person should pay : ${each_pay}")


