bal = int(input())
transactions = int(input())
operations_commit = []
overall = []
temp = 0

for transaction in range(transactions):
    ops = list(map(str, input().split()))
    if len(ops) == 2:
        amt = int(ops[1])
    option = ops[0].lower()

    if option == "read":
        print(max(0,bal))

    elif option == "credit":
        temp = temp + amt
        operations_commit.append(-amt)
        #print("Credit", bal, temp)

    elif option == "debit":
        temp = temp - amt
        operations_commit.append(+amt)
        #print("Debit", bal, temp)

    elif option == "commit":
        #print("Commit", operations_commit)
        bal = bal + temp
        #print(bal, temp)
        overall.append([operations_commit, bal])
        temp = 0
        operations_commit = []

    elif option == "abort":
        amt -= 1
        #print("BeforeAbort", operations_commit, bal)
        if len(operations_commit) >= 1:
            bal += operations_commit[amt]
            operations_commit.pop(amt)
        #print("Aborted", operations_commit, bal)

    elif option == "rollback":
        amt -= 1
        #print("BeforeRollback", overall, bal)
        if overall:
            bal = overall[amt][1]
            operations_commit = []
            temp = 0
        #print("RolledBack", overall, bal)

