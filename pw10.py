n = int(input())
def cup_supporter(n, x):
    a = "* "
    if x<0:
      return
    else:
        print(" "*(n-x)+a*x, end=" ")
        print()
        cup_supporter(n, x-1)
def cup(n):
    cup_supporter(n, n)                
cup(n)




s = int(input())
a = int(input())
def guess(s, a):
    if a==0:
        print(f"Sorry, you lose! The secret number is {s} and you have no more attempts remaining.")
    else:
        print(f"Attempts remaining: {a}")
        z = int(input())
        print(f"You guessed: {z}")
        if z>s:
            if a==1:
                print(f"Sorry, you lose! The secret number is {s} and you have no more attempt(s) remaining.")
            else:
                print("Your guess is too high. Try again!")
                guess(s, a-1)
        elif z<s:
            if a==1:
                print(f"Sorry, you lose! The secret number is {s} and you have no more attempts remaining.")
            else:
                print("Your guess is too low. Try again!")
                guess(s, a-1)
        elif z==s:
            print(f"Congratulations, you won! You guessed the secret number {s} with {a-1} attempt(s) remaining.")  



def slow_conceal(s):
    if len(s) == 0:
        return
    else:
        print(s)
        slow_conceal(s[:-1]) 