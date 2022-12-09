import requests
import os
from collections import defaultdict

'''
Rope Motions
--------------------------
part1: relative motion
part2: 
'''

def part1(text) -> int:
    spaces = set()
    for line in text:
        direction, distance = line.split(' ')
        distance = int(distance)
        print(direction, distance)

    head = tail = 0

    return len(spaces)

def part2(text) -> int:
    pass

try:
    #day = os.path.basename(__file__).split('.')[0]
    #url = 'https://adventofcode.com/2022/day/'+day+'/input'
    #cookies = {'session': os.environ['ADVENT_TOKEN']}
    #r = requests.get(url, cookies=cookies)
    #text = r.text.split('\n')[:-1]

    #print(part2(text))

    with open('test9.py') as f:
        text = f.read().split('\n')[:-1]
        print(part1(text))
except e:
    print(e)
