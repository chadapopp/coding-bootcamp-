# Given two sentences, return an arry
# that has the words that appear in both sentences

# sentence1 = 'We are really pleased to meet you in our city'
# sentence2 = 'The city was hit by a really heavy storm'
# output = ['city', 'really']



# def common_words(sentence1, sentence2):
#     words1_list = sentence1.split()
#     words2_list = sentence2.split()
#     result = []

#     for word1 in words1_list:
#         if word1 in words2_list:
#             result.append(word1)
#     return result

# print(common_words(sentence1, sentence2))


my_string1 = "apple|banana|cherry|date|elderberry"
my_string2 = "1 2 3 4 5 6 7 8 9 10"
my_string3 = "Python is an awesome programming language"



def my_split(string, delimiter):
    substring = ""
    substring_list = []
    for letter in string:
        if letter == delimiter:
            substring_list.append(substring)
            substring = " "
        else:
            substring += letter
    substring_list.append(substring)
    return substring_list

print(my_split(my_string1,"|"))
