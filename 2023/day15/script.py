class Sequence():
    def __init__(self, seq):
        self.seq = seq

    def __repr__(self):
        return "< " + self.seq + " >"

    def hash(self):
        val = 0
        for char in self.seq:
            val += ord(char)
            val = val * 17
            val = val % 256

        return val

def load_seqs(path="input.txt"):
    with open("input.txt") as file:
        seqs = []

        for seq in file.readline().strip().split(","):
            newSeq = Sequence(seq)
            seqs.append(newSeq)
        return seqs

if __name__ == "__main__":
    grand_total = 0
    data = load_seqs()
    for seq in data:
        grand_total += seq.hash()
    print(grand_total)
