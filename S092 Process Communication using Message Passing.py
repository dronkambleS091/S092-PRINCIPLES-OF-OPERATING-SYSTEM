from multiprocessing import Process, Queue, Lock
import time
import random

def producer(queue, lock):
    for i in range(5):
        item = random.randint(1, 100)
        with lock:
            print(f"Producer produced: {item}")
        queue.put(item)
        time.sleep(random.random())

def consumer(queue, lock):
    for i in range(5):
        item = queue.get()
        with lock:
            print(f"Consumer consumed: {item}")
        time.sleep(random.random())

if __name__ == "__main__":
    q = Queue()
    print_lock = Lock()
    
    p1 = Process(target=producer, args=(q, print_lock))
    p2 = Process(target=consumer, args=(q, print_lock))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Producer and Consumer have finished.")
