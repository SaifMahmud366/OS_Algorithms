n = int(input("Enter Process Number = "))

Process = []
Burst_Time = []
Complition_Time = []
Response_Time = [0] * n
Waiting_Time = []
Turnaround_Time = []

for i in range(n):
    Process.append(int(input("Enter Process " + str(i) + " = ")))

for i in range(n):
    Burst_Time.append(int(input("Enter Burst Time " + str(i) + " = ")))

for i in range(n):
    Complition_Time.append(int(input("Enter Compilation Time " + str(i) + " = ")))

for i in range(1, n):
    Response_Time[i] = Response_Time[i-1] + Burst_Time[i-1] + Complition_Time[i-1]

for i in range(n):
    Turnaround_Time.append(Response_Time[i] + Burst_Time[i])
    Waiting_Time.append(Turnaround_Time[i] - Burst_Time[i])

avg_waiting_time = sum(Waiting_Time) / n
avg_turnaround_time = sum(Turnaround_Time) / n

print('Response Time = ', Response_Time)
print('Average Waiting Time =', avg_waiting_time)
print('Average Turnaround Time =', avg_turnaround_time)