from typing import List

def ImportData(path: str ) -> List[int]:
    with open(path) as file:
        while line := file.readline():
            digits = [int(x) for x in line]
            return digits

def list_of_matches(register: List[int]) -> List[int]:
    valid = []
    forward = len(register) // 2
    for ind, val in enumerate(register):
        to_check = ind
        for i in range(forward):
            to_check =( to_check + 1) % len(register)
        if register[to_check] == val:
            valid.append(val)
    return valid


if __name__ == "__main__":
    register = ImportData("input.txt")
    valid = list_of_matches(register=register)
    print(sum(valid))