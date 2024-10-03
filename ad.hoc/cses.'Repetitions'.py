string = input()

last = 'a'
count = 0
largest_count = 0
for i in string:
    if last == i:
        count += 1
        if count > largest_count:
            largest_count = count
    else:
        count = 1
        last = i

print(largest_count)