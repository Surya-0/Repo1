def jobs_sequencing(job_list, time):
    job_list.sort(key=lambda x: x[2], reverse=True)
    print(job_list)
    free_time_slots = [False] * time
    jobs_performed = [-1] * time
    profit_count = 0
    for i in range(len(job_list)):
        for j in range(min(time - 1, job_list[i][1] - 1), -1, -1):
            if free_time_slots[j] is False:
                free_time_slots[j] = True
                jobs_performed[j] = job_list[i][0]
                profit_count += job_list[i][2]
                break
    return jobs_performed


if __name__ == "__main__":
    jobs = [('a', 4, 70), ('b', 1, 80), ('c', 1, 60), ('d', 2, 50), ('e', 3, 40), ('f', 1, 30)]
    t = 3
    profit = jobs_sequencing(jobs, t)
    print(profit)
