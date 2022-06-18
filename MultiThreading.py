import threading

def function1(s):
    for i in range(100):
        print(s)

def function2(s):
    for i in range(50):
        print(s)


t1 = threading.Thread(target=lambda:function1("Nazif"))
t2 = threading.Thread(target=lambda: function2("Ishrak"))

t1.start()
t2.start()
