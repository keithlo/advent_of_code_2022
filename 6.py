import requests
import os

# classic sliding window problem
def solve(text) -> int:
    start, chars = 0, set()
    part1 = part2 = None      # part2
    for end, char in enumerate(text):
        while char in chars:
            chars.remove(text[start])
            start += 1
        chars.add(char)
        if len(chars) == 4:
            part1 = end+1
        if len(chars) == 14:   # part2
            part2 = end+1
    return part1, part2

try:
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)
    text = r.text.split('\n')[0]

    print(solve(text))
except e:
    print(e)
