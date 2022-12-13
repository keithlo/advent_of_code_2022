import requests, os, sys
from functools import cmp_to_key
'''
--- Day 13: Distress Signal ---
part1: eval lines into list(s). Process based on rules:
        - if types are not lists, convert to lists
part2: sort based on signal:
        1 - make Signal class with custom comparators or 
        2 - sorted with lambda function/ cmp_to_key
'''

def process(l, r):
    if type(l) != list: l = [l]
    if type(r) != list: r = [r]
    i = 0
    while i < max(len(l), len(r)):
        if i == len(r): return -1
        if i == len(l): return 1
        if type(l[i]) == list or type(r[i]) == list:
            p = process(l[i], r[i])
            if p != 0: return p
        if type(l[i]) == type(r[i]) == int:
            if l[i] < r[i]: return 1
            if l[i] > r[i]: return -1
        i+=1
    return 0


def part1(text) -> int:
    count = 0
    for i in range(0, len(text), 3):
        p = process(eval(text[i]), eval(text[i+1]))
        if p != -1: count += (i+3)//3
    return count

'''
Implemented __lt__ with a Signal class for sorting without lambda fn
''' 
class Signal:
    def __init__(self, signal):
        self.signal = signal

    def __repr__(self):
        return 'signal: '+ str(self.signal)

    def process(self, l, r):
        if type(l) != list: l = [l]
        if type(r) != list: r = [r]
        i = 0
        while i < max(len(l), len(r)):
            if i == len(r): return -1
            if i == len(l): return 1
            if type(l[i]) == list or type(r[i]) == list:
                p = self.process(l[i], r[i])
                if p != 0: return p
            if type(l[i]) == type(r[i]) == int:
                if l[i] < r[i]: return 1
                if l[i] > r[i]: return -1
            i+=1
        return 0

    def __lt__(self, other):
        return False if self.process(self.signal, other.signal) == -1 else True

def part2(text):
    dividerOne, dividerTwo = Signal([[2]]), Signal([[6]])
    signals = [dividerOne, dividerTwo]
    for line in text:
        if line: signals.append(Signal(eval(line)))
    signals.sort()
    #signals.sort(key=cmp_to_key(process))
    return (signals.index(dividerOne)+1) * (signals.index(dividerTwo)+1)

try:
    args = sys.argv
    log =  True if 'print' in args else False
    test = True if 'test'  in args else False
    two =  True if 'two'   in args else False
    one =  True if 'one'   in args else False
    
    if test:
        with open('test13.py') as f:
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
