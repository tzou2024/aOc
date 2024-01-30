class Race():
    from functools import lru_cache
    #wrapper class for a race
    def __init__(self, time, distance ):
        #store time
        self.time = time
        #store distance
        self.distance = distance
    
    def __str__(self):
        return "Race: " + str(self.time) + " | " + str(self.distance)

    @lru_cache(maxsize=None)
    def calculate_wins(self, init_speed=0, accel=1):
        #win total
        min_win = (self.time + 1) // 2
        # function to calculate the number of wins
        # for each o the possible lengts to hold the button
        for hold_length in range(0, (self.time + 1) // 2):
            final_speed = init_speed + hold_length * accel
            #calculate final speed- init.speed + time held
            # speed = speed + hold_length

            #calculate time-let - time - time_held
            time_left = self.time - hold_length

            # print("tl",time_left,"s", final_speed,"->", final_speed * time_left)

            #calculate whether or not you'd win
            #if your final_speed * time_left > dance
            #increase the number of wins
            if time_left * final_speed > self.distance:
                min_win = hold_length
                break
        win_total = ((self.time + 1) // 2 - min_win) * 2

        if (self.time + 1) // 2 != (self.time + 1) / 2:
            win_total += 1

        return win_total
        
def importData(path: str):
    '''
    Args:
    path: path of the txt file
    
    Returns:
    races: a list of race objects to use to calc wins

    '''
            


    with open(path) as file:
        times = []
        distances = []
        while line := file.readline():
            line = line.split(":")
            attr = line[0]
            info = line[1]
            info = info.split()
            info = [int("".join(info))]
            if attr.strip() == "Time":
                times = info
            else:
                distances = info
        
        races = []
        for time, distance in zip(times, distances):
            newRace = Race(time, distance)
            races.append(newRace)

        return races
            

#import the data into races
# generate the wins for each of these race objects
#multiply them all together
if __name__ == "__main__":
    races = importData("input.txt")
    win_totals = []
    for race in races:
        
        win_totals.append(race.calculate_wins())
    final = 1
    for i in win_totals:
        final = i * final
    print(final)
