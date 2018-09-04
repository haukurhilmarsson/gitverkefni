count = 1
num1 = 1
num2 = 2
num3 = 3
tala = 1
n = int(input("Enter the length of the sequence: ")) # Do not change this line
while count<=n:
    if count <=3:
        print(tala)
        tala += 1
    if count>3:
        tala = num2+num3+num1
        print(tala)
        num1 = num2 
        num2 = num3 
        num3 = tala
    count += 1
    


    