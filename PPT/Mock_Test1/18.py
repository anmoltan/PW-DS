import time

def timer(func):
    def start(*args,**kwargs):
        start_tm = time.time()
        res = func(*args,**kwargs)
        end_tm = time.time()
        tt= end_tm - start_tm
        print(f"Execution time ={tt}")
        return res;
    return start
 
@timer
def my_func():
    for i in (1,5000):
        if i%5 == 0:
            print(i)
            time.sleep(5)
    return i

my_func()