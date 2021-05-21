# Loop 1

# for i in range(5):
#     k = 1
#     for j in range(i+1):
#         print(k, end = '')
#         k += 1
#     print()


# Loop 2

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end = '')
#     print()


# Loop 3
#
# n = input('Please enter your desired no.:')
# sum_num =0
# for i in range(int(n) +1):
#     sum_num += i
#
# print(sum_num)


# Loop 4

# n = int(input('Please enter your desired no.:'))
# for i in range (1,11):
#     table = n*i
#     print(table)


# Loop 5
#
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#
# for num in list1:
#     if (num % 5 == 0 and num <= 150):
#         print(num)


# Loop 6

# n = int(input('Enter your Number:'))
# count = 0
# while (n != 0):
#     n //= 10
#     count += 1
#
# print(count)


# Loop 7

# for i in range(5):
#     for j in range(5-i, 0, -1):
#         print(j, end = "")
#
#     print()


# Loop 8

# list1 = [10, 20, 30, 40, 50]
# start = len(list1) - 1
# stop = -1
# step = -1
# for i in range(start, stop, step) :
#     print(list1[i])


# Loop 9

# for i in range(-10,0):
#     print(i)


# Loop 10

# for i in range(5):
#     print(i)
# else:
#    print('Done!')


   # Loop 11



# Loop 12
#
num1 = 0
num2 = 1
sum1 = 0
n = int(input('Enter your number:'))
for i in range(0,n):
    print(num1, end= " ")
    sum1 = num1 + num2
    num1 = num2
    num2 = sum1


# ABCD Printing
# for i in range (65,70):
#    # inner loop
#     for j in range(65,i+1):
#         print(chr(j),end="")   # chr()- character function takes a numerical ASCII Value & Returns either an alphabet, number or special character corresponding to that ASCII Value
#     print()

# for i in range (65,70):
#     k =i
#    # inner loop
#     for j in range(65,i+1):
#         print(chr(i),end="")
#         k+=k
#     print()

#
# for i in range(65,80):
#     k=i
#     for j in range(65,i+1):
#         print(chr(k), end= " ")
#     k +=1
#     print()

# k=1
# for i in range(4):
#     for j in range(i+1):
#         print(k, end = " ")
#         k +=1
#     print()





