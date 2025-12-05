def read_inputs():
    with open("realinputs.txt") as file:
        content = [line.rstrip() for line in file]            
    return content

input_rolls = read_inputs()

def is_retrievable(row, column, max_surrounding = 4):

    running_count = -1
    
    if(input_rolls[row][column] != "@"):
        return False    
    x_ind = row - 1    
    for x in range(3):
        y_ind = column-1
        for y in range(3):
            if(0 <= x_ind < len(input_rolls) and 0 <= y_ind < len(input_rolls[row]) and input_rolls[x_ind][y_ind] == "@"):
                running_count += 1
            y_ind += 1
        x_ind += 1

    return running_count < max_surrounding

    
def sum_retrievable_rolls(roll_matrix):
    running_count = 0
    for row in range(len(roll_matrix)):
        for column in range(len(roll_matrix[row])):
            if(is_retrievable(row,column)):
                running_count += 1
    
    return running_count
    
print(sum_retrievable_rolls(input_rolls))