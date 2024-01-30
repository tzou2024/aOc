class Network():
    def __init__(self, sequence, mapping):
        self.sequence = sequence
        self.mapping = mapping
        self.maptracks = []
        self.generate_initial_maptracks()
    
    def __str__(self):
        return "newtork: " + self.sequence

    def generate_initial_maptracks(self):
        for key in self.mapping.keys():
            if key[len(key) - 1] == 'A':
                self.maptracks.append(key)
    
    def step(self, seqchar, i):
        #take in a list ex where each item starts at a starting
        #change the maptracks to update each step
        self.maptracks[i] = self.mapping[self.maptracks[i]][seqchar]
    
    def finished(self, i):
        return self.maptracks[i][-1] == 'Z'

    def stepcount_a_z(self):
        finals = []

        for i in range(len(self.maptracks)):
            stepcount = 0
            seqtrack = 0

            while not self.finished(i):
                print(self.maptracks)
                stepcount += 1
                seqchar = self.sequence[seqtrack]
                # print(seqchar)
                self.step(seqchar, i)
                seqtrack = (seqtrack + 1) % len(self.sequence)

            finals.append(stepcount)
        from math import gcd
           #will work for an int array of any length
        lcm = 1
        for i in finals:
            lcm = lcm*i//gcd(lcm, i)
        print(lcm)

        return finals

def load_data(path: str):
    sequence = ""
    mapping = {}
    with open(path) as file:
        lines = file.readlines()
        lines = [x.strip() for x in lines]
        sequence = lines[0]

        for line in lines[2:]:
            parts = line.split(" = ")
            key = parts[0]
            to_remove = ["(", ",",")"]
            for character in to_remove:
                parts[1] = parts[1].replace(character, "")
            [l, r] = parts[1].split()
            mapping[key] = {
                "L": l,
                "R": r
            }
    new_network = Network(sequence=sequence, mapping=mapping)

    return new_network



    # load in the data into a network object and return it


if __name__ == "__main__":
    network = load_data("input.txt")
    print(network.stepcount_a_z())


    