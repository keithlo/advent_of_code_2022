import requests
import os
from collections import defaultdict

'''
file system traversal
--------------------------------------------------
`cd` only command that (pushes|pops) a stackframe.
Parse until you see a `cd`
'''
class Day7Solver:
    def __init__(self) -> None:
        self.i = 0

    def valid_line(self, text) -> bool:
        return self.i < len(text)

    def is_command(self, line) -> bool:
        return line[0] == '$'

    def is_cd(self, line) -> bool:
        return self.is_command(line) and line[1] == 'cd'

    def traverse(self, cur, dir_sizes, text) -> None:
        _, _, directory = text[self.i].split(' ')
        cur_dir = cur + directory
        self.i += 1
        while self.valid_line(text):
            line = text[self.i].split(' ')
            if self.is_cd(line):
                dest = line[2]
                if dest == '..':
                    return
                self.traverse(cur_dir, dir_sizes, text)
                dir_sizes[cur_dir] += dir_sizes[cur_dir+dest]
            elif not self.is_command(line) and line[0] != 'dir':
                dir_sizes[cur_dir] += int(line[0])
            self.i += 1

    def solve(self, text) -> int:
        dir_sizes = defaultdict(int)
        self.traverse('', dir_sizes, text)
        part1 = sum([v for k,v in dir_sizes.items() if v <= 100000])

        # part 2
        total_disk_space, space_for_update = 70_000_000, 30_000_000
        available_space = total_disk_space - dir_sizes['/']
        need_to_free_amount = space_for_update - available_space
        part2 = min([v for k,v in dir_sizes.items() if v > need_to_free_amount])

        return part1, part2

try:
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)
    text = r.text.split('\n')[:-1]

    print(Day7Solver().solve(text))

    #with open('test7.py') as f:
    #    text = f.read().split('\n')[:-1]
    #    print(Day7Solver().solve(text))
except e:
    print(e)
