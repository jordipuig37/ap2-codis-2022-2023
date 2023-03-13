from yogi import tokens, read

def inversions_merge(numbers: list[int]) -> tuple[int, list[int]]:
    
    if len(numbers) <= 1:
        return 0, numbers
    
    mid = len(numbers) // 2
    inv1, left = inversions_merge(numbers[:mid])
    inv2, right = inversions_merge(numbers[mid:])
    
    inv = inv1 + inv2
    i1, i2 = 0, 0
    numbers = []

    while i1 < len(left) and i2 < len(right):

        if left[i1] <= right[i2]:
            numbers.append(left[i1])
            inv += i2
            i1 += 1
        else:
            numbers.append(right[i2])
            i2 += 1

    numbers.extend(left[i1:])
    numbers.extend(right[i2:])
    
    inv += i2 * (len(left) - i1)

    return inv, numbers
    

def main() -> None:
    
    for n in tokens(int):
        numbers = [read(int) for _ in range(n)]        
        print(inversions_merge(numbers)[0])

if __name__ == '__main__':
    main()
