import random

def shuffle(arr):
    for i in range(len(arr)):
        rand_index = random.randint(0, len(arr)-1)
        temp=arr[i]
        arr[i] = arr[rand_index]
        arr[rand_index] = temp
    return arr

def skyline_heights(building_heights):
    max_building_height = 0
    visible_buildings = []
    for building_height in building_heights:
        if building_height > max_building_height:
            visible_buildings.append(building_height)
            max_building_height=building_height
    return visible_buildings

def zip_it(arr1, arr2):
    larger_arr = arr1 if len(arr1)> len(arr2) else arr2
    new_arr = []
    for i in range(len(larger_arr)):
        if i <= (len(arr1)) -1:
            new_arr.append(arr1[i])
        if i <= (len(arr2))-1:
            new_arr.append(arr2[i])
    return new_arr

def is_credit_card_valid(digit_Arr):
    last_digit = digit_Arr.pop()
    
    for i in range(len(digit_Arr)):
        if i % 2 == 0:
            digit_Arr[i] *= 2
    
    for i in range(len(digit_Arr)):
        if digit_Arr[i] > 9:
            digit_Arr[i] -= 9

    total = sum(digit_Arr)

    total += last_digit
    return total % 10 ==0

digit_Arr = [5,2,2,8,2]
is_valid = is_credit_card_valid(digit_Arr)
print(is_valid)






# # print(skyline_heights([-1,1,1,7,3]))

# print(shuffle([4,5,6,2,3,4,5]))

# print(zip_it([4,15,100], [10,20,30,40]))