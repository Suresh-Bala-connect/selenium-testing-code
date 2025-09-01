try:
    num=int(input("Enter the Number"))
    print(100/num)
except ZeroDivisionError:
    print("you cant dovode by Zero")
except ValueError:
    print("please Enter the valid number")