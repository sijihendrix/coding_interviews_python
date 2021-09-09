def larger_than(str1, str2):
    if len(str1) > len(str2):
        return True
    elif len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] > str2[i]:
                return True

    return False



print(larger_than("24","25"))