def gametomaxdraw(game):
    sets = game.split(";")
    sets = [x.lstrip().rstrip() for x in sets]
    drawlist = []
    for set in sets:
        drawlist = drawlist + organizeset(set)
    maxdraw = maxdraws(drawlist)
    print("maxdraw", maxdraw)
    return maxdraw

def organizeset(set):
    draws = set.split(",")
    draws = [x.lstrip().rstrip() for x in draws]
    drawlist = []
    for draw in draws:
        [n, c] = draw.split(" ")
        drawlist.append({
            "color": c,
            "number": n
        })
    return drawlist

def maxdraws(drawlist):
    master = {
        "blue": 0,
        "red": 0,
        "green": 0
    }
    for val in drawlist:
        if int(val["number"]) > master[val["color"]]:
            master[val["color"]] = int(val["number"])
    return master

def checkmaxdraws(maxdraw):
    return maxdraw["red"] <= 12 and maxdraw["green"] <= 13 and maxdraw["blue"] <= 14

with open("input.txt") as file:
    ind = 0
    trulist = []
    for item in file:
        ind += 1
        print(item)
        colon = item.index(":")
        sub = item[colon + 2:]
        sub = sub.rstrip().lstrip()
        maxdraw = gametomaxdraw(sub)
        if checkmaxdraws(maxdraw):
            trulist.append(ind)
        # print("sets", sets)
    print(sum(trulist))