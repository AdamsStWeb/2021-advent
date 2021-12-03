arr = open('input.txt').readlines()
print([int(x) < int(y) for x, y in zip(arr, arr[1:])].count(True))

arr = [int(x) + int(y) + int(z) for x, y, z in zip(arr, arr[1:], arr[2:])]
print([int(x) < int(y) for x, y in zip(arr, arr[1:])].count(True))
