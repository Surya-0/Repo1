def coin_change(total, denomination):
    denomination.sort(reverse=True)
    coin_count = 0
    iterator = 0
    while total > 0 and iterator < len(denomination):
        if total >= denomination[iterator]:
            n = total // denomination[iterator]
            total = total - denomination[iterator] * n
            coin_count = coin_count + n
        iterator += 1
    if total == 0:
        return coin_count
    else:
        return -1


if __name__ == '__main__':
    currency = [2, 10, 5]
    change = 37
    l = coin_change(change, currency)
    print(l)