# Number of processes
n = int(input("Enter the number of processes: "))

# Initialize process list, burst times, and remaining times
processes = []
burst_times = []
remaining_times = []

# Input burst times and initialize remaining times
for i in range(1, n+1):
    processes.append(i)
    burst_time = int(input(f"Enter burst time for process {i}: "))
    burst_times.append(burst_time)
    remaining_times.append(burst_time)

# Initialize variables
time = 0
completed = 0
turnaround_times = [0] * n
waiting_times = [0] * n

# Simulate SRTF algorithm
while completed != n:
    min_time = float('inf')
    shortest_index = -1
    
    # Find process with shortest remaining time
    for i in range(n):
        if remaining_times[i] > 0 and remaining_times[i] < min_time:
            min_time = remaining_times[i]
            shortest_index = i
    
    # If no process found, increment time
    if shortest_index == -1:
        time += 1
        continue
    
    # Execute the shortest process
    remaining_times[shortest_index] -= 1
    time += 1
    
    # If process is completed
    if remaining_times[shortest_index] == 0:
        completed += 1
        turnaround_times[shortest_index] = time
        waiting_times[shortest_index] = time - burst_times[shortest_index]

# Calculate average waiting time and average turnaround time
avg_waiting_time = sum(waiting_times) / n
avg_turnaround_time = sum(turnaround_times) / n

# Display the result
print(f"Average waiting time using SRTF: {avg_waiting_time}")
print(f"Average turnaround time using SRTF: {avg_turnaround_time}")
