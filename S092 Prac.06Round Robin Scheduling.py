from collections import deque

# Round Robin Scheduling
def round_robin(processes, quantum):
    n = len(processes)

    remaining = [p[2] for p in processes]
    completion = [0] * n
    response = [-1] * n

    ready_queue = deque()
    ready_queue.extend(range(n))

    time = 0
    context_switches = 0
    last_process = -1

    while ready_queue:

        index = ready_queue.popleft()

        # Count context switch when CPU changes process
        if last_process != -1 and last_process != index:
            context_switches += 1

        last_process = index

        # First time process gets CPU
        if response[index] == -1:
            response[index] = time

        # Execute process
        execution_time = min(quantum, remaining[index])

        time += execution_time
        remaining[index] -= execution_time

        # If process is not finished, add it back to queue
        if remaining[index] > 0:
            ready_queue.append(index)
        else:
            completion[index] = time

    # Calculate TAT, WT and RT
    for i in range(n):
        arrival_time = processes[i][1]
        burst_time = processes[i][2]

        turnaround = completion[i] - arrival_time
        waiting = turnaround - burst_time
        response[i] = response[i] - arrival_time

        processes[i] = (
            processes[i][0],
            arrival_time,
            burst_time,
            completion[i],
            turnaround,
            waiting,
            response[i]
        )

    return processes, context_switches


# -----------------------------
# Main Program
# -----------------------------

print("ROUND ROBIN CPU SCHEDULING")
print("---------------------------")

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    print("\nProcess P" + str(i + 1))

    arrival = int(input("Enter Arrival Time: "))
    burst = int(input("Enter Burst Time: "))

    processes.append([
        "P" + str(i + 1),
        arrival,
        burst
    ])

quantum = int(input("\nEnter Time Quantum: "))

result, context_switches = round_robin(processes, quantum)

# Display result
print("\n\nRESULT")
print("---------------------------------------------------------------")
print("Process\tAT\tBT\tCT\tTAT\tWT\tRT")
print("---------------------------------------------------------------")

total_tat = 0
total_wt = 0
total_rt = 0

for p in result:
    print(
        p[0], "\t",
        p[1], "\t",
        p[2], "\t",
        p[3], "\t",
        p[4], "\t",
        p[5], "\t",
        p[6]
    )

    total_tat += p[4]
    total_wt += p[5]
    total_rt += p[6]

print("---------------------------------------------------------------")

print("\nAverage Turnaround Time =",
      round(total_tat / n, 2))

print("Average Waiting Time =",
      round(total_wt / n, 2))

print("Average Response Time =",
      round(total_rt / n, 2))

print("Context Switches =", context_switches)
