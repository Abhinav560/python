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
with open("file1.txt","r") as f:
          content=f.read()
          print(content)