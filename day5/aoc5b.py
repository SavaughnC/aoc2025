def read_inputs():
    with open("testinputs.txt") as file:
        content = [line.rstrip() for line in file]     
        div = content.index('')
        fresh_ids = content[:div]  
        available_ids = content[div + 1:] 
    return fresh_ids, available_ids  

fresh_id_ranges, available_ids = read_inputs()


def sum_fresh_ids(fresh_ranges):
    total_fresh_ids = 0

    for i in _available_ids:
       for r in fresh_ranges:
            div = r.index("-")
            lower_bound = int(r[:div])
            upper_bound = int(r[div + 1:])
            #print("checking if id: " + str(i) + " is in range: " + str(r) )
            if (lower_bound <= int(i) <= upper_bound):
                total_fresh_ingredients += 1
                break
        
        
            
    return total_fresh_ingredients
    
print(sum_fresh_ids(fresh_id_ranges))
    