import requests
import os

def part1(input_):
    for line in input_.split('\n'):
        print(line)
    return input_

try:
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)

    print(part1(r.text))

except e:
    print(e)
