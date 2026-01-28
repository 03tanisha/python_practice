# recursion

# factorial
def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num-1)

# sum of first n numbers
def sum_n(num):
    if num == 1:
        return 1
    else:
        return num + sum_n(num-1)

# count digit in a num
def count_n(num):
    if num == 1:
        return 1
    else:
        return 1 + count_n(num//10)



if __name__ == "__main__":
    num = 5
    print("factorial of num:", fac(num))

    num = 5
    print("sum of numbers:", sum_n(num))

    num = 1234566
    print("count the numbers:", count_n(num))


