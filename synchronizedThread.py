import time, threading
x=100
#Demonstrating how two threads are operating on one variable
# and doing inverse effects on that variable
def multiply(num):
    global x
    while x<=100:
        x= num*x
        print(x)
        time.sleep(1)


def divide(num):
    global x
    while x>=100:
        x = x/num
        print(x)
        time.sleep(1)

t1 = threading.Thread(target=lambda: multiply(2))
t2 = threading.Thread(target=lambda: divide(2))

t1.start()
t2.start()