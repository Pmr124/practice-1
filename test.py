# arr = []
# arr = [11, 12, 13, 14, 15]
# a = sum (arr)
# print(a)

#2. Python Program to find largest element in a list
# def largest(arr, n):
#    arr.sort()
#    return arr[n-1]
# arr = [11,22,44,400,300]
# n = len(arr)
# Ans = largest(arr, n)
# print("Largest in given array ", Ans)
#  3. Python program to find second largest number in a list
# def findLargest(arr):
#     secondLargest = 0
#     largest = min(arr)
 
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             secondLargest = largest
#             largest = arr[i]
#         else:
#             secondLargest = max(secondLargest, arr[i])
 
#     return secondLargest
# print(findLargest([11,12,14,5,20,25]))

# 4. Python program to print positive numbers in a list

# list = [10, -12, 20, 121, -30, -8]
# po_num = [num for num in list if num >= 0]
# print("Positive numbers in the list: ", po_num)

# String Programs:

# 1. Python program to check if a string is palindrome or not
# x = "Priti"
# y = ""
# for i in x:
#     y = i + y
# if (x == y):
#     print("Yes")
# else:
#     print("No")
# 2. Reverse words in a given String in Python
# string = "I am doing practice"
# s = string.split()[::-1]
# l = []
# for i in s:
#     l.append(i)
# print(" ".join(l))
# 3. Ways to remove i’th character from string in Python

# test_str = "GeeksForGeeks"
# new_str = test_str[:2] + test_str[3:]
# print ("The string after removal of i'th character : " + new_str)

# 4. Check if a Substring is Present in a Given String
string1 = " I am going to office"
 
if "ing" in string1:
    print("Yes it is present in the string")
else:
    print("No it is not present")