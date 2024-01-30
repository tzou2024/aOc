startOpts = {
    "N": {
        "|": (1,0),
        "L": (1,0),
        "J": (1,0),
    },
    "S": {
        "|": (-1,0),
        "7": (-1,0),
        "F": (-1,0)
    },
    "E": {
        "-": (0, 1),
        "J": (0, 1),
        "7": (0,1)
    },
    "W": {
        "-": (0,-1),
        "L": (0,-1),
        "F": (0,-1)
    }
}

moveOpts = {
    "|": [(1,0), (-1, 0)],
    "-": [(0,1), (0,-1)],
    "L": [(-1, 0), (0,1)],
    "J": [(0,-1), (-1,0)],
    "7": [(0,-1), (1,0)],
    "F": [(1,0), (0,1)]
}