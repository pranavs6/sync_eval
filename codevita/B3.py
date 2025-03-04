bal = int(input())
transactions = int(input())
operations_commit = []
overall = []
temp = 0

for transaction in range(transactions):
    ops = input().split()
    option = ops[0].lower()

    if len(ops) == 2:
        amt = int(ops[1])

    if option == "read":
        print(max(0, bal))

    elif option == "credit":
        temp = temp + amt
        operations_commit.append(-amt)
        # print("Credit", bal, temp)

    elif option == "debit":
        temp = temp - amt
        operations_commit.append(+amt)
        # print("Debit", bal, temp)

    elif option == "commit":
        # print("Commit", operations_commit)
        bal = bal + temp
        # print(bal, temp)
        overall.append([operations_commit.copy(), bal])
        temp = 0
        operations_commit = []

    elif option == "abort":
        amt -= 1
        if 0 <= amt < len(operations_commit):
            # print("BeforeAbort", operations_commit, bal)
            bal += operations_commit[amt]
            operations_commit.pop(amt)
            # print("Aborted", operations_commit, bal)

    elif option == "rollback":
        amt -= 1
        if 0 <= amt < len(overall):  
            # print("BeforeRollback", overall, bal)
            bal = overall[amt][1]
            operations_commit = []
            temp = 0
            # print("RolledBack", overall, bal)

