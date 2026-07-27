print("S092 Dron Kamble")

# Process Details
processes = ["P1", "P2", "P3", "P4"]
arrival = [0, 2, 4, 5]
burst = [7, 4, 1, 4]

n = len(processes)

completed = [False] * n
waiting = [0] * n
turnaround = [0] * n
completion = [0] * n

current_time = 0
completed_count = 0
gantt = []

while completed_count < n:
    idx = -1
    min_burst = 9999

    # Find the shortest job among arrived processes
    for i in range(n):
        if arrival[i] <= current_time and not completed[i]:
            if burst[i] < min_burst:
                min_burst = burst[i]
                idx = i

    if idx == -1:
        current_time += 1
    else:
        start = current_time
        current_time += burst[idx]
        completion[idx] = current_time
        turnaround[idx] = completion[idx] - arrival[idx]
        waiting[idx] = turnaround[idx] - burst[idx]
        completed[idx] = True
        completed_count += 1
        gantt.append((processes[idx], start, current_time))

# Display Results
print("\nNon-Preemptive SJF Scheduling\n")
print("Process\tAT\tBT\tWT\tTAT")

avgWT = 0
avgTAT = 0

for i in range(n):
    print(f"{processes[i]}\t{arrival[i]}\t{burst[i]}\t{waiting[i]}\t{turnaround[i]}")
    avgWT += waiting[i]
    avgTAT += turnaround[i]

print("\nAverage Waiting Time = {:.2f} ms".format(avgWT / n))
print("Average Turnaround Time = {:.2f} ms".format(avgTAT / n))

# Gantt Chart
print("\nGantt Chart:")
for p, s, e in gantt:
    print(f"{s} ----{p}---- {e}", end=" ")
print()
