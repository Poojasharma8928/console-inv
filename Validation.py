
# import re


# x='abc'
# print(re.findall('[abcdefghij]',x))


# def fname(name):
#     name=input("Enter your first Name: ")
#     if(re.search('[a-zA-Z]',name)):
#         print(name)
#     else:
#         print("Enter Valid Name")
# fname(name)

# FIRST NAME:**********************************************************
# fname=input("Enter your First Name: ")
# def first():
#     if fname.isalpha():
#         print(fname)
#     else:
#         print("ENTER VALID FIRST NAME")
#         first()  # This function wil call only after the condition will false
# first()

# # LAST NAME*********************************************************
# def last():
#     lname=input("Enter your Last Name: ")
#     if lname.isalpha():
#         print(lname)
#     else:
#         print("INVALID LAST NAME")
#         last()
# last()

# print(fname+" "+lname)

# # CONTACT NUMBER******************************************************

def phn_no():
    number= input("Enter Your Contact Number: ")

    if number.isdigit() and len(number)==10:
            print(number)
    else:
        print("INVALID CONTACT NUMBER")
        phn_no()


    

# def phn_no():
#     number= input("Enter Your Contact Number: ")

#     if type(number)==int and len(number)==10:
#             print(number)
#     else:
#         print("INVALID CONTACT NUMBER")
#         phn_no()
# phn_no()    