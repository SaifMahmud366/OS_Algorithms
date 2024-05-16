# Number of processes
n = int(input("Enter the number of processes: "))
quantum = int(input("Enter the time quantum: "))

# Initialize process list and burst times
processes = []
burst_times = []

# Input burst times
for i in range(1, n+1):
    processes.append(i)
    burst_time = int(input(f"Enter burst time for process {i}: "))
    burst_times.append(burst_time)

# Initialize variables
time = 0
waiting_time = 0
turnaround_time = 0

# Execute processes in round-robin manner
while True:
    done = True
    for i in range(n):
        if burst_times[i] > 0:
            done = False
            if burst_times[i] > quantum:
                time += quantum
                burst_times[i] -= quantum
                waiting_time += time
            else:
                time += burst_times[i]
                waiting_time += time
                turnaround_time += time
                burst_times[i] = 0

    if done == True:
        break

# Calculate average waiting time and average turnaround time
avg_waiting_time = waiting_time / n
avg_turnaround_time = turnaround_time / n

# Display the result
print(f"Average waiting time using Round Robin: {avg_waiting_time}")
print(f"Average turnaround time using Round Robin: {avg_turnaround_time}")
