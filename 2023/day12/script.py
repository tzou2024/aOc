from itertools import chain, combinations
from copy import deepcopy
from pprint import pprint as pp

def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    subs = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    subs = [list(x) for x in subs]
    return subs

def load_data(path):
    class Config():
        def __init__(self, data, record):
            self.data = data
            self.record = record
        
        def __repr__(self):
            return "< " + self.data + " " + str(self.record) + ">"
    
        def find_blanks(self):
            '''
            find all of the questionable indices
            '''
            inds = []
            for ind, val in enumerate(self.data):
                if val == "?":
                    inds.append(ind)
            return inds
        
        def fill_in(self, inds_to_fill):
            '''
            take the mystery inds and return an adjust list with 
            all of the subsets of inds
            with each of them filled in
            '''
            # print(self.data)
            subsets = powerset(inds_to_fill)
            # print(subsets)
            adjusted = []
            for subset in subsets:
                copy = list(deepcopy(self.data))
                for ind in subset:
                    copy[ind] = "#"
                copy = [x if x != "?" else '.' for x in copy]
                adjusted.append("".join(copy))
            return adjusted
        
        def calc_ways(self):
            inds_to_fill = self.find_blanks()
            adjusted = self.fill_in(inds_to_fill)
            count = 0
            for adjustment in adjusted:
                # print(self.record)
                # print(adjustment)
                # print(self.is_valid(adjustment))
                if self.is_valid(adjustment):
                    count += 1
            return count
        
        def is_valid(self, adjusted):
            '''
            given an adjusted configuration,
            does it fit the guideline?
            '''
            # print(adjusted)
            split = adjusted.split(".")
            split = [x for x in split if len(x) > 0]
            if len(split) != len(self.record):
                return False
            for val1, val2 in zip(split, self.record):
                # print(val1, val2)
                if len(val1) != val2:
                    return False
            # print("+++++++++++++++")
            return True


    with open(path) as file:
        configs = []
        while line := file.readline():
            [data, record] = line.split()
            record = record.strip().split(",")
            record = [int(x) for x in record]
            newConfig  = Config(data, record)
            configs.append(newConfig)

    return configs

if __name__ == "__main__":
    data = load_data("input.txt")
    total = 0
    stopper = 0
    for i in data:
        summy = i.calc_ways()
        print(summy)
        total += summy
        stopper += 1
        # if stopper > 5:
        #     break
    print("++++")
    print(total)