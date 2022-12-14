def check(g, k, n, stocks):
    t = g * k
    i = 0
    while i < n:
        if stocks[i] > g:
            t = t - g
        else:
            t = t - stocks[i]
        i += 1

    if t <= 0:
        return True
    return False


def solve(n, k, stock):
    sums = 0
    for i in range(n):
        sums += stock[i]

    ans = 0

    lo, hi = 0, 1e18
    y = 0

    while lo <= hi and y == 0:
        mid = (lo + hi) // 2
        # print(mid)
        if (check(mid, k, n, stock) == True and check(mid + 1, k, n, stock) == False):
            ans = mid
            y = 1
        elif check(mid, k, n, stock) == True:
            lo = mid + 1
        else:
            hi = mid - 1

    return ans


if __name__ == "__main__":
    print(solve(n=4, k=2, stock=[2, 3, 5, 3]))
