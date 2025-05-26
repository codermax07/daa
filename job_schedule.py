def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = len(jobs)
    max_deadline = max([job[1] for job in jobs])
    slot = [-1] * (max_deadline + 1)
    profit = 0

    for job in jobs:
        for j in range(job[1], 0, -1):
            if slot[j] == -1:
                slot[j] = job[0]
                profit += job[2]
                break
    return profit

n = int(input("Enter number of jobs: "))
jobs = []
for _ in range(n):
    job_id, deadline, profit = input("Enter job_id deadline profit: ").split()
    jobs.append((job_id, int(deadline), int(profit)))

print("Max Profit:", job_scheduling(jobs))
