# Greedy algorithms
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

# Dynamic programming algorithm
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

if __name__ == "__main__":
    amount = 113
    greedy_result = find_coins_greedy(amount)
    dp_result = find_min_coins(amount)

    print("Greedy algorithms:", greedy_result)
    print("Dynamic programming:", dp_result)