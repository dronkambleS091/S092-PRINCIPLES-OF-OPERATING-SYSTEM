import threading
import time

# Buffer size
BUFFER_SIZE = 5

# Circular buffer
buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0

# Mutex for synchronized access to buffer
mutex = threading.Lock()

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # Empty slots
full = threading.Semaphore(0)             # Filled slots


# Producer function
def producer():
    global in_index

    for item in range(1, 11):

        # Wait for an empty slot
        empty.acquire()

        # Enter critical section
        with mutex:
            buffer[in_index] = item
            print(f"Producer produced: {item} at position {in_index}")

            # Circular queue
            in_index = (in_index + 1) % BUFFER_SIZE

        # Signal that one slot is full
        full.release()

        time.sleep(1)


# Consumer function
def consumer():
    global out_index

    for _ in range(1, 11):

        # Wait for a filled slot
        full.acquire()

        # Enter critical section
        with mutex:
            item = buffer[out_index]
            buffer[out_index] = None

            print(f"Consumer consumed: {item} from position {out_index}")

            # Circular queue
            out_index = (out_index + 1) % BUFFER_SIZE

        # Signal that one slot is empty
        empty.release()

        time.sleep(1.5)


# Create threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()

print("\nProducer-Consumer execution completed.")
print("Dron Kamble")

