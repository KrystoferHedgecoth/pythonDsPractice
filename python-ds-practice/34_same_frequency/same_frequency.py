def same_frequency(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)

    freq_dict1 = {}
    freq_dict2 = {}

    for digit in str_num1:
        if digit in freq_dict1:
            freq_dict1[digit] += 1
        else:
            freq_dict1[digit] = 1

    for digit in str_num2:
        if digit in freq_dict2:
            freq_dict2[digit] += 1
        else:
            freq_dict2[digit] = 1

    for key, value in freq_dict1.items():
        if key not in freq_dict2 or value!= freq_dict2[key]:
            return False

    return True