import requests
import os
from collections import defaultdict

'''
forest elevations         
--------------------------
part1: view from every side. O(n)
part2: expand outward... 
'''

def visible(forest,i,j,temp,max_height) -> int:
    if forest[i][j] > max_height:
        temp[i][j] = 1
        return forest[i][j]
    else: return -1

def part1(text) -> int:
    forest = [[int(char) for char in row] for row in text]
    temp   = [[        0 for char in row] for row in text]
    l = len(forest)
    for i in range(l):
        max_height, temp[i][0] = forest[i][0], 1      # ->
        for j in range(1,l):
            max_height = max(visible(forest, i, j, temp, max_height), max_height)
        max_height, temp[i][l-1] = forest[i][l-1], 1  # <-
        for j in range(l-2,0,-1):
            max_height = max(visible(forest, i, j, temp, max_height), max_height)
        max_height, temp[0][i] = forest[0][i], 1      # invert west -> east == north -> south
        for j in range(1,l):
            max_height = max(visible(forest, j, i, temp, max_height), max_height)
        max_height, temp[l-1][i] = forest[l-1][i], 1  # invert east -> west == south -> north
        for j in range(l-2,0,-1):
            max_height = max(visible(forest, j, i, temp, max_height), max_height)

    return sum([sum(row) for row in temp])

def part2(text) -> int:
    forest, scenic_score = [[int(char) for char in row] for row in text], 0
    l = len(forest)
    for i in range(l):
        for j in range(l):
            tree_height = forest[i][j]
            up = left = down = right = 0
            m, n = i, j
            while m > 0:
                m -= 1; up += 1
                if forest[m][n] >= tree_height: break
            m, n = i, j
            while n > 0:
                n -= 1; left += 1
                if forest[m][n] >= tree_height: break
            m, n = i, j
            while m < len(forest)-1:
                m += 1; down += 1
                if forest[m][n] >= tree_height: break
            m, n = i, j
            while n < len(forest)-1:
                n += 1; right += 1
                if forest[m][n] >= tree_height: break

            scenic_score = max(scenic_score, up * left * right * down)
    return scenic_score

try:
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)
    text = r.text.split('\n')[:-1]

    print(part2(text))

    #with open('test8.py') as f:
    #    text = f.read().split('\n')[:-1]
    #    print(part2(text))
except e:
    print(e)
