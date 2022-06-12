pos = 0
neg = 0
sum_pos = 0
n = int(input("How many terms? "))
for i in range(0, n):
    num = int(input("Enter number: "))
    print(num, "->", num*num)
    if num > 0:
        sum_pos += num
        pos += 1
    else:
        neg += 1
print("\nTotal sum of positive integers: ", sum_pos)
print("Total number of positive integers: ", pos)
print("Total number of negative integers: ", neg)
