def read_inputs():
    with open("testinputs.txt") as file:
        content = [line.rstrip() for line in file]     
        div = content.index('')
        fresh_ids = content[:div]  
        available_ids = content[div + 1:] 
    return fresh_ids, available_ids  

fresh_id_ranges, available_ids = read_inputs()

def get_fresh_ids(ranges):
    bonzo = str(len(ranges))
    fresh_ids = []
    for r in ranges:
        parts = r.split('-')
        start = int(parts[0])
        end = int(parts[1])
        print("starting work on range " + str(ranges.index(r) + 1) + " of " + bonzo)
        
        for n in range(start, end + 1):
            if n not in fresh_ids:
                print("new id: " + str(n))
                fresh_ids.append(n)
            
    return len(fresh_ids)

    
print(get_fresh_ids(fresh_id_ranges))
    