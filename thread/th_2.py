from threading import Thread, Lock, Event
from time import sleep
lock= Lock()
event= Event()
file= 'test.txt'
l = 0
def fun_1(file,c):
    global l  
    while l<20:
        print(f"l in start is {l}")
        # sleep(c)
        lock.acquire()
        with open(file, "r") as f:
            l = int(f.readlines()[-1])
            l = int(l)+c
            print(f"value if l after add is {l}")
        lock.release()
        lock.acquire()
        with open(file, 'a') as f1:
            f1.write(f"\n{str(l)}")
        lock.release()
        if l%2==0:
            event.set()
            print(f"event is set, when l is: {l}")                
        sleep(c)
    
    print("DONE")
    event.set()  
def c_event(t):
    global l
    while l<20:
    # while t.is_alive():  
        event.wait()
        print(f"{t.name} thread is_alive") 
        print("event was set, unsetting the event now.")
        event.clear()
    
    # print(f"{t.name} status is {t.is_alive()}")


t1= Thread(target=fun_1, args=(file,1))
t2= Thread(target=fun_1, args=(file,2))
t3= Thread(target=fun_1, args=(file,3))
t4= Thread(target=fun_1, args=(file,4))
t5= Thread(target=c_event, args=(t1,))
t1.name= "T1_THREAD"

print(t1.name)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
# t3.join()
print(f"Thread execution Ends here.")
print(t1.is_alive())