import math

def readpoint():
    num = int(input().split())
    a = []
    for i in range(0, num):
        nums = int(input().split())
        print(nums)
        for j in range(0, 3):
            v = nums[j]
            a.append(v)
    return a

def distance(point):
    nums = 0
    for i in point:
        nums += math.pow(i, 2)
    return math.pow(nums, 0.5)

n = int(input())
for i in range(n):
    p = readpoint()
    print('Ponit = {},type = {},distance={:.3f}'.format(p, type(p), distance(p)))
