class Reading():
    '''
    wrapper class for readings
    '''
    def __init__(self, line):
        self.line = line[::-1]
        self.next = 0
    
    def __repr__(self):
        return "<line: " + str(self.line) + ">"
    
    def zero_check(self, arr):
        '''
        conditional for checking zeros
        '''
        for x in arr:
            if x != 0:
                return False
        return True

    def differences(self, arr):
        '''
        return a list of differences
        '''
        diffs = []
        for i in  range(1, len(arr)):
            diffs.append(arr[i] - arr[i - 1])
        return diffs

    # def calc_next(self, history):
    #     history = history[::-1]
    #     for i in range(len(history) - 1):
    #         first_end = history[i][-1]
    #         second_end = history[i+1][-1]
    #         history[i+1].append(first_end + second_end)
    #     return history[-1][-1]

    def predict(self):
        history = []
        #add differences in to this history object until
        #zero check is true
        curr_line = self.line
        while not self.zero_check(curr_line):
            history.append(curr_line[-1])
            curr_line = self.differences(curr_line)
        self.next = sum(history)

        
        


def load_data(path: str):
    '''
    create and return list of reading objects
    '''
    readings = []
    with open(path) as file:
        while line := file.readline():
            line = line.split()
            line = [int(x) for x in line]
            newReading = Reading(line)
            readings.append(newReading)
    return readings
        

if __name__ == "__main__":
    listings = load_data('input.txt')
    for i in listings:
        i.predict()
    print(sum([i.next for i in listings]))