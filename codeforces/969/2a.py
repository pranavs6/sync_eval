import heapq

def process_operations(n, m, arr, operations):
    arr = list(set(arr))
    n = len(arr)

    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)

    freq = {x: arr.count(x) for x in arr}

    res = []
    for op, l, r in operations:
        for i in range(n):
            if l <= arr[i] <= r:
                heapq.heappush(max_heap, -arr[i]) 
                freq[arr[i]] -= 1

                if op == "+":
                    arr[i] += 1
                else:
                    arr[i] -= 1

                if arr[i] in freq:
                    freq[arr[i]] += 1
                else:
                    freq[arr[i]] = 1

                heapq.heappush(max_heap, -arr[i])

        while freq[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        
        res.append(-max_heap[0])

    return res

resmain = []

# Input Reading and Handling
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    operations = [input().split() for _ in range(m)]
    operations = [(op, int(l), int(r)) for op, l, r in operations]
    
    resmain.append(process_operations(n, m, arr, operations))

for itr in resmain:
    print(" ".join(map(str, itr)))
