def find(s, n):
    num_map = {}
    for i, num in enumerate(s):
        complement = n - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return None

if __name__ == "__main__":
    print(find([2,7,11,15], 9))
    print(find([3,2,4], 6))
    print(find([3,3], 6))
    print(find([1,2,3,4], 8))