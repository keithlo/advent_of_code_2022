import requests
import logging
import os

def setup_request_logs():
    import http.client as http_client
    http_client.HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def part1(input_):
    equal =        { 'A':'X', 'B':'Y', 'C':'Z' }
    choice_win =   { 'A':'Y', 'B':'Z', 'C':'X' }
    choice_score = { 'X': 1,  'Y': 2,  'Z': 3  }
    score = 0
    for round_ in input_.split('\n')[:-1]:
        theirs, mine = round_.split(' ')
        if equal[theirs] == mine: score += 3
        elif choice_win[theirs] == mine:
            score += 6
        score += choice_score[mine]
    return score

def part2(input_):
    # X = lose, Y = tie, Z = win
    score_map = { 
            'A': { 'X': 3, 'Y': 1, 'Z': 2 },
            'B': { 'X': 1, 'Y': 2, 'Z': 3 },
            'C': { 'X': 2, 'Y': 3, 'Z': 1 },
            }
    result_score = { 'X': 0, 'Y': 3, 'Z': 6 }
    score = 0
    for round_ in input_.split('\n')[:-1]:
        theirs, force = round_.split(' ')
        score += score_map[theirs][force]
        score += result_score[force]
    return score

try:
    #setup_request_logs()

    # name the files after the day. ie. 1.py for day 1
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)

    res = part1(r.text)
    print(res)
    res = part2(r.text)
    print(res)
except e:
    print(e)
