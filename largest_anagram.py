
def find_largest_anagram(string_list):
    
    list_of_anagrams = []
    
    for x in range(len(string_list)):
        anagrams = []
        for y in range(len(string_list)):

            if sorted(string_list[x]) == sorted(string_list[y]):
                anagrams.append(string_list[y])

        list_of_anagrams.append(anagrams)

    max_length = len(list_of_anagrams[0])
    max_index = 0
    
    for i in range(len(list_of_anagrams)):    
        if max_length < len(list_of_anagrams[i]):
            max_length = len(list_of_anagrams[i])
            max_index = i 

    return list_of_anagrams[max_index]




if __name__ == '__main__':
    
    list_of_strings = []
    
    num_elements = int(input())

    for i in range(num_elements):
        input_string = input()
        list_of_strings.append(input_string)


    longest_anagram = find_largest_anagram(list_of_strings)
    
    print(longest_anagram)

