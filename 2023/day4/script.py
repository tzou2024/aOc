

def get_numb_lists(card):
    colon = card.index(":")
    card = card[colon + 1:]
    [winning, mine] = card.split(" | ")
    winning = [x.strip() for x in winning.split()]
    mine = [x.strip() for x in mine.split()]
    return winning, mine

def count_up_score(winning, mine):
    scored = list(filter(lambda number: number in winning, mine))
    if len(scored) == 0:
        return 0
    elif len(scored) == 1:
        return 1
    else:
        return 1 * (2 ** (len(scored) - 1))

    
with open("input.txt") as file:
    totalworth = 0
    for item in file:
        item = item.strip()
        winning, mine = get_numb_lists(item)
        totalworth += count_up_score(winning, mine)
    print(totalworth)