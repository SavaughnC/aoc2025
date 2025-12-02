def read_inputs():
    with open("realinputs.txt") as file:
        content = file.read()
        list_of_ranges = content.split(",")
            
    return list_of_ranges

input_ranges = read_inputs()

def isValid(an_id):
    stringed_id = str(an_id)
    midpoint = len(stringed_id) // 2
    front_half = stringed_id[:midpoint]
    back_half = stringed_id[midpoint:]
    if(front_half == back_half):
        return False
    else:
        return True
    
#range_of_ids is a string formatted like '###-###'
def retrieve_invalid_ids_from_range(range_of_ids):
    invalid_ids = []
    split_range = range_of_ids.split("-")
    start = int(split_range[0])
    end = int(split_range[1])
    range_of_ids_enumerated = range(start,end + 1)
    for _id in range_of_ids_enumerated:
        if(isValid(_id) != True):
            invalid_ids.append(_id)
    return invalid_ids
    
def sum_invalid_ids(list_of_id_ranges):
    running_total = 0
    for id_range in list_of_id_ranges:
        for _id in retrieve_invalid_ids_from_range(id_range):
            running_total += _id
    return running_total
    
print(sum_invalid_ids(input_ranges))
    