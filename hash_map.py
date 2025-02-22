def __hash(key):
    my_hash = 0
    for letter in key:
        my_hash = (my_hash + ord(letter) * 3) % 7
    return my_hash


# print(__hash("bolt"))


def list_items(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for i in list2:
        if i in my_dict:
            return True
    return False


def find_duplicates(list1):
    my_dict = {}
    output = []
    for key in list1:
        if key in my_dict:
            my_dict[key] = True
        else:
            my_dict[key] = False

    for key in my_dict:
        if my_dict[key]:
            output.append(key)
    return output


# print(find_duplicates([1, 2, 3, 4, 2, 1]))
# ---------------------------------------------non repeating char---------------
def first_non_repeating_char(input_str):
    my_dict = {}
    for i in input_str:
        if i in my_dict:
            my_dict[i] = my_dict[i] + 1
        else:
            my_dict[i] = 1

    for i in input_str:
        if my_dict[i] > 1:
            return None if i == input_str[0] else input_str[0]


# print( first_non_repeating_char('leetcode'))
# print( first_non_repeating_char('hhello'))
# print( first_non_repeating_char('aabbcc'))


#
{"eat": {"e": 1, "a": 1, 't': 1}}


# ---------------------------------------------anagramas
def anagrams(list1):
    my_dict = {}
    output_list = []
    for word in list1:
        my_dict[word] = {}

    for key in my_dict:
        my_dict2 = {}
        for letter in key:
            if letter in my_dict2:
                my_dict2[letter] = my_dict2[letter] + 1
            else:
                my_dict2[letter] = 1
        my_dict[key] = my_dict2
    print(my_dict)
    keys_added = []
    for word in list1:
        value = my_dict[word]
        list_obj = []
        if word not in keys_added:
            for key in my_dict:
                if my_dict[key] == value:
                    list_obj.append(key)
                    keys_added.append(key)
            output_list.append(list_obj)
    print(output_list)

    # for word in output_list:


# anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

# ----------------------------------------target indicies------------

# def two_sum(list1, target):
#     hash = {}
#     for i, value in enumerate(list1):
#         rem = target - value
#         if rem in hash:
#             return [hash[rem], i]
#         hash[value] = i
#
#     return []

# print(two_sum([5, 5, 7, 2, 9, 3], 10))
# print(two_sum([4, 2, 11, 7, 6, 3], 9))
# print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
# print(two_sum([1, 3, 5, 7, 9], 10))
# print ( two_sum([1, 2, 3, 4, 5], 10) )
# print ( two_sum([1, 2, 3, 4, 5], 7) )
# print ( two_sum([1, 2, 3, 4, 5], 3) )

# ---------------------

def subarray_sum(list1, target):
    my_dict = {}
    for i, value in enumerate(list1):
        my_dict[value] = i
        if target in my_dict:
            return [my_dict[target], my_dict[target]]

    for idx in range(len(list1)):
        new_target = target
        output_list = [idx]
        for key_idx in range(idx+1, len(list1)):
            new_target = new_target - list1[key_idx-1]
            if new_target == 0:
                return output_list
            output_list.append(key_idx)


# nums = [1, 2, 3, 4, 5]
# target = 9
# print ( subarray_sum(nums, target))
#
# nums = [-1, 2, 3, -4, 5]
# target = 0
# print ( subarray_sum(nums, target) )
#
# nums = [2, 3, 4, 5, 6]
# target = 3
# print ( subarray_sum(nums, target) )
#
# nums = []
# target = 0
# print ( subarray_sum(nums, target) )


# ---------------------longest consecutive number ------------

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0

    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence

# longest_consecutive_sequence([5, 1,100,300, 2,4,3])
print(longest_consecutive_sequence([5, 1,100,101, 102, 103, 104,105,106, 106, 2,4,3]))
