
# ATM Transaction Sequence Simulation

balance = float(input("Enter initial account balance: "))

total_deposits = 0
total_withdrawals = 0

successful_deposits = 0
successful_withdrawals = 0
rejected_transactions = 0

transactions = []

n = int(input("Enter number of transactions: "))

# Process transactions
for i in range(n):

    print("\nTransaction", i + 1)

    transaction_type = input(
        "Enter transaction type (deposit/withdraw): "
    ).lower()

    amount = float(input("Enter transaction amount: "))

    if amount <= 0:
        print("Invalid amount! Transaction rejected.")
        rejected_transactions += 1
        transactions.append(("Invalid", amount, "Rejected"))

    elif transaction_type == "deposit":

        balance += amount
        total_deposits += amount
        successful_deposits += 1

        print("Deposit successful.")

        transactions.append(("Deposit", amount, "Successful"))

    elif transaction_type == "withdraw":

        if amount > 10000:
            print("Withdrawal limit exceeded!")
            rejected_transactions += 1

            transactions.append(("Withdraw", amount, "Rejected"))

        elif amount > balance:
            print("Insufficient balance!")
            rejected_transactions += 1

            transactions.append(("Withdraw", amount, "Rejected"))

        else:
            balance -= amount
            total_withdrawals += amount
            successful_withdrawals += 1

            print("Withdrawal successful.")

            transactions.append(("Withdraw", amount, "Successful"))

    else:
        print("Invalid transaction type!")
        rejected_transactions += 1

        transactions.append(("Invalid", amount, "Rejected"))

# Display transaction summary
print("\n====== ATM TRANSACTION SUMMARY ======")

print("\nTransaction Details:")

for transaction in transactions:
    transaction_type, amount, status = transaction

    print(transaction_type, amount, status)

print("\nTotal Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)

print("Successful Deposits:", successful_deposits)
print("Successful Withdrawals:", successful_withdrawals)

print("Rejected Transactions:", rejected_transactions)

print("Final Account Balance: Rs.", balance)
