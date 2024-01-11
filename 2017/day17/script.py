

def cycle_turn(spinlock, step_size, curr_ind, to_insert):

    for i in range(step_size):
        curr_ind = ((curr_ind + 1) % len(spinlock))
    
    spinlock.insert(curr_ind + 1, to_insert)
    return spinlock, curr_ind + 1
    

if __name__ == "__main__":
    current_position = 0
    spinlock = [0]
    step_size = 344

    for i in range(1,2018):
        spinlock, current_position = cycle_turn(spinlock=spinlock, 
                                                step_size=step_size, 
                                                curr_ind=current_position,
                                                to_insert=i)
    
    print(spinlock[current_position:current_position + 3])