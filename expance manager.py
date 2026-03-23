# Expense Tracker Project

expenses = []  # list of all expenses

print("Welcome to Expense Tracker : Kharch Kam Kiya Karo")

while True:
    print("=====MENU======")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

    if choice == 1:
        date = input("Kis Date Par Kharcha Kiya? (DDMMYY): ")
        category = input("Kis Type Ka kharcha hai? (food, travel, makeup, books): ")
        description = input("Short description: ")
        amount = float(input("Kitne ka kharcha hai?: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Done Bro, Expense Added Successfully ✅")

    elif choice == 2:
        if(len(expenses)==0):
            print("No Expenses Found . Jao Pahle Kharche Karo")
        else:
            print("Ye hai Apke Pura kharcha")
            count=0
            for ex in expenses:
                
                print(f"Kharcha No. {count} -> Date: {ex['date']} |  Category: {ex['category']} | Amount: {ex['amount']}")
                count += 1
    elif choice==3:
        total=0
        for ex in expenses:
            total=total+ex["amount"]
        print(total)
    elif choice==4:
        print("Exit Done ")
        break
    else:
        print("invalid Input")