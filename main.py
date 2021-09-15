def getInputs():
    num = [0,0,0,0,0]

    for i in range(5):
        num[i] = input("What is a number? ")

    return num

def getSum(num):
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])

    return sum

def main():
    num = getInputs()
    sum = getSum(num)

    print("Number is " + str(sum))

main()