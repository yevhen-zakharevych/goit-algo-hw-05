def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    upper_bound = arr[-1]
    count_iter = 0

    if upper_bound < x:
        return -1

    if arr[0] > x:
        return -1

    while low <= high:
        mid = (high + low) // 2
        count_iter += 1

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1

        else:
            upper_bound = arr[mid]
            break

    return count_iter, upper_bound


if __name__ == "__main__":
    data = [2.13, 3.01, 4.2, 10, 40, 55, 80.3, 99, 101.11]
    search_value = 1
    result = binary_search(data, search_value)

    print(f"result: {result}")

