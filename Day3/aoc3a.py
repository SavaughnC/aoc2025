def read_inputs():
    with open("realinputs.txt") as file:
        content = [line.rstrip() for line in file]
            
    return content

input_banks = read_inputs()




#get the highest digit's index from a list of digits
def get_highest_digit_index(trimmed_bank):
    
    highest_digit_index = 0
    #i need to get the leftmost index
    for index in range(len(trimmed_bank)):
        if(trimmed_bank[index] > trimmed_bank[highest_digit_index]):
            highest_digit_index = index
    #print("returning an index of: " + str(highest_digit_index))    
    return highest_digit_index
    

  
def evaluate_highest_joltage(raw_bank):
    list_bank = list(str(raw_bank))
    proxy_bank = list_bank.copy()
    #get tens digit first
    del list_bank[len(list_bank)-1]
    #print(list_bank)
    tens_index = get_highest_digit_index(list_bank)
    
    #trim the proxy bank based on the index of the tens digit
    for i in range(tens_index + 1):
        del proxy_bank[0]
    
    ones_index = get_highest_digit_index(proxy_bank)
    
    tens_digit = list_bank[tens_index]
    ones_digit = proxy_bank[ones_index]
    
    max_joltage = tens_digit  + ones_digit
    #print(ones_digit)
    #print(tens_digit)
   # print("max joltage: " + max_joltage)
    return int(max_joltage)


  
def sum_max_joltage(list_of_banks):   
    
    running_total= 0
    
    for bank in list_of_banks:
        joltage = evaluate_highest_joltage(bank)
        running_total += joltage
    
    return running_total
    
#evaluate_highest_joltage(238869373421)
print(sum_max_joltage(input_banks))