#Sum of a List

l = [4, 17, 2, 9, 33, 7, 15]
Totalsum = 0
largest=l[0]
for num in l:
    print(num)
    Totalsum=num+Totalsum
    if num > largest:
        largest = num
print(Totalsum)
print(largest)
