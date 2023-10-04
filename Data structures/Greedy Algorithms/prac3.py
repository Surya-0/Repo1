def task_selection(activities, time):
    activities.sort(key=lambda x: x[2], reverse=True)
    free_time_slots = ['False'] * time
    jobs_performed = [-1] * time
    profit_count = 0
    for i in range(len(activities)):
        for j in range(min(time - 1, activities[i][1] - 1), -1, -1):
            if free_time_slots[j] == 'False':
                free_time_slots[j] = 'True'
                jobs_performed[j] = activities[i][0]
                profit_count += activities[i][2]
                break
    return profit_count


if __name__ == '__main__':
    jobs = [('a', 4, 70), ('b', 1, 80), ('c', 1, 60), ('d', 2, 50), ('e', 3, 40), ('f', 1, 30)]
    t = 3
    profit = task_selection(jobs, t)
    print(profit)
