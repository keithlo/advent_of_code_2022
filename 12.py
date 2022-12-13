import requests
import os
from collections import deque

'''
--- Day 12: Hill Climbing Algorithm ---
part1: Shortest path. BFS☑ or heap(djikstra)
       - Heuristic function g(x) := could naively be manhattan distance to `E`
part2: More start spots
'''

def findStartEnd(text, startIndicators):
    start, end = [], None
    for i, row in enumerate(text):
        for j, char in enumerate(row):
            if char in startIndicators: start.append((i,j))
            if char == 'E': end = (i,j)
    return start, end

def findPath(text, start, end) -> int:
    n, m, q, visited = len(text), len(text[0]), deque(), set()
    for s in start:
        q.append([s,0])
        visited.add(s)
    while q:
        location, distance = q.popleft()
        if location == end:
            return distance
        i,j = location
        char = text[i][j]
        for i, j in (i+1,j),(i,j+1),(i-1,j),(i,j-1):
            if n>i>=0<=j<m and (i,j) not in visited:
                next_char = text[i][j]
                if next_char == 'E' and ord(char) < ord('y'): continue
                if char == 'S' or ord(next_char) <= ord(char)+1:
                    next_location = (i,j)
                    visited.add(next_location)
                    q.append([next_location, distance+1])
    return -1

def part1(text) -> int:
    start, end = findStartEnd(text, set('S'))
    return findPath(text, start, end)

def part2(text) -> int:
    start, end = findStartEnd(text, set('Sa'))
    return findPath(text, start, end)

try:
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)
    text = r.text.split('\n')[:-1]
    print(part1(text))
    print(part2(text))

    #with open('test12.py') as f:
    #    text = f.read().split('\n')[:-1]
    #    print(part1(text))
    #    print(part2(text))
except e:
    print(e)
