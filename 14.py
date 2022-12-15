import requests, os, sys
'''
--- Day 14: Regolith Reservoir ---
part1: simulation of sand, using set for solid indicator
        - potentially keep highest point for each column?
part2: 
'''

def build_walls(text):
    #print(text)
    # do we need a grid? or can we just place in set?
    # think a set and simulate just dropping vertically
    walls = set()
    max_depth = 0
    for path in text:
        previous_edge = None
        for edges in path.split('->'):
            split = edges.strip().split(',')
            edge,depth = list(map(int, split))
            max_depth = max(max_depth, depth)
            if previous_edge:
                if previous_edge[0] == edge:
                    _min = min(previous_edge[1], depth) 
                    _max = max(previous_edge[1], depth) 
                    for i in range(_min,_max+1):
                        walls.add((edge, i))

                if previous_edge[1] == depth:
                    _min = min(previous_edge[0], edge) 
                    _max = max(previous_edge[0], edge) 
                    for i in range(_min,_max+1):
                        walls.add((i, depth))
            previous_edge = [edge, depth]
    return walls, max_depth

def add_sand(solids, i, j, depth, count):
    if j == depth: return True
    if (i,j+1) not in solids:
        return add_sand(solids, i, j+1, depth, count)
    if (i-1,j+1) not in solids:
        return add_sand(solids, i-1, j+1, depth, count)
    if (i+1,j+1) not in solids:
        return add_sand(solids, i+1, j+1, depth, count)
    solids.add((i,j))
    count[0] += 1

def part1(text):
    solids, depth = build_walls(text)
    print(depth) if log else 0;
    if log: [print(wall) for wall in sorted(solids)]
    placement, abyss = [0], False
    while not abyss:
       abyss = add_sand(solids, 500, 0, depth, placement)
    return placement[0]

def add_sand2(solids, i, j, depth, count):
    if (500,0) in solids:
        return True
    if j == depth+1:
        solids.add((i,j))
        count[0] += 1
        return 
    if (i,j+1) not in solids:
        return add_sand2(solids, i, j+1, depth, count)
    if (i-1,j+1) not in solids:
        return add_sand2(solids, i-1, j+1, depth, count)
    if (i+1,j+1) not in solids:
        return add_sand2(solids, i+1, j+1, depth, count)
    solids.add((i,j))
    count[0] += 1

def part2(text):
    solids, depth = build_walls(text)
    placement, source = [0], False
    while not source:
       source = add_sand2(solids, 500, 0, depth, placement)
    return placement[0]

try:
    args = sys.argv
    log =  True if 'log'  in args else False
    test = True if 'test' in args else False
    two =  True if 'two'  in args else False
    one =  True if 'one'  in args else False
    
    if test:
        with open('test14.py') as f:
            text = f.read().split('\n')[:-1]
            if two: print(part2(text))
            if one: print(part1(text))
    else:
        day = os.path.basename(__file__).split('.')[0]
        url = 'https://adventofcode.com/2022/day/'+day+'/input'
        cookies = {'session': os.environ['ADVENT_TOKEN']}
        r = requests.get(url, cookies=cookies)
        text = r.text.split('\n')[:-1]
        if two: print(part2(text))
        if one: print(part1(text))

except e:
    print(e)
