"""
MIKISA FAITH DEBORAH
S26B38/038
CUSTOMER ACCOUNT PROGRAM
"""
def check_eligibility(age, account_type):
    if account_type == "S" or account_type == "C":
        return True
    elif account_type == "T" and age <= 25:
        return True
    else:
        return False
 
 
def get_minimum_deposit(account_type):
    if account_type == "S":
        return 50000
    elif account_type == "C":
        return 100000
    elif account_type == "T":
        return 20000
    else:
        return 0
 
 
def open_account(name, age, account_type):
    if not check_eligibility(age, account_type):
        if account_type == "T":
            print("Sorry, Student accounts are only for age 25 or below.")
        else:
            print("Sorry, this account type is not valid for this customer.")
        return None
 
    deposit_amount = float(input("Initial deposit: "))
    minimum = get_minimum_deposit(account_type)
    account_names = {"S": "Savings", "C": "Current", "T": "Student"}
 
    if deposit_amount < minimum:
        print(f"Deposit too low. Minimum for {account_names[account_type]} is {int(minimum)} UGX.")
        return None
    else:
        account = {"name": name, "type": account_type, "balance": deposit_amount}
        print(f"Account opened successfully for {name}. Balance: {int(deposit_amount)} UGX")
        return account
 
 
def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be positive.")
        return False
    else:
        account["balance"] += amount
        print(f"Deposited {int(amount)} UGX. New balance: {int(account['balance'])} UGX")
        return True
 
 
def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return False
    else:
        if amount > account["balance"]:
            print("Insufficient funds for this withdrawal.")
            return False
        else:
            account["balance"] -= amount
            print(f"Withdrew {int(amount)} UGX. New balance: {int(account['balance'])} UGX")
            return True
 
 
def show_benefits(account_type):
    if account_type == "S":
        print("Savings benefits: interest on balance, free withdrawals at CityLink ATMs.")
    elif account_type == "C":
        print("Current benefits: unlimited transactions, chequebook access, overdraft eligibility.")
    elif account_type == "T":
        print("Student benefits: no monthly fees, free mobile banking, low minimum balance.")
    else:
        print("No benefits information available for this account type.")
 
 
def main():
    num_customers = int(input("How many customers? "))
 
    accounts_opened = 0
    total_deposited = 0
 
    for i in range(1, num_customers + 1):
        print(f"--- Customer {i} ---")
        name = input("Name: ")
        age = int(input("Age: "))
        account_type = input("Account type (S/C/T): ").strip().upper()
 
        account = open_account(name, age, account_type)
 
        if account is None:
            continue
 
        accounts_opened += 1
        total_deposited += account["balance"]
 
        while True:
            print(f"{name}'s account menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Benefits")
            print("4. Done with this customer")
            choice = input("Choose an option: ").strip()
 
            if choice == "1":
                amount = float(input("Deposit amount: "))
                if deposit(account, amount):
                    total_deposited += amount
            elif choice == "2":
                amount = float(input("Withdraw amount: "))
                if withdraw(account, amount):
                    total_deposited -= amount
            elif choice == "3":
                show_benefits(account["type"])
            elif choice == "4":
                break
            else:
                print("Invalid option, please choose 1-4.")
 
    print("===== SESSION SUMMARY =====")
    print(f"Accounts opened: {accounts_opened}")
    print(f"Total deposited: {int(total_deposited)} UGX")
 
 
if __name__ == "__main__":
    main()