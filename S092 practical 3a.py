import threading      # For creating and managing threads
import time           # For adding delays and measuring execution time
print("S092 Dron Kamble")

# Simulates a time-consuming function
def task(name):
    print(f"{name} started")      # Shows when the task starts
    time.sleep(2)                 # Simulates work by pausing for 2 seconds
    print(f"{name} finished")     # Shows when the task ends


# -------- Sequential Execution --------
print("\n--- Sequential Execution ---")

start_time = time.time()          # Save current time

task("Task 1")                    # Runs for 2 seconds
task("Task 2")                    # Runs for another 2 seconds

end_time = time.time()            # Capture end time

print("Sequential Execution Time:",
      round(end_time - start_time, 2), "seconds")


# -------- Threaded Execution --------
print("\n--- Threaded Execution ---")

start_time = time.time()          # Record start time

# Create threads
t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))

# Launch both threads simultaneously
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

end_time = time.time()            # Capture end time

print("Threaded Execution Time:",
      round(end_time - start_time, 2), "seconds")

