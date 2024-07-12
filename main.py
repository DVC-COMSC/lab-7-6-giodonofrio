
def getInput():
    uservalues = input()
    numbers = list(map(int, uservalues.split()))
    return numbers


def makeReverse(numbers):
    temp = 0
    reverseList = []
    
    for i in range(1,len(numbers)+1):
        reverseList.append(numbers[-i])

    return reverseList


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
