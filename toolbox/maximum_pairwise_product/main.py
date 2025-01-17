
def max_pairwise_product(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return  arr[0] * arr[1]

    max_int = max(arr)
    arr.remove(max_int)
    max_int_2 = max(arr)

    return max_int * max_int_2

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))