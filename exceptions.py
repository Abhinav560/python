# #division by zero
# try:
#     result=10/0
# except ZeroDivisionError:
#     print("can't be divided by zero.")

# try:
#     mylist=[1,2,3]
#     print(mylist[5])
# except IndexError:
#     print("Index out of range")

num=int(input("enter a number: "))
if num>0: 
    print("the number is positive")
elif num==0:
    print("number is zero")
elif num<0:
    print("the number is negative")