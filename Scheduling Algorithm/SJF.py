# Number of processes
n = int(input("Enter the number of processes: "))
processes = []
burst_times = []
waiting_time = 0
turnaround_time = 0  # Total turnaround time

# Input burst times
for i in range(1, n+1):
    processes.append(i)
    burst_time = int(input(f"Enter burst time for process {i}: "))
    burst_times.append(burst_time)

# Sort burst times and processes based on burst times
sorted_processes = [p for _, p in sorted(zip(burst_times, processes))]
sorted_burst_times = sorted(burst_times)

# Calculate waiting time and turnaround time
for i in range(n):
    waiting_time += sum(sorted_burst_times[:i])
    turnaround_time += sum(sorted_burst_times[:i+1])

# Calculate average waiting time and average turnaround time
avg_waiting_time = waiting_time / n
avg_turnaround_time = turnaround_time / n

# Display the result
print(f"Average waiting time using SJF: {avg_waiting_time}")
print(f"Average turnaround time using SJF: {avg_turnaround_time}")
