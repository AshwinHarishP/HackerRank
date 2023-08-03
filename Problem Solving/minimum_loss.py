def minimumLoss(price):
    use = sorted(price, reverse = True)
    r = use[0]
    for i in range(len(use) - 1):
        c = use[i] - use[i + 1]
        if c < r:
            if price.index(use[i]) < price.index(use[i+1]):
                r = c
    return r

price = [20, 7, 8, 2, 5]
result = minimumLoss(price)
print(result)
