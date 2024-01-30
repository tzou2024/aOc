
ranking = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

types_to_vals = {
    "FiveOfKind": 7,
    "FourOfKind": 6,
    "FullHouse": 5,
    "ThreeOfKind": 4,
    "TwoPair": 3,
    "OnePair": 2,
    "HighCard": 1
}

def freq_ord(camel):
    tracker = {}
    for val in camel.hand:
        tracker[val] = tracker.get(val,0) + 1
    freqord = list(tracker.values())
        
    freqord.sort(reverse=True)

    return freqord

def load_hands(path: str):
    '''
    args:
    path str
    return
    a list of hands (w info included)
    '''
    #making a camel class
    # - hand
    # - bid
    # - rank
    class Camel():
        def __init__(self, hand, bid):
            self.hand = hand
            self.bid = bid
            self.assing_type()

        def __str__(self):
            return "{'" + self.hand + "' | " + self.type + "}"
        
        def assing_type(self):
            distro = freq_ord(self)
            if distro[0] == 5:
                self.type = "FiveOfKind"
            elif distro[0] == 4:
                self.type="FourOfKind"
            elif distro[0] == 3 and distro[1] == 2:
                self.type="FullHouse"
            elif distro[0] == 3:
                self.type="ThreeOfKind"
            elif distro[0] == 2 and distro[1] == 2:
                self.type="TwoPair"
            elif distro[0] == 2:
                self.type="OnePair"
            else:
                self.type="HighCard"
 
    
    with open(path) as file:
        camels = []
        while line := file.readline():
            line = line.split()
            hand = line[0]
            bid = int(line[1])
            new_camel = Camel(hand, bid)
            camels.append(new_camel)

    return camels

def secondarySort(camel1, camel2):
    hand1 = camel1.hand
    hand2 = camel2.hand

    for x, y in zip(hand1, hand2):
        if ranking.index(x) < ranking.index(y):
            return 1
        elif ranking.index(y) < ranking.index(x):
            return -1

    return 0





def camelsort(x,y):
    '''
    take in a 2 cards and return postitive number, 0, neg
    '''
    typeval1 = types_to_vals[x.type]
    typeval2 = types_to_vals[y.type]

    if typeval1 > typeval2:
        return 1
    elif typeval2 > typeval1:
        return -1
    else:
        return secondarySort(x, y)


    
# custom sort function
# sorted_l = sorted(l, cmp=lambda x, y: x ** 3 - y ** 3) # Sort with cmp
#cmp takes x and y and return post 0 neg

if __name__ == "__main__":
    cards = load_hands("input.txt")


    from functools import cmp_to_key

    sorted_l = sorted(cards, key=cmp_to_key(camelsort))
    total_winnings = 0
    for i in range(len(sorted_l)):
        total_winnings += sorted_l[i].bid * (i + 1)

    print(total_winnings)