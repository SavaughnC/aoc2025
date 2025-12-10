def read_inputs():
    with open("realinputs.txt") as file:
        content = [line.rstrip() for line in file]     
        div = content.index('')
        fresh_ids = content[:div]  
        available_ids = content[div + 1:] 
    return fresh_ids, available_ids  

fresh_id_ranges, available_ids = read_inputs()

def get_fresh_ids(ranges):
    fresh_ids = []
    for r in ranges:
        parts = r.split('-')
        start = int(parts[0])
        end = int(parts[1])
        
        for n in range(start, end + 1):
            if n not in fresh_ids:
                fresh_ids.append(n)
            
    return fresh_ids

def sum_fresh_ingredients(fresh_ranges, _available_ids):
    bad_ingredients = 0
    total_fresh_ingredients = 0
    fresh_ids = get_fresh_ids(fresh_ranges)
    for i in _available_ids:
        j = int(i)
        if j in fresh_ids:
            total_fresh_ingredients += 1
        else:
            bad_ingredients += 1
            
    return total_fresh_ingredients
    
print(sum_fresh_ingredients(fresh_id_ranges,available_ids))
    