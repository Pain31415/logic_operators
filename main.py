a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        print("Even number")
    else:
        print("Odd number")
else:
    print("NO")