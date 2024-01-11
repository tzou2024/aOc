from typing import List, Tuple
def importData(path: str) -> List[List[int]]:
    registers = []
    with open(path) as file:
        while line := file.readline():
            line = line.split()
            registers.append([int(x) for x in line])
    return registers

def find_divisors(line: List[int]) -> Tuple:
    for ind1, val1 in enumerate(line):
        for _, val2 in enumerate(line[ind1 + 1:]):
            if (val1 / val2).is_integer():
                    return (val1, val2)
                
            elif (val2 / val1).is_integer():
                    return (val2, val1)

    return ValueError

def find_totals(lines):
    tuples = []
    for line in lines:
        tuples.append(find_divisors(line))
    
    sum = 0
    for  packed in tuples:
        print(packed)
        val1, val2 = packed
        sum += val1 / val2

    return sum
    
if __name__ == "__main__":
    registers = importData("input.txt")
    print(find_totals(registers))