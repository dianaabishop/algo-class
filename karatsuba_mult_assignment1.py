'''
Karatsuba Multiplication - Assignment #1

In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.
To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. 
You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement 
recursive integer multiplication and/or Karatsuba's algorithm.
So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627
'''


def karatsuba(num1, num2):

    if num1 < 10 or num2 < 10:
        return num1 * num2
    else:
        n = int(len(str(num1)))
        n2 = n/2

        a, b = split(num1)
        c, d = split(num2)

        bd = karatsuba(b, d)
        ac = karatsuba(a, c)
        ad_plus_bc = karatsuba((a+b),(c+d)) - ac - bd

        final_output = ((10**n) * ac)  + ((10**n2) * ad_plus_bc) + bd

        return final_output


def split(num):
    num_string = str(num)

    if (len(num_string)%2) == 0:
        num1, num2 = num_string[:len(num_string)/2], num_string[len(num_string)/2:]
    else:
        num1, num2 = num_string[:(len(num_string)/2)+1], num_string[(len(num_string)/2)+1:]
    num1, num2 = int(num1), int(num2)
    return (num1, num2)

def main():

    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967627

    karatsuba_result = karatsuba(num1, num2)
    print karatsuba_result


if __name__ == "__main__":
    main()
