

nums = [1,2,7,6,4]

def is_prime(x):
    for i in range(2,int(x/2)):
        if x%i == 0:
            return False
    return True


def solution(nums):
    result = 0
    for x in range(0,len(nums)-2):
        for y in range(x+1,len(nums)-1):
            for z in range(y+1,len(nums)):
                if is_prime(nums[x]+nums[y]+nums[z]):
                    result += 1
                    print(nums[x],nums[y],nums[z])

    return result
solution(nums)