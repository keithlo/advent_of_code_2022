import requests, os, sys, re
'''
--- Day 15: Beacon Exclusion Zone ---
part1: chord of each sensor circle should be checked for row
        - find distance from y. dy and check `d` which is not radius,
            but manhattan distance.
        - dx = d - dy. This distance goes left and right from sx
            append to set to account for different d circles
part2: 
'''
def part1(text):
    row = 10 if test else 2_000_000
    sensors = []
    for line in text:
        x,y,dx,dy = map(int, re.findall(r'(-?\d+)', line))
        d = abs(dx-x) + abs(dy-y)
        sensors.append([x,y,d])

    signals = set()
    for x,y,d in sensors:
        dy = abs(y-row)
        if dy < d:
            dx = d - dy
            for i in range(x-dx, x+dx):
                signals.add(i)
    return len(signals)

def part2(text):
    y = 2_000_000
    pass

try:
    args = sys.argv
    log  = True if 'log'  in args else False
    test = True if 'test' in args else False
    two  = True if 'two'  in args else False
    one  = True if 'one'  in args else False
    
    if test:
        with open('test15.py') as f:
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
