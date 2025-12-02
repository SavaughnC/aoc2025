def read_inputs():
    with open("realinputs.txt") as file:
        content = file.read()
        list_of_ranges = content.split(",")
            
    return list_of_ranges

input_ranges = read_inputs()

def isValid(an_id):
    stringed_id = str(an_id)

    #look at and compare increasingly larger slices
    max_div_length = len(stringed_id) // 2
    
    for div_length in range(1,max_div_length + 1):
        partitioned_id = []
        total_divs = -(-(len(stringed_id))// div_length) 

        #make a list out of the id based on partition length

        for div in range(0,total_divs,):
            start = div*div_length
            content = stringed_id[start:start+div_length]
            partitioned_id.append(content)
            
        for i in range(len(partitioned_id)-1):
            if(partitioned_id[i] != partitioned_id[i + 1]):
                break
            elif(i == len(partitioned_id) - 2):
                return False
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

