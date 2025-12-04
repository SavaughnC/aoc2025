def read_inputs():
    with open("realinputs.txt") as file:
        content = [line.rstrip() for line in file]
            
    return content

input_banks = read_inputs()




#get the leftmost highest digit's index from a list of digits
def get_highest_digit_index(trimmed_bank):
    
    highest_digit_index = 0
    for index in range(len(trimmed_bank)):
        if(trimmed_bank[index] > trimmed_bank[highest_digit_index]):
            highest_digit_index = index
    #print("returning an index of: " + str(highest_digit_index) + " from the trimmed bank of: " + str(trimmed_bank))    
    return highest_digit_index

  #need 12 digits, when evaluating digits (12 - n) digits need to be left off the end 
  # so list slice is like [:len(bank)-(12-n)]  
def evaluate_highest_joltage(_bank, total_digits = 12):
    
    storage_bank = []
    list_bank = list(str(_bank))
    proxy_bank = list_bank.copy()
    
    for digit in range(total_digits): 
        
        offset = len(proxy_bank) - (total_digits - digit) + 1
        highest_digit_index = get_highest_digit_index(proxy_bank[:offset])
        
        storage_bank.append(proxy_bank[highest_digit_index])   
        
        #trim proxy
        for i in range(highest_digit_index + 1):
            del proxy_bank[0]
    
    max_joltage = 0
    #get number from bank and merge into a n'th digit number
    for i in range(total_digits):
        max_joltage += int(storage_bank[i]) * (10 ** (total_digits-i))
    
    fixed_joltage = max_joltage / 10
    return int(fixed_joltage)


  
def sum_max_joltage(list_of_banks):   
    
    running_total= 0
    
    for bank in list_of_banks:
        joltage = evaluate_highest_joltage(bank)
        running_total += joltage
    
    return running_total
    
#evaluate_highest_joltage(238869373421)
print(sum_max_joltage(input_banks))