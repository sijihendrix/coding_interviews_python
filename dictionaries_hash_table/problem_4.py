
arr =  ['Tom', 'James', 'Frank', 'James', 'John']

def appears_twice(list):
    name_dict = {}

    for i in range(len(list)):
        if list[i] in name_dict:
            return list[i]
        else:
            name_dict[list[i]] = 1 
    return ""

print(appears_twice(arr))