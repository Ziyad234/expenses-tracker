import json

incomes = []
expenses = []



try:
    with open("transactions.json", "r") as file:
        data = json.load(file)

except (FileNotFoundError, json.JSONDecodeError):
    print ("No valid saved data found. Starting fresh")
    data = {
        "incomes": [],
        "expenses": []
    }

incomes = data ["incomes"]
expenses = data ["expenses"]


while True:

    print ("===================================")
    print ("        EXPENSE TRACKER")
    print ("===================================\n")
    print ("1. Add Income")
    print ("2. Add Expense")
    print ("3. View Transactions")
    print ("4. View Balance")
    print ("5. Exit")

    try:
        choice = int(input("Choose an option: "))

    except ValueError:
        print("Please enter valid number")
        continue

    if choice == 5:
        print("Thank you for using our app :)")
        break

    elif choice == 1:
        while True:
            try:
                income = float(input("Enter income amount (RM): "))
                if income <= 0:
                    print("Amount must be greater than 0")
                    continue
                incomes.append(income)
            except ValueError:
                print("Please enter an amount number!")
                continue

            print ("Income added successfully!")
            print (f"You entered RM {income}")
            break

    elif choice == 2:
        while True:
            try:
                expense= float(input("Enter expense amount (RM): "))
                if expense <= 0:
                    print ("Expense must be greater than 0")
                    continue
                expenses.append(expense)

            except ValueError:
                print ("Plese enter an amount number!")
                continue

            print ("Expense added successfully!")
            
            print (f"You spent: {expense:.2f}")
            break
        
    elif choice == 3:
        print("========== TRANSACTIONS ==========")
        for index, income in enumerate(incomes, start=1):
            print (f"Income {index}: RM {income:.2f}")
        print()
        if not incomes:
            print("No transactions found for incomes..")
        print()

        for index, expense in enumerate(expenses, start=1):
            print (f"Expense {index}: RM {expense:.2f}")
        if not expenses:
            print("No transaction found for expenses..")

        input("please enter to continue..")

    elif choice == 4:
        print("========== BALANCE ==========")
        total_income = sum(incomes)
        total_expenses = sum(expenses)
        balance = total_income - total_expenses

        print(f"Your income: RM {total_income:.2f}")
        print(f"Total Expenses: RM {total_expenses:.2f}")
        print("-------------------------------")
        print(f"Balance: {balance:.2f}")
        input("Please enter to continue..")
        print("==============================")


    else:
        print("Invalid option")

data = {
    "incomes": incomes,
    "expenses": expenses
}

try:
    with open ("transactions.json", "w") as file:
        json.dump(data,file, indent=4)
except FileNotFoundError:
        print ("File does not exist")


    
    