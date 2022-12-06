import requests
import os

'''
Sets up stacks using a matrix.
'''
def setupStacks(text) -> [[str]]:
    stacks_block = []
    for line in text:
        if line[0] == '[': stacks_block.append(line)
        else: break

    stacks = [[]]
    depth = len(stacks_block)
    for i, char in enumerate(line):
        if char.isnumeric():
            j = depth-1
            stack = []
            while j >= 0:
                cargo = stacks_block[j][i]
                if cargo.isalpha(): stack.append(cargo)
                j -= 1
            stacks.append(stack)
    return stacks

def setupStacks(text) -> [[str]]:
    stack_count = len(text[0]) // 4 + 2
    stacks = [[] for _ in range(stack_count)]
    for line in text:
        if line[0:2] == ' 1': break
        for i, char in enumerate(line):
            if i % 4 == 1 and char.isalpha():
                stacks[(i//4)+1].append(char)
    return [stack[::-1] for stack in stacks]

def moveCargo(stacks, count, src, dest):
    for _ in range(count):
        stacks[dest].append(stacks[src].pop())

def moveCargo2(stacks, count, src, dest):
    stacks[dest].extend(stacks[src][-count:])
    del stacks[src][-count:]

def solve(text) -> int:
    stacks = setupStacks(text)
    stacks2 = [stack[:] for stack in stacks] # part2

    for line in text:
        if line and line[0:4] == 'move':
            _, count, _, src, _, dest = line.split(' ')
            count, src, dest = map(int, [count, src, dest])
            moveCargo(stacks, count, src, dest)
            moveCargo2(stacks2, count, src, dest) # part2

    res = ''.join([stack[-1] for stack in stacks[1:]])
    res2 = ''.join([stack[-1] for stack in stacks2[1:]]) # part2
    return res, res2

try:
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)
    text = r.text.split('\n')

    print(solve(text))
except e:
    print(e)
