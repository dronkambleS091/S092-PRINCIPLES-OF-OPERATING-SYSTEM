print("S092 Dron Kamble")

# Process Details
processes = ["P1", "P2", "P3", "P4"]
arrival = [0, 1, 2, 3]
burst = [5, 3, 8, 6]

n = len(processes)

waiting = [0] * n
turnaround = [0] * n
completion = [0] * n
start = [0] * n

# First Process
start[0] = arrival[0]
completion[0] = start[0] + burst[0]
waiting[0] = 0
turnaround[0] = completion[0] - arrival[0]

# Remaining Processes
for i in range(1, n):
    start[i] = max(completion[i - 1], arrival[i])
    completion[i] = start[i] + burst[i]
    waiting[i] = start[i] - arrival[i]
    turnaround[i] = completion[i] - arrival[i]

# Display Results
print("\nFCFS Scheduling\n")
print("Process\tAT\tBT\tWT\tTAT")

avgWT = 0
avgTAT = 0

for i in range(n):
    print(f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t{waiting[i]}\t{turnaround[i]}")
    avgWT += waiting[i]
    avgTAT += turnaround[i]

avgWT /= n
avgTAT /= n

print("\nAverage Waiting Time = {:.2f} ms".format(avgWT))
print("Average Turnaround Time = {:.2f} ms".format(avgTAT))

# Gantt Chart
print("\nGantt Chart:")
print("0", end="")
for i in range(n):
    print(f" ----{processes[i]}---- {completion[i]}", end="")
print()
