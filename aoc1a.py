
def read_inputs():
    tuples_list = []
    with open("realinputs.txt") as file:
        for line in file:
            letter = line[0]
            number = int(line[1:])
            tuples_list.append((letter, number))
            
    return tuples_list

inputs = read_inputs()

#print(inputs[1][1])

def spin_lock(spins):
    current_position = 50
    times_on_zero = 0
    for spin in spins:
        direction = spin[0] 
        raw_amount = spin[1]
        amount = spin[1] 
        if(amount > 99):
            times_on_zero = times_on_zero + (amount // 100)
            amount = amount % 100
        if (direction == 'L' and amount <= current_position):
            current_position -= amount
        elif (direction == 'L' and amount > current_position):
            if(current_position != 0):
                times_on_zero += 1
            current_position = 100 - (amount - current_position)
        if (direction == 'R' and amount <= 99 - current_position):
            current_position += amount
        elif (direction == 'R' and amount > 99 - current_position):
            times_on_zero += 1
            current_position = amount - (99 - current_position) - 1
        if(current_position == 0 and direction == "L"):
            times_on_zero += 1

        print("I just spun: " + str(raw_amount) + " times in the " + str(direction) + " direction, the times landed on 0 counter is at " + str(times_on_zero) + " and the current position is:" + str(current_position) )
    return times_on_zero   
    


print(spin_lock(inputs))