def countdown_array(number):
    result = []
    for i in range(number, -1, -1):
        result.append(i)
    return result
input_number = 10
countdown = countdown_array(input_number)
print(countdown)
print("Length of the array:", len(countdown))

def calculate_sum(array):
    first_value = array[0]
    array_length = len(array)

    if isinstance(first_value, (int, float)):
        return first_value + array_length
    else:
        return "First value is not a number"

number_array = [5,2,8,3,9]
string_array = ["what", "Hello","World"]
boolean_array = [False, True, False]

print(calculate_sum(number_array))
print(calculate_sum(string_array))
print(calculate_sum(boolean_array))

def count_greater_than_second(array):
    second_value = array[1]
    count = 0

    for value in array:
        if value > second_value:
            print(value)
            count +=1
    return count

my_array = [1,3,4,7,9,13]
greater_values_count = count_greater_than_second(my_array)
print("Number of values greater than the second value:", greater_values_count)


def filter_greater_than_second(array):
    if len(array) <= 1:
        print("Array has only one element.")
        return []
    
    second_value = array[1]
    result = []
    for value in array:
        if value > second_value:
            result.append(value)
    
    count = len(result)
    print("Number of values greater than the second value:", count)
    return result

my_array = [1, 3, 5, 7, 9, 13]
my_array_1 = [1]

filtered_array = filter_greater_than_second(my_array)
print("Filtered array:", filtered_array)

filtered_array = filter_greater_than_second(my_array_1)
print("Filtered array:", filtered_array)

def create_array(num1, num2):
    if num1 == num2:
        print("Jinx!")
    
    result = [num2] * num1
    return result
number1 = 3
number2 = 3

result_array = create_array(number1, number2)
print("Result Array", result_array)

def fit_first_value(array):
    if array[0] > len(array):
        return("Too Big!")
    elif array[0] < len(array):
        return("Too Small!")
    else:
        return("Just Right")

arr1 = [4,2,3,4]
result = fit_first_value(arr1)
print(result)

def fahrenheightToCelsius(fDegrees):
    cDegrees = (fDegrees -32) * 5/9
    return cDegrees

fahrenheit = 80
celsius = fahrenheightToCelsius(fahrenheit)
print(f"{fahrenheit} degrees F is equal to {celsius} degrees C. ")