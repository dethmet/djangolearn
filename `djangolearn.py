def even_numbers(arr,n):
    number = []
    for i in range(len(arr)):
        if arr(len(arr) - 1 - i) % 2 == 0:
            number.insert(0, arr(len(arr) - 1 - i))
        if len(number) == n:
            return number