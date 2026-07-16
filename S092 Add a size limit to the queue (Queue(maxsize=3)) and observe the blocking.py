from multiprocessing import Process, Queue
import time

# Producer Process
def producer(queue):
    for i in range(1, 6):
        print("Producer produced:", i)
        queue.put(i)
        time.sleep(1)

# Consumer Process
def consumer(queue):
    for i in range(1, 6):
        item = queue.get()
        print("Consumer consumed:", item)
        time.sleep(2)

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Program Finished")
