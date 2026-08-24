import threading
import time
import random

# Semaphores and locks
resource = threading.Semaphore(1)   # Controls access to shared resource
readTry = threading.Semaphore(1)    # Gives priority to waiting writers
rmutex = threading.Semaphore(1)     # Protects reader_count
wmutex = threading.Semaphore(1)     # Protects writer_count

reader_count = 0
writer_count = 0

# Shared data
shared_data = 0


# ---------------- READER ----------------
def reader(reader_id):
    global reader_count

    time.sleep(random.uniform(0.1, 0.5))

    # Reader tries to enter
    readTry.acquire()
    rmutex.acquire()

    reader_count += 1

    # First reader locks the resource
    if reader_count == 1:
        resource.acquire()

    rmutex.release()
    readTry.release()

    # Reading section
    print(f"Reader {reader_id} is reading data = {shared_data}")
    time.sleep(1)

    # Reader exits
    rmutex.acquire()
    reader_count -= 1

    # Last reader releases the resource
    if reader_count == 0:
        resource.release()

    rmutex.release()

    print(f"Reader {reader_id} finished reading")


# ---------------- WRITER ----------------
def writer(writer_id):
    global writer_count
    global shared_data

    time.sleep(random.uniform(0.1, 0.5))

    # Give writers priority
    wmutex.acquire()
    writer_count += 1

    # First waiting writer blocks new readers
    if writer_count == 1:
        readTry.acquire()

    wmutex.release()

    # Only one writer can access resource
    resource.acquire()

    # Writing section
    shared_data += 10
    print(f"Writer {writer_id} is writing...")
    time.sleep(1)

    print(f"Writer {writer_id} updated data = {shared_data}")

    resource.release()

    # Writer exits
    wmutex.acquire()
    writer_count -= 1

    # Last writer allows readers
    if writer_count == 0:
        readTry.release()

    wmutex.release()

    print(f"Writer {writer_id} finished writing")


# ---------------- MAIN ----------------
if __name__ == "__main__":

    threads = []

    # Create readers and writers
    for i in range(1, 6):
        threads.append(
            threading.Thread(target=reader, args=(i,))
        )

        threads.append(
            threading.Thread(target=writer, args=(i,))
        )

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads
    for thread in threads:
        thread.join()

    print("\nAll readers and writers have completed.")
    print("Final shared data =", shared_data)
