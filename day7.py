# recusion

# print n till 1
def count_n(num):
    if num == 0 :
        return
    print(num)
    count_n(num-1)
#
# if __name__ == "__main__":
#     num = 5
#     count_n(num)


# sum of digits
def sum_digits(n):
    if n == 0 :
        return 1
    # print(n)
    else:
        last_digit = n % 10
        remain = n // 10

        return last_digit + sum_digits(remain)

if __name__ == "__main__":
    num = 5
    print(count_n(num))

    n = 12345

    print(sum_digits(n))


# xⁿ = x * xⁿ⁻¹
# find power
def find_power(x,n):
    if n == 0 :
        return 1
    else:
        return x * find_power(x, n-1)

# x = 2
# n = 5

if __name__ == "__main__":
    x = 2
    n = 5
    print(find_power(x,n))


# revers a num
def rev_num(n,rev=0):
    if n == 0 :
        return rev
    else:
        # n = 1234/


        return rev_num(n // 10 ,rev * 10 + n % 10)



if __name__ == "__main__":
    n = 123
    print(rev_num(n))