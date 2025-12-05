def read_inputs():
    with open("realinputs.txt") as file:
        content = [line.rstrip() for line in file]
            
    return content

input_rolls = read_inputs()

def is_retrievable(row, column, max_surrounding = 4):
    x_ind = row - 1
    #y_ind = column - 1
    running_count = -1
    #check if roll is in space to begin with
    if(input_rolls[row][column] != "@"):
        return False    
    
    for x in range(3):
        y_ind = column-1
        for y in range(3):
            #check if within range and contains roll
            if(0 <= x_ind < len(input_rolls) and 0 <= y_ind < len(input_rolls[row]) and input_rolls[x_ind][y_ind] == "@"):
                #print("i found a roll at: " + str(x_ind) + "," + str(y_ind) + " which is adjacent to: " + str(row) + "," + str(column))
                running_count += 1
            #else:
                #print("i found NOTHING at: " + str(x_ind) + "," + str(y_ind) + " which is adjacent to: " + str(row) + "," + str(column))
            y_ind += 1
        x_ind += 1
    
    #print("running_count: " + str(running_count) + " at the location of " + str(row) + ", " + str(column))
    
    if(running_count < max_surrounding):
        return True
    else:
        return False
    
def sum_retrievable_rolls(roll_matrix):
    running_count = 0
    for row in range(len(roll_matrix)):
        for column in range(len(roll_matrix[row])):
            if(is_retrievable(row,column)):
                running_count += 1
    
    return running_count
    
print(sum_retrievable_rolls(input_rolls))