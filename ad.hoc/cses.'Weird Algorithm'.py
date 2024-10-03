n = int(input())

n_vals = [n]

while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = 3*n + 1

    n_vals.append(n)

print(' '.join(str(x) for x in n_vals))