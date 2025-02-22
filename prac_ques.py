def minmax(nums):
    min = nums[0]
    max = nums[0]
    for i in nums:
        if i < min:
            min = i
        elif i > max:
            max = i

    return (max, min)


def minmax2(strNums):
    max_str = ''
    for st in strNums:
        if len(st) > len(max_str):
            max_str = st

    return [max_str]


def remEle(nums):
    i = 0
    while i < len(nums):
        value = nums[i]
        if value in nums[i+1::]:
            nums.remove(value)
        else:
            i = i + 1
    return nums

def max_profit(list_price):
    min = list_price[0]
    max = list_price[0]
    for i in range(1, len(list_price)):
        if list_price[i] < min:
            min = list_price[i]
            max = list_price[i]
        elif list_price[i] > max:
            max= list_price[i]
    return max - min



def rotate(nums, k):
    while k!=0:
        value = nums.pop()
        nums.insert(0, value)
        k = k-1
    return nums


def max_subarray(nums):
    if len(nums)==0:
        max_sum = 0
    else:
        max_sum = nums[0]
    for i in range(1, len(nums)):
        if max_sum < nums[i]:
            max_sum = nums[i]
        elif max_sum < max_sum +nums[i]:
            max_sum = max_sum +nums[i]

    return max_sum


# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)

# Example 2: Case with a negative numbe
# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2)

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)

print("Example 3: Input:", input_case_3, "\nResult:", result_3)


