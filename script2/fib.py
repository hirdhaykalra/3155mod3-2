#Worked with Haley Siharath
import time
def fib_calc(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(n>1):
        return fib_calc(n-1) + fib_calc(n-2)

print(f"Hard Coded for 35: {(fib_calc(35))}")
print(f"Process time: {time.process_time()} seconds")

#Used internet to find fib formula
#Source: https://docs.python.org/3/library/time.html#time.process_time
#Chose to use time.process_time() which outputs the seconds elapsed in currrent program