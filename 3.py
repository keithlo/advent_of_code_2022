import requests
import os

def priority(char):
    lower_offset, upper_offset = 96, 38
    return (ord(char)-lower_offset) if char.islower() \
            else (ord(char)-upper_offset)

def part1(input_):
    res = 0
    for line in input_.split('\n'):
        half = len(line)>>1
        for char in set(line[:half]) & set(line[half:]):
            res += priority(char)
    return res

def part2(input_):
    res = 0
    lines = input_.split('\n')
    for i in range(0, len(lines)-1, 3):
        badge = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
        res += priority(''.join(badge))
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
