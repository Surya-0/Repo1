def jobs_scheduling(arr,t):
    arr.sort(key=lambda x:x[2],reverse=True)
    free_time_slots = [False]*t
    jobs_performed = [-1]*t
    profit = 0
    for i in range(len(arr)):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if free_time_slots[j] is False :
                free_time_slots[j] = True
                jobs_performed[j] = arr[i][0]
                profit += arr[i][2]
                break
    return profit


if __name__ == '__main__':
    jobs = [('a', 4, 70), ('b', 1, 80), ('c', 1, 60), ('d', 2, 50), ('e', 3, 40), ('f', 1, 30)]
    t = 3
    profit = jobs_scheduling(jobs, t)
    print(profit)