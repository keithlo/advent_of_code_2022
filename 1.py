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
    max_, cur = 0, 0
    for line in input_.split('\n'):
        if line == '':
            cur = 0
        else:
            cur += int(line)
            max_ = max(max_, cur)
    return max_

from heapq import *
def part2(input_):
    cur = 0
    heap = []
    for line in input_.split('\n'):
        if line == '':
            heappush(heap, -cur)
            cur = 0
        else:
            cur += int(line)
    return sum([-heappop(heap) for _ in range(3)])

try:
    #setup_request_logs()
    # name the files after the day. ie. 1.py for day 1
    day = os.path.basename(__file__).split('.')[0]
    url = 'https://adventofcode.com/2022/day/'+day+'/input'
    cookies = {'session': os.environ['ADVENT_TOKEN']}
    r = requests.get(url, cookies=cookies)

    print(part1(r.text))
    print(part2(r.text))

except e:
    print(e)
