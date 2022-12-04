import requests
import os

def contains(one, two) -> bool:
    oneStart, oneEnd = map(int, one.split('-'))
    twoStart, twoEnd = map(int, two.split('-'))
    return (oneStart <= twoStart and oneEnd >= twoEnd) or \
            (twoStart <= oneStart and twoEnd >= oneEnd)

def overlap(one, two) -> bool:
    oneStart, oneEnd = map(int, one.split('-'))
    twoStart, twoEnd = map(int, two.split('-'))
    return oneStart <= twoEnd and twoStart <= oneEnd

def part1(input_) -> int:
    res = 0
    for line in input_.split('\n')[:-1]:
        interval1, interval2 = line.split(',')
        if contains(interval1, interval2):
            res += 1
    return res

def part2(input_) -> int:
    res = 0
    for line in input_.split('\n')[:-1]:
        interval1, interval2 = line.split(',')
        if overlap(interval1, interval2):
            res += 1
    return res

try:
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)

    print(part1(r.text))
    print(part2(r.text))

except e:
    print(e)
