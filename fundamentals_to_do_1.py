for num in range(-300, 1, 3):
    if num == -3 or num ==-6:
        continue
    print(num)

num = 2000

while num <= 5280:
    print(num)
    num += 1

for num in range(1,101):
    if num % 10 ==0:
        print("Coding Dojo")
    elif num %5 == 0:
        print("Coding")
    else:
        print(num)

lowNum = 2
highNum = 9
mult = 3

for num in range(highNum, lowNum -1, -1):
    if num % mult == 0:
        print(num)