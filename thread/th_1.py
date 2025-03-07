from threading import Thread, Lock, Event
from time import sleep
lock= Lock()
event= Event()
file= 'test.txt'
# l = 0    // why it an not be declared outside the function?? "UnboundLocalError: local variable 'l' referenced before assignment"
def fun_1(file,c):
    l = 0
    while l<20:
        with open(file, "r+") as f:
            lock.acquire()
            m = int(f.readlines()[-1])
            m = int(m)+c
            l=m
            if m%2==0:
                event.set()
            f.write(f"\n{str(l)}")
            print(f"value if l is {l}, value if m is {m}")          
            sleep(c)
            lock.release()

def c_event(t):
    # while True: 
    while t.is_alive():   
        event.wait()
        print(t.getName())
        print("event was set, unsetting the event now.")
        event.clear()
    if not t.is_alive():
        return "T1 thread ends."

t1= Thread(target=fun_1, args=(file,2))
t2= Thread(target=fun_1, args=(file,3))
t3= Thread(target=c_event, args=(t1,))

t1.start()
# print(t1.is_alive())
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(f"Thread execution Ends here.")
print(t1.is_alive())