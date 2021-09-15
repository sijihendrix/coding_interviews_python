sample_arr = [1,2,4,5,6,7,9]


def adds_up_to_ten(list, key=10):
    a_dict = {}
    for i in range(len(list)):
        base_case =  key - list[i]
        if base_case in a_dict:
            return base_case, list[i]
        else:
            a_dict[list[i]] = "value"
    return f"print there is no pair that adds up to {key}"

print(adds_up_to_ten(sample_arr, 17))