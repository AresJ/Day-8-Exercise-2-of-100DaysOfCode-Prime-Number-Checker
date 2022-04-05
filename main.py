#Write your code below this line 👇
def prime_checker(number):
  flag = False
  if number > 1:
    for a in range(2, number):
      if (number % a) == 0:
        flag = True
        break

  if flag:
    print(f"{number} is a prime number")
  else:
    print(f"{number} is not a prime number")     

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



