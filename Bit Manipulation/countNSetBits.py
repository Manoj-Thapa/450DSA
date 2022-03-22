# Time complexity: O(n)
# Space complexity: O(1)

def countSetBits(n):
    mem = [0] * (n + 1)
    for i in range(1, n + 1):
        mem[i] = mem[i >> 1] + (i & 1)

    return sum(mem)

print(countSetBits(4))
