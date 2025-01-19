class Transactions:
    def __init__(self, t, a, n, c):
        self.type = t
        self.amount = a
        self.no = n
        self.is_commit = c


def solve():
    T = []
    C = []
    i = 0
    k = 0
    CB = int(input())
    n = int(input())

    for _ in range(n):
        ops = input().strip().split()
        op_type = ops[0]

        if op_type == "credit":
            X = int(ops[1])
            CB += X
            i += 1
            T.append(Transactions("cr", X, i, False))

        elif op_type == "debit":
            X = int(ops[1])
            CB -= X
            i += 1
            T.append(Transactions("d", X, i, False))

        elif op_type == "read":
            print(CB)

        elif op_type == "commit":
            for tx in T:
                tx.is_commit = True
            k += 1
            C.append((k, CB))

        elif op_type == "rollback":
            X = int(ops[1])
            for commit in C:
                if commit[0] == X:
                    CB = commit[1]
                    break

        elif op_type == "abort":
            X = int(ops[1])
            for tx in T:
                if tx.no == X and not tx.is_commit:
                    if tx.type == "cr":
                        CB -= tx.amount
                    elif tx.type == "d":
                        CB += tx.amount


if __name__ == "__main__":
    solve()

