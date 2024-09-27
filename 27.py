def count_frequency(my_list):
    freq_dict = {}  
    for item in my_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict

my_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
frequency = count_frequency(my_list)
print(frequency)
