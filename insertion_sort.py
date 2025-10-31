def main():
    arr = [40, 20, 60, 10, 50, 30]

    for j in range(len(arr)):
        k = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > k:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i+1] = k
        # print(j, arr)
    print(arr)


if __name__ == "__main__":
    main()