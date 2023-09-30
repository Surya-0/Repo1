def coin_switch(currency_list, total):
    currency_list.sort(reverse=True)
    coin_count = 0
    iterator = 0
    while total > 0 and iterator < len(currency_list):
        if total >= currency_list[iterator]:
            n = total//currency_list[iterator]
            total = total - currency_list[iterator]*n
            coin_count = coin_count + n
        iterator += 1

    if total == 0:
        return coin_count
    else:
        return -1


if __name__ == '__main__':
    currency_available = [1, 5, 2, 10]
    amount = int(input("Enter the amount to exchange"))
    num = coin_switch(currency_available, amount)
    print("The number of coins required will be : ",num)