# Number of processes and resources
n = int(input("Enter the number of processes: "))
m = int(input("Enter the number of resources: "))

# Available resources
available = list(map(int, input("Enter the available resources: ").split()))

# Maximum resources needed by each process
max_resources = []
for i in range(n):
    max_resources.append(list(map(int, input(f"Enter the maximum resources needed for process {i+1}: ").split())))

# Allocated resources for each process
allocated = []
for i in range(n):
    allocated.append(list(map(int, input(f"Enter the allocated resources for process {i+1}: ").split())))

# Calculate the need matrix
need = []
for i in range(n):
    need.append([max_resources[i][j] - allocated[i][j] for j in range(m)])

# Initialize finish array
finish = [False] * n

# Safety algorithm
safe_sequence = []
work = available[:]
while len(safe_sequence) < n:
    for i in range(n):
        if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
            work = [work[j] + allocated[i][j] for j in range(m)]
            safe_sequence.append(i)
            finish[i] = True
            break

# Check if a safe sequence exists
if len(safe_sequence) == n:
    print("Safe Sequence:", safe_sequence)
else:
    print("No safe sequence exists.")
