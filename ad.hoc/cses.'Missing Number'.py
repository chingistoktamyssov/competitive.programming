n = int(input())
lst = [int(x) for x in input().split()]
lst.sort()
found = False

for i in range(n-1):
    if lst[i] != i+1:
        found=True
        print(i+1)
        break

if not found:
    print(n)