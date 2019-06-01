
import operations

def choices():
  print("For Concatenation  press 1")
  print("For Reptition press 2")
  print("For edit press 3")
  print("To find press 4")
  print("To count press 5")
   
  print("Exit press 0")
  return input("your Choice")


def main():
  print("!! Welcome to our String Manipulation Program !!")
  while(True):
    choice = choices()
    if choice == "0":
      break;
    elif choice == "1":
      print(operations.cont())
    elif choice == "2":
      operations.rept()
    elif choice == "3":
      print(operations.edit())
    elif choice =="4":
      print(operations.find())
    elif choice =="5":
      print(operations.count())
    else:
      print("Invalid input try again")


# def rept():
#   x= input("Enter String:")
#   n= int(input("Enter number of repeation:"))
#   for r in range(n):
#     print(x) 


# def cont():

#   x = input("Enter first String:")
#   y = input("Enter Second String:")
#   return x+" "+y

# def edit():
#   s=input("Enter String")
#   index=int(input("Enter Index"))
#   ch=input("Enter Character")
#   return(s[:index]+ch+s[index+1:])

# def find():
#   index=0
#   s=input("Enter string")
#   sub=input("Enter substring")
#   while index<(len(s)-len(sub)+1):
#     if s[index:len(sub)+index]==sub:
#       return True
#     else:
#       index +=1
#   return False 


# def count():
#   index=0
#   count=0
#   s=input("Enter string")
#   sub=input("Enter substring")
#   while index<(len(s)-len(sub)+1):
#     if s[index:len(sub)+index]==sub:
#       count +=1
#     index +=1
#   return count


main()
