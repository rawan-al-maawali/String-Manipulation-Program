def cont():
  x = input("Enter first String:")
  y = input("Enter Second String:")
  return (x+" "+y)
  
 

def rept():
  x= input("Enter String:")
  n= int(input("Enter number of reptition:"))
  for r in range(n):
    print(x)
    



def edit():
  s=input("Enter String")
  index=int(input("Enter Index"))
  ch=input("Enter Character")
  return(s[:index]+ch+s[index+1:])


def find():
  index=0
  s=input("Enter string")
  sub=input("Enter substring")
  while index<(len(s)-len(sub)+1):
    if s[index:len(sub)+index]==sub:
      return True
    else:
      index +=1
  return False 

def count():
  index=0
  count=0
  overlap = input("With overlap? Answer Y for yes, N for no: ")
  s=input("Enter string")
  sub=input("Enter substring")
  if overlap=="Y":

    while index<(len(s)-len(sub)+1):
      if s[index:len(sub)+index]==sub:
        count +=1
      index +=1
    return count
  if overlap=="N":
     while index<(len(s)-len(sub)+1):
      if s[index:len(sub)+index]==sub:
        count +=1
      index +=1+len(sub)
     return count
  else:
    return "Sorry! I can't figure out if you want overlap or not"


