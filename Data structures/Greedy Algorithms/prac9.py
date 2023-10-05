def coin_change(change, currency):
    iterator = 0
    change_counter = 0
    while change > 0 and iterator < len(currency):
        if change >= currency[iterator]:
            fraction = change // currency[iterator]
            change = change - fraction * currency[iterator]
            change_counter += fraction
        iterator += 1
    if change == 0:
        return change_counter
    else:
        return -1


if __name__ == '__main__':
    denomination = [2, 10, 5]
    denomination.sort(key=lambda x: x, reverse=True)
    print(denomination)
    value = int(input("Enter the amount to change"))
    number = coin_change(value, denomination)
    print(number)
